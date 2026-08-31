# Bugku 0084 - Virtual Shop

- 来源页：https://ctf.bugku.com/challenges/index/gid/2.html?page=5
- 详情页：https://ctf.bugku.com/challenges/detail/id/471.html
- 赛事：HackINI-2023
- 类型：WEB
- 状态：method_only

## 识别

题名指向虚拟商店业务逻辑题，可能涉及价格、余额、库存、订单状态、优惠券、支付回调或参数篡改。

## 方法

在授权题目环境中梳理登录、商品、购物车、下单、支付、回调等流程；重点检查客户端价格、整数溢出/负数、并发条件竞争、优惠券复用、JWT/session、IDOR 和业务状态机绕过。

## 验证

未执行；无 flag。