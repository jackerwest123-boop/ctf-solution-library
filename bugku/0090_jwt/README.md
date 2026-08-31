# Bugku 0090 - jwt

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/544.html
- 赛事：NUAACTF-2020
- 类型：WEB
- 状态：method_only

## 识别

题名指向 JWT 认证题，重点是 token 获取、解码、签名算法、密钥、声明字段和服务端验证逻辑。

## 方法

在授权环境中抓取 JWT，Base64URL 解码 header/payload，检查 `alg:none`、HS/RS 混淆、弱密钥、kid 文件路径/注入、过期时间、角色字段和签名验证差异。当前未执行。

## 验证

未执行；无 flag。