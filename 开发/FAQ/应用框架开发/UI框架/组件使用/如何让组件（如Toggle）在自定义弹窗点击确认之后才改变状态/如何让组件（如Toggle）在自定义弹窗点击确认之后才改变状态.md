# 如何让组件（如Toggle）在自定义弹窗点击确认之后才改变状态

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1231

#### 问题现象

使用组件（如Toggle），点击后出现弹窗，如何在弹窗点击确认之后才改变组件（如Toggle）状态，点确认之前组件（Toggle）状态不变。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/pRp7Q8H9TQ2L0X5ujK85pg/zh-cn_image_0000002628753942.png?HW-CC-KV=V1&HW-CC-Date=20260730T072347Z&HW-CC-Expire=86400&HW-CC-Sign=26BB19CDA284BD0B92AB0CF22BA93E656D72648C42BE8CACF8C1A0311B402277)

 
 

#### 背景知识

- 组件可以使用[自定义事件拦截](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-touch-intercept)，开发者可根据事件在控件上按下时发生的位置，输入源等事件信息决定控件上的[HitTestMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#hittestmode9)属性。
- [CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog)自定义弹出框，使用@CustomDialog装饰器装饰，可在此装饰器内自定义弹出框内容、属性及回调。通过[CustomDialogController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontroller)类显示弹窗。

 
 

#### 解决方案

给组件（如Toggle）绑定自定义拦截事件，在该拦截事件中执行弹窗逻辑，并在弹窗确认和取消事件中变更组件（如Toggle）状态。
 
```text
@Entry
@Component
struct CustomDialogUser1 {
  @State isToggleOn: boolean = false;
 <em> // 创建自定义弹窗控制器对象</em>
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample1({
      confirm: () => {
        this.onAccept();
      },
      reject: () => {
        this.reject();
      }
    })
  });

  onAccept() {
   <em> // 弹窗中点击确定执行的操作</em>
    this.isToggleOn = !this.isToggleOn;
  }

  reject() {
   <em> // 弹窗中点击取消执行的操作</em>
  }

  build() {
    Column() {
      Toggle({ type: ToggleType.Switch, isOn: this.isToggleOn })
   <em>   // 调用onTouchIntercept修改该组件的HitTestMode属性</em>
        .onTouchIntercept(() => {
          this.dialogController.open();
          return HitTestMode.None;
        })
        .onChange((isOn: boolean) => {
          console.info(`isOn:${isOn}`);
          if (isOn) {
        <em>    // 需要执行的操作</em>
          }
        })
        .margin({ top: 16 })
    }
    .height('100%')
    .width('100%')
  }
}

<em>// </em><em>自定义弹窗</em>
@CustomDialog
struct CustomDialogExample1 {
  controller?: CustomDialogController;
  confirm?: () => void;
  reject?: () => void;

  build() {
    Column({ space: 32 }) {
      Text('确认执行此操作？').fontSize(24)
      Row() {
        Button('取消')
          .onClick(() => {
            this.controller?.close();
            if (this.reject) {
              this.reject();
            }
          })
        Button('确认')
          .onClick(() => {
            this.controller?.close();
            if (this.confirm) {
              this.confirm();
            }
          })
      }
      .padding({ left: 32, right: 32 })
      .width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
    }
    .padding({ top: 32, bottom: 32 })
  }
}
```
