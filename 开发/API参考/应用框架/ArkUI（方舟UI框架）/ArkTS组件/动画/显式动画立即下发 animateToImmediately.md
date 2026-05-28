# 显式动画立即下发 (animateToImmediately)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

animateToImmediately接口用来提供[显式动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)立即下发功能。同时加载多个属性动画的情况下，使用该接口可以立即执行闭包代码中状态变化导致的过渡动效。
 
与[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)相比，animateToImmediately能即时将生成的动画指令发送至渲染层执行，无需等待vsync信号，从而在视觉效果上实现部分动画的优先呈现。当应用的主线程存在耗时操作，且需提前更新部分用户界面时，此接口可有效缩短应用的响应延迟。需要注意的是，animateToImmediately仅支持渲染层上的属性动画提前执行，无法用于UI侧的逐帧动画。
 
此外，该接口会将调用前的状态和新生成的动画一并发送至渲染层，因此渲染结果可能会基于调用时的状态进行。务必确保调用时的状态完整，否则前几帧可能出现渲染异常。
 
因此，建议开发者优先使用[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)，以防止干扰框架的显示时序，避免在动画启动时因状态设置不完整而导致的显示错误。
 
> [!NOTE]
> 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

##### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### animateToImmediately

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

animateToImmediately(value: AnimateParam , event: () => void): void
 
提供显式动画立即下发功能。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | AnimateParam | 是 | 设置动画效果相关参数。 |
| event | () => void | 是 | 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |
 
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该示例主要演示通过[animateToImmediately](#animatetoimmediately)接口来实现显式动画立即下发。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct AnimateToImmediatelyExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State opacitySize: number = 0;
  private flag: boolean = true;

  build() {
    Column() {
      Column()
      .width(this.widthSize)
      .height(this.heightSize)
      .backgroundColor(Color.Green)
      .opacity(this.opacitySize)
      Button('change size')
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.opacitySize = 1;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.widthSize = 150;
              this.heightSize = 60;
            })
          } else {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.widthSize = 250;
              this.heightSize = 100;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.opacitySize = 0;
            })
          }
          this.flag = !this.flag;
        })
    }.width('100%').margin({ top: 5 })
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Ic2aexr9SXa6nv2_ZMPmLg/zh-cn_image_0000002581436170.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024159Z&HW-CC-Expire=86400&HW-CC-Sign=D11C111B717D41F567CF9CF515FD3730F125F881373362695FC0A03FD473F32B)
