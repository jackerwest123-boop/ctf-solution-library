# 011 robots

- 平台：Bugku
- 赛事：NUAACTF 2017
- 类型：Reverse
- Bugku ID：238
- 状态：`pending_attachment_validation`
- Flag 格式：`flag{}`

## 当前结论

Bugku 公共题面只确认该题为 Reverse、需要下载附件以及 flag 格式；公开可访问资料尚不足以可靠恢复具体校验算法和 flag。为避免把猜测写入能力库，本题暂不伪造答案。

## 推荐复现流程

1. 对附件执行 `file`、`strings -a`、`checksec`（如适用）做初筛。
2. 用 IDA/Ghidra 定位 `main`、输入读取函数和成功/失败字符串交叉引用。
3. 逆向输入变换与比较逻辑；若存在循环、查表、XOR/加减/位运算，写 Python 脚本复现。
4. 若静态分析受阻，使用 gdb/x64dbg 在比较前断点，观察目标缓冲区。
5. 只有在原附件上复现成功后填写 `verification.flag`。

## 来源

- https://ctf.bugku.com/challenges/detail/id/238.html

> 本条保留为待附件验证，不将未知 flag 写死。
