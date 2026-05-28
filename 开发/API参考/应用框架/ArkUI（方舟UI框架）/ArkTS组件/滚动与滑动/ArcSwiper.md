# ArcSwiper

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

弧形滑块视图容器，提供子组件滑动轮播显示的能力。

> [!NOTE]
> 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> ArcSwiperAttribute是用于配置ArcSwiper组件属性的关键接口。API version 21及之前版本，导入ArcSwiper组件后需要开发者手动导入ArcSwiperAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcSwiper组件后，会自动导入ArcSwiperAttribute，无需开发者手动导入ArcSwiperAttribute。 如果开发者手动导入ArcSwiperAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。


API version 21及之前版本：

```text
import {
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';
```

API version 22及之后版本：

```text
import {
  ArcSwiper,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';
```



##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可以包含子组件。

> [!NOTE]
> 子组件类型：系统组件和自定义组件，支持渲染控制类型（ if/else 、 ForEach 和 LazyForEach ）。 不建议在执行翻页动画过程中增加或减少子组件，会导致未进行动画的子组件提前进入视窗，引起显示异常。




##### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcSwiper(controller?: ArcSwiperController)

创建弧形滑块视图容器。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | ArcSwiperController | 否 | 给组件绑定一个控制器，用来控制组件翻页。 |




##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性。



##### index

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

index(index: Optional&lt;number&gt;)

设置当前在容器中显示的子组件的索引值。设置小于0或大于等于子组件数量时，按照默认值0处理。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | Optional&lt;number&gt; | 是 | 当前在容器中显示的子组件的索引值。 当index值为undefined时，按取值为0处理。 |




##### indicator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

indicator(style: Optional<ArcDotIndicator | boolean>)

设置弧形圆点指示器样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<ArcDotIndicator \| boolean> | 是 | 弧形圆点指示器样式。 - ArcDotIndicator：弧形圆点指示器属性及功能。 - boolean：是否启用弧形圆点指示器。设置为true启用，false不启用。 默认值：true 默认类型：ArcDotIndicator |




##### duration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

duration(duration: Optional&lt;number&gt;)

设置子组件切换的动画时长。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | Optional&lt;number&gt; | 是 | 子组件切换的动画时长。 默认值：400 单位：毫秒 |




##### vertical

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

vertical(isVertical: Optional&lt;boolean&gt;)

设置是否为纵向滑动。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVertical | Optional&lt;boolean&gt; | 是 | 是否为纵向滑动。 true: 纵向滑动；false: 横向滑动。 默认值：false |




##### disableSwipe

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

disableSwipe(disabled: Optional&lt;boolean&gt;)

是否禁用组件滑动切换功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | Optional&lt;boolean&gt; | 是 | 是否禁用组件滑动切换功能。设置为true禁用，false不禁用。 默认值：false |




##### digitalCrownSensitivity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

digitalCrownSensitivity(sensitivity: Optional&lt;CrownSensitivity&gt;)

设置旋转表冠的灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | Optional&lt;CrownSensitivity&gt; | 是 | 旋转表冠的灵敏度。 默认值：CrownSensitivity.MEDIUM |




##### effectMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

effectMode(edgeEffect: Optional&lt;EdgeEffect&gt;)

