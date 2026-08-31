# 0016 -++--

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/243.html
- 赛事：NUAACTF-2017
- 类型：MISC
- 当前状态：solved_verified

## 解题方法

本题是 Brainfuck 颜文字方言。关键是不能只过滤 ASCII `><+-.,[]`，因为真实附件由颜文字 token 组成。应按最长 token 优先替换，再执行标准 Brainfuck。

已修正映射包括：

- `(♥ ͜ʖ♥)` -> `-`
- `(> ͜ʖ(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*)` -> `.`

## 验证

复用 `solvers/misc/brainfuck_emoticon.py`，支持：

```bash
python3 solvers/misc/brainfuck_emoticon.py --self-test
```

已记录自测输出：

```text
SELF_TEST expected_output=A
translated_len=24 output='A'
translated_len=24 output='A'
SELF_TEST PASS
```

flag：`nuaactf{br41nfuck_p1us}`
