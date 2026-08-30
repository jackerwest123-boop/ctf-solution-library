# -*- coding: utf-8 -*-
"""Recover repeating-XOR key slots from aligned known plaintext."""
import sys


def recover(cipher: bytes, known: bytes, keylen: int):
    key = [None] * keylen
    for i, b in enumerate(known):
        v = cipher[i] ^ b
        j = i % keylen
        if key[j] is not None and key[j] != v:
            raise ValueError("inconsistent known plaintext/key length")
        key[j] = v
    return key


def xor_with_key(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


if len(sys.argv) != 4:
    raise SystemExit(f"usage: {sys.argv[0]} <hex_cipher> <known_text> <keylen>")

cipher = bytes.fromhex(sys.argv[1])
known = sys.argv[2].encode()
keylen = int(sys.argv[3])
slots = recover(cipher, known, keylen)
print("key slots:", slots)
if all(v is not None for v in slots):
    key = bytes(slots)
    print("key:", key)
    print("plain:", xor_with_key(cipher, key))
