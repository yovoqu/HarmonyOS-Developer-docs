# Pocket2和PuraX机型进行UI适配，怎么区分

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-56

## Pocket2和PuraX机型进行UI适配，怎么区分
 


##### 问题现象

Pocket2和PuraX机型进行UI适配，请问怎么区分这两个机型？
 
 

##### 解决方案

Pocket2和PuraX机型在展开态时都是横向断点sm，纵向断点lg，无法通过断点区分。可根据当前机型来判断，通过[设备信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info)的marketName字段获取外部产品系列名称。
