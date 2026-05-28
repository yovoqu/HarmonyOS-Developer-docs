# ArkUI_NodeAttributeType（滚动容器类组件相关属性）

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ative-node-h-nodeattributetype-scrollablecontainer

```text
enum ArkUI_NodeAttributeType
```
  

##### 概述

定义ArkUI在Native侧可以设置的滚动容器类组件相关属性样式集合，包含Scroll、List、ListItem、ListItemGroup、Refresh、WaterFlow、Grid、GridItem等组件属性设置。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_node.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h)
 
  

##### NODE_SCROLL_BAR_DISPLAY_MODE

```text
NODE_SCROLL_BAR_DISPLAY_MODE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_SCROLL = 1002000
```
 
设置滚动条状态，支持属性设置，属性重置和属性获取接口。[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)/[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)/[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)从API version 12开始支持，[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型ArkUI_ScrollBarDisplayMode，List、Grid、Scroll组件默认值为ARKUI_SCROLL_BAR_DISPLAY_MODE_AUTO，WaterFlow组件默认值为ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动条状态，数据类型ArkUI_ScrollBarDisplayMode。 |
 
 
  

##### NODE_SCROLL_BAR_WIDTH

```text
NODE_SCROLL_BAR_WIDTH = 1002001
```
 
设置滚动条的宽度，支持属性设置，属性重置和属性获取接口。[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)/[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)/[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)从API version 12开始支持，[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp，默认值4。 取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条宽度，单位vp。 |
 
 
  

##### NODE_SCROLL_BAR_COLOR

```text
NODE_SCROLL_BAR_COLOR = 1002002
```
 
设置滚动条的颜色，支持属性设置，属性重置和属性获取接口。[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)/[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)/[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)从API version 12开始支持，[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。默认值：0x66182431。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .data[0].u32 | 滚动条颜色，0xargb类型。 |
 
 
  

##### NODE_SCROLL_SCROLL_DIRECTION

```text
NODE_SCROLL_SCROLL_DIRECTION = 1002003
```
 
设置滚动方向，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 滚动方向，数据类型ArkUI_ScrollDirection，默认值ARKUI_SCROLL_DIRECTION_VERTICAL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 滚动方向，数据类型ArkUI_ScrollDirection。 |
 
 
  

##### NODE_SCROLL_EDGE_EFFECT

```text
NODE_SCROLL_EDGE_EFFECT = 1002004
```
 
设置边缘滑动效果，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型ArkUI_EdgeEffect，Grid、Scroll、WaterFlow组件默认值为ARKUI_EDGE_EFFECT_NONE，List组件默认值为ARKUI_EDGE_EFFECT_SPRING。 |
| .value[1]?.i32 | 可选值，组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0，List、Grid、WaterFlow组件默认值为0，Scroll组件默认值为1。 |
| .value[2]?.i32 | 边缘效果生效的方向，参数类型ArkUI_EffectEdge，默认值ARKUI_EFFECT_EDGE_START \| ARKUI_EFFECT_EDGE_END。 该参数从API version 18开始支持。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 边缘滑动效果，参数类型ArkUI_EdgeEffect。 |
| .value[1].i32 | 组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0。 |
| .value[2].i32 | 边缘效果生效的方向，参数类型ArkUI_EffectEdge。该参数从API version 18开始支持。 |
 
 
  

##### NODE_SCROLL_ENABLE_SCROLL_INTERACTION

```text
NODE_SCROLL_ENABLE_SCROLL_INTERACTION = 1002005
```
 
设置是否支持滚动手势，当设置为0时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。
 
List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势，默认值1。1：支持滚动手势，0：不支持滚动手势。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滚动手势。 |
 
 
  

##### NODE_SCROLL_FRICTION

```text
NODE_SCROLL_FRICTION = 1002006
```
 
设置摩擦系数，手动滑动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。
 
List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 摩擦系数，默认值：非可穿戴设备为0.6，可穿戴设备为0.9。取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 摩擦系数。 |
 
 
  

##### NODE_SCROLL_SNAP

```text
NODE_SCROLL_SNAP = 1002007
```
 
设置[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件的限位滚动模式，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Scroll组件限位滚动时的对齐方式，数据类型ArkUI_ScrollSnapAlign，默认值ARKUI_SCROLL_SNAP_ALIGN_NONE。 |
| .value[1].i32 | 在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在开头和第一页间自由滑动，设置为false后，允许Scroll在开头和第一页间自由滑动，默认值true。该参数仅在限位点为多个时生效。 |
| .value[2].i32 | 在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在最后一页和末尾间自由滑动，设置为false后，允许Scroll在最后一页和末尾间自由滑动，默认值true。该参数仅在限位点为多个时生效。 |
| .value[3...].f32 | Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量。可以1个或多个。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Scroll组件限位滚动时的对齐方式，数据类型ArkUI_ScrollSnapAlign。 |
| .value[1].i32 | 在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在开头和第一页间自由滑动，设置为false后，允许Scroll在开头和第一页间自由滑动，默认值true。该参数仅在限位点为多个时生效。 |
| .value[2].i32 | 在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在最后一页和末尾间自由滑动，设置为false后，允许Scroll在最后一页和末尾间自由滑动，默认值true。该参数仅在限位点为多个时生效。 |
| .value[3...].f32 | Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量。 |
 
 
  

##### NODE_SCROLL_NESTED_SCROLL

```text
NODE_SCROLL_NESTED_SCROLL = 1002008
```
 
嵌套滚动选项，支持属性设置，属性重置和属性获取。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 可滚动组件往末尾端滚动时的嵌套滚动，参数类型ArkUI_ScrollNestedMode。 |
| .value[1].i32 | 可滚动组件往起始端滚动时的嵌套滚动，参数类型ArkUI_ScrollNestedMode。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 可滚动组件往末尾端滚动时的嵌套滚动，参数类型ArkUI_ScrollNestedMode。 |
| .value[1].i32 | 可滚动组件往起始端滚动时的嵌套滚动，参数类型ArkUI_ScrollNestedMode。 |
 
 
  

##### NODE_SCROLL_OFFSET

```text
NODE_SCROLL_OFFSET = 1002009
```
 
[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)滑动到指定位置，支持属性设置，属性重置和属性获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 水平滑动偏移，单位为vp。取值范围：当值小于0时按0处理，表示不带动画的滚动。值大于0表示带动画的滚动，默认滚动到起始位置后停止。可通过设置ScrollOptions中的animation参数，使滚动在越界时启动回弹动画。 |
| .value[1].f32 | 垂直滑动偏移，单位为vp。取值范围：当值小于0时按0处理，表示不带动画的滚动。值大于0表示带动画的滚动，默认滚动到起始位置后停止。可通过设置animation参数，使滚动在越界时启动回弹动画。 |
| .value[2]?.i32 | 可选值，滚动时长，单位为毫秒，默认值1000。 |
| .value[3]?.i32 | 可选值，滚动曲线，参数类型ArkUI_AnimationCurve。默认值为ARKUI_CURVE_EASE。 |
| .value[4]?.i32 | 可选值，是否使能默认弹簧动效，默认值为0不使能。 |
| .value[5]?.i32 | 可选值，设置动画滚动到边界是否转换为越界回弹动画，默认值为0不转换越界回弹动画。 |
| .value[6]?.i32 | 可选值，设置滚动是否可以停留在越界位置，默认值为0不停留在越界位置。该参数从API version 20开始支持。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平滑动偏移，单位为vp。 |
| .value[1].f32 | 垂直滑动偏移，单位为vp。 |
 
 
  

##### NODE_SCROLL_EDGE

```text
NODE_SCROLL_EDGE = 1002010
```
 
[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)滚动到容器边缘位置，支持属性设置，属性获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 容器边缘位置，参数类型ArkUI_ScrollEdge。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 容器是否位于边缘，-1：表示未处于边缘，如果处于边缘状态，参数类型ArkUI_ScrollEdge。 |
 
 
  

##### NODE_SCROLL_ENABLE_PAGING

```text
NODE_SCROLL_ENABLE_PAGING = 1002011
```
 
设置是否支持滑动翻页，支持属性设置，属性重置和属性获取接口。如果同时设置了滑动翻页[enablePaging](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#enablepaging11)和限位滚动[scrollSnap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollsnap10)，则[scrollSnap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollsnap10)优先生效，[enablePaging](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#enablepaging11)不生效。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滑动翻页，默认值0。0：不支持滑动翻页，1：支持滑动翻页。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滑动翻页。0：不支持滑动翻页，1：支持滑动翻页。 |
 
 
  

##### NODE_SCROLL_PAGE

```text
NODE_SCROLL_PAGE = 1002012
```
 
滚动到下一页或者上一页。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否向下翻页。0表示向下翻页，1表示向上翻页。 |
| .value[1]?.i32 | 是否开启翻页动画效果。1有动画，0无动画。默认值：0。 |
 
 
  

##### NODE_SCROLL_BY

```text
NODE_SCROLL_BY = 1002013
```
 
滑动指定距离。从API version 12开始List/Scroll/WaterFlow组件支持滑动指定距离。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 水平方向滚动距离，默认单位为vp。 |
| .value[1].f32 | 竖直方向滚动距离，默认单位为vp。 |
 
 
  

##### NODE_SCROLL_FLING

```text
NODE_SCROLL_FLING = 1002014
```
 
滚动类组件按传入的初始速度进行惯性滚动。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 13
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 惯性滚动的初始速度，默认单位为vp/s。值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向下滚动；如果值为负数，则向上滚动。 |
 
 
  

##### NODE_SCROLL_FADING_EDGE

```text
NODE_SCROLL_FADING_EDGE = 1002015
```
 
设置滚动类组件边缘渐隐效果。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 14
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果，默认值0。 |
| .value[1]?.f32 | 边缘渐隐效果长度。单位：vp，默认值：32。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果。 |
| .value[1].f32 | 边缘渐隐效果长度。单位：vp。 |
 
 
  

##### NODE_SCROLL_SIZE

```text
NODE_SCROLL_SIZE = 1002016
```
 
获取滚动类组件所有子组件全展开尺寸。
 
作为属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 14
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动类组件所有子组件全展开的宽度，默认单位为vp。 |
| .value[1].f32 | 滚动类组件所有子组件全展开的高度，默认单位为vp。 设置NODE_PADDING、NODE_MARGIN或NODE_BORDER_WIDTH后，NODE_PADDING、NODE_MARGIN或NODE_BORDER_WIDTH在单位vp转换成单位px时会进行像素取整，返回值根据取整后的值计算。 |
 
 
  

##### NODE_SCROLL_CONTENT_START_OFFSET

```text
NODE_SCROLL_CONTENT_START_OFFSET = 1002017
```
 
设置滚动类组件内容起始端偏移量。[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件从API version 15开始支持，[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)/[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)/[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 内容起始端偏移量，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 内容起始端偏移量，单位vp。 |
 
 
  

##### NODE_SCROLL_CONTENT_END_OFFSET

```text
NODE_SCROLL_CONTENT_END_OFFSET = 1002018
```
 
设置滚动类组件内容末尾端偏移量。[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件从API version 15开始支持，[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)/[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)/[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)从API version 22开始支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 内容末尾端偏移量，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 内容末尾端偏移量，单位vp。 |
 
 
  

##### NODE_SCROLL_FLING_SPEED_LIMIT

```text
NODE_SCROLL_FLING_SPEED_LIMIT = 1002019
```
 
限制跟手滑动结束后，Fling动效开始时的最大初始速度。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度，单位：vp/s。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | Fling动效开始时的最大初始速度。 |
 
 
  

##### NODE_SCROLL_CLIP_CONTENT

```text
NODE_SCROLL_CLIP_CONTENT = 1002020
```
 
设置滚动容器的内容层裁剪区域。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 内容裁剪模式，参数类型ArkUI_ContentClipMode。Grid、Scroll组件默认值为ARKUI_CONTENT_CLIP_MODE_BOUNDARY，List、WaterFlow组件默认值为ARKUI_CONTENT_CLIP_MODE_CONTENT_ONLY。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 内容裁剪模式，参数类型ArkUI_ContentClipMode。 |
 
 
  

##### NODE_SCROLL_BACK_TO_TOP

```text
NODE_SCROLL_BACK_TO_TOP = 1002021
```
 
设置滚动容器是否在点击状态栏时回到顶部。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否回到顶部，1表示回到顶部，0表示保持当前位置不变，默认值：API version 18之前：0。API version 18及以后：滚动方向是水平方向时为0，是垂直方向时为1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否回到顶部。 |
 
 
  

##### NODE_SCROLL_BAR_MARGIN

```text
NODE_SCROLL_BAR_MARGIN = 1002022
```
 
设置滚动条的边距，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置滚动条起始边距，默认值为0，单位：vp。 |
| .value[1].f32 | 设置滚动条末尾边距，默认值为0，单位：vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 滚动条起始边距，单位：vp。 |
| .value[1].f32 | 滚动条末尾边距，单位：vp。 |
 
 
  

##### NODE_SCROLL_MAX_ZOOM_SCALE

```text
NODE_SCROLL_MAX_ZOOM_SCALE = 1002023
```
 
设置滚动内容最大缩放比例。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容最大缩放比例。默认值：1 取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容最大缩放比例。 |
 
 
  

##### NODE_SCROLL_MIN_ZOOM_SCALE

```text
NODE_SCROLL_MIN_ZOOM_SCALE = 1002024
```
 
设置滚动内容最小缩放比例。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容最小缩放比例，默认值：1 取值范围：(0, NODE_SCROLL_MAX_ZOOM_SCALE]，小于或等于0时按默认值1处理，大于NODE_SCROLL_MAX_ZOOM_SCALE时按NODE_SCROLL_MAX_ZOOM_SCALE处理。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容最小缩放比例。 |
 
 
  

##### NODE_SCROLL_ZOOM_SCALE

```text
NODE_SCROLL_ZOOM_SCALE = 1002025
```
 
设置滚动内容缩放比例。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置内容缩放比例，默认值：1 取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取内容缩放比例。 |
 
 
  

##### NODE_SCROLL_ENABLE_BOUNCES_ZOOM

```text
NODE_SCROLL_ENABLE_BOUNCES_ZOOM = 1002026
```
 
设置是否支持过缩放回弹效果。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持过缩放回弹效果，0：不支持，1：支持。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持过缩放回弹效果，0：不支持，1：支持。 |
 
 
  

##### NODE_LIST_DIRECTION

```text
NODE_LIST_DIRECTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST = 1003000
```
 
设置[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件排列方向。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件排列方向，数据类型ArkUI_Axis，默认值ARKUI_AXIS_VERTICAL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件排列方向，数据类型ArkUI_Axis。 |
 
 
  

##### NODE_LIST_STICKY

```text
NODE_LIST_STICKY = 1003001
```
 
配合[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型ArkUI_StickyStyle，默认值ARKUI_STICKY_STYLE_NONE。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型ArkUI_StickyStyle。 |
 
 
  

##### NODE_LIST_SPACE

```text
NODE_LIST_SPACE = 1003002
```
 
设置列表项间距，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔。默认值0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件主轴方向的间隔。 |
 
 
  

##### NODE_LIST_NODE_ADAPTER

```text
NODE_LIST_NODE_ADAPTER = 1003003
```
 
List组件适配器，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeAdapter对象作为适配器。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_NodeAdapter。 |
 
 
  

##### NODE_LIST_CACHED_COUNT

```text
NODE_LIST_CACHED_COUNT = 1003004
```
 
List组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合List组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 15开始支持。 |
| .value[2]?.i32 | 设置List最大缓存数量，默认值与第一个参数相同。该参数从API version 22开始支持。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 15开始支持。 |
| .value[2]?.i32 | List最大缓存数量。该参数从API version 22开始支持。 |
 
 
  

##### NODE_LIST_SCROLL_TO_INDEX

```text
NODE_LIST_SCROLL_TO_INDEX = 1003005
```
 
滑动到指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。 |
| .value[1]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型ArkUI_ScrollAlignment, 默认值：ARKUI_SCROLL_ALIGNMENT_START。 |
| .value[3]?.f32 | 额外偏移量，默认值：0，单位：vp。该参数从API version 15开始支持。 |
 
 
  

##### NODE_LIST_ALIGN_LIST_ITEM

```text
NODE_LIST_ALIGN_LIST_ITEM = 1003006
```
 
设置List交叉轴方向宽度大于ListItem交叉轴宽度 * lanes时，ListItem在List交叉轴方向的布局方式，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 交叉轴方向的布局方式。参数类型ArkUI_ListItemAlign。默认值：ARKUI_LIST_ITEM_ALIGNMENT_START。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 交叉轴方向的布局方式。参数类型ArkUI_ListItemAlign。 |
 
 
  

##### NODE_LIST_CHILDREN_MAIN_SIZE

```text
NODE_LIST_CHILDREN_MAIN_SIZE = 1003007
```
 
设置List子组件默认主轴尺寸。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为ArkUI_ListChildrenMainSize。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 参数格式为ArkUI_ListChildrenMainSize。 |
 
 
  

##### NODE_LIST_INITIAL_INDEX

```text
NODE_LIST_INITIAL_INDEX = 1003008
```
 
设置当前List初次加载时视口起始位置显示的item的索引值，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 当前List初次加载时视口起始位置显示的item的索引值。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 当前List初次加载时视口起始位置显示的item的索引值。 |
 
 
  

##### NODE_LIST_DIVIDER

```text
NODE_LIST_DIVIDER = 1003009
```
 
设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 分割线颜色，0xargb类型，默认值为0x08000000。 |
| .value[1].f32 | 分割线宽，默认值：0，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，默认值：0，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，默认值：0，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 分割线颜色，0xargb类型。 |
| .value[1].f32 | 分割线宽。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，单位vp。 |
 
 
  

##### NODE_LIST_SCROLL_TO_INDEX_IN_GROUP

```text
NODE_LIST_SCROLL_TO_INDEX_IN_GROUP = 1003010
```
 
滑动到指定[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)中指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标ListItemGroup在当前List中的索引值。 |
| .value[1].i32 | 要滑动到的目标ListItem在ListItemGroup中的索引值。 |
| .value[2]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[3]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型ArkUI_ScrollAlignment。默认值：ARKUI_SCROLL_ALIGNMENT_START。 |
 
 
  

##### NODE_LIST_LANES

```text
NODE_LIST_LANES = 1003011
```
 
设置List列数（List垂直滚动时表示列数，水平滚动时表示行数），支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | List列数，如果设置了最大最小列宽，则设置列数不生效；默认值：1，取值范围：[1, +∞)，设置异常值时使用默认值。 |
| .value[1]?.f32 | 最小列宽，单位vp。 |
| .value[2]?.f32 | 最大列宽，单位vp。 |
| .value[3]?.f32 | 列间距，默认值：0，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 当前List列数。 |
| .value[1].f32 | 最小列宽，单位vp。 |
| .value[2].f32 | 最大列宽，单位vp。 |
| .value[3].f32 | 列间距，单位vp。 |
 
 
  

##### NODE_LIST_SCROLL_SNAP_ALIGN

```text
NODE_LIST_SCROLL_SNAP_ALIGN = 1003012
```
 
设置List限位对齐模式。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件限位滚动时的对齐方式，数据类型ArkUI_ScrollSnapAlign，默认值ARKUI_SCROLL_SNAP_ALIGN_NONE。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件限位滚动时的对齐方式，数据类型ArkUI_ScrollSnapAlign。 |
 
 
  

##### NODE_LIST_MAINTAIN_VISIBLE_CONTENT_POSITION

```text
NODE_LIST_MAINTAIN_VISIBLE_CONTENT_POSITION = 1003013
```
 
设置List显示区域外插入或删除数据是否保持可见内容位置不变。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。 |
 
 
  

##### NODE_LIST_STACK_FROM_END

```text
NODE_LIST_STACK_FROM_END = 1003014
```
 
设置List从末尾开始布局。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。 |
 
 
  

##### NODE_LIST_FOCUS_WRAP_MODE

```text
NODE_LIST_FOCUS_WRAP_MODE = 1003015
```
 
List组件走焦换行模式，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件走焦换行模式，参数类型ArkUI_FocusWrapMode。默认值：ARKUI_FOCUS_WRAP_MODE_DEFAULT。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件走焦换行模式，参数类型ArkUI_FocusWrapMode。 |
 
 
  

##### NODE_LIST_SYNC_LOAD

```text
NODE_LIST_SYNC_LOAD = 1003016
```
 
List组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否同步加载子节点。0：分帧加载，1：同步加载，默认值为1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否同步加载子节点。0：分帧加载，1：同步加载。 |
 
 
  

##### NODE_LIST_SCROLL_SNAP_ANIMATION_SPEED

```text
NODE_LIST_SCROLL_SNAP_ANIMATION_SPEED = 1003017
```
 
List组件限位滚动动画速度，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件限位滚动动画速度，数据类型ArkUI_ScrollSnapAnimationSpeed。默认值：ARKUI_SCROLL_SNAP_ANIMATION_NORMAL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件限位滚动动画速度，数据类型ArkUI_ScrollSnapAnimationSpeed。 |
 
 
  

##### NODE_LIST_LANES_ITEMFILLPOLICY

```text
NODE_LIST_LANES_ITEMFILLPOLICY = 1003018
```
 
List组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
| .value[1]?.f32 | 列间距，单位vp。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
| .value[1].f32 | 列间距，单位vp。 |
 
 
  

##### NODE_LIST_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING

```text
NODE_LIST_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING = 1003019
```
 
设置当前List组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | List组件是否支持空分支。0：不支持，1：支持。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | List组件是否支持空分支。0：不支持，1：支持。 |
 
 
  

##### NODE_LIST_ITEM_SWIPE_ACTION

```text
NODE_LIST_ITEM_SWIPE_ACTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST_ITEM = 1004000
```
 
设置ListItem的划出组件，支持属性设置，属性重置，属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_ListItemSwipeActionOption对象构造。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 使用ArkUI_ListItemSwipeActionOption对象构造。 |
 
 
  

##### NODE_LIST_ITEM_GROUP_SET_HEADER

```text
NODE_LIST_ITEM_GROUP_SET_HEADER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_LIST_ITEM_GROUP = 1005000
```
 
设置 ListItemGroup 头部组件，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeHandle对象作为ListItemGroup头部组件。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 使用ArkUI_NodeHandle对象作为ListItemGroup头部组件。 |
 
 
  

##### NODE_LIST_ITEM_GROUP_SET_FOOTER

```text
NODE_LIST_ITEM_GROUP_SET_FOOTER = 1005001
```
 
设置 ListItemGroup 尾部组件，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeHandle对象作为ListItemGroup尾部组件。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 使用ArkUI_NodeHandle对象作为ListItemGroup尾部组件。 |
 
 
  

##### NODE_LIST_ITEM_GROUP_SET_DIVIDER

```text
NODE_LIST_ITEM_GROUP_SET_DIVIDER = 1005002
```
 
设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色，0xargb类型，默认值为0x08000000。 |
| .value[1].f32 | 分割线宽，默认值：0，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，默认值：0，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，默认值：0，单位vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色，0xargb类型。 |
| .value[1].f32 | 分割线宽，单位vp。 |
| .value[2].f32 | 分割线距离列表侧边起始端的距离，单位vp。 |
| .value[3].f32 | 分割线距离列表侧边结束端的距离，单位vp。 |
 
 
  

##### NODE_LIST_ITEM_GROUP_CHILDREN_MAIN_SIZE

```text
NODE_LIST_ITEM_GROUP_CHILDREN_MAIN_SIZE = 1005003
```
 
设置ListItemGroup子组件默认主轴尺寸。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为ArkUI_ListChildrenMainSize。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 参数格式为ArkUI_ListChildrenMainSize。 |
 
 
  

##### NODE_LIST_ITEM_GROUP_NODE_ADAPTER

```text
NODE_LIST_ITEM_GROUP_NODE_ADAPTER = 1005004
```
 
[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)组件适配器，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeAdapter对象作为适配器。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_NodeAdapter。 |
 
 
  

##### NODE_REFRESH_REFRESHING

```text
NODE_REFRESH_REFRESHING = MAX_NODE_SCOPE_NUM * ARKUI_NODE_REFRESH = 1009000
```
 
设置组件是否正在刷新，支持属性设置，属性获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型为1或者0，1表示正在刷新，0表示不在刷新。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型为1或者0，1表示正在刷新，0表示不在刷新。 |
 
 
  

##### NODE_REFRESH_CONTENT

```text
NODE_REFRESH_CONTENT = 1009001
```
 
设置下拉区域的自定义内容，支持属性设置和重置。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型ArkUI_NodeHandle。 |
 
 
  

##### NODE_REFRESH_PULL_DOWN_RATIO

```text
NODE_REFRESH_PULL_DOWN_RATIO = 1009002
```
 
设置下拉跟手系数，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 下拉跟手系数,有效值为0-1之间的值。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 下拉跟手系数,有效值为0-1之间的值。 |
 
 
  

##### NODE_REFRESH_OFFSET

```text
NODE_REFRESH_OFFSET = 1009003
```
 
设置触发刷新的下拉偏移量，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 下拉偏移量，单位vp， 默认值：64vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 下拉偏移量，单位vp， 默认值：64vp。 |
 
 
  

##### NODE_REFRESH_PULL_TO_REFRESH

```text
NODE_REFRESH_PULL_TO_REFRESH = 1009004
```
 
设置当下拉距离超过[refreshOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#refreshoffset12)时是否触发刷新，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否触发刷新。支持取值为0或1，其中1为触发刷新，0为不触发刷新。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否触发刷新，1为触发刷新，0为不触发刷新。 |
 
 
  

##### NODE_REFRESH_MAX_PULL_DOWN_DISTANCE

```text
NODE_REFRESH_MAX_PULL_DOWN_DISTANCE = 1009005
```
 
设置刷新的最大下拉距离。此属性可以根据需要通过api进行属性设置，属性重置和属性获取。
 
作为属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最大下拉距离，单位：vp。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最大下拉距离，单位：vp。 |
 
 
  

##### NODE_REFRESH_PULL_UP_TO_CANCEL_REFRESH

```text
NODE_REFRESH_PULL_UP_TO_CANCEL_REFRESH = 1009006
```
 
设置上划是否取消刷新。支持属性设置，属性重置和属性获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 上划是否取消刷新。支持取值为0或1，其中0为上划不取消刷新，1为上划取消刷新。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 上划是否取消刷新。0为上划不取消刷新，1为上划取消刷新。 |
 
 
  

##### NODE_WATER_FLOW_LAYOUT_DIRECTION

```text
NODE_WATER_FLOW_LAYOUT_DIRECTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_WATER_FLOW = 1010000
```
 
定义瀑布流组件布局主轴方向，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型ArkUI_FlexDirection。默认值ARKUI_FLEX_DIRECTION_COLUMN。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型ArkUI_FlexDirection。 |
 
 
  

##### NODE_WATER_FLOW_COLUMN_TEMPLATE

```text
NODE_WATER_FLOW_COLUMN_TEMPLATE = 1010001
```
 
设置当前瀑布流组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .string | 布局列的数量。默认值：'1fr'。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .string | 布局列的数量。 |
 
 
  

##### NODE_WATER_FLOW_ROW_TEMPLATE

```text
NODE_WATER_FLOW_ROW_TEMPLATE = 1010002
```
 
设置当前瀑布流组件布局行的数量，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .string | 布局行的数量。默认值：'1fr'。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .string | 布局行的数量。 |
 
 
  

##### NODE_WATER_FLOW_COLUMN_GAP

```text
NODE_WATER_FLOW_COLUMN_GAP = 1010003
```
 
设置列与列的间距，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 列与列的间距，单位vp。 |
 
 
  

##### NODE_WATER_FLOW_ROW_GAP

```text
NODE_WATER_FLOW_ROW_GAP = 1010004
```
 
设置行与行的间距，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 行与行的间距，单位vp。 |
 
 
  

##### NODE_WATER_FLOW_SECTION_OPTION

```text
NODE_WATER_FLOW_SECTION_OPTION = 1010005
```
 
设置FlowItem分组配置信息，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。 |
| .object | 参数格式为ArkUI_WaterFlowSectionOption。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_WaterFlowSectionOption。 |
 
 
  

##### NODE_WATER_FLOW_NODE_ADAPTER

```text
NODE_WATER_FLOW_NODE_ADAPTER = 1010006
```
 
[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)组件适配器，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeAdapter对象作为适配器。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_NodeAdapter。 |
 
 
  

##### NODE_WATER_FLOW_CACHED_COUNT

```text
NODE_WATER_FLOW_CACHED_COUNT = 1010007
```
 
[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合waterFlow组件Adapter使用，设置adapter中的缓存数量。 |
| .value[1]?.i32 | 是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 16开始支持。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | adapter中的缓存数量。 |
| .value[1].i32 | 是否显示缓存节点，0：不显示，1：显示。该参数从API version 16开始支持。 |
 
 
  

##### NODE_WATER_FLOW_FOOTER

```text
NODE_WATER_FLOW_FOOTER = 1010008
```
 
设置瀑布流组件末尾的自定义显示组件。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型ArkUI_NodeHandle。 |
 
 
  

##### NODE_WATER_FLOW_SCROLL_TO_INDEX

```text
NODE_WATER_FLOW_SCROLL_TO_INDEX = 1010009
```
 
滑动到指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。 |
| .value[1]?.i32 | 设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的元素与当前容器的对齐方式，参数类型ArkUI_ScrollAlignment。默认值为：ARKUI_SCROLL_ALIGNMENT_START。 |
| .value[3]?.f32 | 滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。该参数从API version 23开始支持。 |
 
 
  

##### NODE_WATER_FLOW_ITEM_CONSTRAINT_SIZE

```text
NODE_WATER_FLOW_ITEM_CONSTRAINT_SIZE = 1010010
```
 
设置当前瀑布流子组件的约束尺寸属性，组件布局时，进行尺寸范围限制，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最小宽度，使用-1表示不设置。 |
| .value[1].f32 | 最大宽度，使用-1表示不设置。 |
| .value[2].f32 | 最小高度，使用-1表示不设置。 |
| .value[3].f32 | 最大高度，使用-1表示不设置。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最小宽度，使用-1表示不设置。 |
| .value[1].f32 | 最大宽度，使用-1表示不设置。 |
| .value[2].f32 | 最小高度，使用-1表示不设置。 |
| .value[3].f32 | 最大高度，使用-1表示不设置。 |
 
 
  

##### NODE_WATER_FLOW_LAYOUT_MODE

```text
NODE_WATER_FLOW_LAYOUT_MODE = 1010011
```
 
定义瀑布流组件布局模式，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 布局模式，参数类型ArkUI_WaterFlowLayoutMode，默认值：ARKUI_WATER_FLOW_LAYOUT_MODE_ALWAYS_TOP_DOWN。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 布局模式，参数类型ArkUI_WaterFlowLayoutMode。 |
 
 
  

##### NODE_WATER_FLOW_SYNC_LOAD

```text
NODE_WATER_FLOW_SYNC_LOAD = 1010012
```
 
WaterFlow组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。 |
 
 
  

##### NODE_WATER_FLOW_COLUMN_TEMPLATE_ITEMFILLPOLICY

```text
NODE_WATER_FLOW_COLUMN_TEMPLATE_ITEMFILLPOLICY  = 1010013
```
 
WaterFlow组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
 
 
  

##### NODE_GRID_COLUMN_TEMPLATE

```text
NODE_GRID_COLUMN_TEMPLATE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_GRID = 1013000
```
 
设置当前Grid组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .string | 布局列的数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .string | 布局列的数量。 |
 
 
  

##### NODE_GRID_ROW_TEMPLATE

```text
NODE_GRID_ROW_TEMPLATE = 1013001
```
 
设置当前Grid布局行的数量或最小行高值，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .string | 布局行的数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .string | 布局行的数量。 |
 
 
  

##### NODE_GRID_COLUMN_GAP

```text
NODE_GRID_COLUMN_GAP = 1013002
```
 
设置列与列的间距，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 列与列的间距，单位vp。 |
 
 
  

##### NODE_GRID_ROW_GAP

```text
NODE_GRID_ROW_GAP = 1013003
```
 
设置行与行的间距，支持属性设置、重置和获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 行与行的间距，单位vp。 |
 
 
  

##### NODE_GRID_NODE_ADAPTER

```text
NODE_GRID_NODE_ADAPTER = 1013004
```
 
[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)组件适配器，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 使用ArkUI_NodeAdapter对象作为适配器。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_NodeAdapter。 |
 
 
  

##### NODE_GRID_CACHED_COUNT

```text
NODE_GRID_CACHED_COUNT = 1013005
```
 
[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)组件适配器缓存数量，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 配合Grid组件适配器使用，设置ArkUI_NodeAdapter的缓存数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件适配器的缓存数量。 |
 
 
  

##### NODE_GRID_FOCUS_WRAP_MODE

```text
NODE_GRID_FOCUS_WRAP_MODE = 1013006
```
 
[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)组件走焦换行模式，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件走焦换行模式，参数类型ArkUI_FocusWrapMode。默认值：FOCUS_WRAP_MODE_DEFAULT。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件走焦换行模式，参数类型ArkUI_FocusWrapMode。 |
 
 
  

##### NODE_GRID_SYNC_LOAD

```text
NODE_GRID_SYNC_LOAD = 1013007
```
 
[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。 |
 
 
  

##### NODE_GRID_ALIGN_ITEMS

```text
NODE_GRID_ALIGN_ITEMS = 1013008
```
 
设置Grid中[GridItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem)的对齐方式，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid中GridItem的对齐方式，参数类型ArkUI_GridItemAlignment。默认值：GRID_ITEM_ALIGNMENT_DEFAULT。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid中GridItem的对齐方式，参数类型ArkUI_GridItemAlignment。 |
 
 
  

##### NODE_GRID_LAYOUT_OPTIONS

```text
NODE_GRID_LAYOUT_OPTIONS = 1013009
```
 
设置Grid布局选项，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .object | 参数格式为ArkUI_GridLayoutOptions。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .object | 返回值格式为ArkUI_GridLayoutOptions。 |
 
 
  

##### NODE_GRID_COLUMN_TEMPLATE_ITEMFILLPOLICY

```text
NODE_GRID_COLUMN_TEMPLATE_ITEMFILLPOLICY = 1013010
```
 
Grid组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在不同断点规格下的列数，数据类型ArkUI_ItemFillPolicy。 |
 
 
  

##### NODE_GRID_EDIT_MODE

```text
NODE_GRID_EDIT_MODE = 1013011
```
 
Grid组件是否进入编辑模式，进入编辑模式可以通过NODE_GRID_ON_ITEM_DRAG_START事件拖拽GridItem。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。 |
 
 
  

##### NODE_GRID_DRAG_ANIMATION

```text
NODE_GRID_DRAG_ANIMATION = 1013012
```
 
Grid组件是否启用GridItem拖拽动画。支持属性设置，属性重置和属性获取接口。
 
仅在滚动模式下（只设置NODE_GRID_ROW_TEMPLATE、NODE_GRID_COLUMN_TEMPLATE其中一个）支持动画。
 
仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。 |
 
 
  

##### NODE_GRID_MULTI_SELECTABLE

```text
NODE_GRID_MULTI_SELECTABLE = 1013013
```
 
Grid组件是否启用鼠标框选。支持属性设置，属性重置和属性获取接口。
 
启用后在Grid范围内鼠标框选会触发GridItem的[NODE_GRID_ITEM_ON_SELECT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)事件。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用鼠标框选。0：不启用，1：启用。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否启用鼠标框选。0：不启用，1：启用。 |
 
 
  

##### NODE_GRID_SCROLL_TO_INDEX

```text
NODE_GRID_SCROLL_TO_INDEX = 1013014
```
 
滑动到指定index。
 
开启动效时，会对经过的所有子组件进行加载和布局计算，当大量加载子组件时会导致性能问题。
 
作为属性设置方法参数[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 要滑动到的目标元素在当前容器中的索引值。 |
| .value[1]?.i32 | 设置滑动到目标元素时是否有动效，1表示有动效，0表示没有动效。默认值：0。 |
| .value[2]?.i32 | 指定滑动到的目标元素与当前容器的对齐方式，参数类型ArkUI_ScrollAlignment。默认值：ARKUI_SCROLL_ALIGNMENT_AUTO。 |
| .value[3]?.f32 | 滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。 |
 
 
  

##### NODE_GRID_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING

```text
NODE_GRID_SUPPORT_EMPTY_BRANCH_IN_LAZY_LOADING = 1013015
```
 
设置当前Grid组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Grid组件是否支持空分支。0：不支持，1：支持。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Grid组件是否支持空分支。0：不支持，1：支持。 |
 
 
  

##### NODE_GRID_ITEM_STYLE

```text
NODE_GRID_ITEM_STYLE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_GRID_ITEM = 1014000
```
 
设置GridItem样式，支持属性设置，属性重置和属性获取。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 22
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem样式，参数类型ArkUI_GridItemStyle。默认值：GRID_ITEM_STYLE_NONE。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem样式，参数类型ArkUI_GridItemStyle。 |
 
 
  

##### NODE_GRID_ITEM_SELECTABLE

```text
NODE_GRID_ITEM_SELECTABLE = 1014001
```
 
设置GridItem是否可以被鼠标框选。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem是否可以被鼠标框选。0：不可以，1：可以。默认值：1。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem是否可以被鼠标框选。0：不可以，1：可以。 |
 
 
  

##### NODE_GRID_ITEM_SELECTED

```text
NODE_GRID_ITEM_SELECTED = 1014002
```
 
设置GridItem选中状态。支持属性设置，属性重置和属性获取接口。
 
作为属性设置方法参数、属性获取方法返回值[ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式如下。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | GridItem选中状态。0：未选中，1：已选中。默认值：0。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | GridItem选中状态。0：未选中，1：已选中。 |
