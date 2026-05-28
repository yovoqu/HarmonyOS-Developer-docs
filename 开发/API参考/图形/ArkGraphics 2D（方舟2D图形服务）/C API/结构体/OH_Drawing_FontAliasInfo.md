# OH_Drawing_FontAliasInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontaliasinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Drawing_FontAliasInfo {...} OH_Drawing_FontAliasInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

别名字体信息结构体。
 
**起始版本：** 12
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
**所在头文件：** [drawing_text_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char* familyName | 字体家族名。 |
| int weight | 字体字重值，当字重值大于0时，表示此字体集只包含所指定weight的字体，当字重值等于0时，表示此字体集包含所有字体。 |
