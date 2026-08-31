# 0017 3-最好的语言

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/244.html
- 赛事：网鼎杯-2018
- 类型：Reverse
- 当前状态：solved_unverified

## 已知结论

旧卡中已记录 Python 字节码逻辑：输出由循环 XOR、MD5 中间段和 Base64 组合构成。旧卡记录的结果为：

`flag{PyC_1s_613u21i_N0t_Hard}`

## 为什么不是 solved_verified

旧卡尚未升级成满足新契约的完整 solver/self-test，且本次没有用原始附件重新执行。因此保持 `solved_unverified`。

## 后续要求

需要把旧 solver 改为 `solve(attachment_path, **kwargs)`，加入内置 mock 的 `--self-test`，并记录真实运行输出。
