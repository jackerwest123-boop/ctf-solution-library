# Bugku 第002轮-B：0021—0040 契约文件创建/升级

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=2

## 本轮执行口径

- 本次只处理第0021—0040题。
- 0021—0030：迁移或升级已有旧卡到 canonical 路径。
- 0031—0040：新建 canonical README/card。
- 未取得原始附件并真实执行的题目，不能标 `solved_verified`。
- 本次没有新增 `solved_verified`。

## 完成清单

| 题号 | 题名 | 状态 | canonical path | 说明 |
|---:|---|---|---|---|
| 0021 | 3-track_hacker | method_only | bugku/0021_3_track_hacker | 旧卡提示密码结构分析，未执行。 |
| 0022 | 3-dewas | method_only | bugku/0022_3_dewas | 旧卡提示文件识别/隐写取证，未执行。 |
| 0023 | 3-mirror | method_only | bugku/0023_3_mirror | 旧卡提示镜像/翻转/逆序，未执行。 |
| 0024 | 3-I_like_pack | method_only | bugku/0024_3_i_like_pack | 旧卡提示加壳/脱壳逆向，未执行。 |
| 0025 | 3-babyre | method_only | bugku/0025_3_babyre | 旧卡提示校验逻辑逆向，未执行。 |
| 0026 | 3-Not_only_base | method_only | bugku/0026_3_not_only_base | 旧卡提示多层Base/混合编码，未执行。 |
| 0027 | easy_fs | solved_unverified | bugku/0027_easy_fs | 旧卡含公开flag线索，但未用原始附件和solver执行。 |
| 0028 | baby_N1ES | method_only | bugku/0028_baby_n1es | 旧卡提示Feistel/XOR逆向，缺完整附件执行。 |
| 0029 | Lipstick | method_only | bugku/0029_lipstick | 旧卡提示图像LSB/通道隐写，未执行。 |
| 0030 | APFS | method_only | bugku/0030_apfs | 旧卡提示APFS镜像取证，未执行。 |
| 0031 | patience | blocked | bugku/0031_patience | 缺附件、公开flag和题目特定方法。 |
| 0032 | OldDriver of Akina | blocked | bugku/0032_olddriver_of_akina | 缺附件、公开flag和题目特定方法。 |
| 0033 | N1CTF-LFI | blocked | bugku/0033_n1ctf_lfi | 题名和类型待详情页复核，缺附件和方法。 |
| 0034 | baby_neural_network | blocked | bugku/0034_baby_neural_network | 缺附件、公开flag和可复现模型/参数。 |
| 0035 | N1CTF-baby unity3d | method_only | bugku/0035_n1ctf_baby_unity3d | 保留Unity3D逆向通用方法，未执行。 |
| 0036 | MaybeNotStandrad | blocked | bugku/0036_maybenotstandrad | 题名拼写和附件待复核。 |
| 0037 | 好像说太多了 | method_only | bugku/0037_too_much_said | 保留冗余信息/元数据/附加数据检查思路。 |
| 0038 | 这是什么编码 | method_only | bugku/0038_what_encoding | 保留编码识别与递归解码思路。 |
| 0039 | 一张含有信息的图片 | method_only | bugku/0039_image_with_info | 保留图片隐写检查思路。 |
| 0040 | 一个普通的压缩包 | method_only | bugku/0040_normal_zip | 保留压缩包取证检查思路。 |

## 统计

- solved_verified：0
- solved_unverified：1
- method_only：14
- blocked：5

## 验收说明

- 0021—0040 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 第0027题 `easy_fs` 旧卡含公开flag线索，但没有在本轮通过原始附件和统一solver执行，因此保持 `solved_unverified`。
- 其余有思路线索但无可执行附件的题标为 `method_only`，缺题目特定方法或附件的题标为 `blocked`。
- 所有未执行题均保持 `verification.executed=false`，没有伪造执行输出。

## 下一步完整提示

进入第003轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=3` 的第0041—0060题做清单建档。具体任务：逐题记录全局题号、`page_index`、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_003_page_003.md`。本阶段只做 page=3 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第003轮-B，对第0041—0060题逐题生成或升级 canonical README/card。
