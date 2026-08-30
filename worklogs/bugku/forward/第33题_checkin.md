# 第33题：checkin

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第33题
- 题目名称：checkin
- 题目类型：WEB
- 所属赛事：NUAACTF-2020
- 题目链接：https://ctf.bugku.com/challenges/detail/id/543.html
- 是否有附件：否
- 附件类型：无

## 题面
题目描述只给出 flag 格式：`nuaactf{}`。

## 分析过程
这是典型 checkin / view-source 入门题。题面没有业务交互逻辑，评论区提示“源代码的最下面”“查看页面源代码”，并有用户直接给出 flag。因此通用判断是：优先查看 HTML 源码、注释、末尾隐藏文本。

## 解题步骤
1. 打开题目场景。
2. 查看页面源代码，优先检查 HTML 注释、隐藏节点、页面底部内容。
3. 在源码中搜索 `nuaactf{`、`flag{`、`ctf{` 等 flag 格式。
4. 记录发现的 flag。

## 使用工具和命令
```bash
curl -s "$URL" | grep -Eo 'nuaactf\{[^}]+\}|flag\{[^}]+\}|ctf\{[^}]+\}'
```

## 结果
flag：`nuaactf{we1cOme_to_NuaAcTF}`

## 可复用性判断
- 是否可复用：可复用
- 可复用技法：HTML 源码/注释/隐藏文本 flag 搜索
- 是否需要写 solver：是
- 是否产生 artifact：否

## blocked 情况
- blocked：否

## JSON 解法转化卡
```json
{
  "title": "checkin源码隐藏flag检查",
  "source_id": "[Bugku] 第33题 checkin",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": ["checkin", "view-source", "source", "comment", "源码", "注释", "签到"],
    "attachment_features": "无附件，题面仅给出 flag 格式，页面可能在源码或注释中隐藏 flag",
    "condition": "当 Web 入门题没有明显交互逻辑且题名为 checkin/签到/源码相关时适用"
  },
  "method": {
    "principle": "检查 HTML 源码、注释和隐藏节点中的 flag 字符串。",
    "steps": [
      "请求题目首页或场景页面 HTML",
      "保存或查看页面源代码",
      "搜索常见 flag 格式和 HTML 注释",
      "若页面源码含 flag，直接提取并提交"
    ],
    "tools": ["curl", "grep", "python3"],
    "produces_artifact": false
  },
  "solver": {
    "reusable": true,
    "module_name": "web_source_flag_grep",
    "code": "import re, sys, urllib.request\n\nPAT = re.compile(rb'(?:flag|ctf|nuaactf)\\{[^}]{1,200}\\}', re.I)\n\ndef main():\n    if len(sys.argv) < 2:\n        print('Usage: python3 web_source_flag_grep.py <url>')\n        sys.exit(1)\n    url = sys.argv[1]\n    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    with urllib.request.urlopen(req, timeout=15) as r:\n        data = r.read()\n    hits = sorted(set(m.group(0).decode('utf-8', 'ignore') for m in PAT.finditer(data)))\n    for h in hits:\n        print(h)\n\nif __name__ == '__main__':\n    main()\n",
    "input": "题目场景 URL",
    "output": "页面源码中匹配到的 flag 候选"
  },
  "verification": {
    "flag": "nuaactf{we1cOme_to_NuaAcTF}",
    "how": "python3 web_source_flag_grep.py <challenge_url>"
  }
}
```
