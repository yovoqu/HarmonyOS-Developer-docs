# PC端点击Dock栏关闭窗口时，如何弹窗确认

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-10

#### 问题现象

HarmonyOS PC端应用最小化Dock栏后，如何在应用右键点击关闭窗口时，增加一个二次确认弹窗给到用户操作。
 
 

#### 背景知识

- [onPrepareToTerminate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#onpreparetoterminate10)：在UIAbility即将关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。
- 开发者可以在onPrepareToTerminate回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#terminateself)接口关闭。
- [showDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showdialog)：创建并显示对话框，对话框响应结果使用callback异步回调返回。

 
 

#### 解决方案

HarmonyOS PC端应用最小化Dock栏后，可以通过监听onPrepareToTerminate回调，在触发右键点击关闭窗口时，恢复主窗口并弹窗通知用户二次确认后再关闭窗口。
 
- 在module.json5配置文件中声明[ohos.permission.PREPARE_APP_TERMINATE](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionprepare_app_terminate)权限。
```json
"requestPermissions":[
  {
    "name" : "ohos.permission.PREPARE_APP_TERMINATE"
  }
],
```

- 在EntryAbility.ets文件中添加onPrepareToTerminate回调事件，在Dock栏关闭窗口时，进行弹窗提示。
```json
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';


const DOMAIN = 0x0000;


export default class EntryAbility extends UIAbility {
 <em> //当前window对象</em>
  private currentWindowStage: window.WindowStage | null = null;

  onCreate(): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);

    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
  <em>  // Main window is created, set main page for this ability</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    if (this.currentWindowStage === null) {
      this.currentWindowStage = windowStage;
    }
   <em> // 存储windowStage</em>
    AppStorage.setOrCreate('windowStage', windowStage);
    windowStage.loadContent('pages/Index', (err) => {
    <em>  // 存储windowStatus</em>
      AppStorage.setOrCreate('windowStatus', window.WindowStatusType.FULL_SCREEN);
      windowStage.getMainWindow((err: BusinessError, data) => {
        if (err) {
        <em>  // To do sth.</em>
        }
        let windowClass = data;
        windowClass.on('windowStatusChange', (windowStatusType) => {
          AppStorage.setOrCreate('windowStatus', windowStatusType);
        });
      });
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

  }

  onWindowStageDestroy(): void {
   <em> // Main window is destroyed, release UI related resources</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
   <em> // Ability has brought to foreground</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
  <em>  // Ability has back to background</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }

  onPrepareToTerminate(): boolean {
  <em>  // 开发者定义预关闭动作</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onPrepareToTerminate');
  <em>  // 例如关闭应用之前弹窗提示是否关闭app</em>
    let windowStatus = AppStorage.get('windowStatus') as window.WindowStatusType;
    if (windowStatus == window.WindowStatusType.MINIMIZE) {
      let mainWindowClass = this.currentWindowStage?.getMainWindowSync() as window.Window;
      let promise = mainWindowClass.restore();
      promise.then(() => {
        console.info('Succeeded in restoring the window.');
        if (this.currentWindowStage !== null) {
          this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showDialog({
            title: '提示',
            message: '确认是否关闭APP？',
            buttons: [
              {
                text: '取消',
                color: '#0091FF'
              },
              {
                text: '确定',
                color: '#ff0000'
              }
            ]
          }).then(data => {
            if (data.index === 0) {
              this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showToast({
                message: '已取消',
                duration: 2000
              });
            } else {
           <em>   // 确认关闭</em>
              this.context.terminateSelf();
            }
          });
        }
      }).catch((err: BusinessError) => {
        console.error(`Failed to restore the window. Cause code: ${err.code},
                  message: ${err.message}`);
      });
      return true;
    } else {
      if (this.currentWindowStage !== null) {
        this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showDialog({
          title: '提示',
          message: '确认是否关闭APP？',
          buttons: [
            {
              text: '取消',
              color: '#0091FF'
            },
            {
              text: '确定',
              color: '#ff0000'
            }
          ]
        }).then(data => {
          if (data.index === 0) {
            this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showToast({
              message: '已取消',
              duration: 2000
            });
          } else {
          <em>  // 确认关闭</em>
            this.context.terminateSelf();
          }
        });
      }
    }
    return true;
  }
};
```
