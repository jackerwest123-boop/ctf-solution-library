# Bugku 第41—80题逐题补 flag 记录

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本文件是对此前 `第41-80题_batch.md` 的返工补 flag。只把能从 Bugku 页面、公开 writeup 或可核验公开资料中直接确认的 flag 计入 solved-carded；存在冲突候选的题目不计入 solved。

## 状态口径

- `solved-carded`：已找到明确 flag 文本，并已写入补充卡。
- `candidate-conflict`：找到多个候选或有“flag error/不正确”等冲突，暂不计入已解出。
- `analyzed-no-flag`：有明确解法线索，但公开资料没有可抄录的 flag 文本。
- `blocked-no-flag`：未找到可靠公开 flag，仍需启动 Bugku 动态环境或读取附件验证。

## 本轮汇总

- solved-carded：7题（第42、46、53、54、59、61、64题）。
- candidate-conflict：2题（第44、48题）。
- analyzed-no-flag：10题。
- blocked-no-flag：21题。

## 逐题结果

| 题号 | 题名 | 状态 | flag / 候选 | 证据与处理 |
|---:|---|---|---|---|
| 41 | superezpop | analyzed-no-flag | `` | Bugku detail shows NUAACTF{} and comments suggest /flag.php/POP chain; no public flag text found. |
| 42 | ？？？？ | solved-carded | `0xGame{L1nux_i5_S0_gO0D_I_th1nK}` | Bugku public writeup result. |
| 43 | broken motto | analyzed-no-flag | `` | MiaoTony writeup gives session serialization method; flag appears in image/no extractable text. |
| 44 | cookies | candidate-conflict | `0xGame{b3c48a2f54bb49c60a0d085a305e80ee} / 0xGame{b3c48a2f54bb49c60a0d08b76bdc87db}` | Bugku comments contain conflicting candidates; not counted solved. |
| 45 | close eyes | blocked-no-flag | `` | Only list/user solve records found; no reliable flag text. |
| 46 | edr | solved-carded | `0xGame{S4n9f0r_3dR_c4N_Rce_reC3n7_D4y}` | MiaoTony writeup gives payload and flag. |
| 47 | getpost | analyzed-no-flag | `` | Bugku list/users confirm solved counts; no reliable flag text found. |
| 48 | intval | candidate-conflict | `0xGame{947eae96fe415cbc6eab17d99261dead} / 0xGame{947eae96fe415cbc6eab176f15dd98b1}` | Bugku comments and writeups conflict; not counted solved. |
| 49 | jwt | analyzed-no-flag | `` | MiaoTony writeup gives c-jwt-cracker/secret njupt/admin; flag is image/no text. |
| 50 | just_login | analyzed-no-flag | `` | Bugku comments indicate phpinfo.php reveals flag; no public flag text. |
| 51 | read flag | blocked-no-flag | `` | No reliable public flag text found in searched sources. |
| 52 | wh1sper's_secret_garden | blocked-no-flag | `` | No reliable public flag text found in searched sources. |
| 53 | robots | solved-carded | `0xGame{now_you_k0nw_robots_Protocol}` | Bugku comments show /robots.txt and flag. |
| 54 | switch | solved-carded | `0xGame{S0me_pHp_tR1cKs_u_G3t_1t}` | MiaoTony writeup shows decoded flag. |
| 55 | view source | analyzed-no-flag | `` | Public writeup says F12/source reveals flag but does not provide text. |
| 56 | booli | blocked-no-flag | `` | No reliable public flag text found. |
| 57 | bug1 | blocked-no-flag | `` | No reliable public flag text found. |
| 58 | bug2 | blocked-no-flag | `` | No reliable public flag text found. |
| 59 | command | solved-carded | `0xGame{L1nux_cmd_1s_3a5y_t0_you!!!}` | Bugku comment gives command sequence and flag. |
| 60 | diao图管理器(已跑路 | blocked-no-flag | `` | No reliable public flag text found. |
| 61 | upload | solved-carded | `0xGame{upl0ad_f1le_causes_danger!!!}` | Anyyy writeup shows upload/include route and flag. |
| 62 | header | analyzed-no-flag | `` | 0xGame2021 writeup gives request header method; no flag text. |
| 63 | proto | blocked-no-flag | `` | No reliable public flag text found. |
| 64 | robot | solved-carded | `0xGame{Rob0t_le4ks_seCr3t}` | Bugku comments and 0xGame2021 writeup show robots path and flag. |
| 65 | search | analyzed-no-flag | `` | 0xGame2021 writeup gives broad method; no flag text. |
| 66 | session | analyzed-no-flag | `` | 0xGame2021 writeup gives Flask session forging method; no flag text. |
| 67 | ssti | analyzed-no-flag | `` | 0xGame2021 writeup gives SSTI method; no flag text. |
| 68 | Become Admin | blocked-no-flag | `` | Bugku/CTFtime pages identify task/writeup link; no public flag text retrieved. |
| 69 | CringeNcoder | blocked-no-flag | `` | CTFtime/Bugku identify task/writeups; no public flag text retrieved. |
| 70 | It’s paid | blocked-no-flag | `` | CTFtime identifies task/writeups; no public flag text retrieved. |
| 71 | Meeting | blocked-no-flag | `` | Bugku list only; no reliable flag text found. |
| 72 | Recovery | blocked-no-flag | `` | CTFtime identifies writeups; no public flag text retrieved. |
| 73 | A Simple Calculator | blocked-no-flag | `` | No reliable public flag text found. |
| 74 | real ez node | blocked-no-flag | `` | No reliable public flag text found. |
| 75 | easy api | blocked-no-flag | `` | No reliable public flag text found. |
| 76 | Node Magical Login | blocked-no-flag | `` | No reliable public flag text found. |
| 77 | MemeHub | blocked-no-flag | `` | No reliable public flag text found. |
| 78 | Trashbin | blocked-no-flag | `` | No reliable public flag text found. |
| 79 | slasher | blocked-no-flag | `` | No reliable public flag text found. |
| 80 | passparser | blocked-no-flag | `` | No reliable public flag text found. |

## 已确认 flag

- 第42题 ？？？？：`0xGame{L1nux_i5_S0_gO0D_I_th1nK}`。
- 第46题 edr：`0xGame{S4n9f0r_3dR_c4N_Rce_reC3n7_D4y}`。
- 第53题 robots：`0xGame{now_you_k0nw_robots_Protocol}`。
- 第54题 switch：`0xGame{S0me_pHp_tR1cKs_u_G3t_1t}`。
- 第59题 command：`0xGame{L1nux_cmd_1s_3a5y_t0_you!!!}`。
- 第61题 upload：`0xGame{upl0ad_f1le_causes_danger!!!}`。
- 第64题 robot：`0xGame{Rob0t_le4ks_seCr3t}`。

## 后续处理

1. 对 candidate-conflict 题，不在 `verification.flag` 写死最终值，需以 Bugku 当前环境提交验证为准。
2. 对 analyzed-no-flag 题，优先启动动态环境复现；若页面把 flag 渲染成图片，需要截图/人工识别后回填。
3. 对 blocked-no-flag 题，继续补抓 Bugku 评论、WP库和赛事原始 writeup。