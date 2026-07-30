# NodeController

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

NodeController用于管理自定义节点的创建、显示、更新等操作，并负责将自定义节点挂载到[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)上，适用于需要在页面中动态创建、更新、复用自定义节点的场景。

> [!NOTE]
> 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。 NodeController对象不支持使用JSON序列化。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { NodeController } from '@kit.ArkUI';
```



#### NodeController

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

通常搭配[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)使用。用于创建控制器，管理绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)组件。一个NodeController只允许与一个[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)进行绑定。最佳实践请参考组件动态创建-[组件动态添加、更新和删除](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-component-dynamic-creation#组件动态添加更新和删除)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### makeNode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

abstract makeNode(uiContext : UIContext): FrameNode | null

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)创建时触发此回调。回调方法将返回一个节点，该节点将被挂载至[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)。

或者可以通过NodeController的rebuild()方法触发回调。

> [!NOTE]
> NodeContainer 不支持跨实例复用。如果出现跨实例复用 NodeContainer ，传入 NodeContainer 的 NodeController 触发 makeNode 回调方法时，入参中的 UIContext 对象可能为undefined，此时需要开发者判断该对象是否为undefined，防止后续使用此入参时出现 UIContext无效的JS异常 。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | UIContext | 是 | 回调该方法时，绑定NodeContainer的UI上下文。跨实例复用NodeContainer时，该参数可能为undefined，需要开发者自行判断。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| FrameNode \| null | 一个FrameNode对象，返回的节点将被挂载至NodeContainer的占位节点上。若返回null对象，将清空对应NodeContainer的子节点。 |




#### aboutToAppear

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

aboutToAppear?(): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)挂载显示后触发此回调。

> [!NOTE]
> 回调时机参考 onAppear 。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### aboutToDisappear

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

aboutToDisappear?(): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)销毁时触发此回调。

> [!NOTE]
> 回调时机参考 onDisAppear 。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### onAttach18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAttach?(): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)挂载至主节点树时触发此回调。与[aboutToAppear](#abouttoappear)不同，aboutToAppear在NodeContainer挂载显示后触发，onAttach在NodeContainer挂载至主节点树时触发，两者触发时机可能不同。

> [!NOTE]
> 回调时机参考 onAttach 。


**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### onDetach18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDetach?(): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)从主节点树卸载时触发此回调。与[aboutToDisappear](#abouttodisappear)不同，aboutToDisappear在NodeContainer销毁时触发，onDetach在NodeContainer从主节点树卸载时触发，两者触发时机可能不同。

> [!NOTE]
> 回调时机参考 onDetach 。


**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### onWillBind18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onWillBind?(containerId: number): void

当NodeController与[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)即将绑定前触发此回调。该回调先于[onBind](#onbind18)触发，两者均为可选回调，可根据需要在绑定前或绑定后执行相应逻辑。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，即将与NodeController绑定的NodeContainer的标识。 |




#### onWillUnbind18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onWillUnbind?(containerId: number): void

当NodeController与[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)即将解绑前触发此回调。该回调先于[onUnbind](#onunbind18)触发，两者均为可选回调，可根据需要在解绑前或解绑后执行相应逻辑。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，即将与NodeController解绑的NodeContainer的标识。 |




#### onBind18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onBind?(containerId: number): void

当NodeController与[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)绑定后触发此回调。该回调后于[onWillBind](#onwillbind18)触发，两者均为可选回调，可根据需要在绑定前或绑定后执行相应逻辑。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，已完成与NodeController绑定的NodeContainer的标识。 |




#### onUnbind18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onUnbind?(containerId: number): void

当NodeController与[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)解绑后触发此回调。该回调后于[onWillUnbind](#onwillunbind18)触发，两者均为可选回调，可根据需要在解绑前或解绑后执行相应逻辑。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| containerId | number | 是 | 回调该方法时，已完成与NodeController解绑的NodeContainer的标识。 |




#### aboutToResize

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

aboutToResize?(size: Size): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)布局时触发此回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | Size | 是 | 组件布局大小的宽和高，单位为vp。 |




#### onTouchEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onTouchEvent?(event: TouchEvent): void

当NodeController绑定的[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)收到触摸事件时触发此回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | TouchEvent | 是 | 触摸事件，包含触摸点的坐标、触摸动作类型等信息，具体结构详见TouchEvent。 |




#### rebuild

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rebuild(): void

调用此接口通知[NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)组件重新回调[makeNode](#makenode)方法，更改子节点。例如，当NodeContainer展示的内容数据发生变化、需要更新显示的子节点时，可调用此方法触发重新构建。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

> [!NOTE]
> 由于rebuild方法为应用主动调用的方法，且该操作与UI相关，需要开发者自行保证调用该接口时UI上下文有效，即与绑定的NodeContainer保持UI上下文一致。 监听回调等 UI上下文不明确 时，可以通过 UIContext 的 runScopedTask 方法明确调用时的UI上下文。




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（添加节点布局、Touch、挂载和销毁时的生命周期回调）

该示例通过aboutToResize、onTouchEvent，实现了NodeContainer节点布局、收到Touch事件时的生命周期回调功能。

并通过aboutToAppear、aboutToDisappear接口，实现了NodeContainer节点挂载、销毁时的生命周期回调功能。

该示例还通过NodeController挂载BuilderNode节点。

```text
import { NodeController, BuilderNode, Size, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = 'this is a text';
}

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(12)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Orange)
  }
}

