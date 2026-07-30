# Class (SmartGestureController)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供智慧手势使能、监听、选中态控制，以及动态决策智慧手势行为的能力，适用于应用接入智慧手势、监听系统默认手势处理意图并自定义手势响应行为的场景，可帮助应用灵活控制智慧手势交互流程。
 
> [!NOTE]
> 以下API需先使用UIContext中的 getSmartGestureController() 方法获取SmartGestureController实例，再通过该实例调用对应方法。

 
**起始版本：** 26.0.0
  

#### enableSmartTapAndSlideGestures

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

enableSmartTapAndSlideGestures(enabled: boolean): void
 
设置是否启用智慧手势的敲一敲和划一划操作。
 
> [!NOTE]
> 该接口仅影响智慧手势的敲一敲和划一划手势，不影响翻腕手势。 关闭后，组件侧 smartGestureShortcut 配置仍会保留，但不会响应智慧手势的敲一敲和划一划手势。

 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用智慧手势的敲一敲和划一划手势处理。true表示启用，false表示关闭。 |
 
 
**示例：**
 
本示例通过enableSmartTapAndSlideGestures接口实现了启用和关闭智慧手势，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
  }

  aboutToDisappear(): void {
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iMYWUIEfR_ajVko6OoRKxQ/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=37FE4681B57E8103A1F5F31994F5813EA6C0DB52668B30F71A85C327A48B0C9B)

 
  

#### registerMonitor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
 
注册智慧手势监听回调。在系统处理当前智慧手势前，应用可接收当前手势的默认动作处理并进行自定义干预。使用callback异步回调。
 
> [!NOTE]
> 该接口使应用能够在系统处理当前智慧手势事件前接收其处理意图，并进行自定义干预。 应用可通过该回调自定义决策本次智慧手势的行为。 应用可注册多个监听回调，按照后注册先执行的顺序触发，当某个监听回调消费智慧手势事件后，即返回值 GestureHandlingResolution .isConsumed为true时，后续监听回调不再执行。 当应用重复注册相同回调时，只会保存首次注册的回调，重复注册不生效。 回调返回值必须是合法的 GestureHandlingResolution 实例，否则本次改写不生效。

 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorCallback | Callback<BaseGestureHandlingProposal, GestureHandlingResolution> | 是 | 智慧手势监听回调。回调参数为系统给出的默认动作处理，返回值用于声明是否消费当前智慧手势以及是否替换默认动作处理。 |
 
 
**示例：**
 
本示例通过registerMonitor接口实现了注册智慧手势监听回调，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    // 消费当前智慧手势并沿用系统默认动作处理。
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.unregisterMonitor(this.smartGestureMonitor);
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/aogOxD-8Rvq_xe7jlaGfaQ/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=ABB9536D6BD1F1C6E89BE589E4C52DE2259C14372F2794D7BC66F2FF69AF8CEB)

 
  

#### unregisterMonitor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
 
注销智慧手势监听回调。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorCallback | Callback<BaseGestureHandlingProposal, GestureHandlingResolution> | 是 | 需要注销的智慧手势监听回调。 |
 
 
**示例：**
 
本示例通过unregisterMonitor接口实现了注销智慧手势监听回调，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.unregisterMonitor(this.smartGestureMonitor);
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/BAzIYUtCTRiiKgqJnsR_zA/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=0522C4AB9AE221E6597BAB70631E5232FFC0912EEF20176927D267767E928E54)

 
  

#### clearMonitors

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

clearMonitors(): void
 
清空当前UIContext下注册的全部智慧手势监听回调。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
本示例通过clearMonitors接口实现了清空智慧手势监听回调，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/w5d7kthvTO6B9kF943cuoA/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=FA7A4CDEE7E8DE1831D39CB74FAEDA8E841F5D5CE00A4E1037F14A6E4A64E84E)

 
  

#### requestSelected

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

requestSelected(id: string): void
 
请求将指定组件设置为当前智慧手势选中节点。成功选中后会显示选中提示框，选中框样式根据设备有所不同。
 
