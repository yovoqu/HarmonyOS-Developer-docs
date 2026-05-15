# ArkUI_ScaleOptions

更新时间：2026-03-23 08:10:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-scaleoptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} ArkUI_ScaleOptions
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义组件转场时的缩放效果对象。

**起始版本：** 12

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| float x | x轴的缩放倍数。x&gt;1时以x轴方向放大，0&lt;x&lt;1时以x轴方向缩小，x=0时表示在x轴方向缩小成0，x=1时表示在x轴方向缩放倍数是1，x&lt;0时沿x轴反向并缩放。 |
| float y | y轴的缩放倍数。y&gt;1时以y轴方向放大，0&lt;y&lt;1时以y轴方向缩小，y=0时表示在y轴方向缩小成0，y=1时表示在y轴方向缩放倍数是1，y&lt;0时沿y轴反向并缩放。 |
| float z | 当前为二维显示，该参数无效。 |
| float centerX | 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标，单位为vp。 |
| float centerY | 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标，单位为vp。 |
