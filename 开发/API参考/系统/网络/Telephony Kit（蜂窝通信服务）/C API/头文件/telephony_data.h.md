# telephony_data.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-data-h
**支持设备：** Phone | Tablet | Wearable

#### 概述

**支持设备：** Phone | Tablet | Wearable

为电话蜂窝数据定义C接口。
 
**引用文件：** <telephony/cellular_data/telephony_data.h>
 
**库：** libtelephony_data.so
 
**系统能力：** SystemCapability.Telephony.CellularData
 
**起始版本：** 13
 
**相关模块：** [Telephony](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony)
 
  

#### 汇总

**支持设备：** Phone | Tablet | Wearable

  

#### 函数

**支持设备：** Phone | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| int32_t OH_Telephony_GetDefaultCellularDataSlotId(void) | 获取默认移动数据的SIM卡接口。 |
 
 
  

#### 函数说明

**支持设备：** Phone | Tablet | Wearable

  

#### OH_Telephony_GetDefaultCellularDataSlotId()

**支持设备：** Phone | Tablet | Wearable

```text
int32_t OH_Telephony_GetDefaultCellularDataSlotId(void)
```
 
**描述**
 
获取默认移动数据的SIM卡接口。
 
**系统能力：** SystemCapability.Telephony.CellularData
 
**起始版本：** 13
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 默认移动数据的SIM卡接口 (0 表示卡槽1, 1 表示卡槽2)。 |
