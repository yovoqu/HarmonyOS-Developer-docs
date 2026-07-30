# this.getUIContext().getPromptAction().openCustomDialog撑满全屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1494

#### 问题现象

利用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗，并且给dialog设置宽高100%依旧无法全屏。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/4VBkDjX1Rmi9hJXrevuj2Q/zh-cn_image_0000002658965035.png?HW-CC-KV=V1&HW-CC-Date=20260701T041232Z&HW-CC-Expire=86400&HW-CC-Sign=A72DC8391031441B5E43E1B95910337894CFC0D312203E83CF4B39E8063099F3)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/sCtNi4UYSxSs76-xmrUq3Q/zh-cn_image_0000002628605830.png?HW-CC-KV=V1&HW-CC-Date=20260701T041232Z&HW-CC-Expire=86400&HW-CC-Sign=B44EB0958F7DA5CAC09AE7344A996351B637DA52C36A839D8E0DB85464C1A036)

 
 

#### 背景知识

- [沉浸式页面](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-immersive)：沉浸式页面开发常通过将应用页面延伸到状态栏和导航栏，使用[setWindowLayoutFullScreen](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9)方法可以设置窗口为全屏模式。
- [@ohos.display (屏幕属性)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display)：屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，display.getDefaultDisplaySync().height方法可以获取到设备的屏幕高度。

 
 

#### 解决方案
1. 在EntryAbility中设置窗口全屏。
```json
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync();
   <em> // 1.设置窗口全屏</em>
    let isLayoutFullScreen = true;
    windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
      .then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      });
   <em> // 2.设置状态栏和导航条隐藏</em>
    windowClass.setSpecificSystemBarEnabled('status', false)
      .then(() => {
        console.info('Succeeded in setting the status bar to be invisible.');
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
      });

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
<em>    // Main window is destroyed, release UI related resources</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
   <em> // Ability has brought to foreground</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
   <em> // Ability has back to background</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

2. 把自定义弹窗的窗口高度设置为设备的屏幕高度displayHeight。
```text
import { display, PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private customDialogComponentId: number = 0;
  private promptAction: PromptAction = this.getUIContext().getPromptAction();
  @State displayHeight: number = 0;

  aboutToAppear() {
    this.displayHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
  }

  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗').fontSize(30).margin({ top: 50});
      Row({ space: 50 }) {
        Button('取消')
          .backgroundColor(Color.Transparent)
          .fontColor('#0A59f7')
          .width('38%')
          .onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          });
        Button('确认')
          .width('38%')
          .onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          });
      };
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween);
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Text('组件内弹窗')
          .fontSize(30)
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              width: '100%',
              height: this.displayHeight,
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId;
            });
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
