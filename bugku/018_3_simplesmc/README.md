# 018 3-SimpleSMC

- 平台：Bugku
- 赛事：网鼎杯 2018
- 类型：Reverse / SMC
- Bugku ID：245
- 状态：`solved_verified`

## 解法

该程序把关键函数以 SMC（Self-Modifying Code，自修改/自解密代码）方式隐藏。IDA 中目标区域初始无法正常反编译，并夹有脏字节。

1. 修正脏字节/栈分析，使相关函数可以建立基本控制流。
2. 在 SMC 解密区域比较“正常 x86-64 函数序言”“当前加密函数开头”和另一段异或数据，可恢复 7 字节循环 key：`F1@gChe`。
3. 用该 key 与程序内另一字节区对目标代码逐字节双重 XOR，恢复真实函数。
4. 重新定义函数后，可见输入处理和最终校验逻辑。
5. 对题目给出的 32 字节 `enc` 数组逆向递归 XOR 过程，得到：

```text
flag{d0_y0u_Kn*w_5mC_F1@gCheCk?}
```

## 通用技法

SMC 题先不要把加密后的字节强行当正常指令分析。利用已知/可推断的函数序言、解密循环和运行时内存状态恢复代码，再重新创建函数；如果 SMC key 与 flag 校验本身是两层逻辑，要分别复现并验证。

## 来源

- https://ctf.bugku.com/challenges/detail/id/245.html
- https://cn-sec.com/archives/337876.html
