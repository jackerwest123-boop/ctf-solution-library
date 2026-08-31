# Bugku 0092 - command-injection

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/546.html
- 赛事：NUAACTF-2020
- 类型：WEB
- 状态：method_only

## 识别

题名明确指向命令注入。仅允许在授权 CTF 环境中做最小化验证，不对真实目标使用。

## 方法

定位可控参数和命令执行回显/盲注特征；在授权题目中测试分隔符、换行、管道、反引号、变量展开、编码绕过、空格替代和关键字过滤；读取题目指定 flag 文件前先确认范围。

## 验证

未执行；无 flag。