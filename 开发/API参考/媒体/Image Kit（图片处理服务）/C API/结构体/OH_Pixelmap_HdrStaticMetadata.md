# OH_Pixelmap_HdrStaticMetadata

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-image-nativemodule-oh-pixelmap-hdrstaticmetadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Pixelmap_HdrStaticMetadata {...} OH_Pixelmap_HdrStaticMetadata
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

HDR_STATIC_METADATA关键字对应的静态元数据值。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| float displayPrimariesX[3] | 归一化后显示设备三基色的X坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。 |
| float displayPrimariesY[3] | 归一化后显示设备三基色的Y坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。 |
| float whitePointX | 归一化后白点值的X坐标，以0.00002为单位，范围[0.0, 1.0]。 |
| float whitePointY | 归一化后白点值的Y坐标，以0.00002为单位，范围[0.0, 1.0]。 |
| float maxLuminance | 图像主监视器最大亮度。以1为单位，最大值为65535。 |
| float minLuminance | 图像主监视器最小亮度。以0.0001为单位，最大值6.55535。 |
| float maxContentLightLevel | 显示内容的最大亮度。以1为单位，最大值为65535。 |
| float maxFrameAverageLightLevel | 显示内容的最大平均亮度，以1为单位，最大值为65535。 |
