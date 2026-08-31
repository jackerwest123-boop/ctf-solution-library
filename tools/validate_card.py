#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_STATUS = {"solved_verified", "solved_unverified", "method_only", "blocked"}
REQUIRED = {
    "title", "source_id", "source_url", "capability_id", "category",
    "attachment_type", "attachment", "detection", "method", "solver",
    "verification", "status"
}


def validate_card(path: Path) -> list[str]:
    card = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    missing = sorted(REQUIRED - set(card))
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    status = card.get("status")
    if status not in ALLOWED_STATUS:
        errors.append(f"invalid status: {status!r}")
    solver = card.get("solver", {})
    if solver.get("reusable"):
        if "solve(attachment_path" not in solver.get("entrypoint", ""):
            errors.append("reusable solver missing unified solve(attachment_path, **kwargs) entrypoint")
        if not solver.get("self_test"):
            errors.append("reusable solver missing self_test")
    verification = card.get("verification", {})
    if status == "solved_verified":
        if not verification.get("flag"):
            errors.append("solved_verified requires verification.flag")
        if verification.get("executed") is not True:
            errors.append("solved_verified requires verification.executed=true")
        if not verification.get("executed_output"):
            errors.append("solved_verified requires verification.executed_output")
    return errors


def main(argv=None) -> int:
    paths = [Path(p) for p in (argv or sys.argv[1:])]
    if not paths:
        print("usage: validate_card.py <card.json> [...]", file=sys.stderr)
        return 2
    ok = True
    for path in paths:
        errors = validate_card(path)
        if errors:
            ok = False
            print(f"{path}: FAIL")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"{path}: OK")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
