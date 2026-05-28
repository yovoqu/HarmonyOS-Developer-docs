# ArkUI_NodeAttributeType（信息展示类组件相关属性）

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/native-node-h-nodeattributetype-informationdisplay

```text
enum ArkUI_NodeAttributeType
```
  

#### 概述

定义ArkUI在Native侧可以设置信息展示类组件相关属性样式集合，包含LoadingProgress、Progress等组件属性设置。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_node.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h)
 
  

#### NODE_LOADING_PROGRESS_COLOR

```text
NODE_LOADING_PROGRESS_COLOR = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LOADING_PROGRESS = 6000
```
 
加载进度条前景色属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 前景颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 前景颜色数值，0xargb格式。 |
 
 
  

#### NODE_LOADING_PROGRESS_ENABLE_LOADING

```text
NODE_LOADING_PROGRESS_ENABLE_LOADING = 6001
```
 
LoadingProgress动画显示属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false时不显示动画，true时可以显示动画。默认值为true。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0时不显示动画，1时可以显示动画。 |
 
 
  

#### NODE_PROGRESS_VALUE

```text
NODE_PROGRESS_VALUE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_PROGRESS = 10000
```
 
进度条的当前进度值属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 进度条当前值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 进度条当前值。 |
 
 
  

#### NODE_PROGRESS_TOTAL

```text
NODE_PROGRESS_TOTAL = 10001
```
 
进度条的总长属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 进度条总长。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 进度条总长。 |
 
 
  

#### NODE_PROGRESS_COLOR

```text
NODE_PROGRESS_COLOR = 10002
```
 
进度条显示进度值的颜色属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |
 
 
  

#### NODE_PROGRESS_TYPE

```text
NODE_PROGRESS_TYPE = 10003
```
 
进度条的类型属性，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 进度条类型枚举值ArkUI_ProgressType，默认值为ARKUI_PROGRESS_TYPE_LINEAR。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 进度条类型枚举值ArkUI_ProgressType。 |
 
 
  

#### NODE_PROGRESS_LINEAR_STYLE

```text
NODE_PROGRESS_LINEAR_STYLE = 10004
```
 
线性进度条样式设置，支持属性设置，属性重置和属性获取接口，如果进度条类型不是线性样式则不生效。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_ProgressLinearStyleOption对象设置组件样式。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 使用ArkUI_ProgressLinearStyleOption对象获取组件样式。 |
