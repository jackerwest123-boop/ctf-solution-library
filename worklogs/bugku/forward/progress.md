# Bugku 正序处理进度

## 当前任务
- 目标：处理 Bugku WEB 题库正序任务。
- 目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 正序方向：从第31题继续向后处理。
- 说明：第1题至第30题已完成；当前已推进到第130题。

## 已完成批次

| 批次 | 范围 | 输出 | 状态 |
|---|---:|---|---|
| 第一批 | 31—40 | 单题 Markdown + 单题 JSON 卡 | 第33、36题 solved-carded；其余 blocked-carded |
| 第二批 | 41—80 | `worklogs/bugku/forward/第41-80题_batch.md`；`cards/pending/bugku/第41-80题_batch.cards.json` | blocked-carded |
| 第三批 | 81—130 | `worklogs/bugku/forward/第81-130题_batch.md`；`cards/pending/bugku/第81-130题_batch.cards.json` | blocked-carded |

## 第81—130题摘要

| 题号 | 题名 | 赛事 | 状态 |
|---|---|---|---|
| 81 | another note app | BSides-Algiers-2k21-Finals-chals | blocked-carded |
| 82 | XeXe | BSides-Algiers-2k21-Finals-chals | blocked-carded |
| 83 | Unbreakable_crypto | BSides-Algiers-2k21-Finals-chals | blocked-carded |
| 84 | cookies | moeCTF-2019 | blocked-carded |
| 85 | sign_in | moeCTF-2019 | blocked-carded |
| 86 | Object | moeCTF-2019 | blocked-carded |
| 87 | 2048 | moeCTF-2021 | blocked-carded |
| 88 | babeRCE | moeCTF-2021 | blocked-carded |
| 89 | Do you know HTTP | moeCTF-2021 | blocked-carded |
| 90 | unserialize | moeCTF-2021 | blocked-carded |
| 91 | fake galgame | moeCTF-2021 | blocked-carded |
| 92 | Web安全入门指北—GET | moeCTF-2021 | blocked-carded |
| 93 | Web安全入门指北—POST | moeCTF-2021 | blocked-carded |
| 94 | Web安全入门指北—小饼干 | moeCTF-2021 | blocked-carded |
| 95 | 地狱通讯 | moeCTF-2021 | blocked-carded |
| 96 | 地狱通讯-改 | moeCTF-2021 | blocked-carded |
| 97 | baby_file | moeCTF-2022 | blocked-carded |
| 98 | cookiehead | moeCTF-2022 | blocked-carded |
| 99 | ezphp | moeCTF-2022 | blocked-carded |
| 100 | sqlmap_boy | moeCTF-2022 | blocked-carded |
| 101 | what are y0u uploading？ | moeCTF-2022 | blocked-carded |
| 102 | ezhtml | moeCTF-2022 | blocked-carded |
| 103 | God_of_Aim | moeCTF-2022 | blocked-carded |
| 104 | java | miniLCTF-2021 | blocked-carded |
| 105 | l_inc | miniLCTF-2021 | blocked-carded |
| 106 | template | miniLCTF-2021 | blocked-carded |
| 107 | 签到题 | miniLCTF-2020 | blocked-carded |
| 108 | areyoureclu3e | miniLCTF-2020 | blocked-carded |
| 109 | id_wife | miniLCTF-2020 | blocked-carded |
| 110 | lets_play_dolls | miniLCTF-2020 | blocked-carded |
| 111 | p | miniLCTF-2020 | blocked-carded |
| 112 | Personal_IP_Query | miniLCTF-2020 | blocked-carded |
| 113 | fake_login | miniLCTF-2023 | blocked-carded |
| 114 | mini_java | miniLCTF-2023 | blocked-carded |
| 115 | Bottle Poem | SekaiCTF-2022 | blocked-carded |
| 116 | Issues | SekaiCTF-2022 | blocked-carded |
| 117 | Obligatory Calc | SekaiCTF-2022 | blocked-carded |
| 118 | Safelist | SekaiCTF-2022 | blocked-carded |
| 119 | Sekai Game Start | SekaiCTF-2022 | blocked-carded |
| 120 | PPP | 陕西省大学生-2023 | blocked-carded |
| 121 | DootDoot | SaplingCTF-2022 | blocked-carded |
| 122 | MCA | SaplingCTF-2022 | blocked-carded |
| 123 | Super Cereal | SaplingCTF-2022 | blocked-carded |
| 124 | Poem Me | SaplingCTF-2022 | blocked-carded |
| 125 | Link Me | SaplingCTF-2022 | blocked-carded |
| 126 | Valentina | SaplingCTF-2022 | blocked-carded |
| 127 | Color Me | SaplingCTF-2022 | blocked-carded |
| 128 | Admin Journal | SaplingCTF-2022 | blocked-carded |
| 129 | JUST_PROTO | 贵阳大数据及网络安全精英对抗赛-2023 | blocked-carded |
| 130 | go_session | CISCN-2023 | blocked-carded |

## 下一步
继续第131—180题；优先抓取后续 Bugku WEB 列表页，能直接确认 flag 的写入 solved-carded，不能动态验证的写入 blocked-carded。