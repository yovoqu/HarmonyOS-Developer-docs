# OH_AVRecorder_Metadata

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVRecorder_Metadata {...} OH_AVRecorder_Metadata
```
  

##### 概述

元数据信息数据结构。
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
**所在头文件：** [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char* genre | 媒体资源的类型或体裁。 |
| char* videoOrientation | 视频的旋转方向，单位为度。 |
| OH_AVRecorder_Location location | 视频的地理位置信息。 |
| OH_AVRecorder_MetadataTemplate customInfo | 从 moov.meta.list 读取的自定义参数键值映射。 |
