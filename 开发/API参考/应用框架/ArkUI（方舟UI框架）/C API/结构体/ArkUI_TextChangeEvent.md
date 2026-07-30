# ArkUI_TextChangeEvent

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textchangeevent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_TextChangeEvent
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义文本变化事件的数据结构，用于在文本输入场景中监听和处理文本变更事件。该结构体包含文本内容、扩展信息和数值参数，支持开发者实时获取文本变更数据，适用于输入框内容监听、实时搜索、字数统计等场景。
 
**起始版本：** 15
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_node.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char* pStr | 文本变更事件中的文本内容字符串。 |
| const char* pExtendStr | 文本变更事件中的扩展字符串，用于存储额外的文本信息。 |
| int32_t number | 事件的数字参数值，用于记录文本变更事件中的数值信息。取值范围[-2147483648, 2147483647]。 |
