# 014 traffic

- 平台：Bugku
- 赛事：NUAACTF 2017
- 类型：MISC / Traffic
- Bugku ID：241
- 题面：`Emmm，这是什么流量...`
- 状态：`pending_attachment_validation`

## 当前结论

题面能够确认这是流量分析题，但公开免费资料没有提供足以核实具体协议、提取路径和 flag 的完整过程。不能仅凭题名假定为 HTTP、DNS、USB 或其他协议，因此暂不写死具体答案。

## 原流量包复现流程

1. `capinfos` / `tshark -q -z io,phs` 获取包统计和协议层次。
2. 查看 conversations/endpoints，定位主要通信双方和异常端口。
3. 对 TCP/UDP 流执行 Follow Stream；对 HTTP/FTP/SMB 等尝试导出对象。
4. 使用 `tshark` 搜索可打印字段、URI、DNS 查询、POST body、文件传输和异常载荷。
5. 若协议非标准，按端口和 payload 熵/特征重组应用层数据。
6. 对导出内容继续执行 `file`、`strings`、`binwalk`、解压/解码。

## 来源

- https://ctf.bugku.com/challenges/detail/id/241.html

> 当前卡保持 `verification.flag` 为空，等待原 pcap/pcapng 复验。
