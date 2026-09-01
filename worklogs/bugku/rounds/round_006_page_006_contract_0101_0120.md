# Bugku 第006轮-B：0101—0120 契约文件创建/升级

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=6

## 执行口径

- 本次只处理第0101—0120题。
- 逐题创建 canonical `README.md` 与 `card.json`。
- 按修复后的口径，本轮“完成”只表示契约卡建档完成，不表示真实解题完成。
- 未取得原始附件或真实授权题目环境输出的题目，不能标 `solved_verified`。
- 只有 0119 `Temple of Time` 有公开页面评论中的题目特定 pcap 分析方向，但未下载附件、未执行，因此仅标 `method_only`；其余题保守标 `blocked`。

## 完成清单

| 题号 | 题名 | 状态 | canonical path | detail URL |
|---:|---|---|---|---|
| 0101 | 灵活奋斗 | blocked | bugku/0101_linghuo_fendou | https://ctf.bugku.com/challenges/detail/id/583.html |
| 0102 | 英雄联盟 | blocked | bugku/0102_yingxiong_lianmeng | https://ctf.bugku.com/challenges/detail/id/584.html |
| 0103 | 防ak | blocked | bugku/0103_fang_ak | https://ctf.bugku.com/challenges/detail/id/585.html |
| 0104 | 月色真美 | blocked | bugku/0104_yuese_zhenmei | https://ctf.bugku.com/challenges/detail/id/586.html |
| 0105 | Pyramid Escape | blocked | bugku/0105_pyramid_escape | https://ctf.bugku.com/challenges/detail/id/587.html |
| 0106 | just_sqli | blocked | bugku/0106_just_sqli | https://ctf.bugku.com/challenges/detail/id/588.html |
| 0107 | maze | blocked | bugku/0107_maze | https://ctf.bugku.com/challenges/detail/id/589.html |
| 0108 | harmagedon | blocked | bugku/0108_harmagedon | https://ctf.bugku.com/challenges/detail/id/590.html |
| 0109 | in question | blocked | bugku/0109_in_question | https://ctf.bugku.com/challenges/detail/id/591.html |
| 0110 | stratum | blocked | bugku/0110_stratum | https://ctf.bugku.com/challenges/detail/id/592.html |
| 0111 | trilemma | blocked | bugku/0111_trilemma | https://ctf.bugku.com/challenges/detail/id/593.html |
| 0112 | basic crackme | blocked | bugku/0112_basic_crackme | https://ctf.bugku.com/challenges/detail/id/594.html |
| 0113 | favorites | blocked | bugku/0113_favorites | https://ctf.bugku.com/challenges/detail/id/595.html |
| 0114 | magic function | blocked | bugku/0114_magic_function | https://ctf.bugku.com/challenges/detail/id/596.html |
| 0115 | passcode | blocked | bugku/0115_passcode | https://ctf.bugku.com/challenges/detail/id/597.html |
| 0116 | E_S_P | blocked | bugku/0116_e_s_p | https://ctf.bugku.com/challenges/detail/id/598.html |
| 0117 | Kurukuru Shuffle | blocked | bugku/0117_kurukuru_shuffle | https://ctf.bugku.com/challenges/detail/id/599.html |
| 0118 | Hugtto! | blocked | bugku/0118_hugtto | https://ctf.bugku.com/challenges/detail/id/600.html |
| 0119 | Temple of Time | method_only | bugku/0119_temple_of_time | https://ctf.bugku.com/challenges/detail/id/601.html |
| 0120 | saferm | blocked | bugku/0120_saferm | https://ctf.bugku.com/challenges/detail/id/602.html |

## 统计

- solved_verified：0
- solved_unverified：0
- method_only：1
- blocked：19

## 验收说明

- 0101—0120 均已有 `bugku/<四位编号_题名>/README.md` 与 `bugku/<四位编号_题名>/card.json`。
- 所有题均保持 `verification.executed=false`，没有伪造 flag 或执行输出。
- 第0119题仅记录公开页面评论中的 pcap/HTTP URI 分析方向，仍未真实执行。

## 下一步完整提示

进入第007轮-A：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=7` 的第0121—0140题做清单建档。具体任务：逐题记录全局题号、`page_index`、题名、赛事、类型、detail URL、已解决人数或页面状态、初始仓库状态；写入或追加更新 `data/bugku_gid2_manifest.json`，并创建 `worklogs/bugku/rounds/round_007_page_007.md`。本阶段只做 page=7 的清单建档，不做解题，不创建题目 README/card；完成后把 `progress.json` 的下一步提示改为第007轮-B，对第0121—0140题逐题生成或升级 canonical README/card。