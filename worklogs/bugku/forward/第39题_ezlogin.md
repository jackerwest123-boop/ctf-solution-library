# 第39题：ezlogin

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第39题
- 题目名称：ezlogin
- 题目类型：WEB
- 所属赛事：NUAACTF-2022
- 题目链接：https://ctf.bugku.com/challenges/detail/id/577.html
- 是否有附件：否
- 附件类型：无

## 题面
flag{}

## 分析过程
该题为登录相关 Web 题。Bugku 详情页公开评论给出关键线索：PHP 中数组的 MD5 值相等；看 URL 可发现文件包含漏洞；读取当前页源码后继续读取 `hint.php` 源码；最终 flag 路径为 `/answer/flagggg`。另有评论给出 `php://filter/convert.base64-encode/resource=hint` 和 `php://filter/convert.base64-encode/resource=/answer/flagggg` 的读取方向。

当前无法启动动态场景提交请求，因此不能确认最终 flag。为避免编造 flag，本题先沉淀为 blocked 状态和通用“文件包含读源码+PHP 弱类型绕过”能力卡。

## 解题步骤
1. 启动场景，观察登录表单、跳转 URL 和可控参数。
2. 测试登录校验中是否存在 `md5($a) == md5($b)` 这类弱比较。
3. 用数组参数绕过 MD5 比较，例如 `a[]=1&b[]=2`，使 `md5(array)` 结果同为 `NULL`。
4. 寻找 `file` 参数，使用 `php://filter/convert.base64-encode/resource=当前文件` 读取源码。
5. 读取 `hint.php`，确认 flag 实际路径。
6. 使用 `php://filter/convert.base64-encode/resource=/answer/flagggg` 读取并 base64 解码。

## 使用工具和命令
```bash
curl -i '<scene_url>/setu.php?file=php://filter/convert.base64-encode/resource=hint'
curl -i '<scene_url>/setu.php?file=php://filter/convert.base64-encode/resource=/answer/flagggg'
base64 -d
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：PHP 数组 MD5 弱比较绕过 + php://filter 文件包含读取源码和 flag。
- 是否需要写 solver：否，主要依赖场景 URL 和参数名。
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：当前环境无法启动/访问 Bugku 动态场景，无法读取 `/answer/flagggg` 实际内容。
- 已尝试方法：检索 Bugku 题目页、比赛真题 WEB 列表和公开评论线索。
- 下一步建议：启动场景后按上述路径读取并补全 `verification.flag`。

## JSON 解法转化卡
```json
{
  "title": "ezlogin",
  "source_id": "[Bugku] 第39题",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": ["bugku", "web", "ezlogin", "CTF", "比赛真题", "网页", "login", "登录", "md5", "文件包含", "php://filter"],
    "attachment_features": "无附件；动态 Web 场景题",
    "condition": "题面或评论出现登录、数组 MD5 相等、file 参数或 php://filter 文件包含线索时适用。"
  },
  "method": {
    "principle": "通过 PHP 数组 MD5 弱比较绕过登录，再用 php://filter 文件包含读取源码和 flag。",
    "steps": [
      "测试登录参数是否存在 md5 弱比较",
      "用数组参数让 md5(array) 结果异常或同为 NULL",
      "通过 file 参数和 php://filter 读取当前页源码",
      "继续读取 hint.php 或题目提示文件",
      "读取最终 flag 路径并 base64 解码"
    ],
    "tools": ["curl", "burp", "base64"],
    "produces_artifact": false
  },
  "solver": {
    "reusable": false,
    "module_name": "php_md5_lfi_notes",
    "code": "",
    "input": "动态场景 URL 和可控 file 参数名。",
    "output": "可读取源码或 flag 的 php://filter payload。"
  },
  "verification": {
    "flag": "",
    "how": "启动场景后读取 /answer/flagggg，并将返回内容 base64 解码。"
  }
}
```
