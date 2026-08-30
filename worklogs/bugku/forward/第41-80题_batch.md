# Bugku 第41—80题批量处理记录

目标题库：https://ctf.bugku.com/challenges/index/gid/2/tid/1/status/-1.html

说明：本批为第31—80轮中的第41—80题续做。当前无法启动 Bugku 动态容器，因此已按题库索引、题名和公开列表线索建立 blocked-carded 记录；不编造 flag。

## 第41题：superezpop
- 赛事：NUAACTF-2022
- 类型：WEB
- 状态：blocked-carded
- 判断方向：php-反序列化/POP
- 分析：PHP 反序列化 POP 链，题面和公开评论提示可直接访问 flag.php 或通过对象链读取 flag。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“php-反序列化/POP”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第41题_superezpop.md；cards/pending/bugku/第41题_superezpop.card.json

## 第42题：？？？？
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：基础源码/隐藏路径
- 分析：题名异常，优先检查页面源码、注释、前端资源、robots.txt 和隐藏路由。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“基础源码/隐藏路径”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第42题_？？？？.md；cards/pending/bugku/第42题_？？？？.card.json

## 第43题：broken motto
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：前端/逻辑绕过
- 分析：题名暗示页面口号或前端逻辑损坏，优先审计 HTML/JS、Cookie、LocalStorage 与请求参数。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“前端/逻辑绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第43题_broken-motto.md；cards/pending/bugku/第43题_broken-motto.card.json

## 第44题：cookies
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：Cookie 篡改
- 分析：题名直接指向 Cookie，检查身份字段、签名字段、弱 secret、Base64/JSON Cookie。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“Cookie 篡改”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第44题_cookies.md；cards/pending/bugku/第44题_cookies.card.json

## 第45题：close eyes
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：源码/弱校验
- 分析：题名暗示肉眼不可见或关闭可见界面，优先查源码、隐藏元素、CSS、JS 条件判断。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“源码/弱校验”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第45题_close-eyes.md；cards/pending/bugku/第45题_close-eyes.card.json

## 第46题：edr
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：信息泄露/规则绕过
- 分析：题名较短，按通用 WEB 入门流程检查源码、HTTP 响应头、目录、参数、弱口令与调试信息。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“信息泄露/规则绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第46题_edr.md；cards/pending/bugku/第46题_edr.card.json

## 第47题：getpost
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：GET/POST 参数
- 分析：题名指向 GET 与 POST 同时传参，测试同名参数、方法覆盖和服务端取值优先级。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“GET/POST 参数”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第47题_getpost.md；cards/pending/bugku/第47题_getpost.card.json

## 第48题：intval
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：PHP 弱类型/整数转换
- 分析：题名指向 PHP intval，测试数组、科学计数法、进制、前缀截断、溢出与字符串比较。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“PHP 弱类型/整数转换”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第48题_intval.md；cards/pending/bugku/第48题_intval.card.json

## 第49题：jwt
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：JWT 伪造
- 分析：题名指向 JWT，解析 header/payload，测试 none、弱 secret、kid/jku、用户字段改 admin。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“JWT 伪造”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第49题_jwt.md；cards/pending/bugku/第49题_jwt.card.json

## 第50题：just_login
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：登录绕过
- 分析：题名指向登录逻辑，测试默认账号、SQL 注入、弱比较、Cookie/Session 篡改。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“登录绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第50题_just_login.md；cards/pending/bugku/第50题_just_login.card.json

## 第51题：read flag
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：文件读取
- 分析：题名指向读 flag，测试任意文件读取、路径穿越、include 参数、源码泄露。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“文件读取”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第51题_read-flag.md；cards/pending/bugku/第51题_read-flag.card.json

## 第52题：wh1sper's_secret_garden
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：隐藏路由/信息泄露
- 分析：题名暗示 secret garden，检查 robots、备份文件、前端路径、目录枚举和源码注释。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“隐藏路由/信息泄露”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第52题_wh1sper-s_secret_garden.md；cards/pending/bugku/第52题_wh1sper-s_secret_garden.card.json

## 第53题：robots
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：robots.txt
- 分析：题名直指 robots.txt，访问 /robots.txt 并跟踪 Disallow/Sitemap 中的隐藏路径。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“robots.txt”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第53题_robots.md；cards/pending/bugku/第53题_robots.card.json

