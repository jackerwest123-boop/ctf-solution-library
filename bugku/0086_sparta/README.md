# Bugku 0086 - Sparta

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/520.html
- 赛事：zh3r0-v2
- 类型：WEB
- 状态：method_only

## 识别

题名无法仅凭列表确定具体漏洞点，应作为动态 Web 题先做信息收集与路由枚举。

## 方法

在授权环境中检查首页源代码、HTTP 头、隐藏路径、robots/sitemap、JS、Cookie、参数、错误栈和常见备份文件；再根据响应特征转入注入、模板、文件读取或逻辑绕过方向。

## 验证

未执行；无 flag。