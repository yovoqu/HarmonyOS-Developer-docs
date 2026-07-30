# XComponent

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。同时支持AI图像分析、HDR视频亮度调节、防截屏录屏隐私保护、画布自绘制等能力，适用于视频播放、相机预览、游戏渲染、图像AI识别等需要高性能自绘制和媒体内容展示的场景。具体指南请参考[自定义渲染（XComponent）文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。

> [!NOTE]
> 该组件从API version 8 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无



#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### XComponent19+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

XComponent(params: NativeXComponentParameters)

在Native侧获取XComponent节点实例、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | NativeXComponentParameters | 是 | XComponent的配置参数，用于在Native侧获取XComponent节点实例并注册Surface生命周期回调和组件事件回调。 |




#### XComponent12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

XComponent(options: XComponentOptions)

创建XComponent组件，支持在ArkTS侧获取SurfaceId、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调，支持AI分析。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | XComponentOptions | 是 | XComponent的配置选项，用于在ArkTS侧获取SurfaceId、注册Surface生命周期回调和组件事件回调，以及配置AI分析功能。 |




#### XComponent10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})

创建XComponent组件，支持Native侧触发XComponent生命周期回调。

该接口从API version 12开始不再演进，推荐使用[XComponent(options: XComponentOptions)](#xcomponent12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，字符串长度不超过128个字符，超出时无效。 |
| type | XComponentType | 是 | 用于指定XComponent组件类型。 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅类型为SURFACE或TEXTURE时有效。未设置时不加载动态库。 |
| controller | XComponentController | 否 | 给组件绑定一个控制器，通过控制器调用组件方法（如获取SurfaceId、设置Surface显示区域等），仅类型为SURFACE或TEXTURE时有效。当需要在ArkTS侧控制XComponent行为时传入此参数；不传入时，无法通过控制器调用相关组件方法。 |




#### XComponent(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

XComponent(value: {id: string, type: string, libraryname?: string, controller?: XComponentController})

> [!NOTE]
> 从 API version 8开始支持，从API version 12开始废弃。建议使用 XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController}) 替代。


**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，字符串长度不超过128个字符，超出时无效。 |
| type | string | 是 | 用于指定XComponent组件类型，可选值仅有以下两种： -"surface"：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。 -"component"9+：XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。 其他值均会被视为"surface"类型 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅XComponent类型为"surface"时有效。未设置时不加载动态库。 |
| controller | XComponentController | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅XComponent类型为"surface"时有效。未设置时不绑定控制器。 |




#### XComponentOptions12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义XComponent的具体配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | XComponentType | 否 | 否 | 用于指定XComponent组件类型。 |
| controller | XComponentController | 否 | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。未设置时不绑定控制器。 |
| imageAIOptions | ImageAIOptions | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器，仅类型为SURFACE或TEXTURE时有效。未设置时不配置AI分析选项，可通过enableAnalyzer属性单独启用AI分析。 |




#### NativeXComponentParameters19+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义XComponent的具体配置参数。通过这种构造参数创建的XComponent，可以将其对应的[FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode)对象传递至Native侧，使用NDK接口进行Surface生命周期的相关设置和[添加事件监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-add-component-events)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | XComponentType | 否 | 否 | 用于指定XComponent组件类型。 |
| imageAIOptions | ImageAIOptions | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。未设置时不配置AI分析选项，仅类型为SURFACE或TEXTURE时有效。 |




#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持通用属性外，还支持以下属性：

