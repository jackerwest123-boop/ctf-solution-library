# 015 recover

- 平台：Bugku
- 赛事：NUAACTF 2017
- 类型：MISC / Forensics
- Bugku ID：242
- 题面：`咦，这图片打不开诶，尺寸也不对？`
- 状态：`method_identified_flag_pending`

## 已确认解法方向

公开的 NUAACTF 2017 原赛 WriteUp 记载：附件是无法正常打开的 PNG，作者最初准备修文件头，但先执行了 `strings`，立即发现了关键隐藏内容。因此这题的第一优先级并不是盲目修改 PNG 宽高，而是先从原始字节中提取可打印字符串。

推荐流程：

```bash
file recover.png
strings -a -n 4 recover.png
xxd -l 64 recover.png
```

如果 `strings` 已出现 flag/比赛前缀，直接验证；若只出现提示，再检查 PNG signature、IHDR 宽高和 CRC，并在修复后继续查看图片。

## 当前未填 flag 的原因

现存免费文字版 WriteUp 的 flag 位于一张已失效/无法抓取的截图中，正文没有逐字给出，因此本仓库不把无法核验的截图内容猜成 flag。取得原附件后，随附的通用 `printable_flag_scan.py` 可以直接扫描。

## 来源

- https://ctf.bugku.com/challenges/detail/id/242.html
- https://primykq.github.io/2017/10/22/%E6%88%91%E5%B0%B1%E6%98%AF%E6%83%B3%E8%AF%95%E8%AF%95%E8%BF%99%E4%B8%AA%E7%AB%9E%E8%B5%9B%E7%9A%84%E5%90%8D%E5%AD%97%E7%A9%B6%E7%AB%9F%E8%83%BD%E6%89%93%E5%A4%9A%E9%95%BF%E5%A4%9A%E9%95%BF%E5%A4%9A%E9%95%BF-nuaactf-WriteUp/
