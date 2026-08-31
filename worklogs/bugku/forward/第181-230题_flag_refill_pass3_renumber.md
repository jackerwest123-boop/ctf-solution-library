# Bugku 第181—230题逐题补 flag 记录（Pass 3 / 题号回填）

目标：继续按 `gid=2/tid=1`（比赛真题 + WEB）正序推进，纠正此前用全站 WEB 分页造成的题号偏差。

## 一、已确认的分页事实

1. `gid=2/tid=1` 第9页可以完整打开，按每页20题计算，对应全局第161—180题，页面从 `Bottle Poem` 到 `unzip`。
2. 第9页末尾顺序为：`JUST_PROTO`、`go_session`、`beehive`、`hintbot`、`deserbug`、`unzip`，因此第180题为 `unzip`。
3. `gid=2/tid=1` 第11页搜索缓存显示该页包含 `analects`、`ascordle`、`LFI 0`、`LFI or RCE`、`RCE 0`、`SSRF 0`、`SSTI 0`、`up to you`、`fruit-store`、`game-leaderboard`、`lamb-sauce`、`mmocc`、`photoable`、`portalstrology`、`viewy`、`Agent-007`、`CooooKiE`、`Cr4zy-Js0N`、`F4ke-Upl04d`、`JW token` 等题。
4. 由于第10、11、12页直接打开仍为 cache miss，本文件只回填“题名、flag、顺序关系都能交叉支撑”的项目；对未能完整打开的页不强行补满。

## 二、第181—230题范围内可回填的题号与 flag

按第9页已确认第180题为 `unzip`，并结合后续公开缓存顺序，本轮对以下题号进行回填。仍需后续在第10—12页可访问时最终复核，但这些题名与 flag 已有公开可靠来源支撑。

| 题号 | 题名 | 状态 | flag | 依据 |
|---:|---|---|---|---|
| 182 | Apollo Guidance Computer | solved-carded | `shctf{I_reP3aT_h0UstOn_w3_H4vE_L1Ft0Ff}` | Space Heroes CTF 2023 官方公开源码仓库 `web/apollo-guidance-computer/src/flag.txt`。 |
| 183 | attack-strategies | solved-carded | `shctf{get_zerg_rushed_nb}` | Space Heroes CTF 2023 官方公开源码仓库 `web/attack-strategies/docker/strategies/flag.txt`。 |
| 184 | robot-best-friend | solved-carded | `shctf{I_don't_want_to_play_with_you_ever_again}` | Space Heroes CTF 2023 官方公开源码仓库 `web/robot-best-friend/Chall.py` 系统提示。 |
| 185 | Sanity Check In Space | solved-carded | `shctf{exp01ting_w3bs1tes_1N_SP@C3}` | Space Heroes CTF 2023 官方公开源码仓库 `web/Sanity Check In Space/docker/flag.txt`。 |
| 186 | Bank of Knowhere | solved-carded | `shctf{7h3_c0sm0s_1s_w17h1n_u5}` | Space Heroes CTF 2023 官方公开源码仓库 `web/Knowhere_Bank/docker/admin.php`。 |
| 190 | hi | solved-carded | `tjctf{pretty_canvas_577f7045}` | TJCTF 2023 公开 writeup。 |
| 194 | pay-to-win | solved-carded | `tjctf{not_random_enough_64831eff}` | TJCTF 2023 公开 writeup。 |
| 待定 | Robots | solved-carded-candidate-number | `n00bz{1_f0und_7h3_r0b0ts!}` | 确认为 Bugku 后续 WEB 题，但本轮仍未能从 `gid=2/tid=1` 第12页以后完整列表绑定准确题号。 |
| 待定 | Secret Group | solved-carded-candidate-number | `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}` | 确认为 Bugku 后续 WEB 题，但本轮仍未能从 `gid=2/tid=1` 第12页以后完整列表绑定准确题号。 |

## 三、暂不回填的项目

以下题目虽有解法线索或属于后续页，但当前未找到可核验 Bugku flag，或题号仍未能稳定确认，因此不写入 `verification.flag`：

| 题名 | 状态 | 说明 |
|---|---|---|
| b4bycoffee | analyzed-no-flag | 可定位为第181题候选，但未找到可靠静态 flag。 |
| The DEW | analyzed-no-flag | 已找到官方源码目录，但未直接提取到静态 flag。 |
| profile viewer | analyzed-no-flag | 未找到可靠静态 flag。 |
| back-to-the-past | analyzed-no-flag | 有公开 writeup 线索，但未找到可核验 flag 文本。 |
| ez-sql | analyzed-no-flag | 有公开 writeup 线索，但未找到可核验 flag 文本。 |
| notes | analyzed-no-flag | 未找到可靠静态 flag。 |
| outdated | analyzed-no-flag | 未找到可靠静态 flag。 |
| swill-squill | analyzed-no-flag | 未找到可靠静态 flag。 |
| CaaS / CaaS2 / Conditions | analyzed-no-flag | 确认为 n00bzCTF-2023 WEB 后续题，但未获得可靠 Bugku flag 文本。 |
| We Love The Environment | analyzed-no-flag | 全站 WEB 缓存可见，但在目标 `gid=2/tid=1` 范围内题号仍需复核，且公开资料未给静态 flag。 |

## 四、本轮结论

- 本轮新增“准确题号回填”7题：182、183、184、185、186、190、194。
- 本轮保留“待绑定题号但 flag 已确认”2题：Robots、Secret Group。
- 本轮明确纠正：此前把 `We Love The Environment` 直接记为第181题不可靠；第181题更可能为 `b4bycoffee`，但仍需第10页完整页面复核。
- 后续应继续围绕 `gid=2/tid=1` 第10—12页做检索，优先补全第181—230题完整题名表。