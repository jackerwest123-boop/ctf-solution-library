# Bugku 0097 - superezpop

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/579.html
- 赛事：NUAACTF-2022
- 类型：WEB
- 状态：method_only

## 识别

题名显示为更简单的 PHP POP/反序列化题。需要源码或类链才能落地。

## 方法

在授权环境中寻找源码泄露、类定义、反序列化入口；分析魔术方法调用链、属性可控性、过滤函数和目标 sink，构造最小化序列化对象进行验证。

## 验证

未执行；无 flag。