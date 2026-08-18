# Progress如何控制平滑过渡的速率

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1557

#### 问题现象

如何通过Progress实现进度条功能，且可以控制其过渡速率？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gSA19RF3S1OxzC_mac2BSQ/zh-cn_image_0000002658968451.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005748Z&HW-CC-Expire=86400&HW-CC-Sign=2A9B9CB499089D4F75C10043F1EEDE87D9AC41C0B49FA0BB809C1B62923D3D9C)

 
 

#### 背景知识

- [Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)：进度条组件，用于显示内容加载或操作处理等进度，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress#style8)属性可以设置进度条样式。[CommonProgressStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress#commonprogressstyleoptions10)（进度条通用样式设置）对象中enableSmoothEffect参数可以开启/关闭进度条的平滑动效。
- [animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)：指定由于闭包代码导致的状态变化插入过渡动效。

 
 

#### 解决方案

为实现进度条功能，可通过修改Progress的value值来实现，若要实现控制其过渡速率可将Progress的enableSmoothEffect属性设置为false，关闭进度平滑动效，通过animateTo来设置其过渡动效。
 
```text
@Entry
@Component
struct WidgetsProgress {
  @State proValue: number = 0;

  build() {
    Column() {
      Progress({ value: this.proValue, type: ProgressType.Linear })
        .width(300)
        .style({ strokeWidth: 10, enableSmoothEffect: false });
      // 当进度达到100%时显示“加载完成”文本
      Text('加载完成').visibility(this.proValue >= 100 ? Visibility.Visible : Visibility.None);
      Button('进度条++')
        .margin({ top: 5, bottom: 5 })
        .onClick(() => {
          this.getUIContext().animateTo({
            duration: 1000,
            curve: Curve.Linear,
            playMode: PlayMode.Normal
          }, () => {
            this.proValue += 10;
          });
        });
      Button('进度条重置')
        .onClick(() => {
          // 重置进度值为0
          this.proValue = 0;
        });
    }
    .width('100%')
    .margin({ top: 50 });
  }
}
```
