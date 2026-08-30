# -*- coding: utf-8 -*-
"""Scan arbitrary files for printable CTF-like strings."""
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit(f"usage: {sys.argv[0]} <file>")

data = open(sys.argv[1], "rb").read()
for m in re.finditer(rb"[\x20-\x7e]{4,}", data):
    s = m.group().decode("ascii", "ignore")
    if re.search(r"(?i)(flag|ctf|nuaa)", s) or ("{" in s and "}" in s):
        print(f"{m.start():#x}: {s}")
