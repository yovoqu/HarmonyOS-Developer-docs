# ScsiPeripheral_BasicSenseInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-scsiperipheralddk-scsiperipheral-basicsenseinfo
**支持设备：** PC/2in1


```text
typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```


## 概述
**支持设备：** PC/2in1

sense data的基本信息。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)


## 汇总
**支持设备：** PC/2in1


### 成员变量
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| uint8_t responseCode | 响应码。 |
| bool valid | 信息有效标志位。 |
| uint64_t information | Information字段。 |
| uint64_t commandSpecific | Command-specific information字段。 |
| bool sksv | Sense key specific字段的标志位。 |
| uint32_t senseKeySpecific | Sense key specific字段。 |
