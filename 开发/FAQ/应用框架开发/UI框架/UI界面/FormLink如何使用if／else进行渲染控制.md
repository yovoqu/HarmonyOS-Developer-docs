# FormLink如何使用if/else进行渲染控制

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-912

## FormLink如何使用if/else进行渲染控制
 


##### 问题现象

开发一个卡片，FormLink如何使用if/else进行渲染控制来实现跳转到那个页面？
 
 

##### 背景知识

- [Form Kit（卡片开发服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/formkit-overview)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
- [FormLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-formlink)提供静态卡片交互组件，用于静态卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件。
- [formProvider.updateForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider#formproviderupdateform)更新指定的卡片。

 
 

##### 解决方案

- FormLink本身不具备执行逻辑的能力，但可以通过params传参来进行处理。
- 通过if/else控制哪个FormLink被渲染，从而决定了点击后传递的参数是什么。
- @LocalStorageProp确保了卡片UI能实时响应底层数据的变化，实现按钮的动态切换。

 
参考代码如下:
 
EntryAbility.ets文件：
 
```text
import { ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  private selectPage: string = '';
  private currentWindowStage: window.WindowStage | null = null;

  onCreate(want: Want): void {
    if (want?.parameters?.params) {
      // want.parameters.params对应FormLink()中params内容
      let params: Record = JSON.parse(want.parameters.params as string);
      this.selectPage = params.message as string;
      console.info(`onCreate selectPage: ${this.selectPage}`);
    }
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
  onNewWant(want: Want): void {
    console.info(`Ability onNewWant: ${JSON.stringify(want?.parameters)}`);
    if (want?.parameters?.params) {
      // want.parameters.params对应FormLink()中params内容
      let params: Record = JSON.parse(want.parameters.params as string);
      this.selectPage = params.message as string;
      console.info(`onNewWant selectPage: ${this.selectPage}`);
    }
    if (this.currentWindowStage !== null) {
      this.onWindowStageCreate(this.currentWindowStage);
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    let targetPage: string;
    // 根据传递的targetPage不同，选择拉起不同的页面
    switch (this.selectPage) {
      case 'page':
        targetPage = 'pages/Page';
        break;
      case 'index':
        targetPage = 'pages/Index';
        break;
      default:
        targetPage = 'pages/Page';
    }
    if (this.currentWindowStage === null) {
      this.currentWindowStage = windowStage;
    }
    windowStage.loadContent(targetPage, (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }
};
```
 
EntryFormAbility.ets文件：
 
```text
onFormEvent(formId: string, message: string) {
  if (message) {
    // message是从卡片UI传来的字符串
    let flag: number = JSON.parse(message)['message'];
    // 构建卡片数据对象
    let formData: Record = { 'change': !flag };
    // createFormBindingData将普通对象转换为卡片能识别的FormBindingData对象
    let formInfo = formBindingData.createFormBindingData(formData);
    // 通过formProvider的updateForm接口刷新卡片UI
    formProvider.updateForm(formId, formInfo);
  }
}
```
 
WidgetCard.ets文件：
 
```text
@Entry
@Component
struct FormLinkDemo {
  @LocalStorageProp('change') flag: boolean = false;

  build() {
    Column({ space: 10 }) {
      Text('这是一个静态卡片').fontSize(20);
      // message事件触发FormExtensionAbility的onFormEvent生命周期
      FormLink({
        action: 'message',
        abilityName: 'EntryAbility',
        params: {
          'message': this.flag // 自定义要发送的message
        }
      }) {
        Button('点我切换要跳转的页面').width(220);
      };

      if (this.flag) {
        // router事件用于静态卡片跳转到对应的UIAbility
        FormLink({
          action: 'router',
          abilityName: 'EntryAbility',
          params: {
            'message': 'page' // 自定义要发送的message
          }
        }) {
          Button('跳转到页面二').width(220);
        };
      } else {
        // router事件用于静态卡片跳转到对应的UIAbility
        FormLink({
          action: 'router',
          abilityName: 'EntryAbility',
          params: {
            'message': 'index' // 自定义要发送的message
          }
        }) {
          Button('跳转到页面一').width(220);
        };
      }
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