class MyNodeController extends NodeController {
  private buttonNode: BuilderNode<[Params]> | null = null;
  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode {
    if (this.buttonNode == null) {
      this.buttonNode = new BuilderNode(uiContext);
      this.buttonNode.build(this.wrapBuilder, { text: 'This is a Button' });
    }
    return this.buttonNode!.getFrameNode()!;
  }

  aboutToResize(size: Size) {
    console.info(`aboutToResize width : ${size.width} height : ${size.height}`);
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    this.buttonNode?.dispose();
    console.info('aboutToDisappear');
  }

  onTouchEvent(event: TouchEvent) {
    console.info('onTouchEvent');
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
    }
    .padding({ left: 35, right: 35, top: 35 })
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/APDo9QSGQ0uVf1wmfXSzaA/zh-cn_image_0000002686087737.jpg?HW-CC-KV=V1&HW-CC-Date=20260730T071448Z&HW-CC-Expire=86400&HW-CC-Sign=776242045A4F9004D1358ACED97908F776CC495D9AEFF5B3B2F292099F2ABA8C)




#### 示例2（添加节点上下树和绑定解绑前后的生命周期回调）

该示例通过onAttach、onDetach接口，实现了NodeContainer节点上下主节点树的生命周期回调功能。

并通过onWillBind、onWillUnbind、onBind、onUnbind接口，实现了NodeContainer节点绑定和解绑前后的生命周期回调功能。

```text
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = 'this is a text';
}

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(20)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Grey)
  }
}

class MyNodeController extends NodeController {
  private buttonNode: BuilderNode<[Params]> | null = null;
  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode {
    if (this.buttonNode == null) {
      this.buttonNode = new BuilderNode(uiContext);
      this.buttonNode.build(this.wrapBuilder, { text: 'This is a Button' });
    }
    return this.buttonNode!.getFrameNode()!;
  }

  onAttach(): void {
    console.info('myButton on attach');
  }

  onDetach(): void {
    console.info('myButton on detach');
  }

  onWillBind(containerId: number): void {
    console.info(`myButton on WillBind${containerId}`);
  }

  onWillUnbind(containerId: number): void {
    console.info(`myButton on WillUnbind${containerId}`);
  }

  onBind(containerId: number): void {
    console.info(`myButton on bind: ${containerId}`);
  }

  onUnbind(containerId: number): void {
    console.info(`myButton on unbind: ${containerId}`);
  }

  aboutToDisappear() {
    this.buttonNode?.dispose();
  }
}

@Entry
@Component
struct Index {
  @State buttonShow: boolean = true;
  @State buttonIndex: number = 0;
  private buttonController: MyNodeController = new MyNodeController();
  private buttonNull: null = null;
  private buttonControllerArray: Array<MyNodeController | null> = [this.buttonController, this.buttonNull];

  build() {
    Column() {
      Row() {
        Button('Bind/Unbind')
          .onClick(() => {
            this.buttonIndex++;
          }).margin(5)
        Button('onAttach/onDetach')
          .onClick(() => {
            this.buttonShow = !this.buttonShow;
          }).margin(5)
      }

      if (this.buttonShow) {
        NodeContainer(this.buttonControllerArray[this.buttonIndex % this.buttonControllerArray.length])
      }
    }
    .padding({ left: 35, right: 35 })
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/u0s57jV-RhGkJNUwDH0cDQ/zh-cn_image_0000002685927909.jpg?HW-CC-KV=V1&HW-CC-Date=20260730T071448Z&HW-CC-Expire=86400&HW-CC-Sign=54EB579C01B953E671DCD9FE102414CA72BA94B73CB83518007D1E38093D863E)
