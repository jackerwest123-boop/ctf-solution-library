# Bugku 题库真实做题轮次重置记录

## 重置原因

用户明确要求：必须真正做出题目才算做完一轮。因此此前第001—007轮中的 `A_completed`、`B_completed` 只能视为清单或契约工件建档，不能视为真实完成轮次。

## 新硬规则

- `完成一轮` 只能表示该轮 20 题全部达到 `solved_verified`。
- `solved_verified` 必须具备 `verification.executed=true`、真实执行输出和可复用 solver/self-test。
- `solved_unverified`、`method_only`、`blocked` 均不计入真正做出。
- 第001轮未达到 20/20 `solved_verified` 前，不再把后续页称为已做完。

## 已保留但降格说明

- 第001—007轮已有清单、README、card 仍作为资料和索引保留。
- 这些建档成果不再作为“做完一轮”的依据。
- 后续从第001轮 page=1 重新按真实解题推进。

## 本次实际继续工作

- 第0001题 `Caesar cipher` 已从 `solved_unverified` 升级为 `solved_verified`。
- 新增 `attachments/bugku/0001_caesar_cipher/cipher.txt`，内容为 source-text 密文，不伪称为官方原始附件。
- 新增 `solvers/crypto/caesar_rot.py`，实现 `solve(attachment_path, **kwargs)` 与 `--self-test`。
- 已执行 self-test 和题目输入验证，输出 `Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}`。

## 当前真实轮次状态

第001轮 page=1 当前真正已验证题目：0001、0016。

第001轮距离真正完成仍缺 18 题：0002—0015、0017—0020。

下一步应继续真实解第0002题 `EasyXor`，不能跳到第008轮或把已有建档轮次称为做完。
