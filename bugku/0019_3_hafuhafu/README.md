# 0019 3-hafuhafu

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/246.html
- 赛事：网鼎杯-2018
- 类型：Crypto
- 当前状态：solved_unverified

## 已知结论

旧卡记录本题为 RSA 分解题：已知 n/e/c，分解 n 得到 p/q 后按标准私钥公式解密。旧卡记录 flag：

`flag{D0nT_uS3_Th3_kN0w_n}`

## 为什么不是 solved_verified

当前 canonical 卡尚未通过统一入口 `solve(attachment_path, **kwargs)` 对原始附件执行，也没有 `--self-test` 的真实输出，因此只能保持 `solved_unverified`。
