# 如何判断APP内容是否被截屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1368

#### 问题现象

window模块提供的对截屏事件的监听，不仅在应用内截屏会触发，当系统下拉菜单（通知栏、控制栏）时截屏，也会触发截屏事件，如何区分截屏在应用内还是其他场景？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/C5ddtYrIR56knabzM49_3g/zh-cn_image_0000002658841303.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072419Z&HW-CC-Expire=86400&HW-CC-Sign=6029DAD256F52B294F6B295358C3D650B174CE698FBFDF7FB23BE481FDFFAF4F)

 
 

#### 背景知识

[window模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window)提供对窗口管理的基本能力，可通过[on('screenshot')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#onscreenshot9)接口开启截屏事件的监听。[isFocused](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#isfocused12)是判断当前窗口是否获焦的接口，可以用来判断当前窗口是否位于上层。
 
 

#### 解决方案

使用on('screenshot')监控当前窗口是否发生截屏事件，并在回调中添加isFocused，用于判断当前窗口是否获焦，若获焦，表明应用窗口位于最上层被截图。
 
```text
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Screenshot {
  @State remind: string = '未截图';

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data: window.Window) => {
      if (err) {
        console.error(`GetLastWindow failed, error code: ${err.code}, error message: ${err.message}`);
      }
      data.on('screenshot', () => {
        if (data.isFocused()) {
          this.remind = '应用内截图';
        } else {
          this.remind = '非应用内截图';
        }
      });
    });
  }

  build() {
    Column() {
      Text(this.remind)
        .fontSize(50);
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
