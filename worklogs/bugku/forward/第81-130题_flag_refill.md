# Bugku 第81—130题逐题补 flag 记录

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本文件是对 `第81-130题_batch.md` 的返工补 flag。只把 Bugku 页面、公开评论、公开 writeup 中能直接看到明确 flag 的题目计为 `solved-carded`；仅有 NSSCTF 动态 flag、图片未能 OCR、候选互相冲突或 Bugku 评论提示“提交不对”的题目不计入 solved。

## 状态口径

- `solved-carded`：已找到明确 flag 文本，并已写入补充卡。
- `candidate-format-anomaly`：公开资料有候选，但格式异常或评论提示提交不对，暂不计入 solved。
- `analyzed-no-flag`：有明确解法线索，但公开资料没有可抄录的 flag 文本。
- `blocked-no-flag`：未找到可靠公开 flag，仍需启动 Bugku 动态环境、附件或原题环境验证。

## 本轮汇总

- solved-carded：5题（第87、89、92、93、94题）。
- candidate-format-anomaly：2题（第88、103题）。
- analyzed-no-flag：11题（第90、91、95、96、97、100、101、102、104、105、106题）。
- blocked-no-flag：32题。

## 已确认 flag

| 题号 | 题名 | flag | 依据 |
|---:|---|---|---|
| 87 | 2048 | `moectf{2048_1s_intere5t1ng!}` | 康师傅 MoeCTF 2021 WriteUp，访问 `flag.php?score=50000` 后给出 flag。 |
| 89 | Do you know HTTP | `moectf{HTTPHeaders_1s_s0_ea5y!}` | Bugku 评论区和康师傅 WriteUp 均给出该 flag。 |
| 92 | Web安全入门指北—GET | `moectf{We1c0me_t0_CTF_Web!}` | 康师傅 MoeCTF 2021 WriteUp。 |
| 93 | Web安全入门指北—POST | `moectf{POST_1s_an_1mp0rtant_m3th0d!}` | 康师傅 MoeCTF 2021 WriteUp。 |
| 94 | Web安全入门指北—小饼干 | `moectf{C00kie_1s_sw33t!}` | 康师傅 MoeCTF 2021 WriteUp。 |

## 候选异常/未计入 solved

| 题号 | 题名 | 候选 | 原因 |
|---:|---|---|---|
| 88 | babeRCE | `oectf{Do_y0u_l1k3_Rcccccccccccccce?}` | 康师傅 WriteUp 原文给出 `oectf{...}`，缺少 `m`，与题面 `moectf{}` 格式不一致；不擅自修正为 `moectf{...}`。 |
| 103 | God_of_Aim | `moectf{Oh_you_can_a1m_and_H4ck_Javascript}` | Bugku 评论中有人明确说“不知道为什么，提交不上去”，且还有星号遮蔽候选；暂不计入 solved。 |

## 逐题结果