> [!NOTE]
> 仅当目标组件满足以下全部条件时，请求才会生效：组件可以响应智慧手势，组件在屏幕内可见，且组件绑定了 onClick 或绑定了单击手势 TapGesture 。 组件能否响应智慧手势由 smartGestureShortcut 中的enabled决定。

 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的id，该id对应的目标组件需满足：可以响应智慧手势、在屏幕内可见，且组件绑定了onClick或绑定了单击手势TapGesture。 |
 
 
**示例：**
 
本示例通过requestSelected接口和clearSelected接口实现了请求组件选中并在5000ms后自动清除选中，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
  }

  aboutToDisappear(): void {
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Button('请求选中')
          .onClick(() => {
            this.controller.requestSelected('target_text');
            setTimeout(() => {
              this.controller.clearSelected();
              console.info('smartGesture selected is clear');
            }, 5000);
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qsexQx-zTOykvvGm4Dt6pw/zh-cn_image_0000002656008180.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=E200113AFF29BBE61A329723C5E24DCC208F6D52A66E92A2C8A36BBBC690391F)

 
  

#### clearSelected

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

clearSelected(): void
 
清空当前智慧手势选中节点。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
本示例通过requestSelected接口和clearSelected接口实现了请求组件选中并在5000ms后自动清除选中，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
  }

  aboutToDisappear(): void {
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Button('请求选中')
          .onClick(() => {
            this.controller.requestSelected('target_text');
            setTimeout(() => {
              this.controller.clearSelected();
              console.info('smartGesture selected is clear');
            }, 5000);
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/YfMQ5W6ZQk6CWX2S4lTRQQ/zh-cn_image_0000002656008180.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=557360A528D57C39A26B916058063B3EEF1DD45894EAE48497914C5D55AE3129)

 
  

#### BaseGestureHandlingProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势处理基类。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，其回调参数类型为具体的子类类型实例。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | SmartGestureAction | 否 | 否 | 智慧手势最终执行动作。 |
| operateIntention | OperateIntention | 否 | 否 | 智慧手势底层操作意图。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，从BaseGestureHandlingProposal获取智慧手势处理信息，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal, GestureHandlingResolution,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    console.info('smartGesture action is ', proposal.action, ', operateIntention is ', proposal.operateIntention);
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/5OFf-1WDQ0Kv6vPsE5F6SA/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=57B96D381F20D7A9BE927AD3F28091053308AD8FA8DE5CD2C3A12A0478919F38)

 
  

#### TargetedGestureProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

带目标节点的智慧手势处理基类。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| node | FrameNode | 否 | 否 | 处理当前智慧手势的目标节点。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，从TargetedGestureProposal获取智慧手势处理信息，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  TargetedGestureProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let targetProposal = proposal as TargetedGestureProposal;
    console.info('smartGesture action is', targetProposal.action, ', operateIntention is',
      targetProposal.operateIntention, ', nodeId is', targetProposal.node.getId());
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/2aL9CbfMSkCHk97XZSwzpg/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=1E1A6B824723ED8EE4C3EAD4745AFF333A506203B8E9F2FE394756D20C9F37E5)

 
  

#### ClickActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势点击动作处理。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，会触发目标组件的点击操作。
 
> [!NOTE]
> 该动作处理遵循“先选中，再点击”的处理语义。 当目标节点尚未被选中时，本次处理会优先建立选中态，而不会立即触发点击。

 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(node: FrameNode)
 
智慧手势点击动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | FrameNode | 是 | 响应点击动作的目标节点。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势点击动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  ClickActionProposal,
  GestureHandlingResolution,
  TargetedGestureProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let targetProposal = proposal as TargetedGestureProposal;
    // 消费当前智慧手势，后续通过selectedProposal改写默认动作处理。
    let result = new GestureHandlingResolution(true);
    console.info('smartGesture action is', targetProposal.action, ', operateIntention is',
      targetProposal.operateIntention, ', nodeId is', targetProposal.node.getId());
    if (targetProposal.node && targetProposal.node.getId() == 'target_text') {
      let clickProposal = new ClickActionProposal(targetProposal.node);
      result.selectedProposal = clickProposal;
    }
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/A5DL3b0TTbuXEIxY5P5qjg/zh-cn_image_0000002685927859.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=1724AF07A6A70A6D6FB4A652257F9A054DCBA076975CAB762C717455EB710C9F)

 
  

#### SelectActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势选中动作处理。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，会使目标组件被选中。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(node: FrameNode)
 
智慧手势选中动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | FrameNode | 是 | 响应选中动作的目标节点。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势选中动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  SelectActionProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let node = this.getUIContext().getFrameNodeById('target_text2');
    if (node) {
      let selectProposal = new SelectActionProposal(node);
      result.selectedProposal = selectProposal;
    }
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件1')
          .id('target_text1')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Text('文本组件2')
          .id('target_text2')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/rgvQuPCiRt6rA5uKYcuLdg/zh-cn_image_0000002655848260.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=28D01C2677FF431C7367515F859A8BADE1F67F73D15D25AB588F6CD121B1C165)

 
  

#### NoneActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势空动作处理。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，不会触发任何动作。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
智慧手势空动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势空动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  NoneActionProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let noneProposal = new NoneActionProposal();
    result.selectedProposal = noneProposal;
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件1')
          .id('target_text1')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Text('文本组件2')
          .id('target_text2')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/DAhg4w7vTB67GGCE8Du_Qw/zh-cn_image_0000002686087689.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=CE64EECA5C3BEDF259A06F22CABB3AA6917E3C91C6E920529067128E28A1259C)

 
  

#### BackPressActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势返回动作处理。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，会返回上一页面。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
智慧手势返回动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势返回动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BackPressActionProposal,
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let backProposal = new BackPressActionProposal();
    result.selectedProposal = backProposal;
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件1')
          .id('target_text1')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Text('文本组件2')
          .id('target_text2')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/JH7XLAcpSCCkLQ8sFHS52Q/zh-cn_image_0000002686087689.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=7F371C6DE7DE1804B67DA0D155A8AF3E18B4C8D337C137E8EC11B2492B99EE6D)

 
  

#### PageSwitchActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势翻页动作处理，默认方向为向前翻页，包括向右和向下。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，会触发目标组件的翻页操作。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(node: FrameNode, pageCount: number)
 
智慧手势翻页动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | FrameNode | 是 | 响应翻页动作的目标节点。 |
| pageCount | number | 是 | 翻页数量。 取值范围：[0, +∞)，小于0时按0处理。 单位为页。 |
 
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pageCount | number | 否 | 否 | 智慧手势翻页数量。 取值范围：[0, +∞)，小于0时按0处理。 单位为页。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势翻页动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  PageSwitchActionProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let node = this.getUIContext().getFrameNodeById('target_swiper');
    if (node) {
      let pageSwitchProposal = new PageSwitchActionProposal(node, 2);
      result.selectedProposal = pageSwitchProposal;
    }
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Swiper() {
          Column({ space: 8 }) {
            Text('page 0')
          }
          .justifyContent(FlexAlign.Start)
          .padding(12)

          Column({ space: 8 }) {
            Text('page 1')
          }
          .justifyContent(FlexAlign.Start)
          .padding(12)

          Column({ space: 8 }) {
            Text('page 2')
          }
          .justifyContent(FlexAlign.Start)
          .padding(12)
        }
        .width(180)
        .height(180)
        .id('target_swiper')
        .index(0)
        .loop(false)
        .borderRadius(12)
        .borderWidth(1)
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/5tHWKSw-Tk6I5sBmV8NW9w/zh-cn_image_0000002685927861.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=78BDFBF0B7CBFC3F979FDC652BF23C7A409EAA7863A85E03651F74E4089ADC68)

 
  

