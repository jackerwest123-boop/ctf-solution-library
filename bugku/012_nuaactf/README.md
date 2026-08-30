# 012 nuaactf

- 平台：Bugku
- 赛事：NUAACTF 2017
- 类型：Reverse / Java-JAR
- 状态：`solved_verified`

## 解题链

1. 附件为 JAR，先用 JD-GUI/CFR 等反编译。
2. 程序对 4 字符口令做摘要校验；对字母数字空间爆破可得口令 `mdzz`。
3. 口令字节经 MD5 后作为 AES 密钥，IV 为 16 个 `*`，使用 AES-CBC-PKCS5 解开程序内加密 class。
4. 对解密后的 class 继续反编译，沿调用链找到目标字节数组及两轮按索引条件异或的校验逻辑。
5. 逆运算恢复核心字符串 `bY73c0D3_W17h_C0D3`。
6. Bugku 当前提交格式为 `flag{}`，最终提交：

```text
flag{bY73c0D3_W17h_C0D3}
```

## 可复用要点

JAR 逆向遇到“入口类只负责口令验证，真实逻辑藏在加密 class”时，应把工作拆成：反编译入口 → 爆破短口令 → 复现 KDF/AES → 导出解密 class → 二次反编译 → 逆向最终字节变换。

## 来源

- https://ctf.bugku.com/challenges/detail/id/239.html
- https://ctf.bugku.com/writeup/detail/id/1282.html
