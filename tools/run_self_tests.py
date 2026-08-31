#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "data" / "solver_manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    failed = 0
    for solver in data.get("solvers", []):
        cmd = solver.get("self_test")
        if not cmd:
            continue
        print(f"[self-test] {solver.get('module_name')}: {cmd}")
        proc = subprocess.run(cmd, cwd=root, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(proc.stdout, end="")
        if proc.returncode != 0:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
