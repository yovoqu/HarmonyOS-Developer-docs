# VkNativeBufferUsageOHOS

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos

```text
typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```
  

##### 概述

提供HarmonyOS NativeBuffer用途的说明。
 
**起始版本：** 10
 
**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)
 
**所在头文件：** [vulkan_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK_STRUCTURE_TYPE_NATIVE_BUFFER_USAGE_OHOS。 |
| void* pNext | 下一级结构体指针。 |
| uint64_t OHOSNativeBufferUsage | NativeBuffer的用途说明。 |
