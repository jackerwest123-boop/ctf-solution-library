# -*- coding: utf-8 -*-
import sys, base64, re
from collections import deque

raw = open(sys.argv[1], 'rb').read().strip() if len(sys.argv) > 1 else sys.stdin.buffer.read().strip()
funcs = [
    ('b16', lambda b: base64.b16decode(b, casefold=True)),
    ('b32', lambda b: base64.b32decode(b)),
    ('b64', lambda b: base64.b64decode(b, validate=True)),
    ('b85', base64.b85decode),
    ('a85', base64.a85decode),
]
q = deque([(raw, [])])
seen = {raw}
for _ in range(5000):
    if not q:
        break
    b, path = q.popleft()
    hits = re.findall(rb'(?i)(?:flag|ctf)\{[^}]+\}', b)
    if hits:
        print('path:', ' -> '.join(path) or '(raw)')
        print(hits[0].decode('ascii', 'replace'))
        raise SystemExit(0)
    for name, fn in funcs:
        try:
            x = fn(b.strip())
            if x and x not in seen:
                seen.add(x)
                q.append((x, path + [name]))
        except Exception:
            pass
print('no flag-like token found')
