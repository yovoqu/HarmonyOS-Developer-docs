# swiper.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-swiper-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义Swiper组件的枚举和接口。
 
**引用文件：** <arkui/node_attributes/swiper.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [NDKSwiperSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKSwiperSample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_SwiperIndicator | ArkUI_SwiperIndicator | 定义Swiper组件的导航指示器样式，用于在轮播等场景中展示当前位置和切换状态。支持自定义指示器的大小、颜色、间距等属性配置，能够提升用户对当前浏览位置的感知，增强用户交互体验，适用于需要展示轮播图片、广告位、内容导航等多种应用场景。 |
| ArkUI_SwiperDigitIndicator | ArkUI_SwiperDigitIndicator | 定义Swiper组件的数字导航指示器样式，用于以数字形式展示当前位置和总页数。 |
| ArkUI_SwiperArrowStyle | ArkUI_SwiperArrowStyle | 定义Swiper组件的导航箭头样式结构体，通过配置箭头位置、大小、颜色等属性实现翻页指引。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_SwiperArrow | ArkUI_SwiperArrow | Swiper导航点箭头枚举值。 |
| ArkUI_SwiperNestedScrollMode | ArkUI_SwiperNestedScrollMode | Swiper组件和父组件的嵌套滚动模式。 |
| ArkUI_PageFlipMode | ArkUI_PageFlipMode | Swiper组件鼠标滚轮翻页模式。 |
| ArkUI_SwiperAnimationMode | ArkUI_SwiperAnimationMode | Swiper组件跳转到目标index的动画模式。 |
| ArkUI_SwiperIndicatorType | ArkUI_SwiperIndicatorType | 定义Swiper组件的导航指示器类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type) | 创建Swiper组件的导航指示器。 |
| void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator) | 销毁Swiper组件的导航指示器指针。 |
| void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value) | 设置导航点距离Swiper组件左边的距离。 |
| float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator) | 获取导航点距离Swiper组件左边的距离。 |
| void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value) | 设置导航点距离Swiper组件顶部的距离。 |
| float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator) | 获取导航点距离Swiper组件顶部的距离。 |
| void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value) | 设置导航点距离Swiper组件右边的距离。 |
| float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator) | 获取导航点距离Swiper组件右边的距离。 |
| void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value) | 设置导航点距离Swiper组件底部的距离。 |
| float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator) | 获取导航点距离Swiper组件底部的距离。 |
| void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize) | 设置OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。 |
| int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator) | 获取OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。 |
| void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value) | 设置Swiper组件圆点导航指示器的宽。 |
| float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator) | 获取Swiper组件圆点导航指示器的宽。 |
| void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value) | 设置Swiper组件圆点导航指示器的高。 |
| float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator) | 获取Swiper组件圆点导航指示器的高。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value) | 设置被选中的Swiper组件圆点导航指示器的宽。 |
| float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator) | 获取被选中Swiper组件圆点导航指示器的宽。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value) | 设置被选中的Swiper组件圆点导航指示器的高。 |
| float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator) | 获取被选中Swiper组件圆点导航指示器的高。 |
| void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask) | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator) | 获取是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color) | 设置Swiper组件圆点导航指示器的颜色。 |
| uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator) | 获取Swiper组件圆点导航指示器的颜色。 |
| void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor) | 设置被选中Swiper组件圆点导航指示器的颜色。 |
| uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator) | 获取被选中Swiper组件圆点导航指示器的颜色。 |
| int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount) | 设置圆点导航点指示器样式下，导航点显示个数的最大值。 |
| int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator) | 获取圆点导航点指示器样式下，导航点显示个数的最大值。 |
| ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create() | 创建Swiper组件的数字导航指示器。 |
| void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator) | 销毁Swiper组件的数字导航指示器指针。 |
| void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | 设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator) | 获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | 设置数字导航指示器距离Swiper组件顶部的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator) | 获取数字导航指示器距离Swiper组件顶部的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | 设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator) | 获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value) | 设置数字导航指示器距离Swiper组件底部的距离。 |
| float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator) | 获取数字导航指示器距离Swiper组件底部的距离。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color) | 设置Swiper组件数字导航指示器字体颜色。 |
| uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator) | 获取Swiper组件数字导航指示器字体颜色。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor) | 设置被选中Swiper组件数字导航指示器字体颜色。 |
| uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator) | 获取被选中Swiper组件数字导航指示器字体颜色。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size) | 设置Swiper组件数字导航指示器字体大小。 |
| float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator) | 获取Swiper组件数字导航指示器字体大小。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size) | 设置被选中Swiper组件数字导航指示器字体大小。 |
| float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator) | 获取被选中Swiper组件数字导航指示器字体大小。 |
| ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create() | 创建Swiper组件的导航箭头。 |
| void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle) | 销毁Swiper组件的导航箭头指针。 |
| void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground) | 设置Swiper组件导航箭头底板是否显示。 |
| int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头底板是否显示。 |
| void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle) | 设置Swiper组件导航箭头显示位置。 |
| int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头显示位置。 |
| void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize) | 设置Swiper组件导航箭头底板大小。 |
| float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头底板大小。 |
| void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor) | 设置Swiper组件导航箭头底板颜色。 |
| uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头底板颜色。 |
| void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize) | 设置Swiper组件导航箭头大小。 |
| float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头大小。 |
| void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor) | 设置Swiper组件导航箭头颜色。 |
| uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle) | 获取Swiper组件导航箭头颜色。 |
| void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space) | 设置导航点间距。 |
| float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator) | 获取导航点间距。 |
| void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize) | 设置OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。 |
| int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator) | 获取OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_SwiperArrow

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SwiperArrow
```
 
**描述**
 
Swiper导航点箭头枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_ARROW_HIDE = 0 | 不显示swiper中导航点箭头。 |
| ARKUI_SWIPER_ARROW_SHOW | 显示swiper中导航点箭头。 |
| ARKUI_SWIPER_ARROW_SHOW_ON_HOVER | 在hover状态下显示swiper中导航点箭头。 |
 
 
  

#### ArkUI_SwiperNestedScrollMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SwiperNestedScrollMode
```
 
