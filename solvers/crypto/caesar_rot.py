#!/usr/bin/env python3
"""Generic Caesar/ROT solver for simple CTF flag text."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List

FLAG_RE = re.compile(r"Susctf\{[0-9a-f]{32}\}")


def caesar_shift(text: str, shift: int) -> str:
    out: List[str] = []
    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        else:
            out.append(ch)
    return "".join(out)


def solve(attachment_path: str, **kwargs) -> Dict[str, object]:
    text = Path(attachment_path).read_text(encoding=kwargs.get("encoding", "utf-8")).strip()
    candidates = []
    for shift in range(26):
        decoded = caesar_shift(text, shift)
        candidates.append((shift, decoded))
        m = FLAG_RE.search(decoded)
        if m:
            return {
                "flag": m.group(0),
                "artifacts": [],
                "evidence": f"matched {FLAG_RE.pattern} at caesar shift {shift}",
                "shift": shift,
                "decoded": decoded,
            }
    return {"flag": None, "artifacts": [], "evidence": "no matching flag format", "candidates": candidates}


def _self_test() -> int:
    sample = Path(__file__).with_name("caesar_rot13_sample.txt")
    if not sample.exists():
        sample.write_text("Fhfpgs{3r811r068s5pr27ro4op1p37723q7rr2}\n", encoding="utf-8")
    result = solve(str(sample))
    expected = "Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}"
    print(f"SELF_TEST expected_output={expected}")
    print(f"SELF_TEST result={result}")
    if result.get("flag") != expected:
        print("SELF_TEST FAIL")
        return 1
    print("SELF_TEST PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Solve Caesar/ROT ciphertext file")
    parser.add_argument("attachment_path", nargs="?", help="Path to ciphertext file")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return _self_test()
    if not args.attachment_path:
        parser.error("attachment_path is required unless --self-test is used")
    result = solve(args.attachment_path)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("flag") else 2


if __name__ == "__main__":
    raise SystemExit(main())
