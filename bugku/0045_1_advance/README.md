# 0045 1-advance

- 来源页：<https://ctf.bugku.com/challenges/index/gid/2.html?page=3>
- 详情页：<https://ctf.bugku.com/challenges/detail/id/272.html>
- 赛事：网鼎杯-2018
- 类型：Reverse
- 状态：`method_only`

## 方法要点
按逆向校验题处理，先识别文件格式与字符串，再定位输入校验函数，提取常量、查表、异或或算术约束并脚本化还原。未取得原始附件，未执行验证。

## 验证
`verification.executed=false`，无真实输出，不标 `solved_verified`。