**描述**
 
Swiper组件和父组件的嵌套滚动模式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_NESTED_SRCOLL_SELF_ONLY = 0 | Swiper只自身滚动，不与父组件联动。 |
| ARKUI_SWIPER_NESTED_SRCOLL_SELF_FIRST | Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。 |
 
 
  

#### ArkUI_PageFlipMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_PageFlipMode
```
 
**描述**
 
Swiper组件鼠标滚轮翻页模式。
 
**起始版本：** 15
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PAGE_FLIP_MODE_CONTINUOUS = 0 | 鼠标滚轮连续滚动时翻多页，根据鼠标事件上报次数确定。 |
| ARKUI_PAGE_FLIP_MODE_SINGLE | 一次翻页动画结束前不响应其他鼠标滚轮事件。 |
 
 
  

#### ArkUI_SwiperAnimationMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SwiperAnimationMode
```
 
**描述**
 
Swiper组件跳转到目标index的动画模式。
 
**起始版本：** 15
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_NO_ANIMATION = 0 | 无动画跳转到目标index。 |
| ARKUI_SWIPER_DEFAULT_ANIMATION = 1 | 做动画跳转到目标index。 |
| ARKUI_SWIPER_FAST_ANIMATION = 2 | 先无动画跳转到目标附近再做动画跳转到目标index。 |
 
 
  

#### ArkUI_SwiperIndicatorType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SwiperIndicatorType
```
 
**描述**
 
定义Swiper组件的导航指示器类型。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SWIPER_INDICATOR_TYPE_DOT | 圆点指示器类型。 |
| ARKUI_SWIPER_INDICATOR_TYPE_DIGIT | 数字指示器类型。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_SwiperIndicator_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type)
```
 
**描述**
 
创建Swiper组件的导航指示器。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicatorType type | 导航指示器的类型。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperIndicator* | 导航指示器对象指针。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
销毁Swiper组件的导航指示器指针。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetStartPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置导航点距离Swiper组件左边的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件左边的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetStartPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取导航点距离Swiper组件左边的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件左边的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetTopPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置导航点距离Swiper组件顶部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件顶部的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetTopPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取导航点距离Swiper组件顶部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件顶部的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetEndPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置导航点距离Swiper组件右边的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件右边的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetEndPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取导航点距离Swiper组件右边的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件右边的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetBottomPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置导航点距离Swiper组件底部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件底部的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetBottomPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取导航点距离Swiper组件底部的距离。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件底部的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize)
```
 
**描述**
 
设置OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取OH_ArkUI_SwiperIndicator_SetBottomPosition是否忽略导航点大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 是否忽略导航点大小。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetItemWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置Swiper组件圆点导航指示器的宽。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetItemWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取Swiper组件圆点导航指示器的宽。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetItemHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置Swiper组件圆点导航指示器的高。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetItemHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取Swiper组件圆点导航指示器的高。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetSelectedItemWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置被选中的Swiper组件圆点导航指示器的宽。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetSelectedItemWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取被选中Swiper组件圆点导航指示器的宽。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetSelectedItemHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```
 
**描述**
 
设置被选中的Swiper组件圆点导航指示器的高。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetSelectedItemHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取被选中Swiper组件圆点导航指示器的高。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetMask()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask)
```
 
**描述**
 
设置是否显示Swiper组件圆点导航指示器的蒙版样式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t mask | 是否显示蒙版样式，1表示显示，0表示不显示。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetMask()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取是否显示Swiper组件圆点导航指示器的蒙版样式。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | mask 1表示显示圆点导航指示器的蒙版样式，0表示不显示。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color)
```
 
**描述**
 
