#!/usr/bin/env python3
"""
Bugku 016 "-++--" emoticon Brainfuck solver.

Unified contract:
    solve(attachment_path, **kwargs) -> {'flag': str|None, 'artifacts': [str], 'evidence': str}

It accepts either normal Brainfuck or the NUAACTF emoticon dialect.  The mapping
contains the corrected tokens verified during review:
    (♥ ͜ʖ♥) -> -
    (> ͜ʖ(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*) -> .
"""
from __future__ import annotations

import argparse
import re
import tempfile
from pathlib import Path
from typing import Dict, Iterable, Tuple

DEFAULT_MAPPING: Dict[str, str] = {
    "( ͡° ͜ʖ ͡°)": "+",
    "(♥ ͜ʖ♥)": "-",
    "ᕦ( ͡°ヮ ͡°)ᕥ": ">",
    "(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*": "<",
    "(> ͜ʖ(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*)": ".",
    "( ͡°(": "[",
    ") ͡°)": "]",
}

FLAG_RE = re.compile(r"[A-Za-z0-9_]+CTF\{[^}\r\n]+\}|[a-zA-Z0-9_]+\{[^}\r\n]+\}", re.I)


def tokenize_to_bf(text: str, mapping: Dict[str, str] | None = None) -> str:
    mapping = mapping or DEFAULT_MAPPING
    if any(tok in text for tok in mapping):
        out = []
        i = 0
        tokens: Iterable[Tuple[str, str]] = sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True)
        while i < len(text):
            matched = False
            for token, op in tokens:
                if text.startswith(token, i):
                    out.append(op)
                    i += len(token)
                    matched = True
                    break
            if not matched:
                if text[i] in "><+-.,[]":
                    out.append(text[i])
                i += 1
        return "".join(out)
    return "".join(c for c in text if c in "><+-.,[]")


def run_bf(code: str, input_bytes: bytes = b"", cell_count: int = 30000) -> str:
    jump = {}
    stack = []
    for idx, ch in enumerate(code):
        if ch == "[":
            stack.append(idx)
        elif ch == "]":
            if not stack:
                raise ValueError(f"unmatched ] at {idx}")
            start = stack.pop()
            jump[start] = idx
            jump[idx] = start
    if stack:
        raise ValueError(f"unmatched [ at {stack[-1]}")

    tape = [0] * cell_count
    ptr = 0
    ip = 0
    inp = 0
    out = bytearray()

    while ip < len(code):
        ch = code[ip]
        if ch == ">":
            ptr += 1
            if ptr >= len(tape):
                tape.append(0)
        elif ch == "<":
            ptr -= 1
            if ptr < 0:
                raise ValueError("data pointer moved below zero")
        elif ch == "+":
            tape[ptr] = (tape[ptr] + 1) & 0xFF
        elif ch == "-":
            tape[ptr] = (tape[ptr] - 1) & 0xFF
        elif ch == ".":
            out.append(tape[ptr])
        elif ch == ",":
            tape[ptr] = input_bytes[inp] if inp < len(input_bytes) else 0
            inp += 1
        elif ch == "[" and tape[ptr] == 0:
            ip = jump[ip]
        elif ch == "]" and tape[ptr] != 0:
            ip = jump[ip]
        ip += 1

    return out.decode("utf-8", errors="replace")


def solve(attachment_path: str, **kwargs):
    path = Path(attachment_path)
    text = path.read_text(encoding=kwargs.get("encoding", "utf-8"), errors="ignore")
    bf = tokenize_to_bf(text)
    output = run_bf(bf)
    match = FLAG_RE.search(output)
    return {
        "flag": match.group(0) if match else None,
        "artifacts": [],
        "evidence": f"translated_len={len(bf)} output={output!r}",
    }


def _self_test() -> int:
    direct = "++++++++[>++++++++<-]>+."
    plus = "( ͡° ͜ʖ ͡°)"
    minus = "(♥ ͜ʖ♥)"
    right = "ᕦ( ͡°ヮ ͡°)ᕥ"
    left = "(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*"
    dot = "(> ͜ʖ(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*)"
    lb = "( ͡°("
    rb = ") ͡°)"
    emoticon = plus * 8 + lb + right + plus * 8 + left + minus + rb + right + plus + dot

    with tempfile.TemporaryDirectory() as td:
        direct_path = Path(td) / "direct.bf"
        emote_path = Path(td) / "emote.txt"
        direct_path.write_text(direct, encoding="utf-8")
        emote_path.write_text(emoticon, encoding="utf-8")
        a = solve(str(direct_path))["evidence"]
        b = solve(str(emote_path))["evidence"]
        ok = "output='A'" in a and "output='A'" in b
        print("SELF_TEST expected_output=A")
        print(a)
        print(b)
        print("SELF_TEST", "PASS" if ok else "FAIL")
        return 0 if ok else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("attachment", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return _self_test()
    if not args.attachment:
        parser.error("attachment path required unless --self-test is used")
    result = solve(args.attachment)
    if result["flag"]:
        print(result["flag"])
    print(result["evidence"])
    for artifact in result["artifacts"]:
        print(f"CTF_ARTIFACT {Path(artifact).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
