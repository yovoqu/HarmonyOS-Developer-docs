# 如何设置APP内全局字体大小

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-890

#### 问题现象

在文本量多而杂的场景下，单独给每个Text文本设置字体大小效率不高，有什么方法能够设置APP内的全局字体大小？以便统一设置字体大小，提高效率。
 
 

#### 背景知识

- [动态属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier)是动态设置组件的属性，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。其属性方法[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifiert)支持在当前组件上动态设置属性方法。
- [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)文本组件中的[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontsize)属性可以设置字体大小，[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性可以设置字体列表。
- 接口[ApplicationContext.setFontSizeScale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetfontsizescale13)设置应用字体大小缩放比例。仅支持主线程调用。当应用字体设置为跟随系统时，通过配置[configuration标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#configuration标签)就可以设置应用字体大小跟随系统变化的比例。

 
 

#### 解决方案

- 方案一：通过preferences调节应用内全局字体大小。自定义PreferencesUtil类，通过其提供的创建、保存和查询的数据，将读取到的数据保存到页面带有@State的变量中，通过状态变量对文本字体大小进行设置。具体应用可以参考官网[使用preferences实现应用内字体大小调节功能](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-SetAppFontSize)。
- 方案二：通过动态属性设置全局字体大小。使用动态属性，自定义class实现AttributeModifier接口，设定好Text需要的fontSize后在页面调用，实现字体大小统一修改。

  
```text
class MyTextModifier implements AttributeModifier<TextAttribute> {
  public isDark: boolean = false;


  applyNormalAttribute(instance: TextAttribute): void {
    if (this.isDark) {
      instance.fontSize(100);
    } else {
      instance.fontSize(50);
    }
  }
}


@Entry
@Component
struct Index {
  private message: string = 'test';
  @State modifier: MyTextModifier = new MyTextModifier();


  build() {
    Column() {
      Text(this.message)
        .attributeModifier(this.modifier)
        .onClick(() => {
          this.modifier.isDark = !this.modifier.isDark;
        });
      Blank();
      Text(this.message)
        .attributeModifier(this.modifier)
        .onClick(() => {
          this.modifier.isDark = !this.modifier.isDark;
        });
    }
    .padding(24)
    .width('100%')
    .height('100%');
  }
}
```


  效果预览图：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Udxo0wgMRTmdPLxxNz4Paw/zh-cn_image_0000002658798907.png?HW-CC-KV=V1&HW-CC-Date=20260811T005716Z&HW-CC-Expire=86400&HW-CC-Sign=FC438470D640649A0B5C1BE3EF66F9183551E801C0CD7F7D8D6EAA8D1089A28F)

- 方案三：使用ApplicationContext接口实现设置应用内全局字体大小。通过setFontSizeScale方法设置应用字体的全局缩放比例：在entryability/EntryAbility中调用ApplicationContext接口，并使用setFontSizeScale方法，即可设置应用内全局字体比例大小。页面代码为默认Hello World页面，EntryAbility示例代码如下：

  
```json
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';


const DOMAIN = 0x0000;


export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      console.info(`want: ${want}`);
      console.info(`launchParam: ${launchParam}`);
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
   <em> // Main window is created, set main page for this ability</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');


    windowStage.loadContent('pages/Page', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
    <em>// 设置全局的字体大小</em>
    let applicationContext = this.context.getApplicationContext();
    applicationContext.setFontSizeScale(2); <em>// 将应用字体设置为2倍大小</em>
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
   <em> // Ability has back to background</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```
 Page页面示例代码如下：

  
```text
@Entry
@Component
struct Page {
  @State message: string = 'Hello World';


  build() {
    RelativeContainer() {
      Text(this.message)
        .id('PageHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```


  效果预览图：

  正常字体大小：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/N1XF72zjTkioxksGqImqmA/zh-cn_image_0000002628559546.png?HW-CC-KV=V1&HW-CC-Date=20260811T005716Z&HW-CC-Expire=86400&HW-CC-Sign=E9459D8223B897FE9F190317A7156743CF9A79497FF9BB85B23812137739C34A)


  设置setFontSizeScale(2)方法的字体大小：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/-q6lWHN_SDSVp3EJ65gD7Q/zh-cn_image_0000002658918857.png?HW-CC-KV=V1&HW-CC-Date=20260811T005716Z&HW-CC-Expire=86400&HW-CC-Sign=D63813F58B47DCFDA3A13216A56977107F785EB5053F487D820464DFCFDBBC2D)


 
 

#### 常见FAQ

Q：关于getContext().getApplicationContext().setFont("fontName")方法，经测试，设置一次之后再设置就会无效，不能进行动态修改。
 
A：setFont需要通过this.getUIContext().getFont().registerFont方法进行注册字体，切换其他字体后，fontFamily接口还要绑定成切换后字体的familyName才可以生效。
 
Q：如何全局设置字体颜色？
 
A：目前需要单独对每个Text组件设置属性。可通过动态属性[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)全局复用（模块级）样式。
 
Q：setFontSizeScale是否有生效范围？
 
A：ApplicationContext.setFontSizeScale该设置会应用于：
 1. 应用程序的所有页面。
2. 所有文本控件（如Text、Label等）。
3. 自定义组件中的文本。系统组件中若可将字体大小作为参数传入时，该组件会自行控制字体大小，不受setFontSizeScale控制。
 
 

#### 总结
 
| 方案 | 适用场景 |
| --- | --- |
| 使用preferences | 适用于需要实现应用轻量级数据持久化，并且能够修改和查询数据的场景。 |
| 使用动态属性和registerFont接口 | 适用于需要自定义字体大小和字体样式的场景。 |
| 使用ApplicationContext接口 | 适用于单纯设置字体比例的场景。 |
