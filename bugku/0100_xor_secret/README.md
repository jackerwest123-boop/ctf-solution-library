# Bugku 0100 - 异或的密件

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：待复核（列表缓存确认题名、赛事和类型）
- 赛事：NUAACTF-2022
- 类型：Crypto
- 状态：method_only

## 识别

题名直接指向 XOR 加密或异或密文分析。需要附件中的密文、密钥提示或程序逻辑才能验证。

## 方法

取得附件后，判断单字节 XOR、多字节循环 XOR、已知明文 `NUAACTF{`、重复密钥、频率分析或程序生成密钥；用已知前缀推导 key，再验证整体可读性与格式。

## 验证

未执行；无 flag。