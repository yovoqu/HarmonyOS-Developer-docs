# ArkUI_PickerIndicatorDivider

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-pickerindicatordivider
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} ArkUI_PickerIndicatorDivider
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

分割线样式指示器的样式参数。

**起始版本：** 23

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

**相关示例：** [native_type_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| float strokeWidth | 分割线的线宽。 默认值：0 单位：vp 取值范围：[0, 选中项高度的一半（即20vp）]。strokeWidth小于0时设置分割线样式指示器的样式参数失败，strokeWidth大于选中项高度的一半时使用2.0px。不支持“百分比”类型。 |
| uint32_t dividerColor | 分割线的颜色。 默认值：0 取值范围：0xARGB格式，例如0xFF1122FF。 |
| float startMargin | 分割线与Picker容器侧边起始端的距离。 默认值：0 单位：vp 取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。设置小于0时设置分割线样式指示器的样式参数失败，startMargin与endMargin之和超过Picker容器的宽度时，使用默认值。不支持“百分比”类型。 |
| float endMargin | 分割线与Picker容器侧边结束端的距离。 默认值：0 单位：vp 取值范围：startMargin与endMargin之和不得超过Picker容器的宽度。设置小于0时设置分割线样式指示器的样式参数失败，startMargin与endMargin之和超过Picker容器的宽度时，使用默认值。不支持“百分比”类型。 |
