# Swiper组件被遮挡，导致点击事件不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1308

#### 问题现象

Swiper组件的点击事件不生效，应该如何处理？
 
问题代码示例参考如下：
 
```text
import { PromptAction } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local message: string = 'Hello World';
  swiperController: SwiperController = new SwiperController();
  imaglist: string[] = [
    'www.example.com',
    'www.example.com',
    'www.example.com',
    'www.example.com'
  ]
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  build() {
    RelativeContainer() {
      Swiper(this.swiperController) {
        ForEach(this.imaglist, (imagurl: string, index: number) => {
          Image(imagurl)
            .width('100%')
            .height(300)
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
            .onClick(() => {
              this.promptAction.showToast({
                message: '第' + index + '张',
                duration: 1500,
                bottom: "center",
              })
            })
        })
      }
      .id("swiper")
      .clip(false)
      .autoPlay(true)
      .height(280)

      Column() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message = 'Welcome';
            this.promptAction.showToast({
              message: '轮播图无法点击\n错误示范',
              duration: 1500,
              bottom: "center",
            })
          })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
    .width('100%')
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/z08QF2cJQriOjSuG0_4TVw/zh-cn_image_0000002658958241.png?HW-CC-KV=V1&HW-CC-Date=20260723T012731Z&HW-CC-Expire=86400&HW-CC-Sign=CFC8488FC23B17235285BFA6D7B4717E3A30A4196A60B3C465C49461EF6112F7)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)是滑块视图容器，提供子组件滑动轮播显示的能力。
- [点击事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click)是组件的通用事件。

 
 

#### 问题定位

- 调试业务代码，确认点击事件是否触发。
- 通过ArkUIInspector查看页面布局是否存在问题（例如组件遮挡）导致点击事件未响应。

 
 

#### 分析结论

Column组件遮挡Swiper组件，导致Swiper组件无法响应点击事件。
 
 

#### 修改建议

- **方案一**：若业务上要求UI界面如此，那么可以参考[如何隔离触摸事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1534)（设置hitTestBehavior为HitTestMode.Transparent或HitTestMode.None）来实现Swiper点击事件的响应。
```text
import { PromptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@ComponentV2
struct Index {
  message: string = 'Hello World';
  swiperController: SwiperController = new SwiperController();
 <em> // www.example.com仅做示例，需要替换为有效的图片url/resource</em>
  imageList: string[] = [
    'www.example.com',
    'www.example.com',
    'www.example.com'
  ];
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    RelativeContainer() {
    <em>  // swiper component</em>
      Swiper(this.swiperController) {
        ForEach(this.imageList, (imageUrl: string, index: number) => {
          Image(imageUrl)
            .width('100%')
            .height(300)
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
            .onClick(() => {
              try {
                this.promptAction.showToast({
                  message: '第' + index + '张',
                  duration: 1500,
                  bottom: 'center',
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            });
        });
      }
      .id('swiper')
      .clip(false)
      .autoPlay(true)
      .height(280);

      Column() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message = 'Welcome';
            try {
              this.promptAction.showToast({
                message: '轮播图无法点击\n错误示范',
                duration: 1500,
                bottom: 'center',
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`showToast args error code is ${code}, message is ${message}`);
            }
          });
      }
      .hitTestBehavior(HitTestMode.Transparent)
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/x6q9crcgQJir_eQKklZJDw/zh-cn_image_0000002658838293.png?HW-CC-KV=V1&HW-CC-Date=20260723T012731Z&HW-CC-Expire=86400&HW-CC-Sign=42E80024E7867215103A0342B087FC2CA5BBCF2A10FD4F570A513E13DF057493)

- **方案二**：调整页面UI布局，使得Swiper组件上方无任何组件遮挡。
```text
import { PromptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@ComponentV2
struct Index {
  @Local message: string = 'Hello World';
  swiperController: SwiperController = new SwiperController();
 <em> // www.example.com仅做示例，需要替换为有效的图片url/resource</em>
  imageList: string[] = [
    'www.example.com',
    'www.example.com',
    'www.example.com'
  ];
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    RelativeContainer() {
      Swiper(this.swiperController) {
        ForEach(this.imageList, (imageUrl: string, index: number) => {
          Image(imageUrl)
            .width('100%')
            .height(300)
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
            .onClick(() => {
              try {
                this.promptAction.showToast({
                  message: `第${index}张`,
                  duration: 1500,
                  bottom: 'center',
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            });
        });
      }
      .id('swiper')
      .clip(false)
      .autoPlay(true)
      .height(280);

      Column() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message = 'Welcome';
            try {
              this.promptAction.showToast({
                message: '轮播图无法点击\n错误示范',
                duration: 1500,
                bottom: 'center',
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`showToast args error code is ${code}, message is ${message}`);
            }
          });
      }
      .alignRules({
        'top': { 'anchor': 'swiper', 'align': VerticalAlign.Bottom },
        'left': { 'anchor': 'swiper', 'align': HorizontalAlign.Start }
      })
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Ns-loMxtTHuOfo91UCnLNQ/zh-cn_image_0000002628599024.png?HW-CC-KV=V1&HW-CC-Date=20260723T012731Z&HW-CC-Expire=86400&HW-CC-Sign=5C56095590CD4924DC18FE07F3D27CB68412C157F6DC3278B0291AD74ACC010C)
