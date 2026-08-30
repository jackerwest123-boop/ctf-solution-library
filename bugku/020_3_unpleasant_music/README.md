# 020 3-Unpleasant_music

- 平台：Bugku
- 赛事：网鼎杯 2018
- 类型：MISC
- 状态：`pending_attachment_validation`

## 当前结论

Bugku 公共索引能够确认该题属于网鼎杯 2018 MISC，但目前可公开检索到的免费资料没有提供可逐字核验的附件类型、隐写方式和 flag。题名虽然含 `music`，但不能据此直接认定为频谱、摩斯、DTMF、DeepSound 或其他音频隐写，因此不将任何特定音频技法冒充本题已验证解法。

## 原附件到手后的低成本取证顺序

1. `file`、`ffprobe`、`exiftool`、`strings` 确认真实格式、编码参数和附加数据。
2. 若为 WAV/无损音频，检查 RIFF chunk、尾随数据、双声道差分和低有效位。
3. 用 Audacity/Sonic Visualiser 查看波形、频谱/声谱图。
4. 检查可能的 Morse、DTMF、FSK 等可听/可视编码。
5. 用 `binwalk` 检查嵌入文件；如发现压缩/容器特征再做提取。
6. 只有在原附件上完成复现后，才把具体技法和 flag 写入 validated 能力。

## 来源

- https://ctf.bugku.com/challenges/index/gid/2.html

> 当前 `verification.flag` 留空，防止题名驱动的错误归因。
