# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成；当前已推进到第180题。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批 | 41—80 | `worklogs/bugku/forward/第41-80题_batch.md`；`cards/pending/bugku/第41-80题_batch.cards.json` | blocked-carded |
| 第三批 | 81—130 | `worklogs/bugku/forward/第81-130题_batch.md`；`cards/pending/bugku/第81-130题_batch.cards.json` | blocked-carded |
| 第四批 | 131—180 | `worklogs/bugku/forward/第131-180题_batch.md`；`cards/pending/bugku/第131-180题_batch.cards.json` | blocked-carded |

## 第131—180题摘要

| 题号段 | 涉及题目 | 赛事/来源 | 状态 |
|---|---|---|---|
| 131—134 | beehive、hintbot、deserbug、unzip | SaplingCTF-2023、CISCN-2023 | blocked-carded |
| 135—142 | b4bycoffee、Apollo Guidance Computer、attack-strategies、robot-best-friend、Sanity Check In Space、Bank of Knowhere、The DEW、profile viewer | 长城杯-2022、Space Heroes CTF-2023、TSG live ctf-10 | blocked-carded |
| 143—149 | back-to-the-past、hi、ez-sql、notes、outdated、pay-to-win、swill-squill | TJCTF-2023 | blocked-carded |
| 150—164 | analects、ascordle、LFI 0、LFI or RCE、RCE 0、SSRF 0、SSTI 0、up to you、fruit-store、game-leaderboard、lamb-sauce、mmocc、photoable、portalstrology、viewy | TJCTF-2022、Securinets-Christmas-CTF-2022 | blocked-carded |
| 165—180 | Agent-007、CooooKiE、Cr4zy-Js0N、F4ke-Upl04d、JW token、LoGiC、Request Basics 1/2/3、Tunisia、baby_sqli、inspector、RCE won't help、flasky、toddlersqli、SS Xperience | Securinets-Friendly-2022、Welcome CTF-2023 | blocked-carded |

## 处理原则
- 能直接从公开题面/评论确认 flag 的写入 solved-carded。
- 需要启动 Bugku 动态容器验证的题目，不编造 flag，统一写入 blocked-carded。
- 每题均已保留题名、赛事、判断方向、通用解法步骤和 JSON 卡字段，后续可由本地 Agent 拆分并导入能力库。

## 下一步
继续第181—230题；优先抓取后续 Bugku WEB 列表页，能直接确认 flag 的写入 solved-carded，不能动态验证的写入 blocked-carded。