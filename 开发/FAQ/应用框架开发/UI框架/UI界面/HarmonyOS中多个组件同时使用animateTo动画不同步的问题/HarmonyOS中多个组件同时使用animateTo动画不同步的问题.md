# HarmonyOS中多个组件同时使用animateTo动画不同步的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-692

#### 问题现象

在HarmonyOS应用中，使用animateTo方法实现两个Column组件的属性动画时，动画未能同步执行。
 
问题代码如下：
 
```text
import { display } from '@kit.ArkUI';


const SCREEN_WIDTH = display.getDefaultDisplaySync().width;


@Entry
@Component
struct Index {
  @State translateX: number = SCREEN_WIDTH
  @State lastTranslateX: number = 0


  build() {
    Column() {
      Button('触发动画')
        .onClick(() => this.startAnimation())
        .margin(100)
      Column() {
        Text('B')
          .fontSize(20)
      }
      .width('100%')
      .height(120)
      .backgroundColor('#f1f3f5')
      .opacity(1)
      .translate({ x: this.translateX })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)


      Column() {
        Text('A')
          .fontSize(20)
      }
      .width('100%')
      .height(120)
      .backgroundColor('#f1f3f5')
      .opacity(1)
      .translate({ x: this.lastTranslateX })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
    }


  }


  private startAnimation() {
    this.getUIContext().animateTo({
      duration: 1800,
      curve: Curve.EaseOut
    }, () => {
      this.translateX = 0
      this.lastTranslateX = -SCREEN_WIDTH
    })
  }
}
```
 
 
问题效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/AE0H7F7oS8yWf0qn5OjBGA/zh-cn_image_0000002658914075.png?HW-CC-KV=V1&HW-CC-Date=20260730T072513Z&HW-CC-Expire=86400&HW-CC-Sign=9ECB7DB73FBCBD8DB3AFE4DBCA307766AA013E758591E4D1EFCE009D799B05C1)

 

#### 背景知识

- [translate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#translate)是HarmonyOS提供的一种通用属性，用于设置组件的平移。
- [getDefaultDisplaySync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)是display模块提供的一种方法，用于获取当前默认的display对象，可通过该对象获得width宽度等屏幕相关属性。
- UIContext提供[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)接口来指定由于闭包代码导致的状态变化插入过渡动效。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)是一种组件区域变化事件，当组件区域变化时触发该回调。该函数仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

 
 

#### 问题定位

在animateTo方法中，所有语句是按顺序执行的，并不是同步执行的。
 
 

#### 分析结论

既然animateTo方法中的语句只能顺序执行，那能否用其他回调函数来实现动画效果的同步？可以想到使用onAreaChange回调方法实现动画的同步。
 
 

#### 修改建议

定义newValue状态变量，并使用onAreaChange回调方法实时获取A组件在屏幕中的实时宽度，根据组件的宽度来设置平移的数值即可。
 
完整代码如下所示：
 
```text
@Entry
@Component
struct AnimationOutOfSync {
  @State lastTranslateX: number = 0;
  @State newValue: number = 0;
  @State translateX: number = this.newValue;


  build() {
    Column() {
      Button('触发动画')
        .onClick(() => this.startAnimation())
        .margin(100)
      Column() {
        Text('B')
          .fontSize(20)
      }
      .width('100%')
      .height(120)
      .backgroundColor('#f1f3f5')
      .translate({ x: this.translateX })
      .opacity(1)
    <em>  // 通过onAreaChange来获取当前组件的宽度</em>
      .onAreaChange((oldValue: Area, newValue: Area) => {
        this.newValue = newValue.width as number;
        this.translateX = newValue.width as number;
      })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)


      Column() {
        Text('A')
          .fontSize(20)
      }
      .width('100%')
      .height(120)
      .backgroundColor('#f1f3f5')
      .translate({ x: this.lastTranslateX })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
    }
  }


  private startAnimation() {
    this.getUIContext()?.animateTo({
      duration: 1800,
      curve: Curve.EaseOut
    }, () => {
      this.translateX = 0;
      this.lastTranslateX = -this.newValue;
    });
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/7I2NZns9SFGLqaDTLW9W4Q/zh-cn_image_0000002658794123.png?HW-CC-KV=V1&HW-CC-Date=20260730T072513Z&HW-CC-Expire=86400&HW-CC-Sign=EE9CE0C893019AFEE8B553CC5350D23AA5FBA7A3DA20F3034FCE24696F35F51C)
