# 第40题：loginjection

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第40题
- 题目名称：loginjection
- 题目类型：WEB
- 所属赛事：NUAACTF-2022
- 题目链接：https://ctf.bugku.com/challenges/detail/id/578.html
- 是否有附件：否
- 附件类型：无

## 题面
暂无完整题面。Bugku 比赛真题 WEB 第2页确认题名为 `loginjection`，所属赛事为 NUAACTF-2022。

## 分析过程
题名由 login + injection 组成，优先按登录注入题处理。可能方向包括 SQL 注入认证绕过、NoSQL 注入、LDAP 注入、模板注入或登录参数二次注入。详情页当前无法抓取，不能确认真实注入类型和最终 flag。

## 解题步骤
1. 启动场景，抓取登录请求和响应。
2. 判断参数位置：用户名、密码、remember、redirect、cookie、header。
3. 测试 SQL 认证绕过：`' or 1=1-- -`、`admin' #`、布尔盲注。
4. 若为 JSON 登录，测试 NoSQL 注入：`{"$ne": null}`、`{"$regex":".*"}`。
5. 若出现 LDAP/模板特征，切换对应 payload。
6. 登录成功后访问用户中心或 admin 页面读取 flag。

## 使用工具和命令
```bash
burp
curl -i -X POST '<scene_url>/login' -d 'username=admin&password=admin'
sqlmap -u '<authorized_scene_url>' --forms --batch
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：登录注入入口枚举、认证绕过和盲注读取。
- 是否需要写 solver：否，需先确认注入类型。
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：详情页缓存未取得，当前环境无法启动/访问 Bugku 动态场景。
- 已尝试方法：确认第40题在列表中的题名、赛事和 WEB 类型。
- 下一步建议：启动场景后抓取登录请求，确认注入类型并补全 payload 与 flag。
