# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成；当前已推进到第180题；正在返工补 flag。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批 | 41—80 | `worklogs/bugku/forward/第41-80题_batch.md`；`cards/pending/bugku/第41-80题_batch.cards.json` | 原为批量 blocked-carded，已开始返工补 flag |
| 第二批补充 | 41—80 | `worklogs/bugku/forward/第41-80题_flag_refill.md`；`cards/pending/bugku/第41-80题_flag_refill.cards.json` | 已确认 7 题 solved-carded；2 题 candidate-conflict；其余待动态验证 |
| 第三批 | 81—130 | `worklogs/bugku/forward/第81-130题_batch.md`；`cards/pending/bugku/第81-130题_batch.cards.json` | blocked-carded，待逐题补 flag |
| 第四批 | 131—180 | `worklogs/bugku/forward/第131-180题_batch.md`；`cards/pending/bugku/第131-180题_batch.cards.json` | blocked-carded，待逐题补 flag |

## 第41—80题补 flag 摘要

| 类别 | 数量 | 题号 |
|---|---:|---|
| solved-carded | 7 | 42、46、53、54、59、61、64 |
| candidate-conflict | 2 | 44、48 |
| analyzed-no-flag | 10 | 41、43、47、49、50、55、62、65、66、67 |
| blocked-no-flag | 21 | 45、51、52、56、57、58、60、63、68—80 |

## 已确认 flag

| 题号 | 题名 | flag |
|---:|---|---|
| 42 | ？？？？ | `0xGame{L1nux_i5_S0_gO0D_I_th1nK}` |
| 46 | edr | `0xGame{S4n9f0r_3dR_c4N_Rce_reC3n7_D4y}` |
| 53 | robots | `0xGame{now_you_k0nw_robots_Protocol}` |
| 54 | switch | `0xGame{S0me_pHp_tR1cKs_u_G3t_1t}` |
| 59 | command | `0xGame{L1nux_cmd_1s_3a5y_t0_you!!!}` |
| 61 | upload | `0xGame{upl0ad_f1le_causes_danger!!!}` |
| 64 | robot | `0xGame{Rob0t_le4ks_seCr3t}` |

## 处理原则
- 能直接从公开题面、评论或公开 writeup 确认 flag 的写入 solved-carded。
- 候选冲突或有“flag error/不正确”等提示的题目，不写入最终 verification.flag。
- 需要启动 Bugku 动态容器验证的题目，不编造 flag，统一保留为 analyzed-no-flag 或 blocked-no-flag。
- 后续应优先对 41—80 中未确认 flag 的题目继续查公开 writeup 与动态复现。

## 下一步
继续返工第41—80题未确认项，或按用户要求进入第81—130题逐题补 flag。