# Bugku 0085 - Virtual Shop 2

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/472.html
- 赛事：HackINI-2023
- 类型：WEB
- 状态：method_only

## 识别

Virtual Shop 2 是商店业务逻辑的后续题，通常需要在第一题基础上关注更隐蔽的鉴权、状态和并发问题。

## 方法

保留流程图，比较商品、订单、优惠、余额与支付接口的状态变化；重点测试签名参数、回调伪造、并发购买、库存/余额竞争、隐藏商品或越权订单读取。

## 验证

未执行；无 flag。