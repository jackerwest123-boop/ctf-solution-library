# Bugku 0082 - Upload 1

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/466.html
- 赛事：HackINI-2023
- 类型：WEB
- 状态：method_only

## 识别

题名显示为上传绕过进阶题，应在 Upload 0 基础上进一步关注多层校验和服务端解析差异。

## 方法

抓包定位上传字段、返回路径和服务端响应；检查扩展名黑白名单、MIME、文件头、图片二次渲染、`.htaccess`、解析后缀、Web 容器规则和上传目录执行权限。未进入真实题目环境执行。

## 验证

未执行；无 flag。