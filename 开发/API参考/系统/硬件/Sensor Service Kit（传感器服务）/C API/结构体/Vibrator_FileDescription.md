# Vibrator_FileDescription

更新时间：2026-08-14 11:17:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-filedescription
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Vibrator_FileDescription { ... } Vibrator_FileDescription
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

振动文件描述。用于描述自定义振动序列的文件信息，支持使用自定义振动文件实现精确振动控制。
 
**起始版本：** 11
 
**相关模块：** [Vibrator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator)
 
**所在头文件：** [vibrator_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t fd | 自定义振动序列的文件句柄，需指向包含振动序列数据的有效文件。使用前应通过文件操作API（如open）打开文件并获取句柄。fd必须为有效且可读的文件句柄，不能为负值或无效句柄。 |
| int64_t offset | 自定义振动序列的偏移地址，单位：B（字节）。用于指定从文件中读取振动序列的起始位置，offset≥0且小于文件大小。offset=0表示从文件开头读取，offset>0表示跳过前offset个字节。offset超出文件大小时行为未定义。 |
| int64_t length | 自定义振动序列的总长度，单位：B（字节）。表示从offset位置开始读取的字节数。length必须>0，且offset+length不能超过文件大小。length超出文件剩余大小时可能读取失败或产生未定义行为。 |
