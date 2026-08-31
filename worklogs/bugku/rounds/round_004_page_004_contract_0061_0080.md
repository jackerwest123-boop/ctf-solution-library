# Bugku 第004轮-B：0061—0080 契约文件创建/升级

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=4

## 执行口径

- 本次只处理第0061—0080题。
- 逐题创建 canonical `README.md` 与 `card.json`。
- 优先复核 0066、0067、0071、0073—0080 的 detail URL；本轮保留从列表链接/缓存得到的 URL，并在卡片中标注未执行。
- 未取得原始附件或真实授权题目环境输出的题目，不能标 `solved_verified`。
- 本次没有新增 `solved_verified`。

## 完成清单

| 题号 | 题名 | 状态 | canonical path | detail URL |
|---:|---|---|---|---|
| 0061 | baby lfi | method_only | bugku/0061_baby_lfi | https://ctf.bugku.com/challenges/detail/id/425.html |
| 0062 | baby lfi 2 | method_only | bugku/0062_baby_lfi_2 | https://ctf.bugku.com/challenges/detail/id/426.html |
| 0063 | challenge-creator | method_only | bugku/0063_challenge_creator | https://ctf.bugku.com/challenges/detail/id/427.html |
| 0064 | HEADache | method_only | bugku/0064_headache | https://ctf.bugku.com/challenges/detail/id/428.html |
| 0065 | lfi | method_only | bugku/0065_lfi | https://ctf.bugku.com/challenges/detail/id/429.html |
| 0066 | nextGen 1 | method_only | bugku/0066_nextgen_1 | https://ctf.bugku.com/challenges/detail/id/430.html |
| 0067 | nextGen 2 | method_only | bugku/0067_nextgen_2 | https://ctf.bugku.com/challenges/detail/id/431.html |
| 0068 | Whois | method_only | bugku/0068_whois | https://ctf.bugku.com/challenges/detail/id/432.html |
| 0069 | adversal | method_only | bugku/0069_adversal | https://ctf.bugku.com/challenges/detail/id/445.html |
| 0070 | filter-madness | method_only | bugku/0070_filter_madness | https://ctf.bugku.com/challenges/detail/id/450.html |
| 0071 | charlottesweb | method_only | bugku/0071_charlottesweb | https://ctf.bugku.com/challenges/detail/id/451.html |
| 0072 | zombie-101 | method_only | bugku/0072_zombie_101 | https://ctf.bugku.com/challenges/detail/id/453.html |
| 0073 | zombie-201 | method_only | bugku/0073_zombie_201 | https://ctf.bugku.com/challenges/detail/id/454.html |
| 0074 | zombie-301 | method_only | bugku/0074_zombie_301 | https://ctf.bugku.com/challenges/detail/id/455.html |
| 0075 | zombie-401 | method_only | bugku/0075_zombie_401 | https://ctf.bugku.com/challenges/detail/id/456.html |
| 0076 | just-work-type | method_only | bugku/0076_just_work_type | https://ctf.bugku.com/challenges/detail/id/460.html |
| 0077 | simple web app | method_only | bugku/0077_simple_web_app | https://ctf.bugku.com/challenges/detail/id/461.html |
| 0078 | t3lEpoRt | method_only | bugku/0078_t3leport | https://ctf.bugku.com/challenges/detail/id/462.html |
| 0079 | maSQLsh | method_only | bugku/0079_masqlsh | https://ctf.bugku.com/challenges/detail/id/463.html |
| 0080 | maSQLsh2 | method_only | bugku/0080_masqlsh2 | https://ctf.bugku.com/challenges/detail/id/464.html |

## 统计

- solved_verified：0
- solved_unverified：0
- method_only：20
- blocked：0

## 验收说明

- 0061—0080 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 所有题均保持 `verification.executed=false`，没有伪造 flag 或执行输出。
- 0066、0067、0071、0073—0080 的 detail URL 按列表链接/缓存保留；未把 cache-miss 误写为已执行验证。

## 下一步完整提示

进入第005轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=5` 的第0081—0100题做清单建档。具体任务：逐题记录全局题号、`page_index`、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_005_page_005.md`。本阶段只做 page=5 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第005轮-B，对第0081—0100题逐题生成或升级 canonical README/card。
