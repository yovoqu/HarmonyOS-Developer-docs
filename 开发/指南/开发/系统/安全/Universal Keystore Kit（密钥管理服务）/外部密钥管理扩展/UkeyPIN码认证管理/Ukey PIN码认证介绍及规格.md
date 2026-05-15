# Ukey PIN码认证介绍及规格

更新时间：2026-03-20 09:49:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-pin-authentication-management-overview

PIN（Personal Identification Number）码是Ukey设备的安全访问凭证，采用“硬件设备+PIN码”的双因子认证模式。用户必须同时拥有物理Ukey设备和正确的PIN码才能访问设备内的密钥材料。

 PIN码作用如下：


 Ukey使用resourceId标识Ukey资源，生态应用打开资源之后，如需要操作resourceId对应的私钥执行签名操作，则需要先验证PIN码。


> [!NOTE]
> HUKS提供PIN码认证能力和认证状态查询能力。应用PIN码认证之前，可以先查询认证状态。如果需要PIN码认证，则需要拉起证书管理应用，完成PIN码认证。
