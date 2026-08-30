# -*- coding: utf-8 -*-
"""Small standard-library Brainfuck interpreter."""
import sys

raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
code = "".join(c for c in raw if c in "><+-.,[]")

jump = {}
stack = []
for i, c in enumerate(code):
    if c == "[":
        stack.append(i)
    elif c == "]":
        if not stack:
            raise SystemExit("unmatched ]")
        j = stack.pop()
        jump[i] = j
        jump[j] = i
if stack:
    raise SystemExit("unmatched [")

tape = [0] * 30000
ptr = ip = 0
out = []
while ip < len(code):
    c = code[ip]
    if c == ">": ptr += 1
    elif c == "<": ptr -= 1
    elif c == "+": tape[ptr] = (tape[ptr] + 1) & 0xff
    elif c == "-": tape[ptr] = (tape[ptr] - 1) & 0xff
    elif c == ".": out.append(chr(tape[ptr]))
    elif c == "[" and tape[ptr] == 0: ip = jump[ip]
    elif c == "]" and tape[ptr] != 0: ip = jump[ip]
    ip += 1
print("".join(out))
