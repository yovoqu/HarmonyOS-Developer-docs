# ImageEffect_FilterDelegate

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-filterdelegate
**支持设备：** Phone / PC/2in1 / Tablet / TV


```text
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / TV

自定义滤镜回调函数结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect)

**所在头文件：** [image_effect_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / TV


| 名称 | 描述 |
| --- | --- |
| [OH_EffectFilterDelegate_SetValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_setvalue) setValue | 参数设置函数指针。 |
| [OH_EffectFilterDelegate_Render](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_render) render | 滤镜渲染函数指针。 |
| [OH_EffectFilterDelegate_Save](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_save) save | 序列化效果器函数指针。 |
| [OH_EffectFilterDelegate_Restore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h#oh_effectfilterdelegate_restore) restore | 反序列化效果器函数指针。 |
