# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第41—230题已进入逐题补 flag 和题号纠偏阶段；第181—230题已完成 Pass 1、Pass 2、Pass 3、Pass 4。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批补充 | 41—80 | `worklogs/bugku/forward/第41-80题_flag_refill.md`；`cards/pending/bugku/第41-80题_flag_refill.cards.json` | 已确认 7 题 solved-carded；2 题 candidate-conflict；其余待动态验证 |
| 第三批补充 | 81—130 | `worklogs/bugku/forward/第81-130题_flag_refill.md`；`cards/pending/bugku/第81-130题_flag_refill.cards.json` | 已确认 5 题 solved-carded；2 题 candidate-format-anomaly；其余待动态验证 |
| 第四批补充 | 131—180 | `worklogs/bugku/forward/第131-180题_flag_refill.md`；`cards/pending/bugku/第131-180题_flag_refill.cards.json` | 原映射中确认 12 题 solved-carded，现按目标分页持续复核题号 |
| 第五批补充 Pass 1 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass1.md`；`cards/pending/bugku/第181-230题_flag_refill_pass1.cards.json` | 已记录候选后续题，但发现题号来源混入全站 WEB 分页 |
| 第五批补充 Pass 2 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass2_scope_fix.md`；`cards/pending/bugku/第181-230题_flag_refill_pass2_scope_fix.cards.json` | 已完成范围校准，明确不再强行绑定错号 |
| 第五批补充 Pass 3 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass3_renumber.md`；`cards/pending/bugku/第181-230题_flag_refill_pass3_renumber.cards.json` | 初步回填部分题号，后续发现仍需以 page=11 校准 |
| 第五批补充 Pass 4 | 181—230 | `worklogs/bugku/forward/第181-230题_flag_refill_pass4_number_fix.md`；`cards/pending/bugku/第181-230题_flag_refill_pass4_number_fix.cards.json` | 以 `gid=2/tid=1&page=11` 为锚点重新校准第181—220题；确认 13 个带准确题号的 flag |

## 第181—220题 Pass 4 已确认 flag

| 题号 | 题名 | flag |
|---:|---|---|
| 187 | Apollo Guidance Computer | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` |
| 188 | attack-strategies | `shctf{get_zerg_rushed_nb}` |
| 189 | robot-best-friend | `shctf{I_don't_want_to_play_with_you_ever_again}` |
| 190 | Sanity Check In Space | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` |
| 191 | Bank of Knowhere | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` |
| 195 | hi | `tjctf{pretty_canvas_577f7045}` |
| 199 | pay-to-win | `tjctf{not_random_enough_64831eff}` |
| 200 | swill-squill | `tjctf{swill_sql_1y1029345029374}` |
| 209 | fruit-store | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` |
| 210 | game-leaderboard | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` |
| 211 | lamb-sauce | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` |
| 214 | portalstrology | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` |
| 215 | viewy | `tjctf{4l1_th3_v1eW5_wh3333e333}` |

## 仍需继续

- 第221—230题：继续确认 `gid=2/tid=1&page=12` 的稳定题名列表。
- 待复核全局题号的后续 flag：`Robots` = `n00bz{1_f0und_7h3_r0b0ts!}`；`Secret Group` = `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}`。
- 不写入动态平台 UUID flag；只有公开题面、评论、公开 writeup 或官方源码能核验的 flag 才计入 solved-carded。
