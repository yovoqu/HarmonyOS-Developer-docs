# OH_Pixelmap_HdrGainmapMetadata

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-image-nativemodule-oh-pixelmap-hdrgainmapmetadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Pixelmap_HdrGainmapMetadata {...} OH_Pixelmap_HdrGainmapMetadata
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

HDR_GAINMAP_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint16_t writerVersion | 元数据编写器使用的版本。 |
| uint16_t miniVersion | 元数据解析需要理解的最小版本。 |
| uint8_t gainmapChannelNum | Gainmap的颜色通道数，值为3时RGB通道的元数据值不同，值为1时各通道元数据值相同。 |
| bool useBaseColorFlag | 是否使用基础图的色彩空间，参考ISO 21496-1。true表示使用，false表示不使用。 |
| float baseHeadroom | 基础图提亮比，参考ISO 21496-1。 |
| float alternateHeadroom | 提取的可选择图像提亮比，参考ISO 21496-1。 |
| float gainmapMax[3] | 增强图像的最大值，参考ISO 21496-1。 |
| float gainmapMin[3] | 增强图像的最小值，参考ISO 21496-1。 |
| float gamma[3] | gamma值，参考ISO 21496-1。 |
| float baselineOffset[3] | 基础图的偏移，参考ISO 21496-1。 |
| float alternateOffset[3] | 提取的可选择图像偏移量，参考ISO 21496-1。 |
