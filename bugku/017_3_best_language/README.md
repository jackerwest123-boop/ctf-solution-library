# 017 3-最好的语言

- 平台：Bugku
- 赛事：网鼎杯 2018
- 类型：Reverse / Python Bytecode
- 状态：`solved_verified`

## 解法

附件内容对应 Python 2.7 字节码。还原后可知程序把 flag 分三段处理：前 12 字节循环 XOR、中间 7 字节取 MD5 原始摘要、后 10 字节循环 XOR，最后整体 Base64。

给定输出：

```text
U1VQU05pSHdqCEJrQu7FS7Vngk1OTQ58qqghXmt2AUdrcFBBUEU=
```

Base64 解码后切分为 12 + 16 + 10 字节。

1. 利用已知 flag 前缀对前 12 字节做 XOR 已知明文攻击，恢复 4 位循环密钥 `5914`，得到 `flag{PyC_1s_`。
2. 中间 16 字节为 MD5：`42eec54bb567824d4e4d0e7caaa8215e`，对应 7 字符明文 `613u21i`。
3. 后 10 字节使用另一组 4 位不重复数字密钥。利用结尾 `}` 约束并枚举候选，得到密钥 `4813`，解出 `_N0t_Hard}`。
4. 拼接并重新执行原编码算法，Base64 输出完全一致。

最终：

```text
flag{PyC_1s_613u21i_N0t_Hard}
```

## 可复用技法

重点不是记住两组密钥，而是：反编译 Python bytecode → 恢复数据分段 → 已知明文攻击循环 XOR → 利用格式约束缩小密钥空间 → 对不可逆哈希段单独做字典/查询 → 正向重编码验证完整答案。

## 来源

- https://ctf.bugku.com/writeup/detail/id/1774.html
- https://lb5.net/254.html
