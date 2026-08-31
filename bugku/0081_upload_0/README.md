# Bugku 0081 - Upload 0

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/465.html
- 赛事：HackINI-2023
- 类型：WEB
- 状态：method_only

## 识别

题名指向文件上传类 Web 题，通常需要检查前端限制、后端 MIME/扩展名校验、文件内容检测、路径回显和可访问上传目录。

## 方法

先确认上传接口、允许后缀、MIME、Content-Type 与服务端保存路径；再尝试白名单绕过、双后缀、大小写、特殊解析、图片马校验、目录遍历或条件竞争等思路。当前未取得真实授权题目环境，不能执行验证。

## 验证

未执行；无 flag。