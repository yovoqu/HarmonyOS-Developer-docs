# OH_Drawing_FontGenericInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Drawing_FontGenericInfo {...} OH_Drawing_FontGenericInfo
```
  

##### 概述

系统所支持的通用字体集信息结构体。
 
**起始版本：** 12
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
**所在头文件：** [drawing_text_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char* familyName | 字体家族名。 |
| size_t aliasInfoSize | 别名字体列表的数量。 |
| size_t adjustInfoSize | 字重映射列表的数量。 |
| OH_Drawing_FontAliasInfo* aliasInfoSet | 别名字体列表。 |
| OH_Drawing_FontAdjustInfo* adjustInfoSet | 字重映射列表。 |
