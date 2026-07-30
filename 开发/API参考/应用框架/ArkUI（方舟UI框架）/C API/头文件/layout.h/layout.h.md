# layout.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-layout-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义布局相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/layout.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [LayoutSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/LayoutSample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_AlignmentRuleOption | ArkUI_AlignmentRuleOption | 指定设置在相对容器中子组件的对齐规则。 |
| ArkUI_GuidelineOption | ArkUI_GuidelineOption | Guideline配置选项结构体，用于定义Guideline（RelativeContainer容器内的辅助线）的id、方向和位置。 |
| ArkUI_BarrierOption | ArkUI_BarrierOption | barrier选项，用于定义barrier的id、方向和生成时所依赖的组件。 |
| ArkUI_PixelRoundPolicy | ArkUI_PixelRoundPolicy | 定义组件的像素取整策略结构体。 |
| ArkUI_PositionEdges | ArkUI_PositionEdges | 相对容器内容区边界的位置参数。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_Alignment | ArkUI_Alignment | 定义布局对齐枚举值。 |
| ArkUI_ItemAlignment | ArkUI_ItemAlignment | 设置子组件在父容器交叉轴的对齐格式枚举值。 |
| ArkUI_FlexAlignment | ArkUI_FlexAlignment | 定义垂直方向对齐方式。 |
| ArkUI_FlexDirection | ArkUI_FlexDirection | 定义Flex容器的主轴方向。 |
| ArkUI_FlexWrap | ArkUI_FlexWrap | 定义Flex行列布局模式。 |
| ArkUI_Direction | ArkUI_Direction | 设置容器元素内主轴方向上的布局枚举值。 |
| ArkUI_Axis | ArkUI_Axis | 定义方向或List组件排列方向枚举值。 |
| ArkUI_VerticalAlignment | ArkUI_VerticalAlignment | 定义垂直对齐方式。 |
| ArkUI_HorizontalAlignment | ArkUI_HorizontalAlignment | 定义语言方向对齐方式。 |
| ArkUI_BarrierDirection | ArkUI_BarrierDirection | 定义屏障线的方向。 |
| ArkUI_RelativeLayoutChainStyle | ArkUI_RelativeLayoutChainStyle | 定义链的风格。 |
| ArkUI_SafeAreaEdge | ArkUI_SafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| ArkUI_LayoutSafeAreaType | ArkUI_LayoutSafeAreaType | 定义扩展安全区域的枚举值。 |
| ArkUI_LayoutSafeAreaEdge | ArkUI_LayoutSafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| ArkUI_LocalizedAlignment | ArkUI_LocalizedAlignment | 定义Stack容器中子组件的对齐规则。 |
| ArkUI_LayoutPolicy | ArkUI_LayoutPolicy | 布局策略枚举。 |
| ArkUI_PixelRoundCalcPolicy | ArkUI_PixelRoundCalcPolicy | 定义像素取整计算策略枚举。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size) | 创建RelativeContainer容器内的辅助线信息。 |
| void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline) | 销毁辅助线信息。 |
| void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index) | 设置辅助线的Id。 |
| void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index) | 设置辅助线的方向。 |
| void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index) | 设置距离容器左侧或者顶部的距离。 |
| void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index) | 设置距离容器右侧或者底部的距离。 |
| const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index) | 获取辅助线的Id。 |
| ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index) | 获取辅助线的方向。 |
| float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index) | 获取辅助线距离容器左侧或者顶部的距离。 |
| float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index) | 获取辅助线距离容器右侧或者底部的距离。 |
| ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size) | 创建RelativeContainer容器内的屏障信息。 |
| void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle) | 销毁屏障信息。 |
| void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index) | 设置屏障的Id。 |
| void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index) | 设置屏障的方向。 |
| void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index) | 设置屏障的依赖的组件。 |
| const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index) | 获取屏障的Id。 |
| ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index) | 获取屏障的方向。 |
| const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex) | 获取屏障的依赖的组件。 |
| int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index) | 获取屏障的依赖的组件的个数。 |
| ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create() | 创建相对容器中子组件的对齐规则信息。 |
| void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option) | 销毁相对容器中子组件的对齐规则信息。 |
| void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | 设置相对布局的左对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | 设置相对布局的右对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment) | 设置相对布局的横向居中对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | 设置相对布局的顶部对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | 设置相对布局的底部对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment) | 设置相对布局的纵向居中对齐方式。 |
| void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal) | 设置组件在锚点约束下的水平方向上偏移参数。 |
| void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical) | 设置组件在锚点约束下的垂直方向上偏移参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option) | 获取左对齐参数的Id。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option) | 获取左对齐参数的对齐方式。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option) | 获取右对齐参数。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option) | 获取右对齐参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option) | 获取横向居中对齐方式的参数。 |
| ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option) | 获取横向居中对齐方式的参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option) | 获取顶部对齐的参数。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option) | 获取顶部对齐的参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option) | 获取底部对齐的参数。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option) | 获取底部对齐的参数。 |
| const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option) | 获取纵向居中对齐方式的参数。 |
| ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option) | 获取纵向居中对齐方式的参数。 |
| float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option) | 获取水平方向上的bias值。 |
| float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option) | 获取垂直方向上的bias值。 |
| ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create() | 创建PositionEdges属性对象。 |
| ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges) | 深拷贝PositionEdges属性对象。 |
| void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges) | 销毁PositionEdges属性对象。 |
| void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value) | 设置PositionEdges属性对象的上方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value) | 获取PositionEdges属性对象的上方向值。 |
| void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value) | 设置PositionEdges属性对象的左方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value) | 获取PositionEdges属性对象的左方向值。 |
| void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value) | 设置PositionEdges属性对象的下方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value) | 获取PositionEdges属性对象的下方向值。 |
| void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value) | 设置PositionEdges属性对象的右方向值。 |
| int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value) | 获取PositionEdges属性对象的右方向值。 |
| ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create() | 创建PixelRoundPolicy属性对象。 |
| void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy) | 释放PixelRoundPolicy属性对象。 |
| void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | 设置PixelRoundPolicy属性对象的上部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | 获取PixelRoundPolicy属性对象的上部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | 设置PixelRoundPolicy属性对象的前部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | 获取PixelRoundPolicy属性对象的前部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | 设置PixelRoundPolicy属性对象的下部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | 获取PixelRoundPolicy属性对象的下部方向值。 |
| void OH_ArkUI_PixelRoundPolicy_SetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value) | 设置PixelRoundPolicy属性对象的尾部方向值。 |
| int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value) | 获取PixelRoundPolicy属性对象的尾部方向值。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_Alignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_Alignment
```
 
**描述**
 
定义布局对齐枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ALIGNMENT_TOP_START = 0 | 顶部起始，该值为默认值。 |
| ARKUI_ALIGNMENT_TOP | 顶部居中。 |
| ARKUI_ALIGNMENT_TOP_END | 顶部尾端。 |
| ARKUI_ALIGNMENT_START | 起始端纵向居中。 |
| ARKUI_ALIGNMENT_CENTER | 横向和纵向居中。 |
| ARKUI_ALIGNMENT_END | 尾端纵向居中。 |
| ARKUI_ALIGNMENT_BOTTOM_START | 底部起始端。 |
| ARKUI_ALIGNMENT_BOTTOM | 底部横向居中。 |
| ARKUI_ALIGNMENT_BOTTOM_END | 底部尾端。 |
 
 
  

#### ArkUI_ItemAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ItemAlignment
```
 
