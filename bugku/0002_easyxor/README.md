# 0002 EasyXor

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/206.html
- 赛事：SusCTF-2017
- 类型：Reverse
- 状态：`solved_verified`

## 解法

Bugku-206题目页公开评论给出22项整数数组：`[83,116,113,96,112,99,125,78,87,103,57,110,104,82,102,106,113,32,123,125,115,104]`。逐项执行 `chr(value ^ index)`，拼接得到 flag。

可复用 solver：`solvers/reverse/easyxor_index.py`，实现 `solve(attachment_path, **kwargs)` 和 `--self-test`。

## 真实验证

2026-09-01实际执行输出：

```text
SELF_TEST source=Bugku-206-comment-array
decoded=Susctf{I_n3ed_hea1ing}
SELF_TEST PASS
```

Flag：`Susctf{I_n3ed_hea1ing}`。
