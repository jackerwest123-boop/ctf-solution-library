# 仓库交付契约修复记录（2026-08-31）

## 处理结论

已停止继续跑量，先按用户给出的统一交付契约修仓库结构。

## 已完成

1. 新增 `docs/delivery_contract.md`，固化统一交付契约。
2. 新增 `data/status_schema.json`，统一四种状态：`solved_verified`、`solved_unverified`、`method_only`、`blocked`，并提供旧状态映射。
3. 新增 `data/capabilities.json`，作为能力库本体初始文件。
4. 新增 `data/solver_manifest.json`，作为 solver 调度清单。
5. 新增 `data/experience/README.md`，明确经验沉淀规则。
6. 新增 `tools/README.md`、`tools/validate_card.py`、`tools/run_self_tests.py`、`tools/ingest_solution_card.py`。
7. 新增 `solvers/misc/brainfuck_emoticon.py`，修复第016题 `-++--` 原 solver 只过滤 ASCII Brainfuck 而无法处理真实颜文字附件的问题。
8. 更新 `bugku/016_minus_plus_plus_minus_minus/card.json`，加入 `source_url`、`capability_id`、`attachment`、`solver.entrypoint`、`solver.dependencies`、`solver.self_test`、`verification.executed`、`verification.executed_output`、统一 `status`。
9. 更新根 `README.md`，把 `data/`、`tools/`、四状态和硬性 solver 约定写入仓库入口说明。

## 第016题修复说明

第016题旧 solver 的问题：

- 旧代码只保留附件中已经存在的 `><+-.,[]` 字符。
- 真实附件是颜文字 token，因此会被过滤成空程序。

本次修复：

- 使用最长 token 优先匹配。
- 修正映射：`(♥ ͜ʖ♥)` -> `-`。
- 修正输出 token：`(> ͜ʖ(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*)` -> `.`。
- solver 实现统一入口：`solve(attachment_path, **kwargs)`。
- solver 支持：`python3 solvers/misc/brainfuck_emoticon.py --self-test`。

自测输出：

```text
SELF_TEST expected_output=A
translated_len=24 output='A'
translated_len=24 output='A'
SELF_TEST PASS
```

## 仍未完成

1. `cards/pending/bugku/` 中旧批量卡尚未全部拆成 `bugku/<序号_题名>/card.json`。
2. `index.json` 仍需由规范卡片重新生成，不能继续手工维护旧的 20 条索引。
3. 31—80 中模板化 method 仍需逐题改为题目特有方法。
4. 除第016题外，其他 solver 仍需逐个补 `solve()`、`self_test` 和 `verification.executed_output`。

## 下一步执行顺序

1. 先用 `tools/validate_card.py` 校验现有 `bugku/*/card.json`。
2. 将 `cards/pending/bugku/` 中可转正的卡片拆入 `bugku/<序号_题名>/card.json`。
3. 对无法满足 `solved_verified` 的卡片统一降级为 `solved_unverified`、`method_only` 或 `blocked`。
4. 重新生成 `index.json` 与 `data/capabilities.json`。
5. 继续修复高价值 solver，保证每个可复用脚本都有 `solve()` 和 `--self-test`。
