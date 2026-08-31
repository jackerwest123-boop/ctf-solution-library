# 0014 traffic

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=1
- 详情页：https://ctf.bugku.com/challenges/detail/id/241.html
- 赛事：NUAACTF-2017
- 类型：MISC
- 当前状态：solved_unverified

## 已知线索

公开评论/资料提示本题为 USB 鼠标流量分析，flag 为 `nuaactf{usb_mouse}`。

## 为什么不是 solved_verified

当前仓库没有原始 pcap/usb 流量附件，也没有运行解析脚本并得到真实输出。因此本题只能标记为 `solved_unverified`。

## 后续验证要求

需要补入流量附件，写 `solve(attachment_path, **kwargs)`，解析 HID 鼠标坐标轨迹，输出可读图像或文本；产物类脚本需打印 `CTF_ARTIFACT <绝对路径>`。