**描述**
 
设置子组件在父容器交叉轴的对齐格式枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ITEM_ALIGNMENT_AUTO = 0 | 使用Flex容器中默认配置，该值为默认值。 |
| ARKUI_ITEM_ALIGNMENT_START | 元素在Flex容器中，交叉轴方向首部对齐。 |
| ARKUI_ITEM_ALIGNMENT_CENTER | 元素在Flex容器中，交叉轴方向居中对齐。 |
| ARKUI_ITEM_ALIGNMENT_END | 元素在Flex容器中，交叉轴方向底部对齐。 |
| ARKUI_ITEM_ALIGNMENT_STRETCH | 元素在Flex容器中，交叉轴方向拉伸填充。 |
| ARKUI_ITEM_ALIGNMENT_BASELINE | 元素在Flex容器中，交叉轴方向文本基线对齐。 |
 
 
  

#### ArkUI_FlexAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_FlexAlignment
```
 
**描述**
 
定义垂直方向对齐方式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_ALIGNMENT_START = 1 | 主轴方向首端对齐，该值为默认值。 |
| ARKUI_FLEX_ALIGNMENT_CENTER = 2 | 主轴方向中心对齐。 |
| ARKUI_FLEX_ALIGNMENT_END = 3 | 主轴方向尾部对齐。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_BETWEEN = 6 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素行首对齐，最后的元素行尾对齐。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_AROUND = 7 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素到行首的距离是相邻元素间距离的一半。 |
| ARKUI_FLEX_ALIGNMENT_SPACE_EVENLY = 8 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离、第一个元素到行首的距离和最后的元素到行尾的距离均相等。 |
 
 
  

#### ArkUI_FlexDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_FlexDirection
```
 