#### ScrollActionProposal

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势滚动动作处理，默认方向为向前滚动，包括向右和向下。当通过[registerMonitor](#registermonitor)接口动态自定义智慧手势行为时，设置返回值[GestureHandlingResolution](#gesturehandlingresolution)的selectedProposal为该类型对象，会触发目标组件的滚动操作。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(node: FrameNode, distance: number)
 
智慧手势滚动动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | FrameNode | 是 | 响应滚动动作的目标节点。 |
| distance | number | 是 | 滚动距离。 取值范围：[0, +∞)，小于0时按0处理。 单位为vp。 |
 
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 否 | 是 | 智慧手势滚动距离。 取值范围：[0, +∞)，小于0时按0处理。 单位为vp。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势滚动动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](#示例1启用智慧手势并自定义动作处理)。
 
```text
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  ScrollActionProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private arrayList = [0, 1, 2, 3, 4, 5, 6];
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let node = this.getUIContext().getFrameNodeById('target_list');
    if (node) {
      let scrollProposal = new ScrollActionProposal(node, 60);
      result.selectedProposal = scrollProposal;
    }
    return result;
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        List({ space: 8 }) {
          ForEach(this.arrayList, (item: number) => {
            ListItem() {
              Column({ space: 6 }) {
                Text(`inner list item ${item}`)
                  .id(`inner_list_item_${item}`)
                  .fontSize(14)
                  .padding(8)
                  .width('100%')
                  .borderRadius(10)
                  .borderWidth(1)
                  .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
                  .onClick(() => {
                    console.info('smartGesture click is triggered');
                  })
              }
              .width('100%')
            }
          }, (item: number) => item.toString())
        }
        .id('target_list')
        .width('100%')
        .height(80)
        .borderRadius(12)
        .borderWidth(1)
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/SsTXGM2uQHGreUngIz8JzA/zh-cn_image_0000002656008182.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=55C8C2477BF8215DDBBD8E25C963972BCEE3B206696D3DFBCA05A38042E5684C)

 
  

#### GestureHandlingResolution

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势处理结果声明类。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(isConsumed: boolean)
 
智慧手势处理结果的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isConsumed | boolean | 是 | 是否消费当前智慧手势。 true表示消费当前智慧手势，此时如果未设置selectedProposal沿用系统默认动作处理，设置了selectedProposal以自定义动作处理。 false表示不消费，系统将本次智慧手势视为未处理。 |
 
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isConsumed | boolean | 否 | 否 | 是否消费当前智慧手势。 true表示消费当前智慧手势，此时如果未设置selectedProposal沿用系统默认动作处理，设置了selectedProposal以自定义动作处理。 false表示不消费，系统将本次智慧手势视为未处理。 |
| selectedProposal | BaseGestureHandlingProposal | 否 | 是 | 用户指定的智慧手势处理行为。 当isConsumed为true时，如果未设置selectedProposal沿用系统默认动作处理，设置了selectedProposal以自定义动作处理。 当isConsumed为false时，selectedProposal设置不生效。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 示例1（启用智慧手势并自定义动作处理）

以下示例通过[enableSmartTapAndSlideGestures](#enablesmarttapandslidegestures)接口启用、关闭智慧手势，通过[registerMonitor](#registermonitor)、[unregisterMonitor](#unregistermonitor)、[clearMonitors](#clearmonitors)接口注册、注销或清空监听回调实现自定义动作处理，以及通过[requestSelected](#requestselected)选中组件。
 
从API版本26.0.0开始，新增enableSmartTapAndSlideGestures、registerMonitor、unregisterMonitor、clearMonitors、requestSelected、clearSelected。
 
```text
import {
  BackPressActionProposal,
  BaseGestureHandlingProposal,
  ClickActionProposal,
  GestureHandlingResolution,
  NoneActionProposal,
  PageSwitchActionProposal,
  ScrollActionProposal,
  SelectActionProposal
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  @State clickCount: number = 0;
  @State hint: string = '';
  // 自定义监听回调函数
  private callback = (proposal: BaseGestureHandlingProposal): GestureHandlingResolution => {
    // proposal.operateIntention表示底层操作意图，取值包括TAP/SLIDE_FORWARD/BACK_PRESS
    // proposal.action表示最终执行动作，取值包括NONE/SELECT/CLICK/PAGE_FORWARD/SCROLL_FORWARD/BACK_PRESS
    this.hint = `意图=${proposal.operateIntention}, 动作=${proposal.action}`;

    // 消费当前智慧手势，后续根据proposal.action改写默认动作处理。
    const resolution = new GestureHandlingResolution(true);

    // 覆盖为点击动作
    if (proposal.action === SmartGestureAction.CLICK) {
      const node = this.getUIContext().getFrameNodeById('target_button');
      if (node) {
        resolution.selectedProposal = new ClickActionProposal(node);
      }
    } else if (proposal.action === SmartGestureAction.SELECT) { // 覆盖为选中动作
      const node = this.getUIContext().getFrameNodeById('target_text');
      if (node) {
        resolution.selectedProposal = new SelectActionProposal(node);
      }
    } else if (proposal.action === SmartGestureAction.PAGE_FORWARD) { // 覆盖为翻页动作
      const node = this.getUIContext().getFrameNodeById('scroll_area');
      if (node) {
        // pageCount：取值为[0, +∞)，单位为页
        resolution.selectedProposal = new PageSwitchActionProposal(node, 1);
      }
    } else if (proposal.action === SmartGestureAction.SCROLL_FORWARD) { // 覆盖为滚动动作
      const node = this.getUIContext().getFrameNodeById('scroll_area');
      if (node) {
        // distance：取值为[0, +∞)，单位为vp
        resolution.selectedProposal = new ScrollActionProposal(node, 180);
      }
    } else if (proposal.action === SmartGestureAction.NONE) { // 覆盖为空动作（不执行任何操作）
      resolution.selectedProposal = new NoneActionProposal();
    } else if (proposal.action === SmartGestureAction.BACK_PRESS) { // 覆盖为返回动作
      resolution.selectedProposal = new BackPressActionProposal();
    }

    return resolution;
  };

  build() {
    Scroll() {
      Column({ space: 12 }) {
        // 操作意图提示
        Text(this.hint).fontSize(13).fontColor('#666')

        // 目标节点：文本
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })

        // 目标节点：按钮
        Button(`按钮组件 / 点击=${this.clickCount}`)
          .id('target_button').width('100%')
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            this.clickCount += 1;
          })

        // 目标节点：滚动区域
        Scroll() {
          Column({ space: 6 }) {
            ForEach([0, 1, 2, 3], (item: number) => {
              Text(`滚动内容 ${item}`).width('100%').padding(10).borderRadius(8)
                .backgroundColor(item % 2 === 0 ? '#f6f8fa' : '#ffffff')
            })
          }.width('100%')
        }
        .id('scroll_area').height(120)

        Divider()

        // requestSelected/clearSelected
        Text('选中控制').fontWeight(FontWeight.Bold).fontSize(16)
        Row({ space: 8 }) {
          Button('选中按钮').layoutWeight(1)
            .onClick(() => this.controller.requestSelected('target_button'))
          Button('选中文本').layoutWeight(1)
            .onClick(() => this.controller.requestSelected('target_text'))
          Button('清空选中').layoutWeight(1)
            .onClick(() => this.controller.clearSelected())
        }.width('100%')

        // registerMonitor/unregisterMonitor/clearMonitors
        Text('Monitor 控制').fontWeight(FontWeight.Bold).fontSize(16)
        Row({ space: 8 }) {
          Button('注册').layoutWeight(1)
            .onClick(() => this.controller.registerMonitor(this.callback))
          Button('注销').layoutWeight(1)
            .onClick(() => this.controller.unregisterMonitor(this.callback))
          Button('清空').layoutWeight(1)
            .onClick(() => this.controller.clearMonitors())
        }.width('100%')

        // enableSmartTapAndSlideGestures
        Row({ space: 8 }) {
          Button('启用手势').layoutWeight(1)
            .onClick(() => this.controller.enableSmartTapAndSlideGestures(true))
          Button('禁用手势').layoutWeight(1)
            .onClick(() => this.controller.enableSmartTapAndSlideGestures(false))
        }.width('100%')
      }.width('100%')
    }
    .layoutWeight(1)
    .onAppear(() => {
      this.controller.enableSmartTapAndSlideGestures(true);
      this.controller.registerMonitor(this.callback);
    })
    .width('100%')
    .height('100%')
    .padding(12)
    .backgroundColor('#f1f3f5')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/culJQtwQSoqUxvAof7hZLg/zh-cn_image_0000002655848262.png?HW-CC-KV=V1&HW-CC-Date=20260730T072217Z&HW-CC-Expire=86400&HW-CC-Sign=BDACC26C7E44E5B8D1D7C5125A8DB61269B7FB97BC7FE190B1FFC99B58154F4E)
