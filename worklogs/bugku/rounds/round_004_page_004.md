# Bugku 比赛真题全题库第004轮-A：page=4 清单建档

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=4

## 本轮执行口径

- 本阶段只做 page=4 的清单建档。
- 不解题，不创建题目 README/card。
- 全局编号规则：`global_no = (page - 1) * 20 + page_index`。
- `gid=2.html?page=4` 直接页仍不稳定；本轮以 Bugku WEB 类型列表缓存、分页缓存、题目详情页点击结果交叉整理。
- 其中 0061—0076 由 WEB 类型第1页缓存承接 `sqli-0x1` 后续顺序；0077—0080 由 WEB 类型第2页缓存承接 `just-work-type` 后续顺序。

## 第0061—0080题清单

| global_no | page_index | 题名 | 赛事 | 类型 | detail URL | 页面状态/已解决人数 | 初始仓库状态 |
|---:|---:|---|---|---|---|---|---|
| 0061 | 01 | baby lfi | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/425.html | 约3055—3762解决 | enumerated |
| 0062 | 02 | baby lfi 2 | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/426.html | 约2587—3020解决 | enumerated |
| 0063 | 03 | challenge-creator | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/427.html | 约171—195解决 | enumerated |
| 0064 | 04 | HEADache | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/428.html | 约724—783解决 | enumerated |
| 0065 | 05 | lfi | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/429.html | 约1847—2064解决 | enumerated |
| 0066 | 06 | nextGen 1 | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/430.html | 约1451—1853解决 | enumerated_detail_open_error |
| 0067 | 07 | nextGen 2 | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/431.html | 约1183—1320解决 | enumerated_detail_open_error |
| 0068 | 08 | Whois | HackINI-2022 | WEB | https://ctf.bugku.com/challenges/detail/id/432.html | 约1070—1190解决 | enumerated |
| 0069 | 09 | adversal | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/445.html | 约22—31解决 | enumerated |
| 0070 | 10 | filter-madness | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/450.html | 约1265—1391解决 | enumerated |
| 0071 | 11 | charlottesweb | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/451.html | 约1106—1302解决 | enumerated_detail_cache_miss |
| 0072 | 12 | zombie-101 | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/453.html | 约226—276解决 | enumerated |
| 0073 | 13 | zombie-201 | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/454.html | 约75—93解决 | enumerated_detail_cache_miss |
| 0074 | 14 | zombie-301 | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/455.html | 约39—53解决 | enumerated_detail_cache_miss |
| 0075 | 15 | zombie-401 | WolvCTF-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/456.html | 约27—36解决 | enumerated_detail_cache_miss |
| 0076 | 16 | just-work-type | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/460.html | 约460—518解决 | enumerated_detail_cache_miss |
| 0077 | 17 | simple web app | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/461.html | 约157—221解决 | enumerated |
| 0078 | 18 | t3lEpoRt | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/462.html | 约0解决 | enumerated_detail_cache_miss |
| 0079 | 19 | maSQLsh | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/463.html | 约3解决 | enumerated_detail_cache_miss |
| 0080 | 20 | maSQLsh2 | HackINI-2023 | WEB | https://ctf.bugku.com/challenges/detail/id/464.html | 约9解决 | enumerated_detail_cache_miss |

## 来源与复核说明

- Bugku WEB 类型第1页缓存显示 `sqli-0x1` 后接 `baby lfi`、`baby lfi 2`、`challenge-creator`、`HEADache`、`lfi`、`nextGen 1`、`nextGen 2`、`Whois`、`adversal`、`filter-madness`、`charlottesweb`、`zombie-101`、`zombie-201`、`zombie-301`、`zombie-401`、`just-work-type`。
- Bugku WEB 类型第2页缓存显示 `simple web app`、`t3lEpoRt`、`maSQLsh`、`maSQLsh2` 作为后续条目。
- 详情页点击已复核：0061—0065 为 `id/425.html`—`id/429.html`；0068 为 `id/432.html`；0069 为 `id/445.html`；0070 为 `id/450.html`；0072 为 `id/453.html`；0077 为 `id/461.html`。
- 0066、0067、0071、0073—0080 的 detail URL 由列表链接或点击返回的 cache miss URL 保留，需第004轮-B继续打开复核。

## 下一步完整提示

进入第004轮-B：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=4` 的第0061—0080题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`。具体任务：优先复核 0066、0067、0071、0073—0080 的 detail URL；能通过原始附件或真实授权题目环境和 solver 真实执行的才允许写 `verification.executed=true` 并标 `solved_verified`；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`；不得伪造 flag 或执行输出。完成后更新 `data/bugku_gid2_manifest.json` 和 `progress.json`；若0061—0080完成，再把下一步提示改为第005轮-A，对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=5` 的第0081—0100题做清单建档。
