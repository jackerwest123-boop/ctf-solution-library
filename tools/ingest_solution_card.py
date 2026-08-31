#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_STATUS = {"solved_verified", "solved_unverified", "method_only", "blocked"}


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def save_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ingest(card_path: Path, root: Path, dry: bool = False):
    card = json.loads(card_path.read_text(encoding="utf-8"))
    status = card.get("status")
    if status not in ALLOWED_STATUS:
        raise SystemExit(f"{card_path}: invalid status {status!r}")

    capabilities_path = root / "data" / "capabilities.json"
    manifest_path = root / "data" / "solver_manifest.json"

    capabilities = load_json(capabilities_path, {"schema_version": 1, "capabilities": []})
    manifest = load_json(manifest_path, {"schema_version": 1, "solvers": []})

    cap = {
        "capability_id": card["capability_id"],
        "category": card["category"],
        "title": card["title"],
        "status": status,
        "cards": [str(card_path.relative_to(root)) if card_path.is_relative_to(root) else str(card_path)]
    }
    existing = [c for c in capabilities["capabilities"] if c.get("capability_id") == cap["capability_id"]]
    if existing:
        existing[0].update(cap)
    else:
        capabilities["capabilities"].append(cap)

    solver = card.get("solver", {})
    if solver.get("reusable"):
        self_test = solver.get("self_test", "")
        if isinstance(self_test, dict):
            self_test = self_test.get("command", "")
        item = {
            "module_name": solver.get("module_name"),
            "path": solver.get("path", ""),
            "category": card["category"],
            "entrypoint": solver.get("entrypoint"),
            "dependencies": solver.get("dependencies", []),
            "self_test": self_test,
            "status": "active" if status == "solved_verified" else "pending_validation",
        }
        existing = [s for s in manifest["solvers"] if s.get("module_name") == item["module_name"]]
        if existing:
            existing[0].update(item)
        else:
            manifest["solvers"].append(item)

    if dry:
        print(json.dumps({"capability": cap}, ensure_ascii=False, indent=2))
    else:
        save_json(capabilities_path, capabilities)
        save_json(manifest_path, manifest)
        print(f"ingested {card_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("card", nargs="+")
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    for card in args.card:
        ingest(Path(card).resolve(), root, args.dry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
