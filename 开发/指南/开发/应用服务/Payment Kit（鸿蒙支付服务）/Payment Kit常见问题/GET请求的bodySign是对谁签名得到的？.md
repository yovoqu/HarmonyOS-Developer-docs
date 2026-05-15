# GET请求的bodySign是对谁签名得到的？

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-3

GET请求需要对path url进行签名，例如[查询支付订单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-sys-query-order)的待签名内容是：“/api/v2/aggr/transactions/orders/{sysTransOrderNo}”。
