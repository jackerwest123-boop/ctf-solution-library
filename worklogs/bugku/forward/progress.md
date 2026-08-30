# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku 比赛真题 WEB 题库第31题至第80题。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成，本批从第31题开始。

## 已确认题号范围
根据 Bugku 题库分页，当前页每页20题；第2页第11题至第20题对应全局第31题至第40题。

| 全局题号 | 题名 | Bugku detail id | 赛事 | 类型 | 当前状态 | 备注 |
|---|---|---:|---|---|---|---|
| 31 | strpos and substr | 521 | zh3r0-v2 | WEB | queued | detail 页面当前未能抓取，待二次访问 |
| 32 | web1 | 542 | NUAACTF-2018 | WEB | queued | detail 页面当前未能抓取，待二次访问 |
| 33 | checkin | 543 | NUAACTF-2020 | WEB | solved-from-page | 页面描述为 nuaactf{}，评论区可见 flag：nuaactf{we1cOme_to_NuaAcTF} |
| 34 | jwt | 544 | NUAACTF-2020 | WEB | analyzed | JWT 伪造，评论提示 secret key 为 NuAa，需启动场景复现获取 flag |
| 35 | easy-pop | 545 | NUAACTF-2020 | WEB | analyzed | PHP 反序列化 POP，评论区给出序列化 payload，需启动场景复现获取 flag |
| 36 | command-injection | 546 | NUAACTF-2020 | WEB | solved-from-page | 文件包含 / createfun 调用，评论区可见 flag：nuaactf{php_IS_thE_best_language} |
| 37 | 逃逸 | 547 | NUAACTF-2020 | WEB | queued | detail 页面当前未能抓取，待二次访问 |
| 38 | Make Me Cry | 568 | NUAACTF-2021 | WEB | queued | detail 页面当前未能抓取，待二次访问 |
| 39 | ezlogin | 577 | NUAACTF-2022 | WEB | analyzed | PHP 数组 MD5 相等 + 文件包含，flag 页面路径为 /answer/flagggg，需启动场景复现获取 flag |
| 40 | loginjection | unknown | NUAACTF-2022 | WEB | queued | detail 页面当前未能抓取，待二次访问 |

## 下一步
1. 为第33、36题生成正式 Markdown 解题记录和 JSON 解法卡。
2. 对第34、35、39题按评论和题面线索构造通用方法卡，flag 暂标 blocked，等待场景可访问后验证。
3. 继续抓取第41题至第80题列表；若分页抓取失败，改用题名搜索和赛事 tag 页补齐。

## 输出规范
每题 Markdown 输出：`worklogs/bugku/forward/第XX题_题名.md`

每题 JSON 卡输出：`cards/pending/bugku/第XX题_题名.card.json`

每5题更新一次本文件。
