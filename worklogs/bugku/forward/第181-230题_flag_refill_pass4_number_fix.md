# Bugku 第181—230题逐题补 flag 记录（Pass 4 / 题号纠偏）

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本轮继续对第181—230题做题号纠偏和 flag 回填。此前混入了 `/challenges/index/tid/1.html` 的“全站 WEB”分页。本轮以 `gid=2/tid=1` 搜索缓存为准：`page=11` 明确从 `analects` 到 `JW token` 共 20 个 WEB 题，因此按每页 20 题可校准为第201—220题；同时结合相邻赛事标签页顺序，反推第181—200题。

## 本轮依据

- `gid=2/tid=1&page=11` 缓存显示：`analects`、`ascordle`、`LFI 0`、`LFI or RCE`、`RCE 0`、`SSRF 0`、`SSTI 0`、`up to you`、`fruit-store`、`game-leaderboard`、`lamb-sauce`、`mmocc`、`photoable`、`portalstrology`、`viewy`、`Agent-007`、`CooooKiE`、`Cr4zy-Js0N`、`F4ke-Upl04d`、`JW token`。
- TJCTF-2023 标签页显示 `back-to-the-past`、`hi`、`ez-sql`、`notes`、`outdated`、`pay-to-win`、`swill-squill` 后接 TJCTF-2022 WEB 题序列。
- Space Heroes CTF-2023 标签页显示 `Apollo Guidance Computer`、`attack-strategies`、`robot-best-friend`、`Sanity Check In Space`、`Bank of Knowhere`、`The DEW` 的相邻顺序。

## 校准后的第181—220题

| 题号 | 题名 | 赛事 | 状态 | flag |
|---:|---|---|---|---|
| 181 | go_session | CISCN-2023 | blocked-no-flag |  |
| 182 | beehive | SaplingCTF-2023 | blocked-no-flag |  |
| 183 | hintbot | SaplingCTF-2023 | blocked-no-flag |  |
| 184 | deserbug | CISCN-2023 | blocked-no-flag |  |
| 185 | unzip | CISCN-2023 | blocked-no-flag |  |
| 186 | b4bycoffee | 长城杯-2022 | blocked-no-flag |  |
| 187 | Apollo Guidance Computer | Space Heroes CTF-2023 | solved-carded | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` |
| 188 | attack-strategies | Space Heroes CTF-2023 | solved-carded | `shctf{get_zerg_rushed_nb}` |
| 189 | robot-best-friend | Space Heroes CTF-2023 | solved-carded | `shctf{I_don't_want_to_play_with_you_ever_again}` |
| 190 | Sanity Check In Space | Space Heroes CTF-2023 | solved-carded | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` |
| 191 | Bank of Knowhere | Space Heroes CTF-2023 | solved-carded | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` |
| 192 | The DEW | Space Heroes CTF-2023 | analyzed-no-flag |  |
| 193 | profile viewer | TSG live ctf-10 | blocked-no-flag |  |
| 194 | back-to-the-past | TJCTF-2023 | analyzed-no-flag |  |
| 195 | hi | TJCTF-2023 | solved-carded | `tjctf{pretty_canvas_577f7045}` |
| 196 | ez-sql | TJCTF-2023 | analyzed-no-flag |  |
| 197 | notes | TJCTF-2023 | blocked-no-flag |  |
| 198 | outdated | TJCTF-2023 | analyzed-no-flag |  |
| 199 | pay-to-win | TJCTF-2023 | solved-carded | `tjctf{not_random_enough_64831eff}` |
| 200 | swill-squill | TJCTF-2023 | solved-carded | `tjctf{swill_sql_1y1029345029374}` |
| 201 | analects | TJCTF-2022 | analyzed-no-flag |  |
| 202 | ascordle | TJCTF-2022 | analyzed-no-flag |  |
| 203 | LFI 0 | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 204 | LFI or RCE | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 205 | RCE 0 | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 206 | SSRF 0 | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 207 | SSTI 0 | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 208 | up to you | Securinets-Christmas-CTF-2022 | analyzed-no-flag |  |
| 209 | fruit-store | TJCTF-2022 | solved-carded | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` |
| 210 | game-leaderboard | TJCTF-2022 | solved-carded | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` |
| 211 | lamb-sauce | TJCTF-2022 | solved-carded | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` |
| 212 | mmocc | TJCTF-2022 | analyzed-no-flag |  |
| 213 | photoable | TJCTF-2022 | analyzed-no-flag |  |
| 214 | portalstrology | TJCTF-2022 | solved-carded | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` |
| 215 | viewy | TJCTF-2022 | solved-carded | `tjctf{4l1_th3_v1eW5_wh3333e333}` |
| 216 | Agent-007 | Securinets-Friendly-2022 | analyzed-no-flag |  |
| 217 | CooooKiE | Securinets-Friendly-2022 | analyzed-no-flag |  |
| 218 | Cr4zy-Js0N | Securinets-Friendly-2022 | analyzed-no-flag |  |
| 219 | F4ke-Upl04d | Securinets-Friendly-2022 | analyzed-no-flag |  |
| 220 | JW token | Securinets-Friendly-2022 | analyzed-no-flag |  |

## 本轮新增/纠正

- 新增确认：第200题 `swill-squill`，flag 为 `tjctf{swill_sql_1y1029345029374}`。
- 纠正题号：此前第182—194的 Space Heroes/TJCTF 题号整体前移/后移存在偏差；本轮按 `page=11` 起点重新校准。
- 第221—230题仍待 `gid=2/tid=1&page=12` 缓存稳定返回后继续补齐；目前可推测会从 `LoGiC` 继续，但暂不强行写死。

## 下一步

继续处理第221—230题：优先确认 `LoGiC`、`Request Basics 1/2/3`、`Tunisia`、Welcome CTF-2023 系列是否对应第221—230，并继续查找可核验 flag。