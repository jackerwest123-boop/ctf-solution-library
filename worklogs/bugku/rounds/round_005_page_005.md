# Bugku 比赛真题全题库第005轮-A：page=5 清单建档

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5

## 本轮执行口径

- 本阶段只做 page=5 的清单建档。
- 不解题，不创建题目 README/card。
- 全局编号规则：`global_no = (page - 1) * 20 + page_index`。
- `gid=2.html?page=5` 直接页未能稳定读取，本轮使用 Bugku 比赛真题 WEB 类型页缓存、题目详情页点击结果、NUAACTF 标签/全站分页缓存交叉整理。
- 0081—0096 主要承接 WEB 类型第2页中 `maSQLsh2` 后续条目；0097—0100 由 NUAACTF-2022 标签/全站分页缓存承接 `loginjection` 后续条目。

## 第0081—0100题清单

| global_no | page_index | 题名 | 赛事 | 类型 | detail URL | 页面状态/已解决人数 | 初始仓库状态 |
|---:|---:|---|---|---|---|---|---|
| 0081 | 01 | Upload 0 | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/465.html | 约915—1062解决，详情页cache miss | enumerated_detail_cache_miss |
| 0082 | 02 | Upload 1 | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/466.html | 约729—907解决，详情页可打开 | enumerated |
| 0083 | 03 | Upload 2 | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/467.html | 约306—418解决，详情页可打开 | enumerated |
| 0084 | 04 | Virtual Shop | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/471.html | 约368解决，详情页可打开 | enumerated |
| 0085 | 05 | Virtual Shop 2 | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/472.html | 约257解决，详情页可打开 | enumerated |
| 0086 | 06 | Sparta | zh3r0-v2 | WEB | https://ctf.bugku.com/challenges/detail/id/520.html | 约26—31解决，详情页可打开 | enumerated |
| 0087 | 07 | strpos and substr | zh3r0-v2 | WEB | https://ctf.bugku.com/challenges/detail/id/521.html | 约118—144解决，详情页cache miss | enumerated_detail_cache_miss |
| 0088 | 08 | web1 | NUAACTF-2018 | WEB | https://ctf.bugku.com/challenges/detail/id/542.html | 约5—6解决，详情页cache miss | enumerated_detail_cache_miss |
| 0089 | 09 | checkin | NUAACTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/543.html | 约462解决，详情页可打开 | enumerated |
| 0090 | 10 | jwt | NUAACTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/544.html | 约301解决，详情页可打开 | enumerated |
| 0091 | 11 | easy-pop | NUAACTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/545.html | 约257—335解决，详情页可打开 | enumerated |
| 0092 | 12 | command-injection | NUAACTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/546.html | 约270—334解决，详情页可打开 | enumerated |
| 0093 | 13 | 逃逸 | NUAACTF-2020 | WEB | https://ctf.bugku.com/challenges/detail/id/547.html | 约116解决，详情页cache miss | enumerated_detail_cache_miss |
| 0094 | 14 | Make Me Cry | NUAACTF-2021 | WEB | https://ctf.bugku.com/challenges/detail/id/568.html | 约73—90解决，详情页cache miss | enumerated_detail_cache_miss |
| 0095 | 15 | ezlogin | NUAACTF-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/577.html | 约123—154解决，详情页可打开 | enumerated |
| 0096 | 16 | loginjection | NUAACTF-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/578.html | 约15—25解决，详情页cache miss | enumerated_detail_cache_miss |
| 0097 | 17 | superezpop | NUAACTF-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/579.html | 约284—302解决，详情页可打开 | enumerated |
| 0098 | 18 | 从零开始的勇士之路 | NUAACTF-2022 | Crypto |  | 约62—66解决，detail URL待复核 | enumerated_detail_pending |
| 0099 | 19 | 走一步，再走亿步 | NUAACTF-2022 | Crypto |  | 约3解决，detail URL待复核 | enumerated_detail_pending |
| 0100 | 20 | 异或的密件 | NUAACTF-2022 | Crypto |  | 约29解决，detail URL待复核 | enumerated_detail_pending |

## 来源与复核说明

- Bugku 比赛真题 WEB 类型第2页缓存显示 `maSQLsh2` 后接 `Upload 0`、`Upload 1`、`Upload 2`、`Virtual Shop`、`Virtual Shop 2`、`Sparta`、`strpos and substr`、`web1`、`checkin`、`jwt`、`easy-pop`、`command-injection`、`逃逸`、`Make Me Cry`、`ezlogin`、`loginjection`。
- 详情页点击已复核：0082 `id/466.html`、0083 `id/467.html`、0084 `id/471.html`、0085 `id/472.html`、0086 `id/520.html`、0089 `id/543.html`、0090 `id/544.html`、0091 `id/545.html`、0092 `id/546.html`、0095 `id/577.html`、0097 `id/579.html` 可打开。
- 0081、0087、0088、0093、0094、0096 的 detail URL 由列表点击返回的 cache miss URL 保留，需第005轮-B继续复核。
- NUAACTF-2022 标签缓存显示 `ezlogin`、`loginjection` 后接 `superezpop`、`从零开始的勇士之路`、`走一步，再走亿步`、`异或的密件`；其中 0098—0100 的 detail URL 暂未复核，保持待复核。

## 下一步完整提示

进入第005轮-B：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=5` 的第0081—0100题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`。具体任务：优先复核 0098—0100 的 detail URL，并继续复核 0081、0087、0088、0093、0094、0096 的 cache-miss detail URL；能通过原始附件或真实授权题目环境和 solver 真实执行的才允许写 `verification.executed=true` 并标 `solved_verified`；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`；不得伪造 flag 或执行输出。完成后更新 `data/bugku_gid2_manifest.json` 和 `progress.json`；若0081—0100完成，再把下一步提示改为第006轮-A，对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=6` 的第0101—0120题做清单建档。
