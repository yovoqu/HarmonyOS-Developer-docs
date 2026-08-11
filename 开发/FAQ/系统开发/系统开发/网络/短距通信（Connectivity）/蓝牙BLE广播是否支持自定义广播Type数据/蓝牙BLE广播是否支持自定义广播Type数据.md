# 蓝牙BLE广播是否支持自定义广播Type数据

更新时间：2026-07-22 03:28:08

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-kit-new-00002

#### 问题现象

使用BLE广播时，通过nRF Connect工具解析广播包数据，获取的数据类型Type均为0xFF（厂商私有数据），没有0x01（广告标记位）、0x09（设备名称）等其他类型数据。是否可以自定义广播Type数据？
 
 

#### 解决方案

当前API不支持直接设置任意的AD Type值，不同字段对应不同的AD Type，具体如下：
  
| 字段 | AD Type |
| --- | --- |
| serviceUuids（服务UUID声明） | 0x02/0x03/0x06/0x07 |
| serviceData（服务数据，带UUID的自定义数据） | 0x16 |
| manufactureData（厂商私有数据） | 0xFF |
| includeDeviceName: true（设备名称） | 0x09 |
 
 
可以通过[serviceData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#servicedata)（0x16）、includeDeviceName（0x09）等字段来使用蓝牙规范中定义的其他AD Type，而非所有数据都必须通过[manufactureData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#manufacturedata)（0xFF）发送。
 
更多BLE广播相关内容可参考[BLE广播流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide#ble广播流程)。
