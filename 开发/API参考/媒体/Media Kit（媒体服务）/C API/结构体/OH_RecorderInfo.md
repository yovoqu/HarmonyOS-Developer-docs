# OH_RecorderInfo

更新时间：2026-04-02 08:41:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-recorderinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_RecorderInfo {...} OH_RecorderInfo
```
  

##### 概述

录制文件信息。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char* url | 录制文件的URL。 |
| uint32_t urlLen | 录制文件的URL的长度值。 |
| OH_ContainerFormatType fileFormat | 录制文件的格式。 |
