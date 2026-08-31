# Bugku 0098 - 从零开始的勇士之路

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/580.html
- 赛事：NUAACTF-2022
- 类型：Crypto
- 状态：method_only

## 识别

详情页可见题目描述包含 `NUAACTF{}`，评论线索提到 affine/仿射密码和暴力破解，但本仓库未取得附件并执行验证。

## 方法

取得附件后，优先识别密文字符集与仿射密码参数空间；对常见模数和 `a` 可逆条件做暴力枚举，按 `NUAACTF{}` 格式、可读文本或题面提示筛选候选。

## 验证

未执行；无 flag。