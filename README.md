# CTF Solution Library

用于持续沉淀公开 CTF 靶场/比赛真题的完整题解、解法转化卡、可复用 solver 与能力索引。

## 当前来源

- Bugku 比赛真题：https://ctf.bugku.com/challenges/index/gid/2.html

## 目录约定

```text
bugku/<序号_题名>/README.md   # 完整题解
bugku/<序号_题名>/card.json   # 解法转化卡
solvers/<category>/           # 可复用 solver
data/                          # capabilities / manifest / experience
tools/                         # 解法卡模板与导入工具
index.json                     # 全局机器索引
progress.json                  # 当前处理进度
```

## AI 接续读取顺序

1. `README.md`
2. `progress.json`
3. `index.json`
4. `data/`
5. 对应题目的 `bugku/.../card.json` 与 `README.md`

## 固化规则

- `method` 只保存通用技法，不硬编码单题答案。
- `verification.flag` 仅用于验证。
- 可复用脚本进入 `solvers/<category>/`。
- 若脚本产出图片/文件，打印 `CTF_ARTIFACT <绝对路径>`。
- 默认每批处理 10 道题。
