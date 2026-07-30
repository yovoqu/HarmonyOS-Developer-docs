# list.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-list-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义List组件相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/list.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [ScrollableNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ScrollableNDK)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_ListChildrenMainSize | ArkUI_ListChildrenMainSize | 定义List组件子组件的主轴尺寸信息。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_ListItemAlignment | ArkUI_ListItemAlignment | 交叉轴方向的布局方式。 |
| ArkUI_StickyStyle | ArkUI_StickyStyle | 定义列表是否吸顶和吸底枚举值。 |
| ArkUI_ListItemGroupArea | ArkUI_ListItemGroupArea | 定义ListItemGroup组件区域。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create() | 创建ListChildrenMainSize接口设置的配置项。使用结束后需调用OH_ArkUI_ListChildrenMainSizeOption_Dispose释放资源。 |
| void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option) | 销毁由OH_ArkUI_ListChildrenMainSizeOption_Create创建的ListChildrenMainSize实例。销毁后不得继续访问该实例。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize) | 设置List组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option) | 获取List组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize) | 调整List组件子项主轴尺寸数组的长度。扩大数组时，新增元素的初始值为-1。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount) | 从指定索引位置开始删除deleteCount个List组件子项主轴尺寸数组元素，并在该位置插入addCount个初始值为-1的元素。deleteCount超出剩余元素个数时，删除至数组末尾。 |
| int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize) | 更新List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index) | 获取List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_ListItemAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ListItemAlignment
```
 
**描述：**
 
交叉轴方向的布局方式，默认值为ARKUI_LIST_ITEM_ALIGNMENT_START。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_ALIGNMENT_START = 0 | ListItem在List中，交叉轴方向首部对齐。 |
| ARKUI_LIST_ITEM_ALIGNMENT_CENTER = 1 | ListItem在List中，交叉轴方向居中对齐。 |
| ARKUI_LIST_ITEM_ALIGNMENT_END = 2 | ListItem在List中，交叉轴方向尾部对齐。 |
 
 
  

#### ArkUI_StickyStyle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_StickyStyle
```
 
**描述：**
 
定义列表是否吸顶和吸底枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_STICKY_STYLE_NONE = 0 | ListItemGroup的header不吸顶，footer不吸底。 |
| ARKUI_STICKY_STYLE_HEADER = 1 | ListItemGroup的header吸顶，footer不吸底。 |
| ARKUI_STICKY_STYLE_FOOTER = 2 | ListItemGroup的header不吸顶，footer吸底。 |
| ARKUI_STICKY_STYLE_BOTH = 3 | ListItemGroup的header吸顶，footer吸底。 |
 
 
  

#### ArkUI_ListItemGroupArea

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ListItemGroupArea
```
 
**描述：**
 
定义[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)组件区域，默认值为ARKUI_LIST_ITEM_GROUP_AREA_OUTSIDE。
 
**起始版本：** 15
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_GROUP_AREA_OUTSIDE = 0 | ListItemGroup区域外。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_NONE = 1 | ListItemGroup没有header、footer和ListItem时的区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_ITEM = 2 | ListItemGroup的ListItem区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_HEADER = 3 | ListItemGroup的header区域。 |
| ARKUI_LIST_ITEM_SWIPE_AREA_FOOTER = 4 | ListItemGroup的footer区域。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_ListChildrenMainSizeOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create()
```
 
**描述：**
 
创建ListChildrenMainSize接口设置的配置项。使用结束后需调用[OH_ArkUI_ListChildrenMainSizeOption_Dispose](#oh_arkui_listchildrenmainsizeoption_dispose)释放资源。
 
**起始版本：** 12
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_ListChildrenMainSize* | ListChildrenMainSize配置项实例。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option)
```
 
**描述：**
 
销毁由[OH_ArkUI_ListChildrenMainSizeOption_Create](#oh_arkui_listchildrenmainsizeoption_create)创建的ListChildrenMainSize实例。销毁后不得继续访问该实例。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | 要销毁的ListChildrenMainSize实例。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize)
```
 
**描述：**
 
设置[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。为空指针时返回ARKUI_ERROR_CODE_PARAM_INVALID。 |
| float defaultMainSize | 列表项在主轴方向的默认尺寸值，单位为vp，取值范围为大于等于0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option)
```
 
**描述：**
 
获取[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 列表项在主轴方向的默认尺寸值，默认为0，单位为vp，option为空指针时返回-1。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_Resize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize)
```
 
**描述：**
 
调整[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件子项主轴尺寸数组的长度。扩大数组时，新增元素的初始值为-1。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。为空指针时不执行操作。 |
| int32_t totalSize | 目标数组长度，取值范围为大于0。传入小于等于0的值时不执行操作。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_Splice()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount)
```
 
**描述：**
 
从指定索引位置开始删除deleteCount个[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件子项主轴尺寸数组元素，并在该位置插入addCount个初始值为-1的元素。deleteCount超出剩余元素个数时，删除至数组末尾。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。为空指针时返回ARKUI_ERROR_CODE_PARAM_INVALID。 |
| int32_t index | 操作起始索引位置，取值范围为0至数组当前长度减1。 |
| int32_t deleteCount | 从起始位置开始删除的元素数量，取值范围为大于等于0。数量超出剩余元素个数时删除至数组末尾。 |
| int32_t addCount | 从起始位置开始新增的元素数量，取值范围为大于等于0。新增元素的初始值为-1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_UpdateSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize)
```
 
**描述：**
 
更新[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。为空指针时返回ARKUI_ERROR_CODE_PARAM_INVALID。 |
| int32_t index | 目标元素的数组索引位置，取值范围为0至数组当前长度减1。 |
| float mainSize | 要设置的主轴尺寸值，单位为vp，取值范围为大于等于0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |
 
 
  

#### OH_ArkUI_ListChildrenMainSizeOption_GetMainSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index)
```
 
**描述：**
 
获取[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListChildrenMainSize* option | ListChildrenMainSize实例。 |
| int32_t index | 目标元素的数组索引位置，取值范围为0至数组当前长度减1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 数组指定位置的主轴尺寸值，单位为vp。option为空指针或index超出数组范围时返回-1。 |
