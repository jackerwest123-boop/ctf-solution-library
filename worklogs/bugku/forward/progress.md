# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku 比赛真题 WEB 题库第31题至第80题。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成，本批从第31题开始。

## 已确认题号范围
根据 Bugku 题库分页，当前页每页20题；第2页第11题至第20题对应全局第31题至第40题。

| 全局题号 | 题名 | Bugku detail id | 赛事 | 类型 | 当前状态 | 输出 |
|---|---|---:|---|---|---|---|
| 31 | strpos and substr | 521 | zh3r0-v2 | WEB | blocked-carded | `worklogs/bugku/forward/第31题_strpos-and-substr.md`；`cards/pending/bugku/第31题_strpos-and-substr.card.json` |
| 32 | web1 | 542 | NUAACTF-2018 | WEB | blocked-carded | `worklogs/bugku/forward/第32题_web1.md`；`cards/pending/bugku/第32题_web1.card.json` |
| 33 | checkin | 543 | NUAACTF-2020 | WEB | solved-carded | `worklogs/bugku/forward/第33题_checkin.md`；`cards/pending/bugku/第33题_checkin.card.json` |
| 34 | jwt | 544 | NUAACTF-2020 | WEB | blocked-carded | `worklogs/bugku/forward/第34题_jwt.md`；`cards/pending/bugku/第34题_jwt.card.json` |
| 35 | easy-pop | 545 | NUAACTF-2020 | WEB | blocked-carded | `worklogs/bugku/forward/第35题_easy-pop.md`；`cards/pending/bugku/第35题_easy-pop.card.json` |
| 36 | command-injection | 546 | NUAACTF-2020 | WEB | solved-carded | `worklogs/bugku/forward/第36题_command-injection.md`；`cards/pending/bugku/第36题_command-injection.card.json` |
| 37 | 逃逸 | 547 | NUAACTF-2020 | WEB | blocked-carded | `worklogs/bugku/forward/第37题_逃逸.md`；`cards/pending/bugku/第37题_逃逸.card.json` |
| 38 | Make Me Cry | 568 | NUAACTF-2021 | WEB | blocked-carded | `worklogs/bugku/forward/第38题_make-me-cry.md`；`cards/pending/bugku/第38题_make-me-cry.card.json` |
| 39 | ezlogin | 577 | NUAACTF-2022 | WEB | blocked-carded | `worklogs/bugku/forward/第39题_ezlogin.md`；`cards/pending/bugku/第39题_ezlogin.card.json` |
| 40 | loginjection | 578 | NUAACTF-2022 | WEB | blocked-carded | `worklogs/bugku/forward/第40题_loginjection.md`；`cards/pending/bugku/第40题_loginjection.card.json` |

## 最近处理结果
- 第33题 checkin：公开页面评论区可见 flag，已生成正式 Markdown 和 JSON 卡。
- 第36题 command-injection：公开页面评论区可见 flag，已生成正式 Markdown 和 JSON 卡。
- 第31、32、34、35、37、38、39、40题：已根据 Bugku 页面、题面和公开评论线索建立 Markdown 与 JSON 卡；因当前环境无法启动动态场景，未编造最终 flag，统一标记 blocked-carded，等待场景复现补全 `verification.flag`。

## 下一步
1. 继续处理第41题起；优先确认第41—80题列表。
2. 已初步确认第41题可能为 `superezpop`，需以 Bugku WEB 筛选页或赛事 tag 页复核。
3. 对能从公开题面/评论直接确定 flag 的题目，直接生成 solved 卡；对必须启动动态场景的题目，生成 blocked-carded 卡并保留复现步骤。

## 输出规范
每题 Markdown 输出：`worklogs/bugku/forward/第XX题_题名.md`

每题 JSON 卡输出：`cards/pending/bugku/第XX题_题名.card.json`

每5题更新一次本文件。