**描述**
 
定义Flex容器的主轴方向。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_DIRECTION_ROW = 0 | 主轴与行方向一致，该值为默认值。 |
| ARKUI_FLEX_DIRECTION_COLUMN | 主轴与列方向一致。 |
| ARKUI_FLEX_DIRECTION_ROW_REVERSE | 主轴与行方向相反。 |
| ARKUI_FLEX_DIRECTION_COLUMN_REVERSE | 主轴与列方向相反。 |
 
 
  

#### ArkUI_FlexWrap

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_FlexWrap
```
 
**描述**
 
定义Flex行列布局模式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FLEX_WRAP_NO_WRAP = 0 | 单行/单列布局，子项不能超出容器，该值为默认值。 |
| ARKUI_FLEX_WRAP_WRAP | 多行/多列布局，子项允许超出容器。 |
| ARKUI_FLEX_WRAP_WRAP_REVERSE | 反向多行/多列布局，子项允许超出容器。 |
 
 
  

#### ArkUI_Direction

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_Direction
```
 
**描述**
 
设置容器元素内主轴方向上的布局枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_DIRECTION_LTR = 0 | 元素从左到右布局，该值为默认值。 |
| ARKUI_DIRECTION_RTL | 元素从右到左布局。 |
| ARKUI_DIRECTION_AUTO = 3 | 使用系统布局方向。 |
 
 
  

#### ArkUI_Axis

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_Axis
```
 
**描述**
 
定义方向或[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件排列方向枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_AXIS_VERTICAL = 0 | 竖直方向，或者仅支持竖直方向滚动，该值为默认值。 |
| ARKUI_AXIS_HORIZONTAL | 水平方向，或者仅支持水平方向滚动。 |
 
 
  

#### ArkUI_VerticalAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_VerticalAlignment
```
 
**描述**
 
定义垂直对齐方式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_VERTICAL_ALIGNMENT_TOP = 0 | 顶部对齐。 |
| ARKUI_VERTICAL_ALIGNMENT_CENTER | 居中对齐，默认对齐方式。 |
| ARKUI_VERTICAL_ALIGNMENT_BOTTOM | 底部对齐。 |
 
 
  

#### ArkUI_HorizontalAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_HorizontalAlignment
```
 
**描述**
 
定义语言方向对齐方式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HORIZONTAL_ALIGNMENT_START = 0 | 按照语言方向起始端对齐。 |
| ARKUI_HORIZONTAL_ALIGNMENT_CENTER | 居中对齐，默认对齐方式。 |
| ARKUI_HORIZONTAL_ALIGNMENT_END | 按照语言方向末端对齐。 |
 
 
  

#### ArkUI_BarrierDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_BarrierDirection
```
 
**描述**
 
定义屏障线的方向。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BARRIER_DIRECTION_START = 0 | 屏障在其所有referencedId的最左侧。 |
| ARKUI_BARRIER_DIRECTION_END | 屏障在其所有referencedId的最右侧。 |
| ARKUI_BARRIER_DIRECTION_TOP | 屏障在其所有referencedId的最上方。 |
| ARKUI_BARRIER_DIRECTION_BOTTOM | 屏障在其所有referencedId的最下方。 |
 
 
  

#### ArkUI_RelativeLayoutChainStyle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_RelativeLayoutChainStyle
```
 
**描述**
 
定义链的风格。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_SPREAD = 0 | 组件在约束锚点间均匀分布，该值为默认值。 |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_SPREAD_INSIDE | 除首尾2个子组件的其他组件在约束锚点间均匀分布。 |
| ARKUI_RELATIVE_LAYOUT_CHAIN_STYLE_PACKED | 链内子组件无间隙。 |
 
 
  

#### ArkUI_SafeAreaEdge

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SafeAreaEdge
```
 