| 题号 | 题名 | 状态 | flag / 候选 | 处理说明 |
|---:|---|---|---|---|
| 81 | another note app | blocked-no-flag |  | 搜到同名/近名浏览器 note 类题，但与 Bugku BSides-Algiers 题不一致，未找到可核验 flag。 |
| 82 | XeXe | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 83 | Unbreakable_crypto | blocked-no-flag |  | Bugku 列表显示 0 解决，未找到公开 flag。 |
| 84 | cookies | blocked-no-flag |  | 仅确认 MoeCTF-2019 WEB 题存在，未找到公开 flag 文本。 |
| 85 | sign_in | blocked-no-flag |  | 仅确认 MoeCTF-2019 WEB 题存在，未找到公开 flag 文本。 |
| 86 | Object | blocked-no-flag |  | 仅确认 MoeCTF-2019 WEB 题存在，未找到公开 flag 文本。 |
| 87 | 2048 | solved-carded | `moectf{2048_1s_intere5t1ng!}` | 前端 JS 调用 `flag.php?score=50000`。 |
| 88 | babeRCE | candidate-format-anomaly | `oectf{Do_y0u_l1k3_Rcccccccccccccce?}` | 公开候选格式异常，未修正，待动态验证。 |
| 89 | Do you know HTTP | solved-carded | `moectf{HTTPHeaders_1s_s0_ea5y!}` | 自定义 HTTP 方法 HS + XFF/Referer/UA。 |
| 90 | unserialize | analyzed-no-flag |  | Bugku 免费 writeup 可见但公开抓取未显示 flag 文本。 |
| 91 | fake galgame | analyzed-no-flag |  | 找到原型污染/前端题线索，但未找到可抄录 flag。 |
| 92 | Web安全入门指北—GET | solved-carded | `moectf{We1c0me_t0_CTF_Web!}` | GET 参数 `?moe=flag`。 |
| 93 | Web安全入门指北—POST | solved-carded | `moectf{POST_1s_an_1mp0rtant_m3th0d!}` | POST 参数提交。 |
| 94 | Web安全入门指北—小饼干 | solved-carded | `moectf{C00kie_1s_sw33t!}` | 修改 Cookie VIP。 |
| 95 | 地狱通讯 | analyzed-no-flag |  | 找到 Flask format 泄露解法，公开页面未给 flag 文本。 |
| 96 | 地狱通讯-改 | analyzed-no-flag |  | 找到题目列表和同类改版线索，未找到 flag。 |
| 97 | baby_file | analyzed-no-flag |  | NSSCTF 复现环境有动态 `NSSCTF{uuid}`，不能作为 Bugku flag。 |
| 98 | cookiehead | blocked-no-flag |  | Bugku 页面可见题目，但无公开 flag。 |
| 99 | ezphp | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 100 | sqlmap_boy | analyzed-no-flag |  | 找到 SQL 注入步骤和 NSSCTF 动态 flag；不能作为 Bugku flag。 |
| 101 | what are y0u uploading？ | analyzed-no-flag |  | 找到文件上传写法/截图描述，公开文本无可核验 flag。 |
| 102 | ezhtml | analyzed-no-flag |  | 找到 writeup 摘要“evil.js”，未找到完整 flag。 |
| 103 | God_of_Aim | candidate-format-anomaly | `moectf{Oh_you_can_a1m_and_H4ck_Javascript}` | Bugku 评论称该候选提交不上，暂不计入 solved。 |
| 104 | java | analyzed-no-flag |  | miniLCTF-2021 Java Web 题，未找到 flag 文本。 |
| 105 | l_inc | analyzed-no-flag |  | miniLCTF-2021 LFI 题，未找到 flag 文本。 |
| 106 | template | analyzed-no-flag |  | miniLCTF-2021 模板题，未找到 flag 文本。 |
| 107 | 签到题 | analyzed-no-flag |  | Bugku WP 摘要显示交互式 `/readflag` 解法，未显示完整 flag。 |
| 108 | areyoureclu3e | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 109 | id_wife | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 110 | lets_play_dolls | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 111 | p | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 112 | Personal_IP_Query | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 113 | fake_login | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 114 | mini_java | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 115 | Bottle Poem | blocked-no-flag |  | 未找到 Bugku 对应 flag；原赛题需动态环境。 |
| 116 | Issues | blocked-no-flag |  | 未找到 Bugku 对应 flag。 |
| 117 | Obligatory Calc | blocked-no-flag |  | 未找到 Bugku 对应 flag。 |
| 118 | Safelist | blocked-no-flag |  | 未找到 Bugku 对应 flag。 |
| 119 | Sekai Game Start | blocked-no-flag |  | 未找到 Bugku 对应 flag。 |
| 120 | PPP | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 121 | DootDoot | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 122 | MCA | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 123 | Super Cereal | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 124 | Poem Me | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 125 | Link Me | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 126 | Valentina | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 127 | Color Me | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 128 | Admin Journal | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 129 | JUST_PROTO | blocked-no-flag |  | 未找到可靠公开 flag。 |
| 130 | go_session | blocked-no-flag |  | 未找到可靠公开 flag。 |

## 来源记录

- Bugku 第10/11页题库列表用于确认第81—130题题名与所属赛事。
- 康师傅《MoeCTF 2021 WriteUp》用于确认第87、88候选、第89、第92、第93、第94题的解法和 flag。
- Bugku `Do you know HTTP` 页面评论区用于交叉确认第89题 flag。
- Bugku `God_of_Aim` 页面评论区用于标记第103题候选异常。
- 部分 NSSCTF 复现 writeup 仅作为解法参考，动态 `NSSCTF{uuid}` 不写入 Bugku verification.flag。