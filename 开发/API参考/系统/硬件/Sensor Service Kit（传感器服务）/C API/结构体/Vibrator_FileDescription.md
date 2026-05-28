# Vibrator_FileDescription

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-filedescription
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Vibrator_FileDescription { ... } Vibrator_FileDescription
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

振动文件描述。
 
**起始版本：** 11
 
**相关模块：** [Vibrator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator)
 
**所在头文件：** [vibrator_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t fd | 自定义振动序列的文件句柄。 |
| int64_t offset | 自定义振动序列的偏移地址。 |
| int64_t length | 自定义振动序列的总长度。 |
