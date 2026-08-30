# 第38题：Make Me Cry

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第38题
- 题目名称：Make Me Cry
- 题目类型：WEB
- 所属赛事：NUAACTF-2021
- 题目链接：https://ctf.bugku.com/challenges/detail/id/568.html
- 是否有附件：否
- 附件类型：无

## 题面
暂无完整题面。Bugku 比赛真题 WEB 第2页确认题名为 `Make Me Cry`，所属赛事为 NUAACTF-2021。

## 分析过程
当前只能确认题目列表元数据，详情页缓存未取得，无法确认漏洞类型。先按动态 Web 题通用流程建档，后续启动场景后补充题面、payload 和 flag。

## 解题步骤
1. 启动场景，抓取首页源码、注释、静态 JS/CSS 和响应头。
2. 枚举目录和常见文件：`robots.txt`、`.git/`、`www.zip`、`backup.zip`、`index.php~`。
3. 根据题面和源码判断漏洞类型：SQL 注入、文件包含、模板注入、反序列化、XSS/bot 或权限绕过。
4. 构造 payload 并读取 flag。

## 使用工具和命令
```bash
curl -i '<scene_url>'
feroxbuster -u '<scene_url>'
burp
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：Web 动态场景基础探测和源码/备份/参数枚举。
- 是否需要写 solver：否，需先取得具体题面。
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：详情页缓存未取得，当前环境无法启动/访问 Bugku 动态场景。
- 已尝试方法：确认第38题在列表中的题名、赛事和 WEB 类型。
- 下一步建议：启动场景后补全题面并继续复现。
