# experience

本目录存放由 `tools/ingest_solution_card.py` 从规范化卡片生成的经验条目。

写入原则：

- `solved_verified` 才能作为已验证经验进入能力库主索引。
- `solved_unverified` 只能作为待复核经验。
- `method_only` 和 `blocked` 不进入可调度能力，只保留为工作记录。
