# OH_AVRecorder_Metadata

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVRecorder_Metadata {...} OH_AVRecorder_Metadata
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义录制的元数据结构，用于描述媒体资源的体裁分类、视频旋转方向、地理位置及自定义参数等元数据信息，适用于录制过程中需要携带或读取媒体元数据的场景。
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
**所在头文件：** [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char* genre | 媒体资源的体裁分类，应为有效的体裁分类字符串。 |
| char* videoOrientation | 视频的旋转角度，单位为度（°），仅支持特定角度值：0°（无旋转，视频保持原始方向）、90°（顺时针旋转90度）、180°（旋转180度）、270°（顺时针旋转270度）。不设置时默认为0°。传入不支持的角度值时，设置失败。 |
| OH_AVRecorder_Location location | 媒体资源的地理位置信息，包含纬度（latitude）和经度（longitude）。其中latitude取值范围[-90, 90]，longitude取值范围[-180, 180]，单位为度（°）。 |
| OH_AVRecorder_MetadataTemplate customInfo | 从 moov.meta.list 读取的自定义参数键值映射，键和值均为字符串类型，用于在录制时携带应用自定义的元数据标签，如添加业务标识、扩展属性等场景。 |
