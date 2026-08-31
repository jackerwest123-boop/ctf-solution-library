# Bugku 第005轮-B：0081—0100 契约文件创建/升级

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5

## 执行口径

- 本次只处理第0081—0100题。
- 逐题创建 canonical `README.md` 与 `card.json`。
- 优先复核 0098—0100 的 detail URL，并继续复核 0081、0087、0088、0093、0094、0096 的 cache-miss detail URL。
- 未取得原始附件或真实授权题目环境输出的题目，不能标 `solved_verified`。
- 本次没有新增 `solved_verified`。

## 完成清单

| 题号 | 题名 | 状态 | canonical path | detail URL |
|---:|---|---|---|---|
| 0081 | Upload 0 | method_only | bugku/0081_upload_0 | https://ctf.bugku.com/challenges/detail/id/465.html |
| 0082 | Upload 1 | method_only | bugku/0082_upload_1 | https://ctf.bugku.com/challenges/detail/id/466.html |
| 0083 | Upload 2 | method_only | bugku/0083_upload_2 | https://ctf.bugku.com/challenges/detail/id/467.html |
| 0084 | Virtual Shop | method_only | bugku/0084_virtual_shop | https://ctf.bugku.com/challenges/detail/id/471.html |
| 0085 | Virtual Shop 2 | method_only | bugku/0085_virtual_shop_2 | https://ctf.bugku.com/challenges/detail/id/472.html |
| 0086 | Sparta | method_only | bugku/0086_sparta | https://ctf.bugku.com/challenges/detail/id/520.html |
| 0087 | strpos and substr | method_only | bugku/0087_strpos_and_substr | https://ctf.bugku.com/challenges/detail/id/521.html |
| 0088 | web1 | method_only | bugku/0088_web1 | https://ctf.bugku.com/challenges/detail/id/542.html |
| 0089 | checkin | method_only | bugku/0089_checkin | https://ctf.bugku.com/challenges/detail/id/543.html |
| 0090 | jwt | method_only | bugku/0090_jwt | https://ctf.bugku.com/challenges/detail/id/544.html |
| 0091 | easy-pop | method_only | bugku/0091_easy_pop | https://ctf.bugku.com/challenges/detail/id/545.html |
| 0092 | command-injection | method_only | bugku/0092_command_injection | https://ctf.bugku.com/challenges/detail/id/546.html |
| 0093 | 逃逸 | method_only | bugku/0093_escape | https://ctf.bugku.com/challenges/detail/id/547.html |
| 0094 | Make Me Cry | method_only | bugku/0094_make_me_cry | https://ctf.bugku.com/challenges/detail/id/568.html |
| 0095 | ezlogin | method_only | bugku/0095_ezlogin | https://ctf.bugku.com/challenges/detail/id/577.html |
| 0096 | loginjection | method_only | bugku/0096_loginjection | https://ctf.bugku.com/challenges/detail/id/578.html |
| 0097 | superezpop | method_only | bugku/0097_superezpop | https://ctf.bugku.com/challenges/detail/id/579.html |
| 0098 | 从零开始的勇士之路 | method_only | bugku/0098_zero_to_hero | https://ctf.bugku.com/challenges/detail/id/580.html |
| 0099 | 走一步，再走亿步 | method_only | bugku/0099_one_step_many_steps | 待复核 |
| 0100 | 异或的密件 | method_only | bugku/0100_xor_secret | 待复核 |

## detail URL 复核

- 0098 `从零开始的勇士之路` 已复核为 `id/580.html`，详情页显示 NUAACTF 2022、Crypto、下载项，并有仿射密码评论线索。
- 0099、0100 在 NUAACTF-2022 标签页和全站分页缓存中确认题名、赛事、类型和顺序，但本轮未复核到可确认的 detail URL，保持待复核。
- 0081、0087、0088、0093、0094、0096 的 URL 保留自列表点击/cache-miss 结果；未写入执行验证。

## 统计

- solved_verified：0
- solved_unverified：0
- method_only：20
- blocked：0

## 验收说明

- 0081—0100 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 所有题均保持 `verification.executed=false`，没有伪造 flag 或执行输出。
- 0099、0100 的 detail URL 待后续继续复核，但不影响本轮契约卡建档。

## 下一步完整提示

进入第006轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=6` 的第0101—0120题做清单建档。具体任务：逐题记录全局题号、`page_index`、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_006_page_006.md`。本阶段只做 page=6 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第006轮-B，对第0101—0120题逐题生成或升级 canonical README/card。
