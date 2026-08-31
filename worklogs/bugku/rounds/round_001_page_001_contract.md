# Bugku 比赛真题第001轮：page=1（第一轮-A补全 + 第一轮-B启动）

目标页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1

## 本轮执行口径

- 第一轮-A：补齐 page=1 的 0001—0020 题 detail URL、题号、赛事、类型、状态。
- 第一轮-B：启动 0001—0020 契约化整理；本轮先完成状态归一和已知 flag 可信度降级，不把未本地执行的题目冒充 solved_verified。
- 状态只使用：`solved_verified`、`solved_unverified`、`method_only`、`blocked`。

## 0001—0020 汇总

| 题号 | 题名 | 赛事 | 类型 | detail URL | 状态 | flag/候选 | 说明 |
|---:|---|---|---|---|---|---|---|
| 0001 | Caesar cipher | SusCTF-2017 | Crypto | https://ctf.bugku.com/challenges/detail/id/205.html | solved_unverified | Susctf{3e811e068f5ce27eb4bc1c37723d7ee2} | ROT13/凯撒偏移13；公开评论给出flag，未使用本仓库附件执行。 |
| 0002 | EasyXor | SusCTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/206.html | solved_unverified | Susctf{I_n3ed_hea1ing} | 公开评论给出整数数组与 index xor 脚本；本轮计算得到flag，但未用附件独立运行。 |
| 0003 | EasyReverse | SusCTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/207.html | solved_unverified | Susctf{W3lc0me_to_the_rever5e_w0rld!} | 公开评论显示IDA F5/strings可见flag；未本地执行附件。 |
| 0004 | Crack Zip | SusCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/208.html | solved_unverified | Susctf{ec1717de879b19792c77f5edacbb84dc} | 公开评论给出zip密码20170925与flag；未本地爆破附件。 |
| 0005 | misc1 | SusCTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/209.html | blocked |  | 仅补齐detail URL；未找到可核验公开flag或题目特定方法。 |
| 0006 | 鲲or鳗orGame | 强网杯-2019 | MISC | https://ctf.bugku.com/challenges/detail/id/221.html | method_only |  | GameBoy ROM；公开资料提示改内存C0A2/Best Score到FF/FFFF触发flag，但未取得可核验文本flag。 |
| 0007 | 强网先锋辅助 | 强网杯-2019 | Crypto | https://ctf.bugku.com/challenges/detail/id/222.html | blocked |  | 已补齐detail URL；公开缓存仅见附件task_cha.py.zip和收费WP，未找到可核验flag。 |
| 0008 | 强网先锋AD | 强网杯-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/223.html | solved_unverified | flag{mafakuailaiqiandaob} | 公开评论提示IDA中Base64字符串ZmxhZ3ttYWZha3VhaWxhaXFpYW5kYW9ifQ==解码得到flag；未本地运行附件。 |
| 0009 | 强网先锋打野 | 强网杯-2019 | MISC | https://ctf.bugku.com/challenges/detail/id/224.html | solved_unverified | qwxf{you_say_chick_beautiful?} | 公开评论/公开writeup提示zsteg --msb提取BMP隐写得到flag；未本地执行附件。 |
| 0010 | JustRe | 强网杯-2019 | Reverse | https://ctf.bugku.com/challenges/detail/id/225.html | solved_unverified | flag{0dcc509a6f75849b} | Bugku评论给出0dcc509a6f75849b，题面flag{}格式；未本地反编译执行。 |
| 0011 | robots | NUAACTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/238.html | blocked |  | detail ID按相邻题推断且待页面复核；旧目录存在，需升级契约。 |
| 0012 | nuaactf | NUAACTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/239.html | method_only |  | 题面提示.jar反编译、爆破，flag格式flag{}；未找到可核验flag。 |
| 0013 | b1nary | NUAACTF-2017 | Reverse | https://ctf.bugku.com/challenges/detail/id/240.html | blocked |  | detail ID按相邻题推断且待页面复核；旧目录存在，需升级契约。 |
| 0014 | traffic | NUAACTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/241.html | solved_unverified | nuaactf{usb_mouse} | 公开评论提示USB鼠标流量提取并给出flag；未本地运行pcap。 |
| 0015 | recover | NUAACTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/242.html | blocked |  | detail ID按相邻题推断且待页面复核；旧目录存在，需升级契约。 |
| 0016 | -++-- | NUAACTF-2017 | MISC | https://ctf.bugku.com/challenges/detail/id/243.html | solved_verified | nuaactf{br41nfuck_p1us} | 已修复颜文字Brainfuck solver并写入self-test输出。 |
| 0017 | 3-最好的语言 | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/244.html | solved_unverified | flag{PyC_1s_613u21i_N0t_Hard} | 旧卡已确认算法和flag，但尚未升级为契约solver/self-test。 |
| 0018 | 3-SimpleSMC | 网鼎杯-2018 | Reverse | https://ctf.bugku.com/challenges/detail/id/245.html | blocked |  | detail URL已确认；旧目录存在，需升级契约并验证。 |
| 0019 | 3-hafuhafu | 网鼎杯-2018 | Crypto | https://ctf.bugku.com/challenges/detail/id/246.html | solved_unverified | flag{D0nT_uS3_Th3_kN0w_n} | 旧卡有RSA分解解法和flag，但尚未契约化执行。 |
| 0020 | 3-Unpleasant_music | 网鼎杯-2018 | MISC | https://ctf.bugku.com/challenges/detail/id/247.html | blocked |  | detail ID按相邻题推断且待页面复核；旧目录存在，需升级契约。 |

## 统计

- solved_verified：1
- solved_unverified：10
- method_only：2
- blocked：7

## 未完成项

- `solved_unverified` 题目均有公开 flag 或公开评论支撑，但还没有在本仓库通过附件和 solver 真跑，不能算最终完成。
- 第001—010题仍需逐题创建或补齐 `bugku/<编号_题名>/README.md` 与 `card.json`。
- 第011—020题已有旧目录基础，但除第0016题外仍需按新契约升级。
- 第0011、0013、0015、0020 的 detail URL 目前按相邻 ID 推断，后续需要打开页面复核。

## 下一步完整提示

继续第一轮-B，不进入 page=2。具体任务：对 `https://ctf.bugku.com/challenges/index/gid/2.html?page=1` 的第0001—0020题逐题生成或升级 `bugku/<编号_题名>/README.md`、`bugku/<编号_题名>/card.json`；能本地执行的补 `solver.solve()`、`--self-test`、`verification.executed=true` 和真实输出；不能执行的保持 `solved_unverified`、`method_only` 或 `blocked`，不得伪造 `solved_verified`。
