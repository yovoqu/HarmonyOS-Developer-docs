# OH_AI_ShapeInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-shapeinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AI_ShapeInfo {...} OH_AI_ShapeInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。
 
**起始版本：** 9
 
**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)
 
**所在头文件：** [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| size_t shape_num | 维度数组长度。 |
| int64_t shape[OH_AI_MAX_SHAPE_NUM] | 维度数组。 |
