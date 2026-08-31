# Bugku 0087 - strpos and substr

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/521.html
- 赛事：zh3r0-v2
- 类型：WEB
- 状态：method_only

## 识别

题名直接指向 PHP 字符串函数 `strpos` 与 `substr` 的边界、类型转换或过滤绕过。

## 方法

在授权环境中定位参数过滤逻辑，重点关注 `strpos` 返回 0 与 false 的弱比较、大小写/编码归一化、`substr` 截断、数组参数、空字节、URL 编码和多字节字符影响。

## 验证

未执行；无 flag。