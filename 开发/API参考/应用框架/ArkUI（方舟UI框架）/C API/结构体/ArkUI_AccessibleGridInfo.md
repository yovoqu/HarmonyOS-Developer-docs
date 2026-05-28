# ArkUI_AccessibleGridInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_AccessibleGridInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于配置特定组件（如[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)、[Select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)、[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件）的网格布局属性。
 
**起始版本：** 13
 
**相关模块：** [ArkUI_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)
 
**所在头文件：** [native_interface_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t rowCount | 组件的行数。取值范围为大于0的整数。 |
| int32_t columnCount | 组件的列数。取值范围为大于0的整数。 |
| int32_t selectionMode | 值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。 |
