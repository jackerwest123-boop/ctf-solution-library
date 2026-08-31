# Bugku 比赛真题全题库第002轮-A：page=2 清单建档

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=2

## 本轮执行口径

- 本阶段只做 page=2 的清单建档。
- 不解题，不创建题目 README/card。
- 全局编号规则：`global_no = (page - 1) * 20 + page_index`。
- 因本次直接打开 `gid=2.html?page=2` 返回缓存缺失，page=2 题目顺序依据公开索引缓存、全站连续列表缓存、既有仓库 index 交叉整理；后续第002轮-B和实际打开详情页时继续复核 detail URL。

## 第0021—0040题清单

| global_no | page_index | 题名 | 赛事 | 类型 | detail URL | 页面状态/已解决人数 | 初始仓库状态 |
|---:|---:|---|---|---|---|---|---|
| 0021 | 01 | 3-track_hacker | 网鼎杯-2018 | Crypto | https://ctf.bugku.com/challenges/detail/id/248.html | 约502解决 | legacy-card-exists |
| 0022 | 02 | 3-dewas | 网鼎杯-2018 | MISC | https://ctf.bugku.com/challenges/detail/id/249.html | 约492解决 | legacy-card-exists |
| 0023 | 03 | 3-mirror | 网鼎杯-2018 | MISC | https://ctf.bugku.com/challenges/detail/id/250.html | 约596解决 | legacy-card-exists |
| 0024 | 04 | 3-I_like_pack | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/251.html | 约10解决 | legacy-card-exists |
| 0025 | 05 | 3-babyre | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/252.html | 约169解决 | legacy-card-exists |
| 0026 | 06 | 3-Not_only_base | 网鼎杯-2018 | Crypto | https://ctf.bugku.com/challenges/detail/id/253.html | 约755解决 | legacy-card-exists |
| 0027 | 07 | easy_fs | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/254.html | 约36解决 | legacy-card-exists |
| 0028 | 08 | baby_N1ES | N1CTF-2018 | Crypto | https://ctf.bugku.com/challenges/detail/id/255.html | 约128—142解决 | legacy-card-exists |
| 0029 | 09 | Lipstick | N1CTF-2018 | MISC | https://ctf.bugku.com/challenges/detail/id/256.html | 约192解决 | legacy-card-exists |
| 0030 | 10 | APFS | N1CTF-2018 | MISC | https://ctf.bugku.com/challenges/detail/id/257.html | 约20解决 | legacy-card-exists |
| 0031 | 11 | patience | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/258.html | 约9—10解决 | enumerated |
| 0032 | 12 | OldDriver of Akina | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/259.html | 约3—4解决 | enumerated |
| 0033 | 13 | N1CTF-LFI | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/260.html | 约3—5解决 | enumerated |
| 0034 | 14 | baby_neural_network | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/261.html | 约2—4解决 | enumerated |
| 0035 | 15 | N1CTF-baby unity3d | N1CTF-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/262.html | 约3—5解决 | enumerated |
| 0036 | 16 | MaybeNotStandrad | Xp0intCTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/263.html | 约49—51解决 | enumerated |
| 0037 | 17 | 好像说太多了 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/264.html | 约815解决 | enumerated |
| 0038 | 18 | 这是什么编码 | Xp0intCTF-2017 | Crypto | https://ctf.bugku.com/challenges/detail/id/265.html | 约684解决 | enumerated |
| 0039 | 19 | 一张含有信息的图片 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/266.html | 约1713解决 | enumerated |
| 0040 | 20 | 一个普通的压缩包 | Xp0intCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/267.html | 约637解决 | enumerated |

## 来源与复核说明

- 网鼎杯-2018标签页缓存显示 `3-最好的语言` 至 `3-Not_only_base` 的连续顺序，并包含 `3-track_hacker`、`3-dewas`、`3-mirror`、`3-I_like_pack`、`3-babyre`、`3-Not_only_base`。
- 全站列表缓存显示 `Lipstick`、`APFS` 后接 `patience`、`OldDriver of Akina`、`N1CTF-LFI`、`baby_neural_network`、`N1CTF-baby unity3d`、`MaybeNotStandrad`、`好像说太多了`、`这是什么编码`、`一张含有信息的图片`、`一个普通的压缩包`。
- 既有仓库 `index.json` 已有 0021—0030 的旧卡路径，故本轮把 0021—0030 初始状态标为 `legacy-card-exists`。
- detail URL 以 page=1 结束的 `id/247.html` 后连续推断为 `id/248.html`—`id/267.html`；第002轮-B打开详情页时继续复核。

## 下一步完整提示

进入第002轮-B：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=2` 的第0021—0040题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`。具体任务：0021—0030先迁移或升级已有旧卡，0031—0040新建 README/card；能通过原始附件和 solver 真实执行的才允许写 `verification.executed=true` 并标 `solved_verified`；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`；不得伪造 flag 或执行输出。完成后更新 `data/bugku_gid2_manifest.json` 和 `progress.json`；若0021—0040完成，再把下一步提示改为第003轮-A，对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=3` 的第0041—0060题做清单建档。
