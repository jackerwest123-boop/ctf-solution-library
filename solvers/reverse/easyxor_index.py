#!/usr/bin/env python3
import argparse, ast, json, re
from pathlib import Path

DEFAULT_VALUES=[83,116,113,96,112,99,125,78,87,103,57,110,104,82,102,106,113,32,123,125,115,104]
FLAG_RE=re.compile(r"[A-Za-z0-9_]+\{[^}\r\n]+\}")

def decode(values):
    return ''.join(chr(int(v)^i) for i,v in enumerate(values))

def _load(path):
    text=Path(path).read_text(encoding='utf-8',errors='ignore').strip()
    try:
        obj=json.loads(text)
    except Exception:
        obj=ast.literal_eval(text)
    if isinstance(obj,dict): obj=obj.get('values') or obj.get('s')
    if not isinstance(obj,(list,tuple)): raise ValueError('expected integer array')
    return [int(x) for x in obj]

def solve(attachment_path, **kwargs):
    values=_load(attachment_path)
    out=decode(values)
    m=FLAG_RE.search(out)
    return {'flag':m.group(0) if m else None,'artifacts':[],'evidence':f'count={len(values)} decoded={out}'}

def self_test():
    out=decode(DEFAULT_VALUES)
    ok=out=='Susctf{I_n3ed_hea1ing}'
    print('SELF_TEST source=Bugku-206-comment-array')
    print('decoded='+out)
    print('SELF_TEST '+('PASS' if ok else 'FAIL'))
    return 0 if ok else 1

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('attachment',nargs='?'); ap.add_argument('--self-test',action='store_true'); ns=ap.parse_args()
    if ns.self_test: raise SystemExit(self_test())
    if not ns.attachment: ap.error('attachment required unless --self-test')
    print(json.dumps(solve(ns.attachment),ensure_ascii=False))
