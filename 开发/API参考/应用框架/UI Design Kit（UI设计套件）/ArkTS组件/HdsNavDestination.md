# HdsNavDestination

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination
**支持设备：** Phone / PC/2in1 / Tablet / TV

作为子页面的根容器，用于显示[HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)的内容区，默认支持标题栏随内容区滚动的动态模糊样式。6.0.0(20)版本以后，推荐使用[bindToScrollable](#bindtoscrollable)、[bindToNestedScrollable](#bindtonestedscrollable)属性绑定导航组件和可滚动容器组件后，再使用导航组件滚动相关的功能，从而获得更优的体验。如滚动生效动态模糊样式，标题栏随内容区滚动动态显隐功能等。

**起始版本：** 5.1.0(18)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / TV


6.0.1(21)及之前版本：


```ts
import {
  HdsNavDestination,
  HdsNavDestinationAttribute,
} from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：


```ts
import { HdsNavDestination } from '@kit.UIDesignKit';
```


## 子组件
**支持设备：** Phone / PC/2in1 / Tablet / TV


- 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)和[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)）。
- 子组件个数：多个。


## 接口
**支持设备：** Phone / PC/2in1 / Tablet / TV

HdsNavDestination()

创建[HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)子页面的根容器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / TV

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

不推荐设置位置、大小等布局相关属性，可能会造成页面显示异常。


### titleBar
**支持设备：** Phone / PC/2in1 / Tablet / TV

titleBar(options?: HdsNavigationTitleBarOptions)

设置HdsNavDestination组件titleBar区域（包括返回图标区域、标题区域、菜单区域、背景板）样式以及内容。

标题字符串超长时，如果不设置副标题，先缩小再换行（2行）最后以"..."截断。如果设置副标题，先缩小后以"..."截断。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdsNavigationTitleBarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#hdsnavigationtitlebaroptions) | 否 | 标题栏配置信息。 |


### hideTitleBar
**支持设备：** Phone / PC/2in1 / Tablet / TV

hideTitleBar(hide: boolean, animated?: boolean)

设置是否隐藏标题栏，并且可设置在标题栏显示隐藏的状态变化中是否使用动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏标题栏。 默认值：false。 - true：隐藏标题栏。 - false：显示标题栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐标题栏。 默认值：false。 - true：使用动画显示隐藏标题栏。 - false：不使用动画显示隐藏标题栏。 |


### hideBackButton
**支持设备：** Phone / PC/2in1 / Tablet / TV

hideBackButton(value: boolean)

设置是否隐藏标题栏中的返回键。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏中的返回键。 默认值：false。 - true：隐藏返回键。 - false：显示返回键。 |


### mode
**支持设备：** Phone / PC/2in1 / Tablet / TV

mode(value: NavDestinationMode)

设置HdsNavDestination类型，不支持动态修改。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavDestinationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationmode枚举说明11) | 是 | HdsNavDestination类型。 默认值：NavDestinationMode.STANDARD。 |


### toolbarConfiguration
**支持设备：** Phone / PC/2in1 / Tablet / TV

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。未调用本接口时不显示工具栏。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolbarParam | Array&lt;[ToolbarItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#toolbaritem10)&gt; \| [CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8) | 是 | 工具栏内容。 使用Array&lt;[ToolbarItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#toolbaritem10)&gt;写法设置的工具栏有如下特性： - 如果为[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationmode9枚举说明)模式，不推荐使用该写法。推荐使用[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)配合[ToolBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbar)组件写法，避免布局显示问题。 - 工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。 - 文本超长时，若工具栏选项个数小于5个，优先拓展选项的宽度，最大宽度与屏幕等宽，其次逐级缩小，缩小之后换行，最后截断。 - 最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。 使用[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)写法为用户自定义工具栏选项，除均分底部工具栏外不具备以上功能。 |
| options | [NavigationToolbarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationtoolbaroptions11) | 否 | 工具栏选项。 |


> [!NOTE]
> 不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。


### hideToolBar
**支持设备：** Phone / PC/2in1 / Tablet / TV

hideToolBar(hide: boolean, animated?: boolean)

设置是否隐藏工具栏，并且可设置在工具栏显示隐藏的状态变化中是否使用动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏工具栏。 默认值：false。 - true：隐藏工具栏。 - false：显示工具栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐工具栏。 默认值：false。 - true：使用动画显示隐藏工具栏。 - false：不使用动画显示隐藏工具栏。 |


### ignoreLayoutSafeArea
**支持设备：** Phone / PC/2in1 / Tablet / TV

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

控制组件的布局，使其扩展到非安全区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array &lt;[LayoutSafeAreaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#layoutsafeareatype12)&gt; | 否 | 配置扩展安全区域的类型。 默认值：[LayoutSafeAreaType.SYSTEM]。 |
| edges | Array &lt;[LayoutSafeAreaEdge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#layoutsafeareaedge12)&gt; | 否 | 配置扩展安全区域的方向。 默认值：[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |


> [!NOTE]
> 组件设置LayoutSafeArea之后生效的条件为：
> 设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。
> 例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。
> 若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。


### systemBarStyle
**支持设备：** Phone / PC/2in1 / Tablet / TV

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

当HdsNavigation中显示当前HdsNavDestination时，设置对应系统状态栏的样式。若未与HdsNavigation配合使用，systemBarStyle属性可能不会生效，建议开发者在使用前确保已正确配置HdsNavigation组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalStyle | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)&lt;[SystemBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#systembarstyle12)&gt; | 是 | 系统状态栏初始样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |
| scrollEffectStyle | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)&lt;[SystemBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#systembarstyle12)&gt; | 是 | HdsNavDestination动态样式生效后，系统状态栏对应的最终动态样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |


说明：


1. 必须配合HdsNavigation使用，作为其HdsNavigation目的页面的根节点时才能生效。
2. 其他使用限制请参考HdsNavigation对应的[systemBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#systembarstyle)属性说明。


### recoverable
**支持设备：** Phone / PC/2in1 / Tablet / TV

recoverable(recoverable: Optional<boolean>)

配置HdsNavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该HdsNavDestination。该功能需HdsNavDestination对应的HdsNavigation也配置了可恢复属性使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)&lt;boolean&gt; | 是 | HdsNavDestination是否可恢复，默认为不可恢复。 默认值：false。 - true：页面栈可恢复。 - false：页面栈不可恢复。 |


### dynamicHideTitleBar
**支持设备：** Phone / PC/2in1 / Tablet / TV

dynamicHideTitleBar(value: DynamicHideParams)

设置标题栏跟随内容区动态显隐配置，推荐搭配[bindToScrollable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#bindtoscrollable)/[bindToNestedScrollable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#bindtonestedscrollable)体验更佳的滑动效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DynamicHideParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#dynamichideparams) | 是 | 标题栏跟随内容区滚动动态显隐配置。 当配置了标题栏动态显隐时，不支持配置标题栏模式动态切换。 当标题栏模式为HdsNavDestinationTitleMode.MODAL时该接口设置无效。 不支持在显隐过程中动态切换属性。 |


### bindToScrollable
**支持设备：** Phone / PC/2in1 / Tablet / TV

bindToScrollable(scrollers: Array<Scroller>)

绑定导航组件和可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array&lt;[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)&gt; | 是 | 可滚动容器组件的控制器。 |


### bindToNestedScrollable
**支持设备：** Phone / PC/2in1 / Tablet / TV

bindToNestedScrollable(scrollers: Array<NestedScrollInfo>)

绑定导航组件和嵌套的可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array&lt;[NestedScrollInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#nestedscrollinfo)&gt; | 是 | 嵌套的可滚动容器组件的控制器。 |


> [!NOTE]
> 当多个可滚动容器组件绑定了同一个导航组件时，滚动任何一个容器都会触发标题栏显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏显示动效。
> 因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。


### systemTransition
**支持设备：** Phone / PC/2in1 / Tablet / TV

systemTransition(type: NavigationSystemTransitionType)

设置HdsNavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NavigationSystemTransitionType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navigationsystemtransitiontype14枚举说明) | 是 | 系统转场动画类型。 默认值：NavigationSystemTransitionType.DEFAULT。 |


### customTransition
**支持设备：** Phone / PC/2in1 / Tablet / TV

customTransition(delegate: NavDestinationTransitionDelegate)

设置HdsNavDestination自定义转场动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationtransitiondelegate15) | 是 | HdsNavDestination自定义动画的代理函数。 |


### titleMode
**支持设备：** Phone / PC/2in1 / Tablet / TV

titleMode(value: HdsNavDestinationTitleMode)

设置页面标题栏显示模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HdsNavDestinationTitleMode](#hdsnavdestinationtitlemode) | 是 | 页面标题栏显示模式。默认值：HdsNavDestinationTitleMode.MINI。 |


### withTheme
**支持设备：** Phone / PC/2in1 / Tablet / TV

withTheme(value: WithThemeOptions)

设置HdsNavDestination的[WithTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme)能力。使用本功能时，需确保HdsNavDestination组件与对应的[HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)组件配置的[WithTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme)属性保持一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WithThemeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#withthemeoptions) | 是 | WithTheme能力配置信息。 |


## 事件
**支持设备：** Phone / PC/2in1 / Tablet / TV


### onShown
**支持设备：** Phone / PC/2in1 / Tablet / TV

onShown(callback: Callback<void>)

当显示HdsNavDestination页面时，触发onShown回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination页面显示时触发的回调。 |


### onShown
**支持设备：** Phone / PC/2in1 / Tablet / TV

onShown(callback: Callback<VisibilityChangeReason>)

当显示HdsNavDestination页面时，触发onShown回调。通过[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)说明触发的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)&gt; | 是 | 当该HdsNavDestination页面显示时触发的回调。回调会提供入参VisibilityChangeReason以说明onShown触发的原因。 |


### onHidden
**支持设备：** Phone / PC/2in1 / Tablet / TV

onHidden(callback: Callback<void>)

当隐藏HdsNavDestination页面时，触发onHidden回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination页面隐藏时触发的回调。 |


### onHidden
**支持设备：** Phone / PC/2in1 / Tablet / TV

onHidden(callback: Callback<VisibilityChangeReason>)

当隐藏HdsNavDestination页面时，触发onHidden回调。通过[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)说明触发的原因。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.1.0(23)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)&gt; | 是 | 当该HdsNavDestination页面隐藏时触发的回调。回调会提供入参VisibilityChangeReason以说明onHidden触发的原因。 |


### onReady
**支持设备：** Phone / PC/2in1 / Tablet / TV

onReady(callback: Callback<NavDestinationContext>)

当HdsNavDestination即将构建子组件之前会触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;[NavDestinationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationcontext11)&gt; | 是 | 当该HdsNavDestination即将构建子组件之前会触发的回调。 |


### onWillAppear
**支持设备：** Phone / PC/2in1 / Tablet / TV

onWillAppear(callback: Callback<void>)

当该HdsNavDestination挂载之前触发此回调。在该回调中允许修改页面栈，当前帧生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination挂载之前触发的回调。 |


### onWillDisappear
**支持设备：** Phone / PC/2in1 / Tablet / TV

onWillDisappear(callback: Callback<void>)

当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。 |


### onWillShow
**支持设备：** Phone / PC/2in1 / Tablet / TV

onWillShow(callback: Callback<void>)

当该HdsNavDestination显示之前触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination显示之前触发的回调。 |


### onWillHide
**支持设备：** Phone / PC/2in1 / Tablet / TV

onWillHide(callback: Callback<void>)

当该HdsNavDestination隐藏之前触发此回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 5.1.0(18)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void&gt; | 是 | 当该HdsNavDestination隐藏之前触发的回调。 |


### onBackPressed
**支持设备：** Phone / PC/2in1 / Tablet / TV

onBackPressed(callback: Callback<void, boolean>)

当与HdsNavigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该回调。

返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。不推荐同时设置返回键自定义事件与onBackPressed回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;void, boolean&gt; | 是 | 当与HdsNavigation绑定的页面栈中存在内容时，并且点击返回键时，触发的回调。 |


### onActive
**支持设备：** Phone / PC/2in1 / Tablet / TV

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。

**模型约束：** 此接口仅可在Stage��型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.1(21)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)&lt;[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;[NavDestinationActiveReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationactivereason17)&gt;&gt; | 是 | HdsNavDestination由非激活态变为激活态的原因。 |


### onInactive
**支持设备：** Phone / PC/2in1 / Tablet / TV

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.1(21)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)&lt;[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)&lt;[NavDestinationActiveReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationactivereason17)&gt;&gt; | 是 | HdsNavDestination由激活态变为非激活态的原因。 |


## HdsNavDestinationTitleMode
**支持设备：** Phone / PC/2in1 / Tablet / TV

标题栏显示模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 名称 | 值 | 说明 |
| --- | --- | --- |
| MINI | 100 | 固定为小标题模式。标题栏高度为56vp。 |
| MODAL | 101 | 固定为半模态模式。背板高度64vp，标题栏高度为56vp，上padding为8vp。 |


## 示例
**支持设备：** Phone / PC/2in1 / Tablet / TV

通过titleBar属性，自定义设置标题栏随内容区滚动的动态模糊样式。


```ts
// 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
import { HdsNavDestination, HdsNavDestinationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';

const TITLE_BAR_HEIGHT_MINI: number = 56;

@Entry
@Component
struct PageOne {
  scroller: Scroller = new Scroller();

  build() {
    HdsNavDestination() {
      Scroll(this.scroller) {
        Column() {
          Blank().height(TITLE_BAR_HEIGHT_MINI)
          Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
        }
      }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
    }
    .titleBar({
      padding: {
        start: LengthMetrics.vp(2),
        end: LengthMetrics.vp(2)
      },
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR,
          blurEffectiveStartOffset: LengthMetrics.vp(0),
          blurEffectiveEndOffset: LengthMetrics.vp(20)
        },
        originalStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: {
              backgroundColor: $r('sys.color.comp_background_tertiary'),
              iconColor: $r('sys.color.icon_primary')
            },
            backIconStyle: {
              backgroundColor: $r('sys.color.comp_background_tertiary'),
              iconColor: $r('sys.color.icon_primary')
            }
          }
        },
        scrollEffectStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: {
              backgroundColor: $r('sys.color.comp_background_tertiary'),
              iconColor: $r('sys.color.icon_primary')
            },
            backIconStyle: {
              backgroundColor: $r('sys.color.comp_background_tertiary'),
              iconColor: $r('sys.color.icon_primary')
            }
          }
        }
      },
      content: {
        title: {
          mainTitle: "PageOne",
        },
        menu: {
          value: [{
            content: {
              label: 'menu1',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu1");
              }
            }
          }, {
            content: {
              label: 'menu2',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu2");
              }
            }
          }]
        },
      }
    })
    .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
    .hideBackButton(false)
  }
}
```

![](assets/HdsNavDestination/file-20260514164459789-0.gif)

HdsNavDestination更多示例可以参考HdsNavigation[示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#示例)。
