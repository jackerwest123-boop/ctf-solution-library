# Bugku 题库“完成”口径修复记录

## 修复原因

此前对用户汇报中使用“完成一轮”的说法容易被理解为“20题都真实做出”。实际仓库工作大部分是清单建档和契约卡建档，不能等同于真实解题。

## 修复后的统一口径

- A阶段完成：只表示题目清单建档完成。
- B阶段完成：只表示 canonical `README.md` 和 `card.json` 建档或升级完成。
- 真正做出：只统计 `solved_verified`，必须满足 `verification.executed=true` 且有真实运行输出。
- `method_only` 只用于有题目特定解法但尚未核验 flag 的情况。
- 缺附件、缺动态环境、只有通用方向或证据不足时，一律保守标为 `blocked`。

## 已修复位置

- `docs/delivery_contract.md` 增加完成口径修正。
- `progress.json` 增加 `completion_scope`、`overall_stats_current`、`repair_note`。
- `data/bugku_gid2_manifest.json` 增加 `completion_scope` 并在第006轮-B采用更保守状态。

## 当前真实解题统计

截至第006轮-B完成后，001—120 题中，真正达到 `solved_verified` 的仍只有 1 题；其余均不能表述为“已真正做出”。

## 后续执行要求

后续每轮汇报必须明确：本轮是清单建档、契约卡建档，还是新增真实验证题。没有原始附件或真实授权环境输出时，不得写成已经做题成功。