# Bugku 第31—180题处理质量说明

## 结论

第31—180题并不是全部已经“解出 flag”。此前写入仓库的含义是：

1. 已按题库顺序建立 Markdown 记录和 JSON 解法转化卡。
2. 能从公开题面或评论中直接确认 flag 的题，标记为 `solved-carded`。
3. 需要启动 Bugku 动态容器、下载附件或访问在线场景才能验证的题，标记为 `blocked-carded`。
4. `blocked-carded` 不等于已解出，只代表已经完成题名、类型、判断方向、通用解法步骤和卡片结构整理。
5. 对无法验证的题，没有编造 flag。

## 当前状态

- 第31—40题：第33题、第36题为 solved-carded；其余 blocked-carded。
- 第41—80题：批量 blocked-carded。
- 第81—130题：批量 blocked-carded。
- 第131—180题：批量 blocked-carded。

## 后续处理原则

从现在开始，继续推进时统一区分三类状态：

| 状态 | 含义 |
|---|---|
| solved-carded | 已拿到并验证 flag，同时生成解题记录和 JSON 卡 |
| analyzed-carded | 题面、题型、思路和复现步骤明确，但未拿到 flag |
| blocked-carded | 缺动态环境、附件或网页访问条件，不能验证 flag |

如果用户要求“每轮50题继续推进”，后续仍可按批量方式继续建立卡片；但只有 `solved-carded` 才能视为真正解出。
