# Bugku 第131—180题逐题补 flag 记录

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本文件是对 `第131-180题_batch.md` 的返工补 flag。只把 Bugku 页面、公开评论、公开 writeup、或题目官方公开源码仓库中能直接看到明确 flag 的题目计为 `solved-carded`；仅有解法思路但无可核验 flag 文本的题目不计入 solved。

## 状态口径

- `solved-carded`：已找到明确 flag 文本，并写入补充卡。
- `analyzed-no-flag`：有明确解法或源码线索，但未找到可抄录且可核验的 Bugku flag。
- `blocked-no-flag`：未找到可靠公开 flag，仍需启动 Bugku 动态环境、附件或原题环境验证。

## 本轮汇总

- solved-carded：12题（第136、137、138、139、140、144、148、158、159、160、163、164题）。
- analyzed-no-flag：9题（第141、143、145、147、149、150、151、152、153题）。
- blocked-no-flag：29题（第131—135、142、146、154—157、161—162、165—180题）。

## 已确认 flag

| 题号 | 题名 | flag | 依据 |
|---:|---|---|---|
| 136 | Apollo Guidance Computer | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` | Space Heroes CTF 2023 官方源码仓库 `web/apollo-guidance-computer/src/flag.txt`。 |
| 137 | attack-strategies | `shctf{get_zerg_rushed_nb}` | Space Heroes CTF 2023 官方源码仓库 `web/attack-strategies/docker/strategies/flag.txt`。 |
| 138 | robot-best-friend | `shctf{I_don't_want_to_play_with_you_ever_again}` | Space Heroes CTF 2023 官方源码仓库 `web/robot-best-friend/Chall.py` 系统提示。 |
| 139 | Sanity Check In Space | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` | Space Heroes CTF 2023 官方源码仓库 `web/Sanity Check In Space/docker/flag.txt`。 |
| 140 | Bank of Knowhere | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` | Space Heroes CTF 2023 官方源码仓库 `web/Knowhere_Bank/docker/admin.php`。 |
| 144 | hi | `tjctf{pretty_canvas_577f7045}` | TJCTF 2023 公开 writeup。 |
| 148 | pay-to-win | `tjctf{not_random_enough_64831eff}` | TJCTF 2023 公开 writeup。 |
| 158 | fruit-store | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` | TJCTF 2022 公开 writeup。 |
| 159 | game-leaderboard | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` | TJCTF 2022 公开 writeup。 |
| 160 | lamb-sauce | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` | TJCTF 2022 公开 writeup。 |
| 163 | portalstrology | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` | TJCTF 2022 公开 writeup。 |
| 164 | viewy | `tjctf{4l1_th3_v1eW5_wh3333e333}` | TJCTF 2022 公开 writeup。 |

## 逐题结果

| 题号 | 题名 | 状态 | flag / 候选 | 处理说明 |
|---:|---|---|---|---|
| 131 | beehive | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境或附件验证。 |
| 132 | hintbot | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境或附件验证。 |
| 133 | deserbug | blocked-no-flag |  | 未找到可靠公开 flag，需要 CISCN 原题环境/附件验证。 |
| 134 | unzip | blocked-no-flag |  | 未找到可靠公开 flag，需要 CISCN 原题环境/附件验证。 |
| 135 | b4bycoffee | blocked-no-flag |  | 未找到可靠公开 flag，需要长城杯题目源码或动态环境。 |
| 136 | Apollo Guidance Computer | solved-carded | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` | 官方源码仓库 flag.txt 可直接确认。 |
| 137 | attack-strategies | solved-carded | `shctf{get_zerg_rushed_nb}` | 官方源码仓库隐藏 strategies/flag.txt 可直接确认。 |
| 138 | robot-best-friend | solved-carded | `shctf{I_don't_want_to_play_with_you_ever_again}` | 官方源码仓库 Chall.py system prompt 可直接确认。 |
| 139 | Sanity Check In Space | solved-carded | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` | 官方源码仓库 flag.txt 可直接确认。 |
| 140 | Bank of Knowhere | solved-carded | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` | 官方源码仓库 admin.php 可直接确认。 |
| 141 | The DEW | analyzed-no-flag |  | 已定位 Space Heroes 源码目录；尚未在公开文件中确认 flag 文本。 |
| 142 | profile viewer | blocked-no-flag |  | 未找到可靠公开 flag，需要 TSG live ctf 原题环境。 |
| 143 | back-to-the-past | analyzed-no-flag |  | 有公开 writeup/思路线索，未找到可靠 flag 文本。 |
| 144 | hi | solved-carded | `tjctf{pretty_canvas_577f7045}` | 公开 writeup 可确认。 |
| 145 | ez-sql | analyzed-no-flag |  | 公开 writeup 说明动态表/动态 flag，未找到可复用 Bugku flag。 |
| 146 | notes | blocked-no-flag |  | 未找到可靠公开 flag，需要 TJCTF 原题环境。 |
| 147 | outdated | analyzed-no-flag |  | 有公开 writeup/思路线索，未找到可靠 flag 文本。 |
| 148 | pay-to-win | solved-carded | `tjctf{not_random_enough_64831eff}` | 公开 writeup 可确认。 |
| 149 | swill-squill | analyzed-no-flag |  | 有公开 writeup/源码思路，未找到可靠 flag 文本。 |
| 150 | analects | analyzed-no-flag |  | 公开资料多为题目部署/SQLi思路，未找到可靠 flag 文本。 |
| 151 | ascordle | analyzed-no-flag |  | 公开资料提示 Wordle/SQLi方向，未找到可靠 flag 文本。 |
| 152 | LFI 0 | analyzed-no-flag |  | 题名和公开资料指向 LFI，但未找到可核验 flag。 |
| 153 | LFI or RCE | analyzed-no-flag |  | 题名和公开资料指向 LFI/RCE，但未找到可核验 flag。 |
| 154 | RCE 0 | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境验证。 |
| 155 | SSRF 0 | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境验证。 |
| 156 | SSTI 0 | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境验证。 |
| 157 | up to you | blocked-no-flag |  | 未找到可靠公开 flag，需要原题环境验证。 |
| 158 | fruit-store | solved-carded | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` | 公开 writeup 可确认。 |
| 159 | game-leaderboard | solved-carded | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` | 公开 writeup 可确认。 |
| 160 | lamb-sauce | solved-carded | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` | 公开 writeup 可确认。 |
| 161 | mmocc | blocked-no-flag |  | 未找到可靠公开 flag，需要 TJCTF 原题环境/附件验证。 |
| 162 | photoable | blocked-no-flag |  | 未找到可靠公开 flag，需要 TJCTF 原题环境/附件验证。 |
| 163 | portalstrology | solved-carded | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` | 公开 writeup 可确认。 |
| 164 | viewy | solved-carded | `tjctf{4l1_th3_v1eW5_wh3333e333}` | 公开 writeup 可确认。 |
| 165 | Agent-007 | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 166 | CooooKiE | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 167 | Cr4zy-Js0N | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 168 | F4ke-Upl04d | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 169 | JW token | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 170 | LoGiC | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 171 | Request Basics 1 | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 172 | Request Basics 2 | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 173 | Request Basics 3 | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 174 | Tunisia | blocked-no-flag |  | 未找到可靠公开 flag，需要 Securinets 原题环境。 |
| 175 | baby_sqli | blocked-no-flag |  | 未找到可靠公开 flag，需要 Welcome CTF 原题环境。 |
| 176 | inspector | blocked-no-flag |  | 未找到可靠公开 flag，需要 Welcome CTF 原题环境。 |
| 177 | RCE won't help | blocked-no-flag |  | 未找到可靠公开 flag；公开资料中未确认该 Web 题 flag。 |
| 178 | flasky | blocked-no-flag |  | 未找到可靠公开 flag，需要 Welcome CTF 原题环境。 |
| 179 | toddlersqli | blocked-no-flag |  | 未找到可靠公开 flag，需要 Welcome CTF 原题环境。 |
| 180 | SS Xperience | blocked-no-flag |  | 未找到可靠公开 flag，需要 Welcome CTF 原题环境。 |

## 本批结论

第131—180题已完成逐题返工补 flag。本批确认 12 个 flag，其余题目没有找到可核验公开 flag，继续保留非 solved 状态。后续继续处理第181—230题，仍按“可核验 flag 才写入 verification.flag”的标准执行。
