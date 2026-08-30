# 019 3-hafuhafu

- 平台：Bugku
- 赛事：网鼎杯 2018
- 类型：Crypto / RSA
- Bugku ID：246
- 状态：`solved_verified`

## 解法

题目给出 RSA 公钥参数，其中 `e = 65537`，模数 `n` 可以被分解。流程如下：

1. 若密文以文本形式给出，先按题目格式做 Base64 解码，恢复 RSA 密文整数/字节。
2. 分解 `n = p*q`。
3. 计算 `phi = (p-1)*(q-1)`。
4. 计算私钥指数 `d = e^{-1} mod phi`。
5. 计算 `m = c^d mod n`。
6. 将整数 `m` 转成大端字节串；注意明文可能在字节串后部，不应因为前面存在非UTF-8字节就直接丢弃。

Bugku 评论区多条独立记录给出并确认最终结果：

```text
flag{D0nT_uS3_Th3_kN0w_n}
```

## 可复用技法

看到 RSA 已知 `n,e,c` 时先判断 `n` 是否存在可行的分解途径（FactorDB、弱素数、费马分解、共享素因子等）。分解成功后标准恢复私钥；整数转字节时使用 `long_to_bytes`/`int.to_bytes`，不要盲目对整个缓冲区 `.decode()`。

## 来源

- https://ctf.bugku.com/challenges/detail/id/246.html
