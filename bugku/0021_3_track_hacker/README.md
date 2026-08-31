# 0021 3-track_hacker

- 平台：Bugku
- 题库：比赛真题全题库
- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=2
- detail URL：https://ctf.bugku.com/challenges/detail/id/248.html
- 赛事：网鼎杯-2018
- 类型：Crypto
- 当前状态：`method_only`

## 处理说明

从旧卡迁移到 canonical 路径。旧卡仅能确认题名、分类和通用密码分析思路；当前没有原始附件和真实执行输出，因此不能标 `solved_verified`。

## 后续验证

补齐附件后，需识别编码/密钥材料/分组结构，编写 `solve(attachment_path, **kwargs)`，加入 `--self-test`，并写入真实 `verification.executed_output`。