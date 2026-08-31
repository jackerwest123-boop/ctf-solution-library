# Bugku 0083 - Upload 2

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/467.html
- 赛事：HackINI-2023
- 类型：WEB
- 状态：method_only

## 识别

上传系列第三题，通常应假设存在更强过滤或需要组合信息泄露、路径控制、内容构造等步骤。

## 方法

在授权环境中先复现上传行为，再分析文件名清洗、后缀截断、服务端图片处理、临时文件、访问路径和可能的二次触发点；必要时结合源码泄露或错误信息定位真实检查逻辑。

## 验证

未执行；无 flag。