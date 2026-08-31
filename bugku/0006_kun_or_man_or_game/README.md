# 0006 鲲or鳗orGame

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/221.html
- 赛事：强网杯-2019
- 类型：MISC
- 状态：`method_only`

## 当前结论

公开资料提示这是 GameBoy ROM 方向，可能通过修改内存地址 `C0A2` 或 Best Score 到 `FF/FFFF` 触发 flag，但没有取得可核验文本 flag。

## 验证情况

`verification.executed=false`。未取得 ROM 附件并在模拟器中复现。