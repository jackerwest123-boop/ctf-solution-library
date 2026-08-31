# Bugku 第181—230题逐题补 flag 记录（Pass 2 / 范围校准）

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：继续处理第181—230题时，发现此前 Pass 1 主要依赖 `/challenges/index/tid/1.html?page=15` 这类“全站 WEB”分页缓存，而最初目标是“比赛真题 + WEB”（`gid=2/tid=1`）。因此本轮先做范围校准，再继续补 flag：

- `/challenges/index/tid/1.html?page=15` 可支撑 `photoable` 到 `We Love The Environment` 这一全站 WEB 页序。
- `/challenges/index/gid/2/tid/1.html?page=9` 可支撑比赛真题 WEB 中 `Bottle Poem` 到 `unzip` 的页序。
- `/challenges/index/gid/2/tid/1.html?page=11` 搜索缓存可支撑 `analects`、`ascordle`、`LFI 0`、`LFI or RCE`、`RCE 0`、`SSRF 0`、`SSTI 0`、`up to you`、`fruit-store`、`game-leaderboard`、`lamb-sauce`、`mmocc`、`photoable`、`portalstrology`、`viewy`、`Agent-007`、`CooooKiE`、`Cr4zy-Js0N`、`F4ke-Upl04d`、`JW token` 等题。
- Bugku 搜索缓存未能稳定打开 `gid=2/tid=1` 第10、12页，因此本轮不再强行把所有题名绑定到全局题号；只对题名和 flag 都有可靠公开支撑的题目补卡。

## 本轮新增确认

本轮新增确认 2 个后续 WEB 题 flag，仍标记为 `candidate-number`，待第10—12页完整列表复核后再绑定到具体全局题号：

| 题名 | 赛事 | 状态 | flag | 依据 |
|---|---|---|---|---|
| Robots | n00bzCTF-2023 | solved-carded-candidate-number | `n00bz{1_f0und_7h3_r0b0ts!}` | 公开 writeup 显示通过 `/robots.txt` 跟踪隐藏路径获得 flag；Bugku 后续 WEB 列表包含该题。 |
| Secret Group | n00bzCTF-2023 | solved-carded-candidate-number | `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}` | 公开 writeup 显示修改请求头为指定管理员身份获得 flag；Bugku 后续 WEB 列表包含该题。 |

## 已确认但需重新绑定全局题号的题目

下列题目在此前第131—180补 flag中已找到可核验 flag，但在最初目标 `gid=2/tid=1` 的分页体系中，其全局题号需要重新校准。为避免错号，暂不在本轮重写题号，只保留题名、flag 和来源性质：

| 题名 | flag | 来源性质 |
|---|---|---|
| Apollo Guidance Computer | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` | Space Heroes CTF 2023 官方公开源码仓库 `flag.txt` |
| attack-strategies | `shctf{get_zerg_rushed_nb}` | Space Heroes CTF 2023 官方公开源码仓库 `flag.txt` |
| robot-best-friend | `shctf{I_don't_want_to_play_with_you_ever_again}` | Space Heroes CTF 2023 官方公开源码仓库源码系统提示 |
| Sanity Check In Space | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` | Space Heroes CTF 2023 官方公开源码仓库 `flag.txt` |
| Bank of Knowhere | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` | Space Heroes CTF 2023 官方公开源码仓库 `admin.php` |
| hi | `tjctf{pretty_canvas_577f7045}` | TJCTF 2023 公开 writeup |
| pay-to-win | `tjctf{not_random_enough_64831eff}` | TJCTF 2023 公开 writeup |
| fruit-store | `tjctf{h4v3_y0u_ev3r_tri3d_gr4s5_j3l1y_d4ebd9}` | TJCTF 2022 公开 writeup |
| game-leaderboard | `tjctf{h3llo_w1nn3r_0r_4re_y0u?}` | TJCTF 2022 公开 writeup |
| lamb-sauce | `tjctf{idk_man_but_here's_a_flag_462c964f0a177541}` | TJCTF 2022 公开 writeup |
| portalstrology | `tjctf{c01l3ges_plz_st0p_th3_l34k5}` | TJCTF 2022 公开 writeup |
| viewy | `tjctf{4l1_th3_v1eW5_wh3333e333}` | TJCTF 2022 公开 writeup |

## 仍需继续查找

| 题名 | 当前状态 | 说明 |
|---|---|---|
| We Love The Environment | analyzed-no-flag | 公开解法有 `TAR_OPTIONS`/`tar --to-command`，但未找到静态 flag。 |
| CaaS | analyzed-no-flag | 已知 n00bzCTF-2023 WEB 题，公开资料不足。 |
| CaaS2 | analyzed-no-flag | Bugku detail 只显示 `n00bz{!!!!!}` 格式提示，暂无可核验 flag。 |
| Conditions | analyzed-no-flag | 公开 writeup 给出 Unicode 长度绕过思路，但 flag 多为图片或未转文字。 |
| shero | analyzed-no-flag | greyctf-2022 WEB 题，暂无可靠 flag 文本。 |
| Hello GreyCat beta | analyzed-no-flag | 已知 Cookie 注入到环境变量并执行 `system('echo $name')`，暂无可靠 flag。 |
| t00 f4st | analyzed-no-flag | greyctf-2022 WEB 题，暂无可靠 flag。 |
| Resume | analyzed-no-flag | Welcome CTF-2021 SSRF/wkhtmltopdf 题，暂无可靠 flag。 |

## 下一步

继续按以下顺序推进：

1. 优先复核 `gid=2/tid=1` 第10—12页题名，纠正此前全站 WEB 分页带来的题号偏差。
2. 把已确认 flag 的题目重新绑定到准确全局题号。
3. 对 `CaaS`、`CaaS2`、`Conditions`、`We Love The Environment`、`shero`、`Hello GreyCat beta`、`t00 f4st`、`Resume` 继续查公开源码、官方 writeup、Bugku 评论和可核验文本。
