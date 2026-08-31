# Bugku 0096 - loginjection

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/578.html
- 赛事：NUAACTF-2022
- 类型：WEB
- 状态：method_only

## 识别

题名由 login 与 injection 组成，优先考虑登录注入或认证流程中的注入漏洞。

## 方法

在授权环境中抓取登录请求，检查 SQL/NoSQL/LDAP/模板等注入面；注意参数类型、JSON body、过滤关键字、错误提示、布尔差异、时间差异和认证后权限变化。

## 验证

未执行；无 flag。