> [!NOTE]
> 不支持foregroundColor、obscured和pixelStretchEffect属性。API version 17及之前，type为SURFACE类型时也不支持动态属性设置、自定义绘制、背景设置（backgroundColor除外）、图像效果（shadow除外）、maskShape和foregroundEffect属性。从API version 18开始，type为SURFACE类型时，不支持的动态属性包含：background、foregroundColor、animation、gesture、priorityGesture、parallelGesture、useEffect、renderGroup、flexGrow、direction、align、useSizeType、clip、geometryTransition、bindPopup、bindMenu、bindContextMenu、bindContentCover、bindSheet、stateStyles、restoreId、onVisibleAreaChange、accessibilityGroup、obscured、reuseId、accessibilityVirtualNode。 对于TEXTURE和SURFACE类型的XComponent组件，当不设置 renderFit 属性时，取默认值为RenderFit.RESIZE_FILL。 对于SURFACE类型的XComponent组件，其背景色默认为不透明的纯黑色。在API version 18之前，该组件的 renderFit 通用属性仅支持设置为RenderFit.RESIZE_FILL；在API version 18及之后，支持所有的RenderFit枚举值。 对于使用 ArkUI NDK接口 创建的XComponent组件，不支持使用属性获取函数 getAttribute 获取其renderFit属性值。




#### enableAnalyzer12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