## 第54题：switch
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：分支条件绕过
- 分析：题名指向 switch/case，测试参数值、弱类型匹配、case 穿透和默认分支。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“分支条件绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第54题_switch.md；cards/pending/bugku/第54题_switch.card.json

## 第55题：view source
- 赛事：0xGame-2020
- 类型：WEB
- 状态：blocked-carded
- 判断方向：查看源码
- 分析：题名直指查看源码，检查 HTML 源码、source 参数、备份文件和 .phps 泄露。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“查看源码”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第55题_view-source.md；cards/pending/bugku/第55题_view-source.card.json

## 第56题：booli
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：布尔/弱类型绕过
- 分析：题名暗示 bool，测试 true/false、数组、0e、空字符串、JSON 布尔和 PHP 弱比较。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“布尔/弱类型绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第56题_booli.md；cards/pending/bugku/第56题_booli.card.json

## 第57题：bug1
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：通用 WEB 漏洞
- 分析：题名泛化，先做源码、参数、目录、Cookie、响应头、备份文件基础探测。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“通用 WEB 漏洞”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第57题_bug1.md；cards/pending/bugku/第57题_bug1.card.json

## 第58题：bug2
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：通用 WEB 漏洞
- 分析：题名泛化，沿 bug1 思路补测方法覆盖、文件读取、注入、反序列化入口。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“通用 WEB 漏洞”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第58题_bug2.md；cards/pending/bugku/第58题_bug2.card.json

## 第59题：command
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：命令执行/过滤绕过
- 分析：题名指向命令参数，测试白名单、拼接点、分隔符过滤与输出回显。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“命令执行/过滤绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第59题_command.md；cards/pending/bugku/第59题_command.card.json

## 第60题：diao图管理器(已跑路
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：文件上传/图片管理
- 分析：题名指向图片管理器，测试上传校验、扩展名/MIME 绕过、图片马和读取路径。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“文件上传/图片管理”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第60题_diao图管理器-已跑路.md；cards/pending/bugku/第60题_diao图管理器-已跑路.card.json

## 第61题：upload
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：文件上传
- 分析：题名直指上传，测试后缀、MIME、内容魔术头、解析差异与上传目录访问。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“文件上传”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第61题_upload.md；cards/pending/bugku/第61题_upload.card.json

## 第62题：header
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：HTTP Header
- 分析：题名指向请求头，测试 X-Forwarded-For、Referer、User-Agent、Cookie、Authorization。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“HTTP Header”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第62题_header.md；cards/pending/bugku/第62题_header.card.json

## 第63题：proto
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：原型污染/协议字段
- 分析：题名指向 proto，优先测试 JS __proto__/constructor 原型污染或 HTTP 协议字段差异。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“原型污染/协议字段”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第63题_proto.md；cards/pending/bugku/第63题_proto.card.json

## 第64题：robot
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：robots.txt/爬虫路径
- 分析：题名指向 robot，检查 /robots.txt、隐藏目录和禁爬文件。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“robots.txt/爬虫路径”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第64题_robot.md；cards/pending/bugku/第64题_robot.card.json

## 第65题：search
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：搜索参数注入
- 分析：题名指向搜索功能，测试 SQL/NoSQL/模板注入、通配符、正则与回显过滤。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“搜索参数注入”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第65题_search.md；cards/pending/bugku/第65题_search.card.json

## 第66题：session
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：Session 篡改/固定
- 分析：题名指向 session，测试 Cookie 序列化、签名弱密钥、会话固定和身份字段。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“Session 篡改/固定”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第66题_session.md；cards/pending/bugku/第66题_session.card.json

## 第67题：ssti
- 赛事：0xGame-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：模板注入
- 分析：题名直指 SSTI，识别模板引擎，测试表达式回显并构造安全范围内的文件读取。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“模板注入”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第67题_ssti.md；cards/pending/bugku/第67题_ssti.card.json

## 第68题：Become Admin
- 赛事：TamilCTF-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：权限提升
- 分析：题名要求成为管理员，检查 Cookie/JWT/会话字段、IDOR、角色字段和弱签名。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“权限提升”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第68题_become-admin.md；cards/pending/bugku/第68题_become-admin.card.json

## 第69题：CringeNcoder
- 赛事：TamilCTF-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：编码/解码绕过
- 分析：题名暗示 encoder，检查 Base64/URL/HTML/Unicode/多层编码与服务端解码差异。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“编码/解码绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第69题_cringencoder.md；cards/pending/bugku/第69题_cringencoder.card.json

