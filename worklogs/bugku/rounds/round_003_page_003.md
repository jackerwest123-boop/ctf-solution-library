# Bugku 比赛真题全题库第003轮-A：page=3 清单建档

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=3

## 本轮执行口径

- 本阶段只做 page=3 的清单建档。
- 不解题，不创建题目 README/card。
- 全局编号规则：`global_no = (page - 1) * 20 + page_index`。
- 直接打开 `gid=2.html?page=3` 仍不可稳定读取，故本轮使用 Bugku 公开索引缓存、标签页缓存和已知连续顺序交叉整理。
- 其中 0041—0049 的顺序由公开全站索引页和 Xp0intCTF/网鼎杯标签缓存共同支撑；0050—0054 由网鼎杯标签缓存支撑；0055—0060 由公开索引页 `challenges/index.html?page=12` 衔接整理，后续第003轮-B继续复核 detail URL。

## 第0041—0060题清单

| global_no | page_index | 题名 | 赛事 | 类型 | detail URL | 页面状态/已解决人数 | 初始仓库状态 |
|---:|---:|---|---|---|---|---|---|
| 0041 | 01 | 重重flag背后隐藏的秘密 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/268.html | 约592—691解决 | enumerated |
| 0042 | 02 | 犯人留下了信息 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/269.html | 约252—315解决 | enumerated |
| 0043 | 03 | 弗拉戈在哪里2 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/270.html | 约652—772解决 | enumerated |
| 0044 | 04 | 弗拉戈在哪里 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/271.html | 约594—715解决 | enumerated |
| 0045 | 05 | 1-advance | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/272.html | 约70—76解决 | enumerated |
| 0046 | 06 | 1-blend | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/273.html | 约7—10解决 | enumerated |
| 0047 | 07 | 1-Beijing | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/274.html | 约71—75解决 | enumerated |
| 0048 | 08 | 1-minified | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/275.html | 约18解决 | enumerated |
| 0049 | 09 | 1-clip | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/276.html | 约5—6解决 | enumerated |
| 0050 | 10 | 青龙组-crypto091 | 网鼎杯-2022 | Crypto |  | 约68解决 | enumerated_detail_pending |
| 0051 | 11 | 青龙组-david_homework | 网鼎杯-2022 | Crypto |  | 约12解决 | enumerated_detail_pending |
| 0052 | 12 | 青龙组-grasshopper | 网鼎杯-2022 | Crypto |  | 约14解决 | enumerated_detail_pending |
| 0053 | 13 | 青龙组-fakeshell | 网鼎杯-2022 | Reverse |  | 约24解决 | enumerated_detail_pending |
| 0054 | 14 | 青龙组-Handmake | 网鼎杯-2022 | Reverse |  | 约21解决 | enumerated_detail_pending |
| 0055 | 15 | 别开，测试题目 | Test | WEB |  | 约0解决 | enumerated_detail_pending |
| 0056 | 16 | abstract_art | WolvCTF-2023 | MISC |  | 约241解决 | enumerated_detail_pending |
| 0057 | 17 | inspect-me | HackINI-2021 | WEB | https://ctf.bugku.com/challenges/detail/id/403.html | 约7485—7636解决 | enumerated |
| 0058 | 18 | my-first-sqli | HackINI-2021 | WEB |  | 约6761—6918解决 | enumerated_detail_pending |
| 0059 | 19 | post-the-get | HackINI-2021 | WEB |  | 约5431—5538解决 | enumerated_detail_pending |
| 0060 | 20 | sqli-0x1 | HackINI-2021 | WEB |  | 约2282—2362解决 | enumerated_detail_pending |

## 来源与复核说明

- Xp0intCTF 标签页缓存支持 `MaybeNotStandrad` 至 `弗拉戈在哪里` 的连续题名、赛事、类型和解决人数范围。
- Bugku 公开索引页缓存显示 `一个普通的压缩包` 后接 `重重flag背后隐藏的秘密`、`犯人留下了信息`、`弗拉戈在哪里2`、`弗拉戈在哪里`，再接 `1-advance`、`1-blend`、`1-Beijing`、`1-minified`。
- 网鼎杯标签页缓存显示 `1-clip`、`青龙组-crypto091`、`青龙组-david_homework`、`青龙组-grasshopper`、`青龙组-fakeshell`、`青龙组-Handmake` 的连续顺序。
- 公开索引页 `challenges/index.html?page=12` 显示 `1-clip` 后接 `别开，测试题目`、`abstract_art`、`inspect-me`、`my-first-sqli`、`post-the-get`、`sqli-0x1` 等条目；因该页不是 `gid=2.html?page=3` 的直接缓存，0055—0060 在第003轮-B需继续复核。

## 下一步完整提示

进入第003轮-B：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=3` 的第0041—0060题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`。具体任务：优先复核 0050—0060 的 detail URL；能通过原始附件和 solver 真实执行的才允许写 `verification.executed=true` 并标 `solved_verified`；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`；不得伪造 flag 或执行输出。完成后更新 `data/bugku_gid2_manifest.json` 和 `progress.json`；若0041—0060完成，再把下一步提示改为第004轮-A，对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=4` 的第0061—0080题做清单建档。
