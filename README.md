# CTF Solution Library

用于持续沉淀公开 CTF 靶场/比赛真题的完整题解、解法转化卡、可复用 solver 与能力索引。

## 当前来源

- Bugku 比赛真题：https://ctf.bugku.com/challenges/index/gid/2.html

## 目录约定

```text
bugku/<序号_题名>/README.md       # 完整题解
bugku/<序号_题名>/card.json       # 按统一交付契约转正后的解法卡
cards/pending/bugku/              # 未转正/批量补充/待复核卡片
solvers/<category>/               # 可复用 solver，必须实现 solve(attachment_path, **kwargs)
data/capabilities.json            # 能力库本体
data/solver_manifest.json         # solver 统一调度清单
data/status_schema.json           # 四状态命名与旧状态映射
data/experience/                  # 从 verified 卡片沉淀的经验条目
tools/                            # 校验、自测、导入工具
docs/delivery_contract.md         # 统一交付契约
index.json                        # 全局机器索引
progress.json                     # 当前处理进度
```

## AI 接续读取顺序

1. `README.md`
2. `docs/delivery_contract.md`
3. `data/status_schema.json`
4. `progress.json`
5. `index.json`
6. `data/capabilities.json` 与 `data/solver_manifest.json`
7. 对应题目的 `bugku/.../card.json` 与 `README.md`

## 统一状态

只允许四种状态：

- `solved_verified`：`verification.flag` 非空，且 `verification.executed=true`，可复用 solver 有 `self_test`。
- `solved_unverified`：公开来源可见 flag，但本仓库未真实执行。
- `method_only`：有题目特定解法，但没有可核验 flag。
- `blocked`：缺附件、动态环境、目标页或证据冲突。

旧状态统一映射见 `data/status_schema.json`。

## 固化规则

- `solver` 必须有 `solve(attachment_path, **kwargs)` 统一入口。
- 可复用脚本必须支持 `python3 <solver>.py --self-test`。
- `solved_verified` 必须有 `verification.executed=true` 和真实 `executed_output`。
- 产物类脚本必须打印 `CTF_ARTIFACT <绝对路径>`。
- 没有真实执行输出时，不得写 `solved_verified`。
- 批量题解先停跑量，优先保证卡片可校验、可导入、可调度。
