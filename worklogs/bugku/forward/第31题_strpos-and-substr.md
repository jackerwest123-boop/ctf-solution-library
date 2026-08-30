# 第31题：strpos and substr

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第31题
- 题目名称：strpos and substr
- 题目类型：WEB
- 所属赛事：zh3r0-v2
- 题目链接：https://ctf.bugku.com/challenges/detail/id/521.html
- 是否有附件：否
- 附件类型：无

## 题面
Can you bypass this WAF?

## 分析过程
题名和题面均指向 PHP 字符串函数过滤绕过：`strpos` 常用于判断子串位置，`substr` 常用于截取前缀、后缀或关键字符。Bugku 缓存页面只提供题面和“启动场景”，没有泄露源码或 flag。当前无法启动动态场景，因此不能确认具体 WAF 逻辑。

## 解题步骤
1. 启动场景后抓取首页源码和所有可控参数。
2. 判断过滤位置：查询参数、POST 参数、Cookie、Header 或路径。
3. 围绕 `strpos` 的返回值特性测试：位置 0、`false`、弱比较 `==`、强比较 `===`。
4. 围绕 `substr` 截断逻辑测试：空字符串、数组参数、URL 编码、双写、大小写、前后缀拼接。
5. 若存在文件读取或命令执行入口，在绕过 WAF 后读取 flag。

## 使用工具和命令
```bash
curl -i '<scene_url>'
curl -i '<scene_url>?param[]=flag'
curl -i '<scene_url>?param=%66%6c%61%67'
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：分析 PHP 字符串函数和过滤条件，结合数组、编码、弱类型等特性绕过 WAF。
- 是否需要写 solver：否，具体 payload 强依赖源码。
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：当前环境无法启动/访问 Bugku 动态场景，公开缓存只有题面，不能编造 flag。
- 已尝试方法：检索 Bugku 题目页和比赛真题 WEB 列表。
- 下一步建议：启动场景后读取源码或枚举参数，确认 `strpos/substr` 过滤条件后补全 payload 和 flag。

## JSON 解法转化卡
```json
{
  "title": "strpos and substr",
  "source_id": "[Bugku] 第31题",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": ["bugku", "web", "strpos", "substr", "waf", "绕过", "PHP", "字符串函数"],
    "attachment_features": "无附件；动态 Web 场景题",
    "condition": "题面出现 strpos/substr/WAF/bypass 等关键词，且需要绕过 PHP 字符串过滤时适用。"
  },
  "method": {
    "principle": "分析 PHP 字符串函数和过滤条件，结合数组、编码、弱类型等特性绕过 WAF。",
    "steps": ["定位可控参数", "测试 strpos 返回 0/false 的弱比较边界", "测试 substr 前后缀截断", "结合数组参数、URL 编码、双写和大小写绕过过滤", "读取 flag"],
    "tools": ["curl", "burp"],
    "produces_artifact": false
  },
  "solver": {
    "reusable": false,
    "module_name": "php_waf_bypass_notes",
    "code": "",
    "input": "场景 URL 和源码/过滤规则。",
    "output": "可用绕过 payload。"
  },
  "verification": {
    "flag": "",
    "how": "启动 Bugku 场景后根据源码确认过滤逻辑并提交 payload。"
  }
}
```