**描述**
 
定义扩展安全区域的方向的枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SAFE_AREA_EDGE_TOP = 1 | 上方区域，该值为默认值。 |
| ARKUI_SAFE_AREA_EDGE_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI_SAFE_AREA_EDGE_START = 1 << 2 | 前部区域。 |
| ARKUI_SAFE_AREA_EDGE_END = 1 << 3 | 尾部区域。 |
 
 
  

#### ArkUI_LayoutSafeAreaType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_LayoutSafeAreaType
```
 
**描述**
 
定义扩展安全区域的枚举值。
 
**起始版本：** 23
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUT_SAFE_AREA_TYPE_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏。 |
 
 
  

#### ArkUI_LayoutSafeAreaEdge

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_LayoutSafeAreaEdge
```
 
**描述**
 
定义扩展安全区域的方向的枚举值。
 
**起始版本：** 23
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_TOP = 1 | 上方区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_START = 1 << 2 | 前部区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_END = 1 << 3 | 尾部区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_VERTICAL = ARKUI_LAYOUT_SAFE_AREA_EDGE_TOP \| ARKUI_LAYOUT_SAFE_AREA_EDGE_BOTTOM | 垂直区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_HORIZONTAL = ARKUI_LAYOUT_SAFE_AREA_EDGE_START \| ARKUI_LAYOUT_SAFE_AREA_EDGE_END | 水平区域。 |
| ARKUI_LAYOUT_SAFE_AREA_EDGE_ALL = ARKUI_LAYOUT_SAFE_AREA_EDGE_VERTICAL \| ARKUI_LAYOUT_SAFE_AREA_EDGE_HORIZONTAL | 全部区域。 |
 
 
  

#### ArkUI_LocalizedAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_LocalizedAlignment
```
 
**描述**
 
定义Stack容器中子组件的对齐规则。
 
**起始版本：** 23
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LOCALIZED_ALIGNMENT_TOP_START = 0 | 顶部起始。 |
| ARKUI_LOCALIZED_ALIGNMENT_TOP | 顶部居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_TOP_END | 顶部尾端。 |
| ARKUI_LOCALIZED_ALIGNMENT_START | 起始端纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_CENTER | 横向和纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_END | 尾端纵向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM_START | 底部起始端。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM | 底部横向居中。 |
| ARKUI_LOCALIZED_ALIGNMENT_BOTTOM_END | 底部尾端。 |
 
 
  

#### ArkUI_LayoutPolicy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_LayoutPolicy
```
 
**描述**
 
布局策略枚举。
 
**起始版本：** 21
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LAYOUTPOLICY_MATCHPARENT = 0 | 组件自适应父组件布局。 |
| ARKUI_LAYOUTPOLICY_WRAPCONTENT | 组件自适应子组件（内容），且其大小受父组件内容区大小约束。 |
| ARKUI_LAYOUTPOLICY_FIXATIDEALSIZE | 组件自适应子组件（内容），且其大小不受父组件内容区大小约束。 |
 
 
  

#### ArkUI_PixelRoundCalcPolicy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_PixelRoundCalcPolicy
```
 
**描述**
 
定义像素取整计算策略枚举。
 
**起始版本：** 21
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PIXELROUNDCALCPOLICY_NOFORCEROUND = 0 | 非取整计算。 |
| ARKUI_PIXELROUNDCALCPOLICY_FORCECEIL | 向上取整计算。 |
| ARKUI_PIXELROUNDCALCPOLICY_FORCEFLOOR | 向下取整计算。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_GuidelineOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size)
```
 
**描述**
 
创建RelativeContainer容器内的辅助线信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t size | 辅助线数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_GuidelineOption* | 辅助线信息。 |
 
 
  

#### OH_ArkUI_GuidelineOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline)
```
 
**描述**
 
销毁辅助线信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
 
 
  

#### OH_ArkUI_GuidelineOption_SetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index)
```
 
**描述**
 
设置辅助线的Id。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| const char* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32_t index | 辅助线索引值。 |
 
 
  

#### OH_ArkUI_GuidelineOption_SetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index)
```
 
**描述**
 
设置辅助线的方向。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| ArkUI_Axis value | 方向。 |
| int32_t index | 辅助线索引值。 |
 
 
  

#### OH_ArkUI_GuidelineOption_SetPositionStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```
 
