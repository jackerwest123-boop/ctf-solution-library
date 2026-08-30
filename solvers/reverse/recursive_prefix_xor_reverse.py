# -*- coding: utf-8 -*-
"""Apply the recursive prefix-XOR transform seen in some reverse challenges."""
import sys

vals = [int(x, 0) for x in sys.argv[1:]]
if not vals or (len(vals) & (len(vals) - 1)):
    raise SystemExit("provide a power-of-two number of byte values")
if any(v < 0 or v > 255 for v in vals):
    raise SystemExit("all values must be bytes")


def transform(a, n=1):
    if n == len(a):
        return
    for i in range(n):
        a[i + n] ^= a[i]
    transform(a, n << 1)


transform(vals)
out = bytes(vals)
print(out)
try:
    print(out.decode())
except UnicodeDecodeError:
    pass
