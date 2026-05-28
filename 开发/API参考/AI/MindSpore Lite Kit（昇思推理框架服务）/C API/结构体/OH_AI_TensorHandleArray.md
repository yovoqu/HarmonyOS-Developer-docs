# OH_AI_TensorHandleArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandlearray
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AI_TensorHandleArray {...} OH_AI_TensorHandleArray
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

张量数组结构体，用于存储张量数组指针和张量数组长度。
 
**起始版本：** 9
 
**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)
 
**所在头文件：** [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| size_t handle_num | 张量数组长度。 |
| OH_AI_TensorHandle* handle_list | 指向张量数组的指针。 |
