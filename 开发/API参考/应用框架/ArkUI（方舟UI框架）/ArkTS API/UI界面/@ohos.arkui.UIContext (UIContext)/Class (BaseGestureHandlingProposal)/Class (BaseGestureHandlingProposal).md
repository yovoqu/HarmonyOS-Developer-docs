# Class (BaseGestureHandlingProposal)

更新时间：2026-08-07 10:00:25

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-basegesturehandlingproposal
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势处理基类。当通过[registerMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller#registermonitor)接口动态自定义智慧手势行为时，其回调参数类型为具体的子类类型实例。
 
**起始版本：** 26.0.0
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | SmartGestureAction | 否 | 否 | 智慧手势最终执行动作。 |
| operateIntention | OperateIntention | 否 | 否 | 智慧手势底层操作意图。 |
 
 
**示例：**
 
本示例实现了在智慧手势监听回调中，从BaseGestureHandlingProposal获取智慧手势处理信息，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller#示例1启用智慧手势并自定义动作处理)。
 
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/KFKjzit9TMWZNa31gY8Nkg/zh-cn_image_0000002698142269.png?HW-CC-KV=V1&HW-CC-Date=20260811T010214Z&HW-CC-Expire=86400&HW-CC-Sign=3A03434F81932E8C34CAC45E60EAE205C688A1092A671ABC54FA8ED730D2C216)
