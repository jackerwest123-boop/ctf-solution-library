# -*- coding: utf-8 -*-
"""RSA decrypt when p and q have already been recovered."""
import re
import sys

if len(sys.argv) != 5:
    raise SystemExit(f"usage: {sys.argv[0]} <c> <e> <p> <q>")

c, e, p, q = [int(x, 0) for x in sys.argv[1:]]
n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
b = m.to_bytes((m.bit_length() + 7) // 8, "big")
print(b)
for match in re.findall(rb"(?i)(?:flag|ctf)\{[^}]+\}", b):
    print(match.decode("ascii", "replace"))
