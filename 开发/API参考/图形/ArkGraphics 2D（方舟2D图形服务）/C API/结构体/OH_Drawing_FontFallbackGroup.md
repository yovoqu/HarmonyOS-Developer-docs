# OH_Drawing_FontFallbackGroup

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Drawing_FontFallbackGroup {...} OH_Drawing_FontFallbackGroup
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

备用字体集信息结构体。
 
**起始版本：** 12
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
**所在头文件：** [drawing_text_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char* groupName | 备用字体集所对应的字体集名称，如果值为空，表示可以使用备用字体集列表集所有的字体。 |
| size_t fallbackInfoSize | 备用字体集数量。 |
| OH_Drawing_FontFallbackInfo* fallbackInfoSet | 备用字体字体集列表。 |
