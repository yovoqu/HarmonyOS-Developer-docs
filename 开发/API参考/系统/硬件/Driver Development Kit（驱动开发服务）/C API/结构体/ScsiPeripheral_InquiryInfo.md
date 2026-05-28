# ScsiPeripheral_InquiryInfo

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryinfo
**支持设备：** PC/2in1

```text
typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```
  

#### 概述

**支持设备：** PC/2in1

SCSI inquiry 数据。
 
**起始版本：** 18
 
**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)
 
**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)
 
  

#### 汇总

**支持设备：** PC/2in1

  

#### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| uint8_t deviceType | 设备类型。 |
| char idVendor[SCSIPERIPHERAL_VENDOR_ID_LEN + 1] | 制造商 id。 |
| char idProduct[SCSIPERIPHERAL_PRODUCT_ID_LEN + 1] | 产品 id。 |
| char revProduct[SCSIPERIPHERAL_PRODUCT_REV_LEN + 1] | 产品版本。 |
| ScsiPeripheral_DeviceMemMap* data | 所有的查询数据。 |
