# Bugku 第181—230题逐题补 flag 记录（Pass 1）

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本文件是继续第181—230题逐题补 flag 的第一轮返工记录。本轮坚持“可核验才写入 verification.flag”：能从 Bugku 页面、公开评论、公开 writeup 或官方公开源码仓库直接确认的 flag 才计为 `solved-carded`；只有解法思路、动态环境输出、格式提示或无法核验的内容不计入 solved。

## 本轮重要限制

- 通过公开缓存可以确认 Bugku WEB 第15页最后一题为 `We Love The Environment`，承接上一批第180题 `SS Xperience` 后，对应第181题。
- 当前无法直接打开 Bugku 第16—18页列表，公开搜索缓存也未返回完整列表，因此第182—230题的全局题号暂不能可靠枚举。
- 本轮没有强行编造第182—230题名或 flag；仅对能确定属于 Bugku 后续 WEB 题库的公开题目做“候选后续题”补 flag，并标注“全局题号待复核”。

## 状态口径

- `solved-carded`：已找到明确 flag 文本，并可由公开 writeup 或公开题目页支撑。
- `analyzed-no-flag`：有明确解法线索，但公开资料没有可抄录且可核验的 Bugku flag。
- `candidate-later-web`：确认是 Bugku 后续 WEB 题，但第181—230中的全局题号待第16—18页列表复核。
- `blocked-enumeration`：未能可靠枚举题名，暂不写 flag。

## 本轮汇总

- 第181题已定位：1题。
- 第181题已确认 flag：0题。
- 候选后续 WEB 题中已确认 flag：2题（`Robots`、`Secret Group`，均为 n00bzCTF-2023 WEB）。
- 需要第16—18页列表复核题号：49题。

## 已确认第181题

| 题号 | 题名 | 赛事 | 状态 | flag / 候选 | 处理说明 |
|---:|---|---|---|---|---|
| 181 | We Love The Environment | Welcome CTF-2023 | analyzed-no-flag |  | 公开 writeup 给出 `TAR_OPTIONS`/`tar --to-command` 等利用方法，但未给出静态 flag；题目需要在线运行 `/readflag GIVEFLAGPLS`，未能在公开资料中直接确认 Bugku flag。 |

## 候选后续 WEB 题补 flag（全局题号待复核）

| 题名 | 赛事 | 状态 | flag / 候选 | 依据与说明 |
|---|---|---|---|---|
| shero | greyctf-2022 | analyzed-no-flag |  | Bugku greyctf tag 页显示该 WEB 题，但未找到可核验 flag。 |
| Hello GreyCat beta | greyctf-2022 | analyzed-no-flag |  | Bugku 详情页给出题面：Cookie 注入到环境变量 `name` 并执行 `system('echo $name')`，但无公开 flag。 |
| t00 f4st | greyctf-2022 | analyzed-no-flag |  | Bugku greyctf tag 页显示该 WEB 题，但未找到可核验 flag。 |
| Resume | Welcome CTF-2021 | analyzed-no-flag |  | Bugku 详情页给出 SSRF/wkhtmltopdf 本地文件读取题面，公开 WP 摘要没有直接 flag。 |
| Curl as a Service | n00bzCTF-2022 | analyzed-no-flag |  | CTFtime 与 Bugku WP 摘要均说明 `urllib` 支持 `file://`，可读取 `/proc/self/cwd/challenge.py` 找 flag 路径；未找到可核验最终 flag 文本。 |
| CaaS | n00bzCTF-2023 | analyzed-no-flag |  | 公开 writeup 给出 SSTI 思路，未在可索引文本中取得稳定 flag。 |
| CaaS2 | n00bzCTF-2023 | analyzed-no-flag |  | Bugku 详情页只给出格式 `n00bz{!!!!!}`，无真实 flag；公开 writeup 给出 SSTI 思路但未提取可核验 flag。 |
| Conditions | n00bzCTF-2023 | analyzed-no-flag |  | 公开 writeup 提到使用 Unicode 特殊字符绕过长度/upper 逻辑，但未在可索引文本中取得稳定 flag。 |
| Robots | n00bzCTF-2023 | solved-carded-candidate-number | `n00bz{1_f0und_7h3_r0b0ts!}` | 公开 n00bzCTF-2023 writeup 给出访问 `/robots.txt` 后得到该 flag；Bugku 页面显示该题为 n00bzCTF-2023 WEB 后续题。 |
| Secret Group | n00bzCTF-2023 | solved-carded-candidate-number | `n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}` | 公开 n00bzCTF-2023 writeup 给出按要求修改多组 HTTP 头后得到该 flag；Bugku 页面显示该题为 n00bzCTF-2023 WEB 后续题。 |

## 结论

第181—230题第一轮补 flag 已开始，但目前只能可靠确认第181题 `We Love The Environment`。第182—230题的准确题名和全局题号需要 Bugku 第16—18页列表或可用缓存支持，暂不编造。已把能确认属于后续 WEB 题的公开候选题整理到本文件，其中 `Robots` 与 `Secret Group` 已有可核验 flag，但在未复核全局编号前不写成“第XX题已解出”。

## 下一步

1. 继续检索 Bugku 第16—18页列表缓存，补齐第182—230题题名。
2. 一旦题号可确认，立刻把 `Robots`、`Secret Group` 的 flag 写入对应全局题号的 `verification.flag`。
3. 对 `We Love The Environment`、`Curl as a Service`、`Resume`、`CaaS/CaaS2/Conditions` 等仅有解法的题，继续寻找可核验 flag 或等待动态环境验证。
