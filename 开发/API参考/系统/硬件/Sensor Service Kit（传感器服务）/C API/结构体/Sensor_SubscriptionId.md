# Sensor_SubscriptionId

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriptionid
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Sensor_SubscriptionId Sensor_SubscriptionId
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义传感器订阅ID结构体，用于唯一标识传感器订阅请求。该结构体用于标识一个传感器订阅操作，包含传感器类型、订阅的具体订阅条件等信息。开发者可以通过传感器订阅ID来管理传感器的订阅生命周期，包括激活、去激活和查询订阅状态等操作。
 
在订阅传感器数据时，作为订阅请求的参数，用于标识订阅关系，在查询已订阅的传感器信息时，用于获取对应的订阅状态和数据，在取消传感器订阅时，用于指定需要取消的订阅。
 
**起始版本：** 11
 
**相关模块：** [Sensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor)
 
**所在头文件：** [oh_sensor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-sensor-type-h)
