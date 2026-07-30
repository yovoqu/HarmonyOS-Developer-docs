# Text组件字符超过特定长度时，超出部分如何隐藏与显示

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1409

#### 问题现象

在Text中显示文本时，如果文本超过一定长度，通常会有超出部分隐藏与显示的需求，例如：当最多显示的行数为2，组件宽度比例为0.4时，该如何实现？
 
 

#### 背景知识

- [measureText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretext12)方法能够根据文本信息计算文本宽度。
- [getAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)方法能够获取display对象，display对象的width属性为屏幕的宽度。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/r1xThnd5Q-SCmDhTNqZpnw/zh-cn_image_0000002658842531.png?HW-CC-KV=V1&HW-CC-Date=20260730T072441Z&HW-CC-Expire=86400&HW-CC-Sign=68C0A28D7980C645356E3D2FF9914474C0F78D82A828058A1FA9AB8C240F831D)

 
 

#### 解决方案
1. 首先设定的文本长度计算方式：设定文本长度 = 屏幕宽度 * 最大行数 * 组件宽度比例。屏幕宽度可以使用[getAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)获取。
2. 然后使用[measureText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretext12)方法测量实际文本宽度，比较“设定文本长度”与“实际文本宽度”进行大小比较，判断是否需要隐藏。
3. 当需要隐藏时，只展示“设定长度”的文本内容，超出部分显示为“...”。当点击“…”时将该文本变为“…收起”，显示隐藏部分内容。
 
完整示例参考如下：
 
```json
import { MeasureUtils } from '@kit.ArkUI';
import curves from '@ohos.curves';
import { BusinessError } from '@ohos.base';
import display from '@ohos.display';

@Entry
@Component
struct Index {
 <em> // 长文本</em>
  longMessage: string = '走在繁华的城市街头，明空感到无比紧张。他的心跳如雷鼓般擂动着胸膛，使得身上的伪装仿佛随时都要被揭开。然而，他仍然保持着冷静，凭借着过人的胆识与智慧，成功地躲过了敌人的层层封锁。\n' +
    '\n' +
    '　　最终，明空来到了敌对帮派的老巢。此时此刻，那里的守卫正沉浸在欢庆的氛围中，丝毫没有察觉到即将来临的危机。明空深吸一口气，压抑住内心的激动，悄然潜入了这座古老的建筑。';
 <em> // 最大显示行数</em>
  @State lines: number = 2;
  <em>// 长文本状态（展开 or 收起）</em>
  @State collapseText: string = '...';
 <em> // 屏幕宽度（单位px）</em>
  screenWidth: number = 0;
  <em>// </em><em>是否需要显示"展开"字样（注：当文本长度较短时就不需要“展开”）</em>
  @State isExpanded: boolean = false;
  uiContext: UIContext = this.getUIContext();
  uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  <em>// 测量文本宽度（单位px）</em>
  textWidth: number = this.uiContextMeasure.measureText({
    textContent: this.longMessage,
    fontSize: 20
  });
  <em>// 获取当前所有的display对象</em>
  promise: Promise<Array<display.Display>> = display.getAllDisplays();

  aboutToAppear() {
    console.info(`文本宽度为：${this.textWidth}`);
    this.promise.then((data: Array<display.Display>) => {
      console.info(`所有的屏幕信息：${JSON.stringify(data)}`);
    <em>  // 单位为像素</em>
      this.screenWidth = data[0]["width"];
    <em>  // 屏幕宽度 * 最大行数 * 组件宽度比例 和 文字测量宽度</em>
      this.isExpanded = this.screenWidth * this.lines * 0.4 <= this.textWidth;
    }).catch((err: BusinessError) => {
      console.error(`Failed to obtain all the display objects. Code: ${JSON.stringify(err)}`);
    });
  }

  build() {
    Row() {
      Column() {
        if (this.isExpanded) {
          Stack({ alignContent: Alignment.BottomEnd }) {
            Text(this.longMessage)
              .fontSize(20)
              .fontColor(Color.Black)
              .maxLines(this.lines)
              .width("40%")
            Row() {
              Text(this.collapseText)
                .fontSize(20)
                .backgroundColor(Color.White)
            }
            .justifyContent(FlexAlign.End)
            .onClick(() => {
              if (this.collapseText == '...') {
                this.collapseText = '...收起';
              <em>  // 展开动画</em>
                this.uiContext.animateTo({
                  duration: 150,
                  curve: curves.springMotion(0.5, 0.8),
                }, () => {
                  this.lines = -1; <em>// </em><em>使得设置的最大行属性无效</em>
                });
              } else {
                this.collapseText = '...';
               <em> // 收起动画</em>
                this.uiContext.animateTo(
                  {
                    duration: 100,
                    curve: Curve.Friction,
                  }, () => {
                  this.lines = 2; <em>// </em><em>只显示2行</em>
                });
              }
            })
          }
        }
        else {
          Text(this.longMessage)
            .fontSize(20)
            .fontColor(Color.Black)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 
 

#### 常见FAQ

Q：如何设置文字超出宽度后继续显示，不要滚动？
 
A：只使用textOverflow属性不能实现这种效果，可以使用Row嵌套Text，再动态设置文字宽度来实现类似效果。
 
```text
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextDemo {
  textString: string = '我是超长文本，超出的部分显示。I am an extra long text';
  @State textWidth: number = 0;
  uiContext: UIContext = this.getUIContext();
  uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: number = 14;

  aboutToAppear(): void {
   <em> // 计算文字宽度</em>
    this.textWidth = this.uiContextMeasure.measureText({
      textContent: this.textString,
      fontSize: this.textSize
    });
  }

  build() {
    Column() {
      Row() {
        Text(this.textString)
          .fontSize(this.textSize)
          .maxLines(1)
          .width(this.textWidth+'px')
          .backgroundColor(Color.Pink)
      }
      .width(250)
      .border({ width: 1 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Start)
  }
}
```
