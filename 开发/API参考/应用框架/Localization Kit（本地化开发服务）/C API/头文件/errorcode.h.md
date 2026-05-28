# errorcode.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供国际化接口返回的错误码。
 
**引用文件：** <i18n/errorcode.h>
 
**库：** libohi18n.so
 
**系统能力：** SystemCapability.Global.I18n
 
**起始版本：** 22
 
**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| I18n_ErrorCode | I18n_ErrorCode | 国际化错误码。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### I18n_ErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum I18n_ErrorCode
```
 
**描述**
 
国际化错误码。
 
**系统能力：** SystemCapability.Global.I18n
 
**起始版本：** 22
  
| 枚举项 | 描述 |
| --- | --- |
| SUCCESS = 0 | 成功。 |
| ERROR_INVALID_PARAMETER = 8900001 | 传入参数无效。 |
| UNEXPECTED_ERROR = 8900050 | 预期之外的错误，例如内存错误。 |
