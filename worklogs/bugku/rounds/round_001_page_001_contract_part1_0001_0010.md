# Bugku 第001轮-B 第一阶段：0001—0010 契约文件创建

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1

## 完成范围

本次只处理第0001—0010题，未进入 page=2。

已为以下题目创建 canonical 目录、`README.md` 与 `card.json`：

| 题号 | 题名 | 状态 |
|---:|---|---|
| 0001 | Caesar cipher | solved_unverified |
| 0002 | EasyXor | solved_unverified |
| 0003 | EasyReverse | solved_unverified |
| 0004 | Crack Zip | solved_unverified |
| 0005 | misc1 | blocked |
| 0006 | 鲲or鳗orGame | method_only |
| 0007 | 强网先锋辅助 | blocked |
| 0008 | 强网先锋AD | solved_unverified |
| 0009 | 强网先锋打野 | solved_unverified |
| 0010 | JustRe | solved_unverified |

## 验收说明

- 以上10题均已有 `bugku/<编号_题名>/README.md` 与 `bugku/<编号_题名>/card.json`。
- 未使用原始附件执行的题目均保持 `solved_unverified`、`method_only` 或 `blocked`。
- 本次没有新增 `solved_verified`。
- 公开 flag 未经本仓库附件和 solver 真跑，均未标记为 `verification.executed=true`。

## 下一步完整提示

继续第一轮-B第二阶段，不进入 page=2。具体任务：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=1` 的第0011—0020题逐题生成或升级 canonical 路径 `bugku/<四位编号_题名>/README.md`、`bugku/<四位编号_题名>/card.json`；第0016题可以复用已修复的 `solvers/misc/brainfuck_emoticon.py` 并保持 `solved_verified`；其余题如果不能用原始附件真实执行，就只能保持 `solved_unverified`、`method_only` 或 `blocked`，不得伪造 `solved_verified`。
