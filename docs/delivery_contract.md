# 统一交付契约

本仓库从本文件生效后停止使用多套状态名，统一使用四种状态：

| 状态 | 含义 | 可否计入完成 |
|---|---|---|
| `solved_verified` | `verification.flag` 非空，且 `verification.executed=true`，可复用 solver 必须有 `self_test` | 是 |
| `solved_unverified` | 公开来源可见 flag，但本仓库没有真实执行输出 | 否，待复核 |
| `method_only` | 有题目特定解法，但没有可核验 flag | 否 |
| `blocked` | 缺附件、动态环境、目标页或证据冲突 | 否 |

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

没有真实运行输出时，不得写 `solved_verified`。公开 writeup 可见 flag 但没有本地执行，只能是 `solved_unverified`。
