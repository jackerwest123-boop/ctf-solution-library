# -*- coding: utf-8 -*-
"""Generic helper for XOR-based Feistel decryption.
Provide recovered 8-byte round keys from the challenge-specific key schedule.
"""

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def decrypt_block(block, round_keys):
    if len(block) != 16:
        raise ValueError('block must be 16 bytes')
    if any(len(k) != 8 for k in round_keys):
        raise ValueError('each round key must be 8 bytes')
    L, R = block[:8], block[8:]
    for k in reversed(round_keys):
        L, R = xor_bytes(R, k), L
    return L + R


if __name__ == '__main__':
    print('Reusable helper loaded. Recover the challenge key schedule, then call decrypt_block().')
