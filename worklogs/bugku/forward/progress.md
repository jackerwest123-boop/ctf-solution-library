# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成；当前重点是逐题补 flag，并纠正此前全站 WEB 分页与 `gid=2/tid=1` 目标分页混用导致的题号偏差。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批补充 | 41—80 | `worklogs/bugku/forward/第41-80题_flag_refill.md`；`cards/pending/bugku/第41-80题_flag_refill.cards.json` | 已确认 7 题 solved-carded；2 题 candidate-conflict；其余待动态验证 |
| 第三批补充 | 81—130 | `worklogs/bugku/forward/第81-130题_flag_refill.md`；`cards/pending/bugku/第81-130题_flag_refill.cards.json` | 已确认 5 题 solved-carded；2 题 candidate-format-anomaly；其余待动态验证 |
| 第四批补充 | 131—180 | `worklogs/bugku/forward/第131-180题_flag_refill.md`；`cards/pending/bugku/第131-180题_flag_refill.cards.json` | 原映射中确认 12 题 solved-carded，现需按目标分页复核题号 |
| 第五批补充 Pass 1 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass1.md`；`cards/pending/bugku/第181-230题_flag_refill_pass1.cards.json` | 已记录候选后续题，但发现题号来源混入全站 WEB 分页 |
| 第五批补充 Pass 2 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass2_scope_fix.md`；`cards/pending/bugku/第181-230题_flag_refill_pass2_scope_fix.cards.json` | 已完成范围校准，明确不再强行绑定错号 |
| 第五批补充 Pass 3 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass3_renumber.md`；`cards/pending/bugku/第181-230题_flag_refill_pass3_renumber.cards.json` | 已回填 7 个较可靠题号，另保留 2 个待复核题号 flag |

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

## 第181—230题 Pass 3 回填摘要

| 类别 | 数量 | 题号/题名 |
|---|---:|---|
| solved-carded（题号已回填） | 7 | 182 Apollo Guidance Computer；183 attack-strategies；184 robot-best-friend；185 Sanity Check In Space；186 Bank of Knowhere；190 hi；194 pay-to-win |
| solved-carded-candidate-number | 2 | Robots；Secret Group，均待 `gid=2/tid=1` 后续页完整列表复核题号 |
| analyzed-no-flag | 多项 | b4bycoffee、The DEW、profile viewer、back-to-the-past、ez-sql、notes、outdated、swill-squill、CaaS/CaaS2/Conditions、We Love The Environment 等 |

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
| 182 | Apollo Guidance Computer | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` |
| 183 | attack-strategies | `shctf{get_zerg_rushed_nb}` |
| 184 | robot-best-friend | `shctf{I_don't_want_to_play_with_you_ever_again}` |
| 185 | Sanity Check In Space | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` |
| 186 | Bank of Knowhere | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` |
| 190 | hi | `tjctf{pretty_canvas_577f7045}` |
| 194 | pay-to-win | `tjctf{not_random_enough_64831eff}` |
| 待复核全局题号 | Robots / n00bzCTF-2023 | `n00bz{1_f0und_7h3_r0b0ts!}` |
| 待复核全局题号 | Secret Group / n00bzCTF-2023 | `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}` |

## 处理原则
- 能直接从公开题面、评论、公开 writeup 或官方公开源码仓库确认 flag 的写入 solved-carded。
- 候选冲突、格式异常或有“提交不上/不正确”等提示的题目，不写入最终 verification.flag。
- 未复核全局题号的后续 WEB 题，即便已找到 flag，也先标记为 `solved-carded-candidate-number`，不强行归入具体题号。
- NSSCTF 等复现平台中的动态 `NSSCTF{uuid}` 不作为 Bugku flag。
- 需要启动 Bugku 动态容器验证的题目，不编造 flag，统一保留为 analyzed-no-flag 或 blocked-no-flag。

## 下一步
继续复核 `gid=2/tid=1` 第10—12页题名；优先补全第181—230题完整题名表，并继续对第181、187—189、191—193、195—230等未解题补 flag。