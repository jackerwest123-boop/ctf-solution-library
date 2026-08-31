# Bugku 第003轮-B：0041—0060 契约文件创建/升级

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=3

## 执行口径

- 本次只处理第0041—0060题。
- 逐题创建 canonical `README.md` 与 `card.json`。
- 优先复核 0050—0060 的 detail URL。
- 未取得原始附件或真实场景输出的题目，不能标 `solved_verified`。
- 本次没有新增 `solved_verified`。

## 完成清单

| 题号 | 题名 | 状态 | canonical path | detail URL |
|---:|---|---|---|---|
| 0041 | 重重flag背后隐藏的秘密 | method_only | bugku/0041_many_flags_secret | https://ctf.bugku.com/challenges/detail/id/268.html |
| 0042 | 犯人留下了信息 | method_only | bugku/0042_criminal_left_info | https://ctf.bugku.com/challenges/detail/id/269.html |
| 0043 | 弗拉戈在哪里2 | method_only | bugku/0043_where_is_flago_2 | https://ctf.bugku.com/challenges/detail/id/270.html |
| 0044 | 弗拉戈在哪里 | method_only | bugku/0044_where_is_flago | https://ctf.bugku.com/challenges/detail/id/271.html |
| 0045 | 1-advance | method_only | bugku/0045_1_advance | https://ctf.bugku.com/challenges/detail/id/272.html |
| 0046 | 1-blend | method_only | bugku/0046_1_blend | https://ctf.bugku.com/challenges/detail/id/273.html |
| 0047 | 1-Beijing | method_only | bugku/0047_1_beijing | https://ctf.bugku.com/challenges/detail/id/274.html |
| 0048 | 1-minified | method_only | bugku/0048_1_minified | https://ctf.bugku.com/challenges/detail/id/275.html |
| 0049 | 1-clip | method_only | bugku/0049_1_clip | https://ctf.bugku.com/challenges/detail/id/276.html |
| 0050 | 青龙组-crypto091 | method_only | bugku/0050_qinglong_crypto091 | https://ctf.bugku.com/challenges/detail/id/1449.html |
| 0051 | 青龙组-david_homework | method_only | bugku/0051_qinglong_david_homework | https://ctf.bugku.com/challenges/detail/id/1450.html |
| 0052 | 青龙组-grasshopper | method_only | bugku/0052_qinglong_grasshopper | https://ctf.bugku.com/challenges/detail/id/1451.html |
| 0053 | 青龙组-fakeshell | method_only | bugku/0053_qinglong_fakeshell | https://ctf.bugku.com/challenges/detail/id/1452.html |
| 0054 | 青龙组-Handmake | method_only | bugku/0054_qinglong_handmake | https://ctf.bugku.com/challenges/detail/id/1453.html |
| 0055 | 别开，测试题目 | blocked | bugku/0055_do_not_open_test | 待复核 |
| 0056 | abstract_art | method_only | bugku/0056_abstract_art | https://ctf.bugku.com/challenges/detail/id/402.html |
| 0057 | inspect-me | method_only | bugku/0057_inspect_me | https://ctf.bugku.com/challenges/detail/id/403.html |
| 0058 | my-first-sqli | method_only | bugku/0058_my_first_sqli | https://ctf.bugku.com/challenges/detail/id/404.html |
| 0059 | post-the-get | method_only | bugku/0059_post_the_get | https://ctf.bugku.com/challenges/detail/id/405.html |
| 0060 | sqli-0x1 | method_only | bugku/0060_sqli_0x1 | https://ctf.bugku.com/challenges/detail/id/406.html |

## detail URL 复核

- 0050—0054 由 Bugku 网鼎杯标签页链接复核为 `id/1449.html`—`id/1453.html`。
- 0055 `别开，测试题目` 仅在公开索引缓存中出现，未能复核 detail URL，保持 `blocked`。
- 0056 `abstract_art` 复核为 `id/402.html`；0057—0060 分别复核为 `id/403.html`—`id/406.html`。

## 统计

- solved_verified：0
- solved_unverified：0
- method_only：19
- blocked：1

## 验收说明

- 0041—0060 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 所有未执行题均保持 `verification.executed=false`，没有伪造 flag 或执行输出。
- 第0055题因属于测试题且 detail URL 未复核，保持 `blocked`。
- 其余题保留可复用方法框架，后续取得附件或启动场景后再补 solver/self-test/真实验证。

## 下一步完整提示

进入第004轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=4` 的第0061—0080题做清单建档。具体任务：逐题记录全局题号、`page_index`、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_004_page_004.md`。本阶段只做 page=4 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第004轮-B，对第0061—0080题逐题生成或升级 canonical README/card。
