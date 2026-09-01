# Bugku 比赛真题全题库第006轮-A：page=6 清单建档

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=6

## 本轮执行口径

- 本阶段只做 page=6 的清单建档。
- 不解题，不创建题目 README/card。
- 全局编号规则：`global_no = (page - 1) * 20 + page_index`。
- `gid=2.html?page=6` 直接页未能稳定读取，本轮使用 Bugku 全站分页缓存、比赛真题标签缓存、类型页缓存和题目详情页点击结果交叉整理。
- 0101—0118 主要承接全站分页 `challenges/index?page=21` 中 `异或的密件` 后续条目；0119—0120 由 MISC 类型页中 `Hugtto!` 后续条目补齐。

## 第0101—0120题清单

| global_no | page_index | 题名 | 赛事 | 类型 | detail URL | 页面状态/已解决人数 | 初始仓库状态 |
|---:|---:|---|---|---|---|---|---|
| 0101 | 01 | 灵活奋斗 | NUAACTF-2022 | MISC | https://ctf.bugku.com/challenges/detail/id/583.html | 约91—99解决，详情页cache miss | enumerated_detail_cache_miss |
| 0102 | 02 | 英雄联盟 | NUAACTF-2022 | MISC | https://ctf.bugku.com/challenges/detail/id/584.html | 列表约104—112解决，详情页缓存显示27解决 | enumerated_detail_stat_conflict |
| 0103 | 03 | 防ak | NUAACTF-2022 | Reverse | https://ctf.bugku.com/challenges/detail/id/585.html | 约9—11解决，详情页cache miss | enumerated_detail_cache_miss |
| 0104 | 04 | 月色真美 | NUAACTF-2022 | Reverse | https://ctf.bugku.com/challenges/detail/id/586.html | 约7解决，详情页cache miss | enumerated_detail_cache_miss |
| 0105 | 05 | Pyramid Escape | NUAACTF-2022 | Reverse | https://ctf.bugku.com/challenges/detail/id/587.html | 约2解决，详情页cache miss | enumerated_detail_cache_miss |
| 0106 | 06 | just_sqli | InterKosenCTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/588.html | 约377解决，详情页cache miss | enumerated_detail_cache_miss |
| 0107 | 07 | maze | InterKosenCTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/589.html | 约37—42解决，详情页可打开 | enumerated |
| 0108 | 08 | harmagedon | InterKosenCTF-2020 | Reverse | https://ctf.bugku.com/challenges/detail/id/590.html | 约3解决，详情页cache miss | enumerated_detail_cache_miss |
| 0109 | 09 | in question | InterKosenCTF-2020 | Reverse | https://ctf.bugku.com/challenges/detail/id/591.html | 约3解决，详情页cache miss | enumerated_detail_cache_miss |
| 0110 | 10 | stratum | InterKosenCTF-2020 | Reverse | https://ctf.bugku.com/challenges/detail/id/592.html | 约3解决，详情页cache miss | enumerated_detail_cache_miss |
| 0111 | 11 | trilemma | InterKosenCTF-2020 | Reverse | https://ctf.bugku.com/challenges/detail/id/593.html | 约2解决，详情页cache miss | enumerated_detail_cache_miss |
| 0112 | 12 | basic crackme | InterKosenCTF-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/594.html | 约10解决，详情页cache miss | enumerated_detail_cache_miss |
| 0113 | 13 | favorites | InterKosenCTF-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/595.html | 约5解决，详情页cache miss | enumerated_detail_cache_miss |
| 0114 | 14 | magic function | InterKosenCTF-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/596.html | 约4解决，详情页可打开 | enumerated |
| 0115 | 15 | passcode | InterKosenCTF-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/597.html | 约4解决，详情页cache miss | enumerated_detail_cache_miss |
| 0116 | 16 | E_S_P | InterKosenCTF-2019 | Crypto | https://ctf.bugku.com/challenges/detail/id/598.html | 约5解决，详情页cache miss | enumerated_detail_cache_miss |
| 0117 | 17 | Kurukuru Shuffle | InterKosenCTF-2019 | Crypto | https://ctf.bugku.com/challenges/detail/id/599.html | 约8解决，详情页cache miss | enumerated_detail_cache_miss |
| 0118 | 18 | Hugtto! | InterKosenCTF-2019 | MISC | https://ctf.bugku.com/challenges/detail/id/600.html | 约5—6解决，详情页cache miss | enumerated_detail_cache_miss |
| 0119 | 19 | Temple of Time | InterKosenCTF-2019 | MISC | https://ctf.bugku.com/challenges/detail/id/601.html | 约36解决，详情页cache miss | enumerated_detail_cache_miss |
| 0120 | 20 | saferm | InterKosenCTF-2019 | MISC | https://ctf.bugku.com/challenges/detail/id/602.html | 约5解决，详情页cache miss | enumerated_detail_cache_miss |

## 来源与复核说明

- Bugku 全站分页缓存 `challenges/index?page=21` 显示 `走一步，再走亿步`、`异或的密件` 后接 `灵活奋斗` 至 `Hugtto!`，用于承接 page=5 后续顺序。
- NUAACTF-2022 标签缓存显示 `异或的密件` 后接 `灵活奋斗`、`英雄联盟`、`防ak`、`月色真美`、`Pyramid Escape`，用于确认 0101—0105 的赛事、类型和顺序。
- MISC 类型页缓存显示 `Hugtto!` 后接 `Temple of Time`、`saferm`，用于补齐 0119—0120。
- 详情页点击可复核：0102 `id/584.html`、0107 `id/589.html`、0114 `id/596.html` 可打开；其他 detail URL 多数为点击返回的 cache miss URL，后续第006轮-B继续复核。
- 0102 `英雄联盟` 出现列表解决数与详情页缓存解决数不一致，本轮记录为统计冲突，不据此改写为已验证解题。

## 下一步完整提示

进入第006轮-B：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=6` 的第0101—0120题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`。具体任务：优先复核 0101、0103—0106、0108—0113、0115—0120 的 cache-miss detail URL，尤其继续确认 0119、0120 与 page=6 顺序的对应关系；能通过原始附件或真实授权题目环境和 solver 真实执行的才允许写 `verification.executed=true` 并标 `solved_verified`；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`；不得伪造 flag 或执行输出。完成后更新 `data/bugku_gid2_manifest.json` 和 `progress.json`；若0101—0120完成，再把下一步提示改为第007轮-A，对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=7` 的第0121—0140题做清单建档。
