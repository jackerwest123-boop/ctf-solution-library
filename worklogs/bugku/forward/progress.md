# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成；当前已推进到第180题；第41—180题已进入逐题补 flag 阶段；第181—230题已开始 Pass 1 补 flag。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批 | 41—80 | `worklogs/bugku/forward/第41-80题_batch.md`；`cards/pending/bugku/第41-80题_batch.cards.json` | 原为批量 blocked-carded，已返工补 flag |
| 第二批补充 | 41—80 | `worklogs/bugku/forward/第41-80题_flag_refill.md`；`cards/pending/bugku/第41-80题_flag_refill.cards.json` | 已确认 7 题 solved-carded；2 题 candidate-conflict；其余待动态验证 |
| 第三批 | 81—130 | `worklogs/bugku/forward/第81-130题_batch.md`；`cards/pending/bugku/第81-130题_batch.cards.json` | 原为批量 blocked-carded，已返工补 flag |
| 第三批补充 | 81—130 | `worklogs/bugku/forward/第81-130题_flag_refill.md`；`cards/pending/bugku/第81-130题_flag_refill.cards.json` | 已确认 5 题 solved-carded；2 题 candidate-format-anomaly；其余待动态验证 |
| 第四批 | 131—180 | `worklogs/bugku/forward/第131-180题_batch.md`；`cards/pending/bugku/第131-180题_batch.cards.json` | 原为批量 blocked-carded，已返工补 flag |
| 第四批补充 | 131—180 | `worklogs/bugku/forward/第131-180题_flag_refill.md`；`cards/pending/bugku/第131-180题_flag_refill.cards.json` | 已确认 12 题 solved-carded；其余待动态验证 |
| 第五批补充 Pass 1 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass1.md`；`cards/pending/bugku/第181-230题_flag_refill_pass1.cards.json` | 已确认第181题；候选后续题中确认2个 flag，但全局题号待第16—18页列表复核 |

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

## 第131—180题补 flag 摘要

| 类别 | 数量 | 题号 |
|---|---:|---|
| solved-carded | 12 | 136、137、138、139、140、144、148、158、159、160、163、164 |
| analyzed-no-flag | 9 | 141、143、145、147、149、150、151、152、153 |
| blocked-no-flag | 29 | 131—135、142、146、154—157、161—162、165—180 |

## 第181—230题补 flag Pass 1 摘要

| 类别 | 数量 | 题号/题名 |
|---|---:|---|
| confirmed-number | 1 | 第181题 `We Love The Environment` |
| solved-carded-candidate-number | 2 | `Robots`、`Secret Group`，均为 n00bzCTF-2023 WEB，待第16—18页列表复核全局题号 |
| analyzed-no-flag | 8 | `We Love The Environment`、`shero`、`Hello GreyCat beta`、`t00 f4st`、`Resume`、`Curl as a Service`、`CaaS`、`CaaS2`、`Conditions` 中未确认 flag 的部分 |
| blocked-enumeration | 49 | 第182—230题准确全局题号仍需 Bugku 第16—18页列表或缓存支持 |

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
| 136 | Apollo Guidance Computer | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` |
| 137 | attack-strategies | `shctf{get_zerg_rushed_nb}` |
| 138 | robot-best-friend | `shctf{I_don't_want_to_play_with_you_ever_again}` |
| 139 | Sanity Check In Space | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` |
| 140 | Bank of Knowhere | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` |
| 144 | hi | `tjctf{pretty_canvas_577f7045}` |
| 148 | pay-to-win | `tjctf{not_random_enough_64831eff}` |
| 158 | fruit-store | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` |
| 159 | game-leaderboard | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` |
| 160 | lamb-sauce | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` |
| 163 | portalstrology | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` |
| 164 | viewy | `tjctf{4l1_th3_v1eW5_wh3333e333}` |
| 待复核全局题号 | Robots / n00bzCTF-2023 | `n00bz{1_f0und_7h3_r0b0ts!}` |
| 待复核全局题号 | Secret Group / n00bzCTF-2023 | `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}` |

## 处理原则
- 能直接从公开题面、评论、公开 writeup 或官方公开源码仓库确认 flag 的写入 solved-carded。
- 候选冲突、格式异常或有“提交不上/不正确”等提示的题目，不写入最终 verification.flag。
- 未复核全局题号的后续 WEB 题，即便已找到 flag，也先标记为 `solved-carded-candidate-number`，不强行归入第182—230的具体题号。
- NSSCTF 等复现平台中的动态 `NSSCTF{uuid}` 不作为 Bugku flag。
- 需要启动 Bugku 动态容器验证的题目，不编造 flag，统一保留为 analyzed-no-flag 或 blocked-no-flag。

## 下一步
继续检索 Bugku 第16—18页列表缓存，补齐第182—230题题名；题号确认后，将 `Robots` 和 `Secret Group` 的 flag 写入对应全局题号，并继续补 `CaaS/CaaS2/Conditions/Resume/Curl as a Service` 等题。
