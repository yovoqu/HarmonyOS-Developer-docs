# OH_AVRecorder_MetadataTemplate

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadatatemplate
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVRecorder_MetadataTemplate {...} OH_AVRecorder_MetadataTemplate
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义音视频录制过程中元数据的基本模板，通过键值对（key-value）形式组织元数据信息，适用于需要在录制输出中附加自定义元数据（如标题、作者、描述等）的场景。
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
**所在头文件：** [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char* key | 元数据的键。 |
| char* value | 元数据的值。 |
