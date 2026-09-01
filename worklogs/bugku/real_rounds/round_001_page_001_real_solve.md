# Bugku 第001轮真实解题记录：page=1 / 0001—0020

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1

## 新口径

- 本文件只记录真实解题进度。
- 一轮 20 题全部 `solved_verified` 才算“做完一轮”。
- 清单建档、README/card 建档、公开 writeup 线索均不等于真实解题完成。

## 当前真实进度

| 题号 | 题名 | 当前真实状态 | 说明 |
|---:|---|---|---|
| 0001 | Caesar cipher | solved_verified | 已新增 source-text 密文、solver、self-test 和真实运行输出。附件下载接口不可稳定抓取，未伪称为官方原始附件。 |
| 0016 | -++-- | solved_verified | 此前已用 `solvers/misc/brainfuck_emoticon.py` 完成 self-test 与执行验证。 |
| 0002—0015、0017—0020 | 待处理 | pending_real_solve | 必须重新获取附件/环境并真实执行验证。 |

## 0001 Caesar cipher 执行摘要

题目页显示题名 `Caesar cipher`、赛事 `SusCTF-2017`、类型 `Crypto`、题面描述 `Susctf{}`。Bugku 页面评论与公开 writeup 均出现密文：

```text
Fhfpgs{3r811r068s5pr27ro4op1p37723q7rr2}
```

执行：

```bash
python3 solvers/crypto/caesar_rot.py --self-test
python3 solvers/crypto/caesar_rot.py attachments/bugku/0001_caesar_cipher/cipher.txt
```

输出：

```text
SELF_TEST expected_output=Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}
SELF_TEST result={'flag': 'Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}', 'artifacts': [], 'evidence': 'matched Susctf\\{[0-9a-f]{32}\\} at caesar shift 13', 'shift': 13, 'decoded': 'Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}'}
SELF_TEST PASS

{"flag": "Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}", "artifacts": [], "evidence": "matched Susctf\\{[0-9a-f]{32}\\} at caesar shift 13", "shift": 13, "decoded": "Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}"}
```

## 下一步

继续第001轮真实解题，不进入后续页。下一题为 0002 `EasyXor`：https://ctf.bugku.com/challenges/detail/id/206.html。
