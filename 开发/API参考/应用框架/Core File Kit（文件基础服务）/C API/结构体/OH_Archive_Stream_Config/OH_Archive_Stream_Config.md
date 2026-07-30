# OH_Archive_Stream_Config

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive-oh-archive-stream-config
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_Archive_Stream_Config
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

流式压缩配置结构体。
 
**起始版本：** 26.0.0
 
**相关模块：** [Archive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive)
 
**所在头文件：** [oh_archive.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-archive-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t blockSize | 内存块大小，单位为bytes。当OH_Archive_CompressMethod设置为OH_ARCHIVE_COMPRESS_DEFLATE时，blockSize需不小于32768bytes。 起始版本： 26.0.0 |
| int32_t threadNum | 线程数，取值为正整数，如果大于设备核数，则使用设备核数。 起始版本： 26.0.0 |
| OH_Archive_StreamChecksumAlg checksum | 用于计算校验和的哈希算法。 起始版本： 26.0.0 |
| OH_Archive_CompressMethod method | 压缩算法。流式压缩和流式解压缩只支持OH_ARCHIVE_COMPRESS_DEFLATE。 起始版本： 26.0.0 |
