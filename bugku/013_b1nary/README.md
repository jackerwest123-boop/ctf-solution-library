# 013 b1nary

- 平台：Bugku
- 赛事：NUAACTF 2017
- 类型：Reverse
- 状态：`pending_attachment_validation`

## 当前结论

公开可访问资料可以确认该题属于 NUAACTF 2017 Reverse，但没有找到足以逐步复现其实际校验算法和最终 flag 的免费原始题解。为保持能力库可信度，本题不根据题名或解题记录反推答案。

## 原附件到手后的分析顺序

1. `file` / `strings -a` / `checksec` 判断格式、架构、保护。
2. IDA/Ghidra 定位输入函数、比较函数和成功字符串。
3. 优先检查自定义编码、异或、查表、CRC/哈希以及反调试。
4. 若存在大量间接跳转或状态机，识别是否为简单 VM/混淆。
5. 将最终校验逻辑转写为 Python，并以程序成功分支复验。

## 来源

- https://ctf.bugku.com/challenges/index/gid/2.html

> 该卡标记为待原附件验证，`verification.flag` 留空。