设置边缘滑动效果。 目前支持的滑动效果参见[EdgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#edgeeffect)的枚举说明。调用控制器接口时回弹不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | Optional&lt;EdgeEffect&gt; | 是 | 边缘滑动效果。 默认值：EdgeEffect.Spring |




##### disableTransitionAnimation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

disableTransitionAnimation(disabled: Optional&lt;boolean&gt;)

是否关闭特殊动效效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | Optional&lt;boolean&gt; | 是 | 是否关闭特殊动效效果。 true：关闭特殊动效效果；false：不关闭特殊动效效果。 传入参数非法时，按false处理。 |




##### ArcSwiperController

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcSwiper容器组件的控制器，可以将此对象绑定至ArcSwiper组件，可以通过它控制翻页。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()

ArcSwiperController的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### showNext

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

showNext()

翻至下一页。翻页带动效切换过程，时长通过[duration](#duration)指定。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### showPrevious

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

showPrevious()

翻至上一页。翻页带动效切换过程，时长通过[duration](#duration)指定。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### finishAnimation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

finishAnimation(handler?: FinishAnimationHandler)

停止播放动画。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | FinishAnimationHandler | 否 | 动画结束的回调。 默认值：不传入的情况，无回调 |




##### ArcDotIndicator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供弧形圆点指示器属性及功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()

ArcDotIndicator的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### arcDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

arcDirection(direction: Optional&lt;ArcDirection&gt;): ArcDotIndicator

设置弧形指示器的方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | Optional&lt;ArcDirection&gt; | 是 | 设置弧形指示器的方向。 默认值：ArcDirection.SIX_CLOCK_DIRECTION，6点钟方向。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArcDotIndicator | 提供弧形圆点指示器属性及功能。 |




##### itemColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

itemColor(color: Optional&lt;ResourceColor&gt;): ArcDotIndicator

设置弧形指示器中，未选中导航点的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ResourceColor&gt; | 是 | 设置弧形指示器中，未选中导航点的颜色。 默认值：'#A9FFFFFF' |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArcDotIndicator | 提供弧形圆点指示器属性及功能。 |




##### selectedItemColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

selectedItemColor(color: Optional&lt;ResourceColor&gt;): ArcDotIndicator

设置弧形指示器中，选中导航点的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ResourceColor&gt; | 是 | 设置弧形指示器中，选中导航点的颜色。 默认值：'#FF5EA1FF' |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArcDotIndicator | 提供弧形圆点指示器属性及功能。 |




##### backgroundColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

backgroundColor(color: Optional&lt;ResourceColor&gt;): ArcDotIndicator

设置弧形指示器被长按时，弧形指示器的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;ResourceColor&gt; | 是 | 设置弧形指示器被长按时，弧形指示器的颜色。 默认值：'#FF404040' |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArcDotIndicator | 提供弧形圆点指示器属性及功能。 |




##### maskColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

maskColor(color: Optional&lt;LinearGradient&gt;): ArcDotIndicator

设置弧形指示器的遮罩渐变色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional&lt;LinearGradient&gt; | 是 | 设置弧形指示器的遮罩渐变色。 起始颜色默认值：'#00000000' 结束颜色默认值：'#FF000000' |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArcDotIndicator | 提供弧形圆点指示器属性及功能。 |




##### ArcDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

弧形方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| THREE_CLOCK_DIRECTION | 0 | 3点钟方向。 |
| SIX_CLOCK_DIRECTION | 1 | 6点钟方向。 |
| NINE_CLOCK_DIRECTION | 2 | 9点钟方向。 |




##### FinishAnimationHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type FinishAnimationHandler = () => void

停止播放动画时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### IndexChangedHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type IndexChangedHandler = (index: number) => void

当前显示元素的索引变化时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。index序列从0开始。 |




##### AnimationStartHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void

切换动画开始时的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引，动画开始前的index值（不是最终结束动画的index值）。 |
| targetIndex | number | 是 | 切换动画目标元素的索引。 |
| event | SwiperAnimationEvent | 是 | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对ArcSwiper起始位置的位移，以及离手速度。 |




##### AnimationEndHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void

切换动画结束时的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。 |
| event | SwiperAnimationEvent | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于ArcSwiper起始位置的位移。 |




##### GestureSwipeHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type GestureSwipeHandler = (index: number, event: SwiperAnimationEvent) => void

在页面跟手滑动过程中，逐帧触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。 |
| event | SwiperAnimationEvent | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于ArcSwiper起始位置的位移。 |




##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：



##### onChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onChange(handler: Optional&lt;IndexChangedHandler&gt;)

当前显示子组件的索引变化时触发该事件，返回值为当前显示子组件的索引值。

ArcSwiper组件结合[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)使用时，不能在onChange事件里触发子页面UI的刷新。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional&lt;IndexChangedHandler&gt; | 是 | 当前显示元素的索引回调。 |




##### onAnimationStart

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAnimationStart(handler: Optional&lt;AnimationStartHandler&gt;)

切换动画开始时触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional&lt;AnimationStartHandler&gt; | 是 | 切换动画开始时的回调。 |




##### onAnimationEnd

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAnimationEnd(handler: Optional&lt;AnimationEndHandler&gt;)

切换动画结束时触发该回调。

当ArcSwiper切换动效结束时触发，包括动画过程中手势中断，通过[SwiperController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#swipercontroller)调用finishAnimation。参数为动画结束后的index值，多列ArcSwiper时，index为最左侧组件的索引。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional&lt;AnimationEndHandler&gt; | 是 | 切换动画结束时触发该回调。 |




##### onGestureSwipe

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onGestureSwipe(handler: Optional&lt;GestureSwipeHandler&gt;)

在页面跟手滑动过程中，逐帧触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional&lt;GestureSwipeHandler&gt; | 是 | 在页面跟手滑动过程中，逐帧触发该回调。 |




##### customContentTransition

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

customContentTransition(transition: Optional&lt;SwiperContentAnimatedTransition&gt;)

自定义ArcSwiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调。开发者可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。

在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发[SwiperContentTransitionProxy](#swipercontenttransitionproxy)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | Optional&lt;SwiperContentAnimatedTransition&gt; | 是 | ArcSwiper自定义切换动画相关信息。 |




##### SwiperContentAnimatedTransition

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcSwiper自定义切换动画相关信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | ArcSwiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用SwiperContentTransitionProxy的finishTransition接口通知ArcSwiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即在该页面节点下渲染树。单位ms，默认值为0。 |
| transition | Callback&lt;SwiperContentTransitionProxy&gt; | 否 | 否 | 自定义切换动画具体内容。 |




##### SwiperContentTransitionProxy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcSwiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知ArcSwiper组件页面自定义动画已结束。

> [!NOTE]
> 假设当前选中的子组件的索引为0，从第0页切换到第1页的动画过程中，每帧都会对视窗内所有页面触发回调，当视窗内有第0页和第1页两页时，每帧会触发两次回调。其中第一次回调的selectedIndex为0，index为0，position为当前帧第0页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第0页的长度；第二次回调的selectedIndex仍为0，index为1，position为当前帧第1页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第1页的长度。 若动画曲线为弹簧插值曲线，从第0页切换到第1页的动画过程中，可能会因为离手时的位置和速度，先过滑到第2页，再回弹到第1页，该过程中每帧会对视窗内第1页和第2页触发回调。


**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### **属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedIndex | number | 否 | 否 | 当前选中页面的索引。 |
| index | number | 否 | 否 | 视窗内页面的索引。 |
| position | number | 否 | 否 | index页面相对于ArcSwiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |
| mainAxisLength | number | 否 | 否 | index对应页面在主轴方向上的长度。 |




##### finishTransition

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

finishTransition(): void

通知ArcSwiper组件，此页面的自定义动画已结束。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle



##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



##### 示例1（设置arcSwiper基本属性）

该示例通过设置arcSwiper的基本属性，展示了组件的基本功能。

```ArkTS
// xxx.ets
import {
  CircleShape,
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';
// 从API version 22开始，无需手动导入ArcSwiperAttribute。具体请参考ArcSwiper的导入模块说明

class MyDataSource implements IDataSource {
  private list: Color[] = [];

  constructor(list: Color[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): Color {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct TestNewInterface {
  @State itemSimpleColor: Color | number | string = '';
  @State selectedItemSimpleColor: Color | number | string = '';
  private wearableSwiperController: ArcSwiperController = new ArcSwiperController();
  private arcDotIndicator: ArcDotIndicator = new ArcDotIndicator();
  private data: MyDataSource = new MyDataSource([]);
  @State backgroundColors: Color[] =
    [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.White, Color.Gray, Color.Orange, Color.Transparent];
  innerSelectedIndex: number = 0;

  aboutToAppear(): void {
    let list: Color[] = [];
    for (let i = 1; i <= 6; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(this.backgroundColors);
  }

  build() {
    Column() {
      Row() {
        ArcSwiper(this.wearableSwiperController) {
          LazyForEach(this.data, (backgroundColor: Color, index: number) => {
            Text(index.toString())
              .width(233)
              .height(233)
              .backgroundColor(backgroundColor)
              .textAlign(TextAlign.Center)
              .fontSize(30)
          })
        }
        .clipShape(new CircleShape({ width: 233, height: 233 }))
        .effectMode(EdgeEffect.None)
        .backgroundColor(Color.Transparent)
        .index(0)
        .duration(400)
        .vertical(false)
        .indicator(this.arcDotIndicator
          .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION)
          .itemColor(this.itemSimpleColor)
          .selectedItemColor(this.selectedItemSimpleColor)
        )
        .disableSwipe(false)
        .digitalCrownSensitivity(CrownSensitivity.MEDIUM)
        .onChange((index: number) => {
          console.info("onChange:" + index.toString());
        })
        .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
          this.innerSelectedIndex = targetIndex;
          console.info("index: " + index);
          console.info("targetIndex: " + targetIndex);
          console.info("current offset: " + extraInfo.currentOffset);
          console.info("target offset: " + extraInfo.targetOffset);
          console.info("velocity: " + extraInfo.velocity);
        })
        .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
          others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
          if (current) {
            let target = current.getEventTargetInfo();
            if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
              // 此处判断swiperTarget.isBegin()或innerSelectedIndex === 0，表明ArcSwiper滑动到开头
              let swiperTarget = target as ScrollableTargetInfo
              if (swiperTarget instanceof ScrollableTargetInfo &&
                (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
                let panEvent = event as PanGestureEvent;
                if (panEvent && panEvent.offsetX > 0 && (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
                  return GestureJudgeResult.REJECT;
                }
              }
            }
          }
          return GestureJudgeResult.CONTINUE;
        })
        .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
          console.info("index: " + index);
          console.info("current offset: " + extraInfo.currentOffset);
        })
        .disableTransitionAnimation(false)
      }.height('100%')
    }.width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/LwGplpmeTIuluuw1Mzrekw/zh-cn_image_0000002581435776.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024216Z&HW-CC-Expire=86400&HW-CC-Sign=1E15E36C9E49CC42CAAF25623AF8EAD1DD6841CE10F19CA11C822082E658A338)




##### 示例2（设置ArcSwiper自定义页面切换动画）

该示例通过[customContentTransition](#customcontenttransition)接口，实现了自定义ArcSwiper页面切换动画。

```text
import { Decimal } from '@kit.ArkTS';
import { CircleShape, ArcSwiper, ArcSwiperAttribute } from '@kit.ArkUI';

// 从API version 22开始，无需手动导入ArcSwiperAttribute。具体请参考ArcSwiper的导入模块说明
@Entry
@Component
struct TestNewInterface {
  private backgroundColors: Color[] =
    [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.White, Color.Gray, Color.Orange];
  @State scaleList: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.scaleList.push(1.0);
    }
  }

  build() {
    Column() {
      Row() {
        ArcSwiper() {
          ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
            Text(index.toString())
              .width(233)
              .height(233)
              .backgroundColor(backgroundColor)
              .textAlign(TextAlign.Center)
              .fontSize(30)
              .scale({ x: this.scaleList[index], y: this.scaleList[index] })
          })
        }
        .clipShape(new CircleShape({ width: 233, height: 233 }))
        .effectMode(EdgeEffect.None)
        .onChange((index: number) => {
          console.info('onChange:' + index.toString());
        })
        .customContentTransition({
          // 页面移除视窗时超时1000ms下渲染树
          timeout: 1000,
          // 对视窗内所有页面逐帧回调transition，在回调中修改opacity属性值，实现自定义动画
          transition: (proxy: SwiperContentTransitionProxy) => {
            if (proxy.position <= -1 || proxy.position >= 1) {
              // 页面完全滑出视窗外时，重置属性值
              this.scaleList[proxy.index] = 1.0;
            } else {
              let position: number = Decimal.abs(proxy.position).toNumber();
              this.scaleList[proxy.index] = 1 - position;
            }
          }
        })
        .disableTransitionAnimation(false)
      }.height('100%')
    }.width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/TaZFRl9STd-_09EHe77xWg/zh-cn_image_0000002611835605.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024216Z&HW-CC-Expire=86400&HW-CC-Sign=01536CAF513A81A013F0F105EA94ED3EFE5C28104F7A8E1BE7BE2F7B459850DC)
