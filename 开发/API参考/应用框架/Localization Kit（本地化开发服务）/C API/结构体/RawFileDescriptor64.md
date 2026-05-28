# RawFileDescriptor64

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor64
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} RawFileDescriptor64
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH_ResourceManager_GetRawFileDescriptor64](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h#oh_resourcemanager_getrawfiledescriptor64)的输出参数,涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。
 
**起始版本：** 11
 
**相关模块：** [rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)
 
**所在头文件：** [raw_file.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int fd | rawfile文件描述符，单位为int。 |
| int64_t start | rawfile在HAP包中的起始位置，单位为int64_t。 |
| int64_t length | rawfile在HAP包中的长度，单位为int64_t。 |
