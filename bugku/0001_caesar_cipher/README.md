# 0001 Caesar cipher

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/205.html
- 赛事：SusCTF-2017
- 类型：Crypto
- 状态：`solved_verified`
- 是否计入真实做出：是

## 真实解题口径

本题已从原先 `solved_unverified` 修正为真实执行验证。Bugku 附件下载接口未能稳定抓取，仓库内 `attachments/bugku/0001_caesar_cipher/cipher.txt` 是根据 Bugku 题目页评论和公开 writeup 中一致出现的题目密文整理出的 source-text 输入，不伪称为官方原始附件。

## 题目输入

```text
Fhfpgs{3r811r068s5pr27ro4op1p37723q7rr2}
```

## 解题过程

1. 题名为 `Caesar cipher`，题面格式为 `Susctf{}`。
2. 对题目密文枚举 Caesar 位移。
3. 位移 13 时得到符合 `Susctf{[0-9a-f]{32}}` 的 flag。

## 运行验证

```bash
python3 solvers/crypto/caesar_rot.py --self-test
python3 solvers/crypto/caesar_rot.py attachments/bugku/0001_caesar_cipher/cipher.txt
```

self-test 输出：

```text
SELF_TEST expected_output=Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}
SELF_TEST result={'flag': 'Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}', 'artifacts': [], 'evidence': 'matched Susctf\\{[0-9a-f]{32}\\} at caesar shift 13', 'shift': 13, 'decoded': 'Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}'}
SELF_TEST PASS
```

实际运行输出：

```json
{"flag": "Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}", "artifacts": [], "evidence": "matched Susctf\\{[0-9a-f]{32}\\} at caesar shift 13", "shift": 13, "decoded": "Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}"}
```

## flag

```text
Susctf{3e811e068f5ce27eb4bc1c37723d7ee2}
```
