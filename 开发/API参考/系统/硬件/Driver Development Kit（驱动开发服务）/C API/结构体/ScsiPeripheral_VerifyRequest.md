# ScsiPeripheral_VerifyRequest

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-scsiperipheralddk-scsiperipheral-verifyrequest
**支持设备：** PC/2in1


```text
typedef struct ScsiPeripheral_VerifyRequest {...} ScsiPeripheral_VerifyRequest
```


## 概述
**支持设备：** PC/2in1

SCSI命令（verify）的请求结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)


## 汇总
**支持设备：** PC/2in1


### 成员变量
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| uint32_t lbAddress | 起始逻辑块地址。 |
| uint16_t verificationLength | 连续校验逻辑块的个数。 |
| uint8_t control | Control字段，用于指定一些控制信息。 |
| uint8_t byte1 | CDB的第一个字节。 |
| uint8_t byte6 | CDB的第六个字节。 |
| uint32_t timeout | 超时时间(单位: 毫秒)。 |
