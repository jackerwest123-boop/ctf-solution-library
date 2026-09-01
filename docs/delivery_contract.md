# 统一交付契约

本仓库从本文件生效后停止使用多套状态名，统一使用四种状态：

| 状态 | 含义 | 可否计入真正做出 |
|---|---|---|
| `solved_verified` | `verification.flag` 非空，且 `verification.executed=true`，可复用 solver 必须有 `self_test` 与真实运行输出 | 是 |
| `solved_unverified` | 公开来源可见 flag，但本仓库没有真实执行输出 | 否，待复核 |
| `method_only` | 有题目特定解法，但没有可核验 flag 或未完成真实验证 | 否 |
| `blocked` | 缺附件、动态环境、目标页或证据冲突；只有通用方向、没有题目特定解法时也归入此类 | 否 |

## 完成口径修正

- `A_completed` 只表示该页题目清单建档完成，不表示解题。
- `B_completed` 或“契约文件完成”只表示该页 `README.md`、`card.json` 等仓库工件建档完成，不表示 20 道题真实做出。
- 真正做出题目只能按 `solved_verified` 统计。
- 对用户汇报时必须区分“清单建档完成”“契约卡建档完成”和“真实解题完成”。

## 轮次完成硬规则

- 从 2026-09-01 起，`round_done`、`做完一轮`、`完成一轮` 只能用于该轮 20 道题全部达到 `solved_verified` 的情况。
- 只有建档、只有 README/card、只有公开 writeup、只有方法方向、没有真实执行输出，都不能叫“做完一轮”。
- 一轮中哪怕只有 1 道题不是 `solved_verified`，该轮状态也只能写 `real_solve_in_progress` 或 `real_solve_blocked`。
- 后续推进顺序恢复为：先从第001轮 page=1 开始逐题真实解题；第001轮 20/20 真实验证前，不把第002轮称为完成。

## 必填 JSON 字段

卡片必须包含：`title`、`source_id`、`source_url`、`capability_id`、`category`、`attachment_type`、`attachment`、`detection`、`method`、`solver`、`verification`、`status`。

## solver 统一入口

可复用 solver 必须实现：

```python
solve(attachment_path, **kwargs) -> {"flag": str | None, "artifacts": [str], "evidence": str}
```

脚本必须支持：

```bash
python3 <solver>.py --self-test
```

产物类脚本必须输出：

```text
CTF_ARTIFACT <绝对路径>
```

## 执行验证

没有真实运行输出时，不得写 `solved_verified`。公开 writeup 可见 flag 但没有本地执行，只能是 `solved_unverified`。只有通用方向、没有题目特定步骤时不得滥用 `method_only`，应保守标为 `blocked`。

## source-text 例外标注

少数题目如官方下载接口不可抓取，但题目密文在 Bugku 页面评论和公开 writeup 中一致出现时，可以把该密文整理为 `attachment_type=source_text` 进行 solver 验证；此类卡片必须在 `attachment.note` 和 `method.limitations` 中明确“不伪称为官方原始附件”。