设置Swiper组件圆点导航指示器的颜色。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| uint32_t color | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取Swiper组件圆点导航指示器的颜色。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetSelectedColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor)
```
 
**描述**
 
设置被选中Swiper组件圆点导航指示器的颜色。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| uint32_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetSelectedColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取被选中Swiper组件圆点导航指示器的颜色。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetMaxDisplayCount()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount)
```
 
**描述**
 
设置圆点导航点指示器样式下，导航点显示个数的最大值。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| int32_t maxDisplayCount | 导航点显示个数最大值，有效取值范围[6, 9]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 如果maxDisplayCount设置范围错误，返回错误码。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetMaxDisplayCount()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取圆点导航点指示器样式下，导航点显示个数的最大值。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 导航点显示个数最大值，有效取值范围[6, 9]。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create()
```
 
**描述**
 
创建Swiper组件的数字导航指示器。
 
**起始版本：** 19
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperDigitIndicator * | 数字导航指示器对象指针。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
销毁Swiper组件的数字导航指示器指针。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetStartPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```
 
**描述**
 
设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，其距离Swiper组件右边的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetStartPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，其距离Swiper组件右边的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetTopPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```
 
**描述**
 
设置数字导航指示器距离Swiper组件顶部的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件顶部的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetTopPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取数字导航指示器距离Swiper组件顶部的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件顶部的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetEndPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```
 
**描述**
 
设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，其距离Swiper组件左边的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetEndPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，其距离Swiper组件左边的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetBottomPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```
 
**描述**
 
设置数字导航指示器距离Swiper组件底部的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件底部的距离。默认值：0，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetBottomPosition()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取数字导航指示器距离Swiper组件底部的距离。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件底部的距离。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color)
```
 
**描述**
 
设置Swiper组件数字导航指示器字体颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| uint32_t color | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。默认值：0xFF182431。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取Swiper组件数字导航指示器字体颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor)
```
 
**描述**
 
设置被选中Swiper组件数字导航指示器字体颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| uint32_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。默认值：0xFF182431。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取被选中Swiper组件数字导航指示器字体颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 颜色类型，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```
 
**描述**
 
设置Swiper组件数字导航指示器字体大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取Swiper组件数字导航指示器字体大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```
 
**描述**
 
设置被选中Swiper组件数字导航指示器字体大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取被选中Swiper组件数字导航指示器字体大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create()
```
 
**描述**
 
创建Swiper组件的导航箭头。
 
**起始版本：** 19
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_SwiperArrowStyle * | 导航箭头对象指针。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
销毁Swiper组件的导航箭头指针。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetShowBackground()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground)
```
 
**描述**
 
设置Swiper组件导航箭头底板是否显示。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| int32_t showBackground | 导航箭头底板是否显示，0：不显示，1：显示，默认值：0。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetShowBackground()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头底板是否显示。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 导航箭头底板是否显示，0：不显示，1：显示。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle)
```
 
**描述**
 
设置Swiper组件导航箭头显示位置。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| int32_t showSidebarMiddle | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧，默认值：0。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头显示位置。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetBackgroundSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize)
```
 
**描述**
 
设置Swiper组件导航箭头底板大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| float backgroundSize | 导航箭头底板大小，单位：vp。默认值：显示在导航指示器两侧24vp，显示在Swiper两侧32vp。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetBackgroundSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头底板大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航箭头底板大小，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetBackgroundColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor)
```
 
**描述**
 
设置Swiper组件导航箭头底板颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| uint32_t backgroundColor | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000表示红色。默认值：显示在导航指示器两侧为0x00000000，显示在Swiper两侧为0x19182431。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetBackgroundColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头底板颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetArrowSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize)
```
 
**描述**
 
设置Swiper组件导航箭头大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| float arrowSize | 导航箭头大小，单位：vp。默认值：显示在导航指示器两侧18vp，显示在Swiper两侧24vp。显示导航箭头底板时，arrowSize固定为backgroundSize的3/4。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetArrowSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航箭头大小，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_SetArrowColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor)
```
 
**描述**
 
设置Swiper组件导航箭头颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
| uint32_t arrowColor | 导航箭头颜色，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperArrowStyle_GetArrowColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle)
```
 
**描述**
 
获取Swiper组件导航箭头颜色。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperArrowStyle* arrowStyle | 导航箭头对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint32_t | 导航箭头颜色，0xargb格式，形如 0xFFFF0000表示红色。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_SetSpace()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space)
```
 
**描述**
 
设置导航点间距。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
| float space | 导航点间距。默认值：8，单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperIndicator_GetSpace()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator)
```
 
**描述**
 
获取导航点间距。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 导航点间距。单位：vp。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize)
```
 
**描述**
 
设置OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 导航指示器对象指针。 |
| int32_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |
 
 
  

#### OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator)
```
 
**描述**
 
获取OH_ArkUI_SwiperDigitIndicator_SetBottomPosition是否忽略导航点大小。
 
**起始版本：** 19
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 导航指示器对象指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 是否忽略导航点大小。 |