## 第70题：It's paid
- 赛事：TamilCTF-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：支付/价格逻辑
- 分析：题名指向付费逻辑，测试价格参数、优惠券、负数、浮点精度和客户端信任。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“支付/价格逻辑”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第70题_it-s-paid.md；cards/pending/bugku/第70题_it-s-paid.card.json

## 第71题：Meeting
- 赛事：TamilCTF-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：会议/访问控制
- 分析：题名指向会议或预约，测试邀请码、会议 ID 枚举、权限校验和隐藏接口。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“会议/访问控制”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第71题_meeting.md；cards/pending/bugku/第71题_meeting.card.json

## 第72题：Recovery
- 赛事：TamilCTF-2021
- 类型：WEB
- 状态：blocked-carded
- 判断方向：找回流程绕过
- 分析：题名指向密码/账号恢复，测试重置 token、邮箱参数、验证码、Host 头污染。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“找回流程绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第72题_recovery.md；cards/pending/bugku/第72题_recovery.card.json

## 第73题：A Simple Calculator
- 赛事：UMDCTF-2022
- 类型：WEB
- 状态：blocked-carded
- 判断方向：表达式注入
- 分析：题名为计算器，测试 eval、模板表达式、沙箱逃逸和算式解析限制。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“表达式注入”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第73题_a-simple-calculator.md；cards/pending/bugku/第73题_a-simple-calculator.card.json

## 第74题：real ez node
- 赛事：西湖论剑-2023
- 类型：WEB
- 状态：blocked-carded
- 判断方向：Node.js WEB
- 分析：题名指向 Node，测试原型污染、模板注入、反序列化、路由/中间件问题。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“Node.js WEB”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第74题_real-ez-node.md；cards/pending/bugku/第74题_real-ez-node.card.json

## 第75题：easy api
- 赛事：西湖论剑-2023
- 类型：WEB
- 状态：blocked-carded
- 判断方向：API 访问控制
- 分析：题名指向 API，测试接口枚举、鉴权缺失、方法切换、JSON 参数污染。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“API 访问控制”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第75题_easy-api.md；cards/pending/bugku/第75题_easy-api.card.json

## 第76题：Node Magical Login
- 赛事：西湖论剑-2023
- 类型：WEB
- 状态：blocked-carded
- 判断方向：Node 登录绕过
- 分析：题名指向 Node 登录，测试 JSON 类型混淆、NoSQL 注入、JWT/Session 和弱比较。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“Node 登录绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第76题_node-magical-login.md；cards/pending/bugku/第76题_node-magical-login.card.json

## 第77题：MemeHub
- 赛事：BSides-Algiers-2k21-CTF-Quals
- 类型：WEB
- 状态：blocked-carded
- 判断方向：内容平台/上传
- 分析：题名像内容平台，测试上传、对象 ID、模板渲染、XSS/SSRF 的 CTF 安全场景。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“内容平台/上传”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第77题_memehub.md；cards/pending/bugku/第77题_memehub.card.json

## 第78题：Trashbin
- 赛事：BSides-Algiers-2k21-CTF-Quals
- 类型：WEB
- 状态：blocked-carded
- 判断方向：粘贴板/对象访问
- 分析：题名像垃圾箱/粘贴板，测试对象 ID 枚举、删除恢复、未授权读取和路径泄露。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“粘贴板/对象访问”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第78题_trashbin.md；cards/pending/bugku/第78题_trashbin.card.json

## 第79题：slasher
- 赛事：BSides-Algiers-2k21-Finals-chals
- 类型：WEB
- 状态：blocked-carded
- 判断方向：路径/斜杠绕过
- 分析：题名含 slash，测试路径规范化、双斜杠、URL 编码、目录穿越和路由绕过。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“路径/斜杠绕过”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第79题_slasher.md；cards/pending/bugku/第79题_slasher.card.json

## 第80题：passparser
- 赛事：BSides-Algiers-2k21-Finals-chals
- 类型：WEB
- 状态：blocked-carded
- 判断方向：解析器差异
- 分析：题名指向 parser，测试参数解析差异、重复键、数组/对象类型和密码字段绕过。
- 复现步骤：启动场景后先查源码/响应头/Cookie/robots.txt/参数，再围绕“解析器差异”构造最小请求，得到 flag 后回填 verification.flag。
- 输出计划：worklogs/bugku/forward/第80题_passparser.md；cards/pending/bugku/第80题_passparser.card.json
