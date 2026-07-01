# 如何使用Circle组件实现物体自由落体效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-813

## 如何使用Circle组件实现物体自由落体效果
 


##### 问题现象

Circle组件是绘制圆形的组件，如何使用Circle组件实现物体自由落体效果？
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/JJwNQj5eShGiocqTdTDiFg/zh-cn_image_0000002628557802.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025548Z&HW-CC-Expire=86400&HW-CC-Sign=03BEC8F2B72FF553C790BB6DD880FB8AA67FF2C5F9D487127630ECFA4702F541)

 
 

##### 背景知识

- [Circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-circle)：用于绘制圆形的组件。
- [关键帧动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto#keyframeanimateparam对象说明)：可以用来指定若干个关键帧状态，实现分段的动画。
- [插值计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curve)：插值曲线。减速曲线和加速曲线可以用来展示自由落体的曲线效果。

 
 

##### 解决方案

利用自由落体公式根据起始高度算出落地时间，然后利用关键帧动画结合插值计算模拟出小球自由落体的动效，关键步骤如下：
 
- 计算小球活动区域范围。
```text
displayInfo = display.getDefaultDisplaySync();
// 活动区域
maxHeight = this.getUIContext().px2vp(this.displayInfo.height) * 0.85;
// 坐标x
maxWidth = this.getUIContext().px2vp(this.displayInfo.width);
middleX = this.maxWidth * 0.03;
// 起始坐标y
@State sportY: number = 0;
```

- 根据自由落体公式构建在不同时间点Circle的坐标y的值。
```text
generatePosition(): ArrayKeyframeState> {
  // 根据自由落体公式求得时间
  let time = Math.sqrt(2 * this.maxHeight / 9.8);
  let result: ArrayKeyframeState> = [];
  // 第一次落地的速度为v=gt,反弹假设损失0.1的动能,速度为原来的0.9,则第二次的高度为原来的90%,时间0.9*time
  for (let i = 0; i  17; i++) {
    let flag = i % 2 == 0;
    result.push({
      // 一帧等于17ms,1s约等于17ms*63
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

- 完整示例参考如下：
```text
import { display } from '@kit.ArkUI';

@Entry
@Component
struct FreeFallDemo {
  uiContext: UIContext = this.getUIContext?.();
  displayInfo = display.getDefaultDisplaySync();
  // 活动区域
  maxHeight = this.getUIContext().px2vp(this.displayInfo.height) * 0.85;
  // 坐标x
  maxWidth = this.getUIContext().px2vp(this.displayInfo.width);
  middleX = this.maxWidth * 0.03;
  // 起始坐标y
  @State sportY: number = 0;
  generatePosition(): ArrayKeyframeState> {
    // 根据自由落体公式求得时间
    let time = Math.sqrt(2 * this.maxHeight / 9.8);
    let result: ArrayKeyframeState> = [];
    // 第一次落地的速度为v=gt,反弹假设损失0.1的动能,速度为原来的0.9,则第二次的高度为原来的90%,时间0.9*time
    for (let i = 0; i  17; i++) {
      let flag = i % 2 == 0;
      result.push({
        // 一帧等于17ms,1s约等于17ms*63
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
          // 只循环1次,每次的坐标变换由position决定
          this.uiContext.keyframeAnimateTo({ iterations: 1 }, rs);
        });
      Stack() {
        Circle().width(50).height(50).position({ x: this.middleX, y: this.sportY });
      };
    }.width('100%').height('100%');
  }
}
```
