# XEG_RTReflectionCreateInfo

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtreflectioncreateinfo
**支持设备：** Phone / PC/2in1 / Tablet / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / TV

此结构体描述创建[XEG_RTReflection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_RTReflection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg_vulkan_rt_reflection.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-reflection-8h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / TV


| 名称 | 描述 |
| --- | --- |
| XEG_StructureType [sType](#stype) | 识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO。 |
| const void * [pNext](#pnext) | 指向扩展结构的指针。 |
| VkExtent2D [renderSize](#rendersize) | 输入图像的尺寸。 |
| bool [enableFastTrace](#enablefasttrace) | 是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式，默认为false |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet / TV


### enableFastTrace
**支持设备：** Phone / PC/2in1 / Tablet / TV


```cpp
bool XEG_RTReflectionCreateInfo::enableFastTrace
```

**描述**

是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式。


### pNext
**支持设备：** Phone / PC/2in1 / Tablet / TV


```cpp
const void* XEG_RTReflectionCreateInfo::pNext
```

**描述**

指向扩展结构的指针。


### renderSize
**支持设备：** Phone / PC/2in1 / Tablet / TV


```cpp
VkExtent2D XEG_RTReflectionCreateInfo::renderSize
```

**描述**

输入图像的尺寸。


### sType
**支持设备：** Phone / PC/2in1 / Tablet / TV


```cpp
XEG_StructureType XEG_RTReflectionCreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO。
