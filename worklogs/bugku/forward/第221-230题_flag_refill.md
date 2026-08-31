# Bugku 第221—230题逐题补 flag 记录

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本文件继续第181—230题的 Pass 4 校准结果，专门处理第221—230题。由于 `gid=2/tid=1&page=12` 仍未稳定返回完整缓存，本轮采用两个约束进行校准：

1. Pass 4 已以 `gid=2/tid=1&page=11` 为锚点确认第216—220题为 `Agent-007`、`CooooKiE`、`Cr4zy-Js0N`、`F4ke-Upl04d`、`JW token`。
2. Bugku 全站 WEB 缓存页显示 `JW token` 后续连续为 `LoGiC`、`Request Basics 1`、`Request Basics 2`、`Request Basics 3`、`Tunisia`、`baby_sqli`、`inspector`、`RCE won't help`、`flasky`、`toddlersqli`、`SS Xperience`、`We Love The Environment`。

据此，本轮将第221—230题暂按连续顺序校准为 `LoGiC` 至 `toddlersqli`；后续如 `gid=2/tid=1&page=12` 返回更完整列表，再做最终复核。

## 状态口径

- `solved-carded`：公开 writeup 或官方公开源码中有明确 flag 文本，可写入 `verification.flag`。
- `analyzed-no-flag`：有公开解法或题目信息，但未找到可核验 flag 文本。
- `blocked-no-flag`：只确认题目存在，未找到可靠解法和 flag，需要动态环境或附件验证。
- `outside-range-confirmed`：已确认 flag，但按当前题号校准位于第221—230之后，暂不写入本段题号。

## 本轮汇总

- 第221—230题题名校准：10题。
- solved-carded：2题（第226题 `baby_sqli`、第227题 `inspector`）。
- analyzed-no-flag：2题（第228题 `RCE won't help`、第230题 `toddlersqli`）。
- blocked-no-flag：6题（第221—225题、第229题）。
- 额外确认但超出第221—230范围：第231题候选 `SS Xperience`，flag 已知但暂不写入第221—230。

## 第221—230题逐题结果

| 题号 | 题名 | 赛事 | 状态 | flag / 候选 | 处理说明 |
|---:|---|---|---|---|---|
| 221 | LoGiC | Securinets-Friendly-2022 | blocked-no-flag |  | 只确认题目存在和顺序，未找到可靠公开 flag。 |
| 222 | Request Basics 1 | Securinets-Friendly-2022 | blocked-no-flag |  | 只确认题目存在和顺序，未找到可靠公开 flag。 |
| 223 | Request Basics 2 | Securinets-Friendly-2022 | blocked-no-flag |  | 只确认题目存在和顺序，未找到可靠公开 flag。 |
| 224 | Request Basics 3 | Securinets-Friendly-2022 | blocked-no-flag |  | 只确认题目存在和顺序，未找到可靠公开 flag。 |
| 225 | Tunisia | Securinets-Friendly-2022 | blocked-no-flag |  | 只确认题目存在和顺序，未找到可靠公开 flag。 |
| 226 | baby_sqli | Welcome CTF-2023 | solved-carded | `greyhats{B4by_5qL1_1s_e4sy_4nd_fUn}` | Welcome CTF 2023 公开 writeup 给出登录 payload：用户名 `admin`，密码 `' or 1=1;--`，并给出 flag。 |
| 227 | inspector | Welcome CTF-2023 | solved-carded | `greyhats{1_4m_4n_insp3t0r_n0w}` | Welcome CTF 2023 公开 writeup 从首页注释、CSS、JS 拼接出完整 flag。 |
| 228 | RCE won't help | Welcome CTF-2023 | analyzed-no-flag |  | 公开 writeup 标为 Unsolved；仅给出 SSTI/RCE shell 尝试，无可核验 flag。 |
| 229 | flasky | Welcome CTF-2023 | blocked-no-flag |  | Bugku 缓存确认题目存在；未在公开 Welcome CTF 2023 writeup 中找到对应 flag。 |
| 230 | toddlersqli | Welcome CTF-2023 | analyzed-no-flag |  | 公开 writeup 标为 Unsolved，并附 `toddlersqli_attempt.ipynb`；未找到可核验 flag。 |

## 超出本段但已确认的后续 flag

| 推定题号 | 题名 | 状态 | flag | 处理说明 |
|---:|---|---|---|---|
| 231 | SS Xperience | outside-range-confirmed | `greyhats{b4by_x55_scr1pt1ng_92488c0f2286e33bc1eda97a2beb1a2b}` | Welcome CTF 2023 公开 writeup 给出 XSS 窃取 admin cookie 的 flag；因用户本轮要求第221—230题，暂不并入本段 solved 统计。 |

## 解法转化摘要

- `baby_sqli`：基础 SQL 注入登录绕过，payload 为用户名 `admin`、密码 `' or 1=1;--`。
- `inspector`：前端信息泄露，分别从 HTML 注释、CSS 注释、JS 注释拼接 flag。
- `RCE won't help`：公开资料显示可尝试 Jinja/SSTI 到 `os.popen`，但未找到最终 flag。
- `toddlersqli`：公开资料只有尝试 notebook，无最终 flag。
- `LoGiC`、`Request Basics 1/2/3`、`Tunisia`、`flasky`：待动态环境或更多公开 writeup。

## 下一步

继续第231—240题时，应从 `SS Xperience` 和 `We Love The Environment` 开始，并继续查找 Welcome CTF-2023 后续题、n00bzCTF-2023 `Robots`/`Secret Group` 的准确全局题号。