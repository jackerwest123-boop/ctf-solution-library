# Bugku 0119 Temple of Time

- 来源：https://ctf.bugku.com/challenges/detail/id/601.html
- 赛事：InterKosenCTF-2019
- 类型：MISC
- 状态：method_only
- 真实解题：否

## 口径说明

本目录仅完成契约卡建档，不代表已经做出题目。公开页面评论提供了 pcapng/HTTP URI 过滤、URL 解码和 ASCII 拼接的题目特定方向，但本仓库未下载附件、未运行 tshark、未验证 flag。

## 方法框架

1. 获取原始 pcapng 附件。
2. 用 tshark 过滤耗时异常的 HTTP 请求或响应 URI。
3. 对 URI 中编码内容进行 URL 解码。
4. 将十进制 ASCII 拼接为候选 flag。
5. 本地记录命令输出后才能升级为 `solved_verified`。