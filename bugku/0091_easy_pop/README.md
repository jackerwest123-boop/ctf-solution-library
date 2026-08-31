# Bugku 0091 - easy-pop

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/545.html
- 赛事：NUAACTF-2020
- 类型：WEB
- 状态：method_only

## 识别

`pop` 在 Web CTF 中常指 PHP POP 链/反序列化。需要源码或对象结构支撑，不能凭题名填 flag。

## 方法

在授权环境中寻找源码泄露、类定义、反序列化入口和魔术方法；构造对象链时关注 `__wakeup`、`__destruct`、`__toString`、属性可控性、访问修饰符编码和过滤绕过。

## 验证

未执行；无 flag。