# ScsiPeripheral_TestUnitReadyRequest

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iperipheralddk-scsiperipheral-testunitreadyrequest
**支持设备：** PC/2in1


```text
typedef struct ScsiPeripheral_TestUnitReadyRequest {...} ScsiPeripheral_TestUnitReadyRequest
```


## 概述
**支持设备：** PC/2in1

命令（test unit ready）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)


## 汇总
**支持设备：** PC/2in1


### 成员变量
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| uint8_t control | Control字段，用于指定一些控制信息。 |
| uint32_t timeout | 超时时间(单位: 毫秒)。 |
