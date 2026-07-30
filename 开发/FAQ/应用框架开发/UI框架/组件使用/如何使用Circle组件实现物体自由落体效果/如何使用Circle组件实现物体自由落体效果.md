# 如何使用Circle组件实现物体自由落体效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-813

#### 问题现象

Circle组件是绘制圆形的组件，如何使用Circle组件实现物体自由落体效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/JJwNQj5eShGiocqTdTDiFg/zh-cn_image_0000002628557802.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072330Z&HW-CC-Expire=86400&HW-CC-Sign=B49742017C381C9901F649F18075319149D69CD5D590EDD0A84B000FF2D39001)

 
 

#### 背景知识

- [Circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-circle)：用于绘制圆形的组件。
- [关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto#keyframeanimateparam对象说明)：可以用来指定若干个关键帧状态，实现分段的动画。
- [插值计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curve)：插值曲线。减速曲线和加速曲线可以用来展示自由落体的曲线效果。

 
 

#### 解决方案

利用自由落体公式根据起始高度算出落地时间，然后利用关键帧动画结合插值计算模拟出小球自由落体的动效，关键步骤如下：
 1. 计算小球活动区域范围。
```text
displayInfo = display.getDefaultDisplaySync();
<em>// </em><em>活动区域</em>
maxHeight = this.getUIContext().px2vp(this.displayInfo.height) * 0.85;
<em>// </em><em>坐标x</em>
maxWidth = this.getUIContext().px2vp(this.displayInfo.width);
middleX = this.maxWidth * 0.03;
<em>// </em><em>起始坐标y</em>
@State sportY: number = 0;
```

2. 根据自由落体公式构建在不同时间点Circle的坐标y的值。
```text
generatePosition(): Array<KeyframeState> {
 <em> // 根据自由落体公式求得时间</em>
  let time = Math.sqrt(2 * this.maxHeight / 9.8);
  let result: Array<KeyframeState> = [];
 <em> // 第一次落地的速度为v=gt,反弹假设损失0.1的动能,速度为原来的0.9,则第二次的高度为原来的90%,时间0.9*time</em>
  for (let i = 0; i < 17; i++) {
    let flag = i % 2 == 0;
    result.push({
    <em>  // 一帧等于17ms,1s约等于17ms*63</em>
      duration: time * 63 * Math.pow(0.9, Math.ceil(i / 2)),
      curve: flag ? Curve.FastOutLinearIn : Curve.LinearOutSlowIn,
      event: () => {
        this.sportY =
          flag ? this.maxHeight : this.maxHeight - 9.8 / 2 * Math.pow(time * Math.pow(0.9, Math.ceil(i / 2)), 2);
      }
    });
  }
  return result;
}
```

3. 完整示例参考如下：
```text
import { display } from '@kit.ArkUI';

@Entry
@Component
struct FreeFallDemo {
  uiContext: UIContext = this.getUIContext?.();
  displayInfo = display.getDefaultDisplaySync();
 <em> // 活动区域</em>
  maxHeight = this.getUIContext().px2vp(this.displayInfo.height) * 0.85;
<em>  // 坐标x</em>
  maxWidth = this.getUIContext().px2vp(this.displayInfo.width);
  middleX = this.maxWidth * 0.03;
 <em> // 起始坐标y</em>
  @State sportY: number = 0;
  generatePosition(): Array<KeyframeState> {
  <em>  // 根据自由落体公式求得时间</em>
    let time = Math.sqrt(2 * this.maxHeight / 9.8);
    let result: Array<KeyframeState> = [];
    <em>// 第一次落地的速度为v=gt,反弹假设损失0.1的动能,速度为原来的0.9,则第二次的高度为原来的90%,时间0.9*time</em>
    for (let i = 0; i < 17; i++) {
      let flag = i % 2 == 0;
      result.push({
      <em>  // 一帧等于17ms,1s约等于17ms*63</em>
        duration: time * 63 * Math.pow(0.9, Math.ceil(i / 2)),
        curve: flag ? Curve.FastOutLinearIn : Curve.LinearOutSlowIn,
        event: () => {
          this.sportY =
            flag ? this.maxHeight : this.maxHeight - 9.8 / 2 * Math.pow(time * Math.pow(0.9, Math.ceil(i / 2)), 2);
        }
      });
    }
    return result;
  }
  build() {
    Column() {
      Button('点击')
        .width('80%')
        .onClick(() => {
          if (!this.uiContext) {
            return;
          }
          let rs = this.generatePosition();
       <em>   // 只循环1次,每次的坐标变换由position决定</em>
          this.uiContext.keyframeAnimateTo({ iterations: 1 }, rs);
        });
      Stack() {
        Circle().width(50).height(50).position({ x: this.middleX, y: this.sportY });
      };
    }.width('100%').height('100%');
  }
}
```
