# 能否检测到开发者选项中USB调试开关是否开启

更新时间：2026-07-15 01:37:37

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-68

#### 问题现象

希望应用内能够检测手机是否开启了USB调试功能，并在检测到该功能开启时，向用户提示可能存在的安全风险。
 
 

#### 解决方案

可以使用[getValueSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings#settingsgetvaluesync11)获取，传入name参数为字符串格式：'HDC_STATUS'(该参数API19开始支持，API21已废弃但仍可使用)，defValue参数为字符串格式：'NONE'，domainName参数为字符串格式：settings.domainName.DEVICE_SHARED，可参考：
 
```text
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';


@Entry
@Component
struct Index {
  @State message: string = '手机是否开启了USB调试功能？';

  build() {
    Column() {
      Text(this.message)
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let value = settings.getValueSync(context, 'HDC_STATUS', 'NONE', settings.domainName.DEVICE_SHARED);

          this.message = value;

        });
    }
    .height('100%')
    .width('100%');
  }
}
```
