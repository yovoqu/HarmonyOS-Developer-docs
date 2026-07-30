# OH_Archive_StreamInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive-oh-archive-streaminfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_Archive_StreamInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

流式压缩/解压缩信息结构体。
 
**起始版本：** 26.0.0
 
**相关模块：** [Archive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive)
 
**所在头文件：** [oh_archive.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-archive-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint64_t totalInSize | 压缩/解压缩前输入数据大小，单位为bytes。 起始版本： 26.0.0 |
| uint64_t totalOutSize | 压缩/解压缩后输出数据大小，单位为bytes。 起始版本： 26.0.0 |
| uint32_t checksum | 未压缩数据的校验和。当OH_Archive_StreamChecksumAlg设置为OH_ARCHIVE_NO_CHECKSUM时，checksum为0。 起始版本： 26.0.0 |
