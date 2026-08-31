# tools/

仓库工具目录。

- `validate_card.py`：校验单张 `card.json` 是否符合统一交付契约。
- `run_self_tests.py`：扫描 `data/solver_manifest.json` 并运行 solver 自测。
- `ingest_solution_card.py`：把符合契约的卡片导入 `data/capabilities.json` 与 `data/solver_manifest.json`。
