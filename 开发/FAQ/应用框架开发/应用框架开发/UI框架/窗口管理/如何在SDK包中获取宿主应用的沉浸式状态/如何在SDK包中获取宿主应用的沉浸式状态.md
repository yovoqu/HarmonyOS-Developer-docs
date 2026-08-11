# 如何在SDK包中获取宿主应用的沉浸式状态

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1432

#### 问题现象

SDK项目采用HAR包的方式集成到宿主应用中，如何在SDK包中获取宿主应用的沉浸式状态？
 
 

#### 背景知识

[@ohos.window (窗口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window)提供了窗口管理器[WindowStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage)，用于管理各个基本窗口单元。同时，可通过[getWindowProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9)方法获取当前窗口的属性，其中isLayoutFullScreen可以判断窗口是否为沉浸式且处于全屏模式。
 
初次创建SDK项目可参考[创建及发布三方库](https://ohpm.openharmony.cn/#/cn/help/createandpublish)。利用DevEco Studio对开发后的库模块打成HAR包，详情请见：[构建HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har)。在项目中引入三方库参考[配置依赖项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-dependencies#section15420141487)。
 
 

#### 解决方案

- 主要思路：HAR通过提供接口的方式，将相关功能模块开放给HAP使用。在HAP包中调用这些接口方法，将所需数据传递至HAR，从而实现数据交互与共享。

  实现步骤：1. 通过AppStorage.setAndLink存储WindowStage。可参考[如何在Page中获取WindowStage实例](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-298)。

2. 在HAR包中定义方法，通过AppStorage.get获取WindowStage，使用getWindowProperties().isLayoutFullScreen获取宿主应用沉浸式状态，通过export[导出类和方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package#导出类和方法)：
```text
import { window } from '@kit.ArkUI';

export function saveWindowStage(windowStage: window.WindowStage) {
  AppStorage.setAndLink('windowStage', windowStage);
}

export function getFullScreenStatus(): string {
  let winStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
  let isLayoutFullScreen = winStage.getMainWindowSync().getWindowProperties().isLayoutFullScreen;
  console.info(isLayoutFullScreen ? 'isFullScreen' : 'isNotFullScreen');
 <em> // 返回结果给应用页，如不需要则不返回。在应用侧直接调用该函数。</em>
  return (isLayoutFullScreen ? 'isFullScreen' : 'isNotFullScreen');
}
```


3. 在HAP中调用HAR方法，获取HAP窗口沉浸式状态信息，注意代码中SDKName需要替换成HAR包名称。
```text
import { PromptAction } from '@kit.ArkUI';
import { getFullScreenStatus } from 'sdkname';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State isFullScreen: boolean = false;<em> // 切换屏幕全屏</em>
  @State state: string = '';<em> // 存储HAR中获取沉浸式状态</em>
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
   <em> // 通过AppStorage.setAndLink存储WindowStage</em>
    AppStorage.setAndLink('windowStage', this.context.windowStage);
   <em> // 进入应用调用HAR方法获取屏幕状态</em>
    this.state = getFullScreenStatus();
    this.promptAction.showToast({
      message: this.state,
      duration: 2000
    });
  }

  build() {
    Row() {
      Column({ space: 5 }) {
        Text('获取宿主应用窗口是否沉浸式')
          .fontSize(30)
          .fontWeight(FontWeight.Bold);
        Button('changeFullScreenStatus').onClick(async () => {
        <em>  // 切换屏幕状态</em>
          this.isFullScreen = !this.isFullScreen;
          await this.context.windowStage.getMainWindowSync().setWindowLayoutFullScreen(this.isFullScreen);
       <em>   // 调用SDK方法获取屏幕状态</em>
          this.state = getFullScreenStatus();
          this.promptAction.showToast({
            message: this.state,
            duration: 2000
          });
        });
      }
      .width('100%');
    }
    .height('100%')
    .backgroundColor('#eaeaea');
  }
}
```
