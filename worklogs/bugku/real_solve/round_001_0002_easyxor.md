# Round 001 real solve — 0002 EasyXor

- URL: https://ctf.bugku.com/challenges/detail/id/206.html
- Date: 2026-09-01
- Result: `solved_verified`

Bugku题目页公开评论给出数组：

`[83,116,113,96,112,99,125,78,87,103,57,110,104,82,102,106,113,32,123,125,115,104]`

按 `chr(value ^ index)` 实际执行得到：

```text
SELF_TEST source=Bugku-206-comment-array
decoded=Susctf{I_n3ed_hea1ing}
SELF_TEST PASS
```

已新增 `solvers/reverse/easyxor_index.py`，支持 `solve(attachment_path, **kwargs)` 与 `--self-test`。

验收：`verification.executed=true` 且保存真实输出，满足 `docs/delivery_contract.md` 的 `solved_verified` 条件。