本功能需要搭配XComponentController的[startImageAnalyzer](#startimageanalyzer12)和[stopImageAnalyzer](#stopimageanalyzer12)一起使用。

不能和[overlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay#overlay)属性同时使用，两者同时设置时overlay中[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)属性将失效。AI分析功能依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用AI分析功能。 true：开启AI分析；false：关闭AI分析。 默认值：false |


> [!NOTE]
> 仅type为SURFACE或TEXTURE时该功能有效。




#### enableSecure13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

enableSecure(isSecure: boolean)

防止组件内自绘制内容被截屏、录屏。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSecure | boolean | 是 | 是否开启隐私图层模式。 true：开启隐私图层模式；false：关闭隐私图层模式。 默认值：false |


> [!NOTE]
> 仅type为SURFACE时有效。 不支持 ArkUI NDK接口 创建的XComponent组件。




#### hdrBrightness20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

hdrBrightness(brightness: number)

用于调整组件播放HDR视频的亮度。

> [!NOTE]
> 仅XComponent构造参数中的type为 XComponentType .SURFACE时该接口生效，否则该接口不生效。 不支持 ArkUI NDK接口 创建的XComponent组件。


**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | HDR视频的亮度。 默认值：1.0 取值范围：[0.0, 1.0]。小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。 0.0表示视频按照SDR亮度显示，1.0表示视频按照当前允许的最高HDR亮度显示。 |




#### hdrBrightness24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

hdrBrightness(brightness: number, type?: HdrType)

用于调整组件显示HDR内容时的亮度。

当参数type设置为非[HdrType](#hdrtype24枚举说明).DEFAULT时，调用该接口前需先检查[Display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)的hdrFormats属性是否包含对应的[HDRFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hdrcapability#hdrformat)。

仅当hdrFormats包含对应的HDRFormat时，当前设备才支持对应的HDR类型，参数设置才会生效；否则将使用默认值[HdrType](#hdrtype24枚举说明).DEFAULT。

其映射关系如下：

| type取值 | hdrFormats需包含的HDRFormat |
| --- | --- |
| HdrType.AIHDR | HDRFormat.VIDEO_AIHDR |


> [!NOTE]
> 仅XComponent构造参数中的type为 XComponentType .SURFACE时该接口生效，否则该接口不生效。 不支持 ArkUI NDK接口 创建的XComponent组件。


**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | HDR内容的亮度。 默认值：1.0 取值范围：[0.0, 1.0]。小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。 0.0表示内容按照SDR亮度显示，1.0表示内容按照当前允许的最高HDR亮度显示。 |
| type | HdrType | 否 | 显示HDR内容时的HDR类型。 默认值：HdrType.DEFAULT |




#### HdrType24+枚举说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

HDR内容的高动态范围渲染类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认HDR类型，使用标准高动态范围渲染模式。 元服务API： 从API version 24开始，该接口支持在元服务中使用。 |
| AIHDR | 1 | AI HDR类型，使用AI算法对非HDR内容进行智能动态范围扩展，实现HDR的显示效果。 元服务API： 从API version 24开始，该接口支持在元服务中使用。 |




#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

从API version 12开始，type为SURFACE或TEXTURE时，支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

> [!NOTE]
> 当配置libraryname参数时， 点击事件 、 触摸事件 、 挂载卸载事件 、 按键事件 、 焦点事件 、 鼠标事件 仅响应C-API侧事件接口。


仅type为SURFACE或TEXTURE时以下事件有效：



#### onLoad

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onLoad(callback: OnNativeLoadCallback)

插件加载完成时回调事件。

> [!NOTE]
> 仅当XComponent设置了libraryname参数时，会触发该回调；当未设置libraryname参数时，请使用 onSurfaceCreated 等相关回调。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnNativeLoadCallback | 是 | 插件加载完成时回调事件，用于获取XComponent实例对象的context。 |




#### onDestroy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDestroy(event: VoidCallback)

插件卸载完成时回调事件。与[onSurfaceDestroyed](#onsurfacedestroyed12)的区别：onDestroy适用于设置libraryname参数的场景，回调无参数；onSurfaceDestroyed适用于未设置libraryname参数的场景，回调参数为surfaceId。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | 插件卸载完成时回调事件。 |




#### OnNativeLoadCallback18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type OnNativeLoadCallback = (event?: object) => void

XComponent的Native加载完成后回调事件，用于向开发者传递XComponent实例对象的context。与[onSurfaceCreated](#onsurfacecreated12)的区别：onLoad回调参数为context对象，适用于设置libraryname参数的场景；onSurfaceCreated回调参数为surfaceId，适用于未设置libraryname参数的场景。onLoad触发时机早于onSurfaceCreated。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | object | 否 | 获取XComponent实例对象的context，context上挂载的方法由开发者在Native层定义。不传该参数时无法获取context。当需要在回调中使用Native层定义的方法时传入此参数；不传入时，回调中无法获取context对象。 |




#### XComponentController

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

XComponent组件的控制器，可以将此对象绑定至XComponent组件，然后通过控制器来调用组件方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()

XComponentController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```text
xComponentController: XComponentController = new XComponentController();
```



#### getXComponentSurfaceId9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getXComponentSurfaceId(): string

获取XComponent对应Surface的ID，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | XComponent持有Surface的ID。 |


> [!NOTE]
> 使用自定义组件节点创建XComponent组件时，因为onLoad回调触发时机早于 onSurfaceCreated ，所以在onLoad回调中调用 getXComponentSurfaceId 获取surfaceId会失败，建议在 onSurfaceCreated 回调中获取。


**示例：**

```ArkTS
// xxx.ets

@Entry
  @Component
  struct Index {
    myXComponentController: XComponentController = new XComponentController();

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.myXComponentController
        })
          .onLoad(() => {
            let surfaceId: string = this.myXComponentController.getXComponentSurfaceId();
            console.info("XComponent SurfaceId: " + surfaceId);
          })
      }
    }
  }
```



#### setXComponentSurfaceSize(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setXComponentSurfaceSize(value: {surfaceWidth: number, surfaceHeight: number}): void

设置XComponent持有Surface的宽度和高度，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

> [!NOTE]
> 从 API version 9开始支持，从API version 12开始废弃。建议使用 setXComponentSurfaceRect 替代。


**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceWidth | number | 是 | XComponent持有Surface的宽度，取值范围为大于0且不超过8192，单位：px。传入0、负数或其他异常值时接口不生效。 |
| surfaceHeight | number | 是 | XComponent持有Surface的高度，取值范围为大于0且不超过8192，单位：px。传入0、负数或其他异常值时接口不生效。 |




#### getXComponentContext

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getXComponentContext(): Object

获取XComponent实例对象的context，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 获取XComponent实例对象的context，context包含的具体接口方法由开发者自定义，context内容与onLoad回调中的第一个参数一致。 |




#### setXComponentSurfaceRect12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setXComponentSurfaceRect(rect: SurfaceRect): void

设置XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | SurfaceRect | 是 | XComponent持有Surface的显示区域。 |


> [!NOTE]
> rect参数中的offsetX/offsetY不设置或传入异常值时，Surface显示区域相对于XComponent左上角x/y轴的偏移效果默认按照居中显示。 rect参数中的surfaceWidth和surfaceHeight存在0、负数或其他异常值时，调用该接口设置显示区域不生效。未调用该接口主动设置Surface显示区域时，surfaceWidth默认与组件宽度一致，surfaceHeight默认与组件高度一致。 该方法优先级高于 border 、 padding 等可以改变内容偏移和大小的属性。




#### getXComponentSurfaceRect12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getXComponentSurfaceRect(): SurfaceRect

获取XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SurfaceRect | 获取XComponent持有Surface的显示区域。 |




#### onSurfaceCreated12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onSurfaceCreated(surfaceId: string): void

当XComponent持有的Surface创建后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |


> [!NOTE]
> 仅当XComponent组件未设置libraryname参数时，会进行该回调。




#### onSurfaceChanged12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void

当XComponent持有的Surface大小改变后（包括首次创建时的大小改变）进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |
| rect | SurfaceRect | 是 | 回调该方法的时候，绑定XComponent持有Surface的显示区域。 |


> [!NOTE]
> 仅当XComponent组件未设置libraryname参数时，会进行该回调。




#### onSurfaceDestroyed12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onSurfaceDestroyed(surfaceId: string): void

当XComponent持有的Surface销毁后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效，具体可以参考指南[创建XComponent和管理Surface生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines#创建xcomponent和管理surface生命周期)章节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |


> [!NOTE]
> 仅当XComponent组件未设置libraryname参数时，会进行该回调。




#### startImageAnalyzer12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

startImageAnalyzer(config: ImageAnalyzerConfig): Promise&lt;void&gt;

配置AI分析并启动AI分析功能，使用前需先启用图像AI分析能力[enableAnalyzer](#enableanalyzer12)，仅type为SURFACE或TEXTURE时有效。使用Promise异步回调。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

若该方法尚未执行完毕，此时重复调用，则会触发错误回调。

> [!NOTE]
> 分析类型不支持动态修改。 AI分析功能依赖设备能力，不支持该能力的情况下，将返回错误码。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | ImageAnalyzerConfig | 是 | 执行AI分析所需要的入参，用于配置AI分析功能。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。用于获取AI分析是否成功执行。 |


**错误码：**

以下错误码的详细介绍请参见[图像AI分析错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer)。

| 错误码ID | 错误信息 |
| --- | --- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |




#### stopImageAnalyzer12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。仅type为SURFACE或TEXTURE时有效。

> [!NOTE]
> 在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。 该特性依赖设备能力。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### setXComponentSurfaceRotation12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void

设置XComponent持有Surface在屏幕旋转时是否锁定方向，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationOptions | SurfaceRotationOptions | 是 | 设置XComponent持有Surface在屏幕旋转时是否锁定方向。 |


> [!NOTE]
> rotationOptions未配置时，默认XComponent持有Surface在屏幕旋转时不锁定方向，跟随屏幕进行旋转。 仅在屏幕旋转过程中生效，旋转完成后不再锁定Surface。 仅在屏幕旋转90°，即发生横竖屏切换时生效。 锁定旋转后的Buffer宽高需要保持不变，否则会有拉伸问题。




#### getXComponentSurfaceRotation12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getXComponentSurfaceRotation(): Required&lt;SurfaceRotationOptions&gt;

获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Required&lt;SurfaceRotationOptions&gt; | 获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置。 |




#### lockCanvas20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lockCanvas(): DrawingCanvas | null

返回可用于向XComponent上绘制内容的画布对象。具体绘制方法请参考[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DrawingCanvas \| null | 可用于向XComponent区域绘制的画布对象或者空对象null。 |


> [!NOTE]
> 如果当前XComponent状态无法获取画布对象则将返回null。原因通常为： XComponent持有的Surface未创建完成（可通过设置 onLoad / onSurfaceCreated 回调来确定，此回调触发时，Surface已创建完成）。 之前已经调用过lockCanvas来获取过画布对象，且该画布对象未调用 unlockCanvasAndPost 去释放。 只支持TEXTURE和SURFACE模式。 使用此接口后，同时在NDK侧获取NativeWindow并调用NDK绘制接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。 此接口需要和 unlockCanvasAndPost 接口配对使用，具体参考示例3 使用画布对象在XComponent上绘制内容 。




#### unlockCanvasAndPost20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unlockCanvasAndPost(canvas: DrawingCanvas): void

将画布对象中的内容绘制在XComponent区域，并释放该画布对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | DrawingCanvas | 是 | 之前调用lockCanvas方法返回的画布对象。 |


> [!NOTE]
> 画布对象调用unlockCanvasAndPost释放后，不可再使用该画布对象。 只支持TEXTURE和SURFACE模式。 使用此接口后，同时在NDK侧获取NativeWindow并调用相关接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。 此接口需要和 lockCanvas 接口配对使用，具体参考示例3 使用画布对象在XComponent上绘制内容 。




#### setXComponentSurfaceConfig22+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setXComponentSurfaceConfig(config: SurfaceConfig): void

设置XComponent创建的Surface的选项，用于设置XComponent持有的Surface在渲染时是否需要被视为不透明。当Surface绘制内容完全不透明时，可设置为不透明以提升渲染性能；当绘制内容包含透明区域时，需保持非不透明以保证透明效果正确显示。

> [!NOTE]
> 仅当XComponent组件类型为TEXTURE或SURFACE时，本接口生效。


**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | SurfaceConfig | 是 | Surface配置选项，用于设置XComponent持有的Surface在渲染时是否需要被视为不透明。 |




#### SurfaceRotationOptions12+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于描述XComponent持有Surface在屏幕旋转时是否锁定方向的设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lock | boolean | 否 | 是 | Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。 true：锁定方向；false：不锁定方向。 |




#### SurfaceRect12+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于描述XComponent持有Surface的显示区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offsetX | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。未设置时默认按照居中显示。 |
| offsetY | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。未设置时默认按照居中显示。 |
| surfaceWidth | number | 否 | 否 | Surface显示区域的宽度，单位：px。 |
| surfaceHeight | number | 否 | 否 | Surface显示区域的高度，单位：px。 |


> [!NOTE]
> surfaceWidth和surfaceHeight属性在未调用 setXComponentSurfaceRect 也未设置 border 和 padding 等属性时，其取值大小为XComponent组件的大小。 surfaceWidth和surfaceHeight属性的取值都不可超过8192px，否则会导致渲染异常。 沉浸式场景下，默认布局的SurfaceRect不包括安全区，需调用 setXComponentSurfaceRect 接口主动设置Surface显示区域达到沉浸式效果。




#### SurfaceConfig22+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于描述XComponent持有的Surface在渲染时是否需要被视为不透明。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOpaque | boolean | 否 | 是 | XComponent持有的Surface在渲染时是否需要被视为不透明，未设置时默认取值为false，即在渲染时会应用Surface中绘制内容像素的透明度。 true表示需要被视为不透明，false表示不需要被视为不透明。 默认值：false |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。



#### 示例1（图像AI分析功能）

使用enableAnalyzer属性开启图像AI分析功能。可通过XComponentController控制开始、停止图像AI分析。

> [!NOTE]
> 本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考 ArkTS XComponent示例


```ArkTS
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import nativeRender from 'libnativerender.so'; // 开发者自己实现的so，详见上述说明。

class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct XComponentExample {
  xComponentController: XComponentController = new CustomXComponentController();
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  };
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  };
  @State xcWidth: string = "720px";
  @State xcHeight: string = "720px";
  @State currentStatus: string = "index";

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('Native XComponent Sample')
          .fontSize('24fp')
          .fontWeight(500)
          .margin({
            left: 24,
            top: 12
          })
      }
      .margin({ top: 24 })
      .width('100%')
      .height(56)

      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController,
        imageAIOptions: this.options
      })
        .width(this.xcWidth)
        .height(this.xcHeight)
        .enableAnalyzer(true)
        .onClick(() => {
          let surfaceId = this.xComponentController.getXComponentSurfaceId();
          nativeRender.ChangeColor(BigInt(surfaceId));
          let hasChangeColor: boolean = false;
          if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
            hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
          }
          if (hasChangeColor) {
            this.currentStatus = "change color";
          }
        })
      Text(this.currentStatus)
        .fontSize('24fp')
        .fontWeight(500)
      Column() {
        Button('start AI analyze')
          .onClick(() => {
            this.xComponentController.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete");
              })
              .catch((error: BusinessError) => {
                console.error(`Failed to start image analyzer. Code: ${error.code}, message: ${error.message}`);
              })
          })
          .margin(2)
        Button('stop AI analyze')
          .onClick(() => {
            this.xComponentController.stopImageAnalyzer();
          })
          .margin(2)
        Button('get analyzer types')
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes();
          })
          .margin(2)
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            console.info(`surface rect is ${this.xComponentController.getXComponentSurfaceRect()}`);
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .margin(2)
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%")
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/vuqOa19hSpWUp6LqORpQ0w/zh-cn_image_0000002686088331.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071512Z&HW-CC-Expire=86400&HW-CC-Sign=594108765393F5056A7F4ED6CAA2A1D04AD33C9545B0E2B272673EF1D69A868F)




#### 示例2（在Surface旋转过程中锁定）

通过setXComponentSurfaceRotation设置Surface在屏幕旋转过程中锁定方向，不跟随屏幕进行旋转。

> [!NOTE]
> 本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考 ArkTS XComponent示例 。


```ArkTS
// xxx.ets
import nativeRender from 'libnativerender.so';

class MyXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State isLock: boolean = true;
  @State xcWidth: number = 500;
  @State xcHeight: number = 700;
  myXComponentController: XComponentController = new MyXComponentController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
      XComponent({
        id: "XComponent",
        type: XComponentType.SURFACE,
        controller: this.myXComponentController
      })
        .onLoad(() => {
          let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };
          this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation);
          console.info("Surface getXComponentSurfaceRotation lock = " +
          this.myXComponentController.getXComponentSurfaceRotation().lock);
        })
        .width(this.xcWidth)
        .height(this.xcHeight)
      Button("Draw")
        .onClick(() => {
          let surfaceId = this.myXComponentController.getXComponentSurfaceId();
          nativeRender.DrawPattern(BigInt(surfaceId));
        })
    }
  }
}
```



#### 示例3（使用画布对象在XComponent上绘制内容）

从API version 20开始，该示例通过调用[lockCanvas](#lockcanvas20)返回画布对象，通过画布对象调用对应的绘制接口，再调用[unlockCanvasAndPost](#unlockcanvasandpost20)在XComponent上绘制内容。

```ArkTS
// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("80%")
        .height("80%")
        .onLoad(() => {
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 240, 250, 255); // 每次绘制前必须完全重绘整个XComponent区域，可以调用此方法实现
            const brush = new drawing.Brush(); // 创建画刷对象
            brush.setColor({ // 设置画刷的颜色
              alpha: 255,
              red: 39,
              green: 135,
              blue: 217
            });
            this.mCanvas.attachBrush(brush); // 绑定画刷到画布上
            this.mCanvas.drawRect({ // 绘制一个矩形
              left: 300,
              right: 800,
              top: 100,
              bottom: 800
            });
            this.mCanvas.detachBrush(); // 将画刷与画布解绑
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Ch45b0VWSc-otGfPn7sHfA/zh-cn_image_0000002685928499.png?HW-CC-KV=V1&HW-CC-Date=20260730T071512Z&HW-CC-Expire=86400&HW-CC-Sign=43ADEB4C035EDB5EADA40BEAFCC3B7AF74F0CB0949ACB3D5307C7E06587769FD)




#### 示例4（XComponent实现沉浸式效果）

从API version 20开始，在示例3的基础上，调用setXComponentSurfaceRect接口主动设置Surface显示区域达到沉浸式效果。

```ArkTS
// xxx.ets
import { display } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;
  @State screenWidth: number = 0;
  @State screenHeight:number = 0;
  aboutToAppear() {
    try {
      const displayClass = display.getDefaultDisplaySync();
      this.screenWidth = displayClass.width;
      this.screenHeight = displayClass.height;
    } catch (error) {
      console.error(`Failed to get default display. Code: ${error.code}, message: ${error.message}`);
    }
  }

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("100%")
        .height("100%")
        .onLoad(() => {
          // 请在此处设置Surface大小，过大可能会导致绘制时间长
          this.xcController.setXComponentSurfaceRect({surfaceWidth: this.screenWidth, surfaceHeight: this.screenHeight, offsetX: 0, offsetY: 0});
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 39, 135, 217); // 每次绘制前必须完全重绘整个XComponent区域，可以调用此方法实现
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .height('100%')
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/fgO_VZY5TfitTf8_k_jpIA/zh-cn_image_0000002656008822.jpeg?HW-CC-KV=V1&HW-CC-Date=20260730T071512Z&HW-CC-Expire=86400&HW-CC-Sign=44DF1255E7ACE8C4E77EF905E4C52149CF4AA31D4FC8AC9C002C32E67BEE29DA)




#### 示例5（设置XComponent持有Surface在渲染时是否需要被视为不透明）

从API version 22开始，该示例通过调用[setXComponentSurfaceConfig](#setxcomponentsurfaceconfig22)接口设置XComponent持有的Surface在渲染时是否需要被视为不透明。

> [!NOTE]
> 本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考 ArkTS XComponent示例 。


```ArkTS
// xxx.ets
import nativeRender from 'libnativerender.so'; // 开发者自己实现的so，详见上述说明。

// 重写XComponentController，设置生命周期回调
class MyXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }
  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
    // 在onSurfaceChanged中调用ChangeSurface绘制内容
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }
  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State currentStatus: string = "index";
  xComponentController: XComponentController = new MyXComponentController();

  aboutToAppear(): void {
    // 设置XComponent持有的Surface在渲染时被视为不透明
    this.xComponentController.setXComponentSurfaceConfig({ isOpaque: true });
  }

  build() {
    Column() {
      Column({ space: 10 }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .backgroundColor(Color.Transparent)
        Text(this.currentStatus)
          .fontSize('24fp')
          .fontWeight(500)
      }
      .onClick(() => {
        let surfaceId = this.xComponentController.getXComponentSurfaceId();
        nativeRender.ChangeColor(BigInt(surfaceId));
        let hasChangeColor: boolean = false;
        if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
          hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
        }
        if (hasChangeColor) {
          this.currentStatus = "change color";
        }
      })
      .margin({
        top: 27,
        left: 12,
        right: 12
      })
      .height('40%')
      .width('90%')
      Row() {
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .margin({ bottom: 24 })
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .width('53.6%')
          .height(40)
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-fSF5olMRImbSHgumNhVKg/zh-cn_image_0000002655848902.jpeg?HW-CC-KV=V1&HW-CC-Date=20260730T071512Z&HW-CC-Expire=86400&HW-CC-Sign=B502534D29ABFC7F92031BE26E832A9D93C396305511799985EB1C23F8A29718)