**描述**
 
设置距离容器左侧或者顶部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| float value | 距离容器左侧或者顶部的距离。 |
| int32_t index | 辅助线索引值。 |
 
 
  

#### OH_ArkUI_GuidelineOption_SetPositionEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```
 
**描述**
 
设置距离容器右侧或者底部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| float value | 距离容器右侧或者底部的距离。 |
| int32_t index | 辅助线索引值。 |
 
 
  

#### OH_ArkUI_GuidelineOption_GetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index)
```
 
**描述**
 
获取辅助线的Id。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | Id。 |
 
 
  

#### OH_ArkUI_GuidelineOption_GetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index)
```
 
**描述**
 
获取辅助线的方向。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_Axis | 方向。 |
 
 
  

#### OH_ArkUI_GuidelineOption_GetPositionStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index)
```
 
**描述**
 
获取辅助线距离容器左侧或者顶部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器左侧或者顶部的距离。单位为vp。 |
 
 
  

#### OH_ArkUI_GuidelineOption_GetPositionEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index)
```
 
**描述**
 
获取辅助线距离容器右侧或者底部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_GuidelineOption* guideline | 辅助线信息。 |
| int32_t index | 辅助线索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器右侧或者底部的距离。单位为vp。 |
 
 
  

#### OH_ArkUI_BarrierOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size)
```
 
**描述**
 
创建RelativeContainer容器内的屏障信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t size | 屏障数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_BarrierOption* | 屏障信息。 |
 
 
  

#### OH_ArkUI_BarrierOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle)
```
 
**描述**
 
销毁屏障信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
 
 
  

#### OH_ArkUI_BarrierOption_SetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```
 
**描述**
 
设置屏障的Id。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| const char* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32_t index | 屏障索引值。 |
 
 
  

#### OH_ArkUI_BarrierOption_SetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index)
```
 
**描述**
 
设置屏障的方向。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| ArkUI_BarrierDirection value | 方向。 |
| int32_t index | 屏障索引值。 |
 
 
  

#### OH_ArkUI_BarrierOption_SetReferencedId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```
 
**描述**
 
设置屏障的依赖的组件。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| const char* value | 依赖的组件的Id。 |
| int32_t index | 屏障索引值。 |
 
 
  

#### OH_ArkUI_BarrierOption_GetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index)
```
 
**描述**
 
获取屏障的Id。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 屏障的Id。 |
 
 
  

#### OH_ArkUI_BarrierOption_GetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index)
```
 
**描述**
 
获取屏障的方向。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_BarrierDirection | 屏障的方向。 |
 
 
  

#### OH_ArkUI_BarrierOption_GetReferencedId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex)
```
 
**描述**
 
获取屏障的依赖的组件。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| index | 屏障索引值。 |
| int32_t referencedIndex | 依赖的组件Id索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 屏障的依赖的组件。 |
 
 
  

#### OH_ArkUI_BarrierOption_GetReferencedIdSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index)
```
 
**描述**
 
获取屏障的依赖的组件的个数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_BarrierOption* barrierStyle | 屏障信息。 |
| int32_t index | 屏障索引值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 屏障的依赖的组件的个数。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create()
```
 
**描述**
 
创建相对容器中子组件的对齐规则信息。
 
**起始版本：** 12
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_AlignmentRuleOption* | 对齐规则信息。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
销毁相对容器中子组件的对齐规则信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```
 
**描述**
 
设置相对布局的左对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 左对齐锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```
 
**描述**
 
设置相对布局的右对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 右对齐锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```
 
**描述**
 
设置相对布局的横向居中对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 横向居中锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```
 
**描述**
 
设置相对布局的顶部对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 顶部对齐锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```
 
**描述**
 
设置相对布局的底部对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 底部对齐锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetCenterVertical()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```
 
**描述**
 
设置相对布局的纵向居中对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| const char* id | 纵向居中锚点的组件的id值。 |
| value | 相对于锚点组件的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal)
```
 
**描述**
 
