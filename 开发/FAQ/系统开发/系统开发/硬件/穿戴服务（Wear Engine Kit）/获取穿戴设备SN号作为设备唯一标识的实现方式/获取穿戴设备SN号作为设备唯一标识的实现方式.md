# 获取穿戴设备SN号作为设备唯一标识的实现方式

更新时间：2026-07-22 03:28:08

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-kit-new-00001

#### 问题现象

运动表GT系列如何获取设备ID？
 
 

#### 背景知识

穿戴设备不支持OAID、AAID等设备唯一标识。
 
 

#### 解决方案

当前没有直接获取穿戴设备唯一ID的接口。可通过手机获取连接穿戴设备的SN号，调用[wearengine_api#getSerialNumber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api#getserialnumber)接口实现。
