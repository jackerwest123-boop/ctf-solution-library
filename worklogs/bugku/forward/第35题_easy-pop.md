# 第35题：easy-pop

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第35题
- 题目名称：easy-pop
- 题目类型：WEB
- 所属赛事：NUAACTF-2020
- 题目链接：https://ctf.bugku.com/challenges/detail/id/545.html
- 是否有附件：否
- 附件类型：无

## 题面
nuaactf{}

## 分析过程
该题为 PHP 反序列化 POP 链题。Bugku 详情页公开评论给出关键利用方向：构造 `lemon` 对象，并让其内部属性指向 `evil` 对象；部分评论提示 private/protected 属性要注意 NUL 字节编码或整体编码，否则容易因为特殊字符导致反序列化失败。

当前无法启动动态场景读取完整源码，因此不能确认类定义、触发点和最终 flag。为避免编造 flag，本题先沉淀为 blocked 状态和通用 PHP POP 链能力卡。

## 解题步骤
1. 启动场景并读取源码，确认类名、属性名和魔术方法。
2. 找到能够触发文件读取、命令执行、字符串转换或析构逻辑的类。
3. 构造对象链，使入口对象的属性指向危险类实例。
4. 对 private/protected 属性名中的 NUL 字节进行 URL 编码或 base64 编码。
5. 通过 GET 参数 `d` 或题目指定参数传入序列化字符串。
6. 触发反序列化并读取 flag。

## 使用工具和命令
```bash
php -r 'echo serialize($obj);'
python3 - <<'PY'
from urllib.parse import quote
payload='O:5:"lemon":1:{...}'
print(quote(payload, safe=""))
PY
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：读取 PHP 类定义后构造可触发魔术方法的反序列化对象链。
- 是否需要写 solver：否，当前更适合沉淀为手工检查流程。
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：当前环境无法启动/访问 Bugku 动态场景，公开缓存仅提供题面和评论 payload 线索，不能编造最终 flag。
- 已尝试方法：检索 Bugku 题目页、比赛真题 WEB 列表和公开评论线索。
- 下一步建议：启动场景后读取完整源码，修正对象链并补全 `verification.flag`。

## JSON 解法转化卡
```json
{
  "title": "easy-pop",
  "source_id": "[Bugku] 第35题",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": ["bugku", "web", "easy-pop", "CTF", "比赛真题", "网页", "php", "unserialize", "POP", "反序列化"],
    "attachment_features": "无附件；动态 Web 场景题",
    "condition": "题面或列表出现 easy-pop，且为 PHP 反序列化/POP 链动态场景题时适用。"
  },
  "method": {
    "principle": "读取 PHP 类定义后构造可触发魔术方法的反序列化对象链。",
    "steps": [
      "读取/观察源码中的类和魔术方法",
      "构造对象链触发 __destruct/__wakeup/__toString 等方法",
      "对 private/protected 属性名做 NUL 字节编码",
      "URL 编码或 base64 编码后通过参数传入"
    ],
    "tools": ["php", "python3", "burp"],
    "produces_artifact": false
  },
  "solver": {
    "reusable": false,
    "module_name": "php_pop_payload_notes",
    "code": "",
    "input": "动态场景源码和类定义。",
    "output": "可提交的序列化 payload。"
  },
  "verification": {
    "flag": "",
    "how": "启动 Bugku 场景后读取源码，构造 lemon/evil 对象链并提交 payload。"
  }
}
```