设置组件在锚点约束下的水平方向上偏移参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| float horizontal | 水平方向上的bias值。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_SetBiasVertical()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical)
```
 
**描述**
 
设置组件在锚点约束下的垂直方向上偏移参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
| horizontal | 垂直方向上的bias值。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetStartId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取左对齐参数的Id。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 锚点的组件的id值。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetStartAlignment()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取左对齐参数的对齐方式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetEndId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取右对齐参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 右对齐参数id。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetEndAlignment()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取右对齐参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 右对齐参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取横向居中对齐方式的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 横向居中对齐方式的参数的id。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取横向居中对齐方式的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_HorizontalAlignment | 横向居中对齐方式的参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetTopId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取顶部对齐的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 顶部对齐的参数id。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetTopAlignment()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取顶部对齐的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 顶部对齐的参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetBottomId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取底部对齐的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 底部对齐的参数的id。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetBottomAlignment()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取底部对齐的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 底部对齐的参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取纵向居中对齐方式的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char* | 纵向居中对齐方式的参数的id。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取纵向居中对齐方式的参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_VerticalAlignment | 纵向居中对齐方式的参数的对齐方式。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取水平方向上的bias值。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 水平方向上的bias值。 |
 
 
  

#### OH_ArkUI_AlignmentRuleOption_GetBiasVertical()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option)
```
 
**描述**
 
获取垂直方向上的bias值。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_AlignmentRuleOption* option | 相对容器中子组件的对齐规则信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 垂直方向上的bias值。 |
 
 
  

#### OH_ArkUI_PositionEdges_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create()
```
 
**描述**
 
创建PositionEdges属性对象。
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_PositionEdges* | 指向PositionEdges对象的指针。 |
 
 
  

#### OH_ArkUI_PositionEdges_Copy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges)
```
 
**描述**
 
深拷贝PositionEdges属性对象。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_PositionEdges* | 指向新PositionEdges对象的指针。 |
 
 
  

#### OH_ArkUI_PositionEdges_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges)
```
 
**描述**
 
销毁PositionEdges属性对象。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
 
 
  

#### OH_ArkUI_PositionEdges_SetTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value)
```
 
**描述**
 
设置PositionEdges属性对象的上方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |
 
 
  

#### OH_ArkUI_PositionEdges_GetTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value)
```
 
**描述**
 
获取PositionEdges属性对象的上方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PositionEdges_SetLeft()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value)
```
 
**描述**
 
设置PositionEdges属性对象的左方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |
 
 
  

#### OH_ArkUI_PositionEdges_GetLeft()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value)
```
 
**描述**
 
获取PositionEdges属性对象的左方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PositionEdges_SetBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value)
```
 
**描述**
 
设置PositionEdges属性对象的下方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |
 
 
  

#### OH_ArkUI_PositionEdges_GetBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value)
```
 
**描述**
 
获取PositionEdges属性对象的下方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PositionEdges_SetRight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value)
```
 
**描述**
 
设置PositionEdges属性对象的右方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |
 
 
  

#### OH_ArkUI_PositionEdges_GetRight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value)
```
 
**描述**
 
获取PositionEdges属性对象的右方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PositionEdges* edges | 指向PositionEdges对象的指针。 |
| float* value | PositionEdges对应方向的值，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create()
```
 
**描述**
 
创建PixelRoundPolicy属性对象。
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_PixelRoundPolicy* | 指向PixelRoundPolicy对象的指针。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy)
```
 
**描述**
 
释放PixelRoundPolicy属性对象。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向要释放的PixelRoundPolicy对象的指针。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_SetTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```
 
**描述**
 
设置PixelRoundPolicy属性对象的上部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_GetTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```
 
**描述**
 
获取PixelRoundPolicy属性对象的上部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_SetStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```
 
**描述**
 
设置PixelRoundPolicy属性对象的前部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_GetStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```
 
**描述**
 
获取PixelRoundPolicy属性对象的前部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_SetBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```
 
**描述**
 
设置PixelRoundPolicy属性对象的下部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_GetBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```
 
**描述**
 
获取PixelRoundPolicy属性对象的下部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_SetEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_PixelRoundPolicy_SetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```
 
**描述**
 
设置PixelRoundPolicy属性对象的尾部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy value | PixelRoundPolicy对应方向的取整策略。 |
 
 
  

#### OH_ArkUI_PixelRoundPolicy_GetEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```
 
**描述**
 
获取PixelRoundPolicy属性对象的尾部方向值。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_PixelRoundPolicy* policy | 指向PixelRoundPolicy对象的指针。 |
| ArkUI_PixelRoundCalcPolicy* value | PixelRoundPolicy对应方向的取整策略。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数无效。 |
