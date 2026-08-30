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
| 第二批 | 41—80 | `worklogs/bugku/forward/第41-80题_batch.md`；`cards/pending/bugku/第41-80题_batch.cards.json` | 原为批量 blocked-carded，已返工补 flag |
| 第二批补充 | 41—80 | `worklogs/bugku/forward/第41-80题_flag_refill.md`；`cards/pending/bugku/第41-80题_flag_refill.cards.json` | 已确认 7 题 solved-carded；2 题 candidate-conflict；其余待动态验证 |
| 第三批 | 81—130 | `worklogs/bugku/forward/第81-130题_batch.md`；`cards/pending/bugku/第81-130题_batch.cards.json` | 原为批量 blocked-carded，已返工补 flag |
| 第三批补充 | 81—130 | `worklogs/bugku/forward/第81-130题_flag_refill.md`；`cards/pending/bugku/第81-130题_flag_refill.cards.json` | 已确认 5 题 solved-carded；2 题 candidate-format-anomaly；其余待动态验证 |
| 第四批 | 131—180 | `worklogs/bugku/forward/第131-180题_batch.md`；`cards/pending/bugku/第131-180题_batch.cards.json` | blocked-carded，待逐题补 flag |

## 第41—80题补 flag 摘要

| 类别 | 数量 | 题号 |
|---|---:|---|
| solved-carded | 7 | 42、46、53、54、59、61、64 |
| candidate-conflict | 2 | 44、48 |
| analyzed-no-flag | 10 | 41、43、47、49、50、55、62、65、66、67 |
| blocked-no-flag | 21 | 45、51、52、56、57、58、60、63、68—80 |

## 第81—130题补 flag 摘要

| 类别 | 数量 | 题号 |
|---|---:|---|
| solved-carded | 5 | 87、89、92、93、94 |
| candidate-format-anomaly | 2 | 88、103 |
| analyzed-no-flag | 11 | 90、91、95、96、97、100、101、102、104、105、106 |
| blocked-no-flag | 32 | 81—86、98、99、107—130 |

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
| 87 | 2048 | `moectf{2048_1s_intere5t1ng!}` |
| 89 | Do you know HTTP | `moectf{HTTPHeaders_1s_s0_ea5y!}` |
| 92 | Web安全入门指北—GET | `moectf{We1c0me_t0_CTF_Web!}` |
| 93 | Web安全入门指北—POST | `moectf{POST_1s_an_1mp0rtant_m3th0d!}` |
| 94 | Web安全入门指北—小饼干 | `moectf{C00kie_1s_sw33t!}` |

## 处理原则
- 能直接从公开题面、评论或公开 writeup 确认 flag 的写入 solved-carded。
- 候选冲突、格式异常或有“提交不上/不正确”等提示的题目，不写入最终 verification.flag。
- NSSCTF 等复现平台中的动态 `NSSCTF{uuid}` 不作为 Bugku flag。
- 需要启动 Bugku 动态容器验证的题目，不编造 flag，统一保留为 analyzed-no-flag 或 blocked-no-flag。

## 下一步
继续返工第81—130题未确认项，或按用户要求进入第131—180题逐题补 flag。