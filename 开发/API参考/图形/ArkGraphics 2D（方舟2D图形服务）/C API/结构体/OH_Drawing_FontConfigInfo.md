# OH_Drawing_FontConfigInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_Drawing_FontConfigInfo {...} OH_Drawing_FontConfigInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

系统字体配置信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing_text_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| size_t fontDirSize | 系统字体文件路径数量。 |
| size_t fontGenericInfoSize | 通用字体集列表数量。 |
| size_t fallbackGroupSize | 备用字体集列表数量。 |
| char** fontDirSet | 系统字体文件路径列表。 |
| [OH_Drawing_FontGenericInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo)* fontGenericInfoSet | 通用字体集列表。 |
| [OH_Drawing_FontFallbackGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup)* fallbackGroupSet | 备用字体集列表。 |
