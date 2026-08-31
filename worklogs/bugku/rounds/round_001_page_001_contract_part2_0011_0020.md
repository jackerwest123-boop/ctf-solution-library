# Bugku 第001轮-B 第二阶段：0011—0020 契约文件创建

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1

## 完成范围

本次只处理第0011—0020题，未进入 page=2。

已为以下题目创建 canonical 目录、`README.md` 与 `card.json`：

| 题号 | 题名 | 状态 |
|---:|---|---|
| 0011 | robots | blocked |
| 0012 | nuaactf | method_only |
| 0013 | b1nary | blocked |
| 0014 | traffic | solved_unverified |
| 0015 | recover | blocked |
| 0016 | -++-- | solved_verified |
| 0017 | 3-最好的语言 | solved_unverified |
| 0018 | 3-SimpleSMC | blocked |
| 0019 | 3-hafuhafu | solved_unverified |
| 0020 | 3-Unpleasant_music | blocked |

## 验收说明

- 0011—0020 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 第0016题复用已修复的 `solvers/misc/brainfuck_emoticon.py`，保持 `solved_verified`。
- 第0014、0017、0019题有旧记录或公开flag线索，但未用原始附件在本仓库重新执行，因此保持 `solved_unverified`。
- 其余题保持 `method_only` 或 `blocked`，未伪造 `solved_verified`。

## 第一轮-B整体状态

第一轮-B已覆盖 0001—0020 的 canonical README/card 创建或升级。仍需后续更深层验证的内容包括：为 `solved_unverified` 题补原始附件、统一 solver、`--self-test` 和 `verification.executed_output`。

## 下一步完整提示

进入第002轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=2` 的第0021—0040题做清单建档。具体任务：逐题记录全局题号、page_index、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_002_page_002.md`。本阶段只做 page=2 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第002轮-B，对第0021—0040题逐题生成或升级 canonical README/card。
