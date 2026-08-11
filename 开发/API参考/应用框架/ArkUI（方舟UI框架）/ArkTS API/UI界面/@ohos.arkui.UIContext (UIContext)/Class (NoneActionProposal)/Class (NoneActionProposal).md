# Class (NoneActionProposal)

更新时间：2026-08-07 10:00:25

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-noneactionproposal
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

智慧手势空动作处理。当通过[registerMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller#registermonitor)接口动态自定义智慧手势行为时，设置返回值[Class (GestureHandlingResolution)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-gesturehandlingresolution)的selectedProposal为该类型对象，不会触发任何动作。
 
**起始版本：** 26.0.0
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
智慧手势空动作处理的构造函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势空动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller#示例1启用智慧手势并自定义动作处理)。
 
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/cshytunwRLyJ6t6_c3x4Ng/zh-cn_image_0000002698142271.png?HW-CC-KV=V1&HW-CC-Date=20260811T010216Z&HW-CC-Expire=86400&HW-CC-Sign=0971C76956E67FD4F7667C3F2DB9B389D46FD4850126DEA3F415DD5EBF1A865A)
