# ForEach实现曲线滑动失败

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-760

#### 问题现象

手势滑动只能让月亮图片内的数字变动，月亮图片并没有位移。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fywTzfj4TnSi8QRHf8M4ow/zh-cn_image_0000002628555690.png?HW-CC-KV=V1&HW-CC-Date=20260723T013112Z&HW-CC-Expire=86400&HW-CC-Sign=386394B7D3E52DBEA63E6D990FA10D4CD176F5EFBF0352E609A82154BBA4C748)

 
**预期描述：** 想要实现通过手势滑动让月亮图片以半圆曲线的轨迹滚动的效果。
 
**曲线滑动相关代码：**
 1. 使用ForEach布置月亮图片：
```text
ForEach(this.data, (item: number, i: number) => {
  Stack() {
   <em> // 开发者需自行配置媒体资源文件</em>
    Image($r('app.media.vip_sn_star'))
      .width('100%')
      .height('100%');
    Text(item.toString())
      .fontSize(14)
      .fontColor('#FF61240D')
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%');
  }
  .animation({ duration: 200, curve: Curve.EaseInOut })
  <em>// 根据位置透明度递减，具体数值需要根据具体情况调整。</em>
  .opacity(1 - 0.4 * (69 +
    (this.getStarPosition(i + this.moveDistance).y - this.maxSize * this.getScale(i + this.moveDistance) / 2)) /
    324)
  .rotate({ angle: -90 }) <em>// 保持文字端正</em>
  .width(this.maxSize * this.getScale(i + this.moveDistance))
  .height(this.maxSize * this.getScale(i + this.moveDistance))
 <em> // 位置信息需要添加位移变量（修改部分）</em>
  .position({
    x: this.getStarPosition(i + this.moveDistance).x - this.maxSize * this.getScale(i + this.moveDistance) / 2,
    y: this.getStarPosition(i + this.moveDistance).y - this.maxSize * this.getScale(i + this.moveDistance) / 2
  });
});
```

2. 手势滑动相关代码：
```text
.gesture(
<em>  // 手势需要触发位移变量的改变（修改部分）</em>
  PanGesture({ direction: PanDirection.Vertical, distance: 20 })
    .onActionUpdate((event: GestureEvent) => {
      console.info(`月亮图片：onActionUpdate event.offsetY = + event.offsetY`);
      if (event.offsetY < -20) {
        this.uiContext?.animateTo({ duration: 200 }, () => {
          this.moveDistance -= 0.1;
        });
      } else if (event.offsetY > 20) {
        <em>// 向下滑：回退</em>
        this.uiContext?.animateTo({ duration: 200 }, () => {
          this.moveDistance += 0.1;
        });
      }
    })
    .onActionEnd((event: GestureEvent) => {
      console.info(`event: ${event}`);
    })
);
```

 
 

#### 背景知识

- [ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach)接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。
- [PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

 
 

#### 问题定位
1. 检查ForEach中是否使用了合适的数据源：想要实现对整体数据进行一个手势滚动，则数据源应使用完整的数据。如果使用数据片段的话无法实现完整数据滚动的目的。
2. 检查PanGesture中手势是否触发合适的属性改变：想要通过手势触发子元素的位移滚动，则需要新增位移变量，并通过手势触发位移变量的改变。如果没有配置合适的位移变量，则无法实现随手势滚动位移的效果。
 
 

#### 分析结论
1. ForEach中需要使用合适的数据源：想要实现对整体数据进行一个手势滚动，则数据源应使用this.data而非this.data.slice(this.startIndex, this.startIndex + this.starCount)。
2. PanGesture中手势需要触发合适的属性改变：需要新增位移变量，并通过手势触发位移变量的改变。
 
 

#### 修改建议

参考分析结论，完整示例代码如下：
 
```text
import { Position } from '@kit.ArkUI';


@Entry
@Component
struct StartPage {
  @State data: number[] = Array.from<number, number>({ length: 30 }, (_, i: number) => i + 1);
  radius: number = 250;
  starCount: number = 8; <em>// 平均分成8份</em>
  maxSize: number = 150;
  scaleStep: number = 0.8; <em>// 缩放比例递减，每边递减20%。</em>
  startIndex: number = 0;<em> // 控制滑动窗口的开始索引</em>
  @State moveDistance: number = 0; <em>// 新增位移变量（修改部分）</em>
  uiContext: UIContext | undefined = undefined;


  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }


 <em> // 计算每个点的坐标</em>
  private getStarPosition(index: number): Position {
    const angleStep = 180 / (this.starCount - 1); /<em>/ 平均分starCount份，间距starCount-1段</em>
    const angleDeg = Math.min(Math.max(180 - angleStep * index, -90), 270);
 <em>   // 从180°往0°递减</em>
    const angleRad = angleDeg * Math.PI / 180;
   <em> // 从右侧0度开始，逆时针画半圆。</em>
    const centerX = this.radius;
    const centerY = this.radius;
    const x = centerX + this.radius * Math.cos(angleRad);
    const y = centerY - this.radius * Math.sin(angleRad);


    return { x, y };
  }


  /<em>/ 计算每个点的缩放比例</em>
  private getScale(index: number): number {
    const centerIndex = Math.floor(this.starCount / 2);
    const distanceFromCenter = Math.abs(index - centerIndex);
    return Math.pow(this.scaleStep, distanceFromCenter);
  }


  build() {
    Stack() {
      Stack({ alignContent: Alignment.Center }) {
       <em> // 布置月亮图片（修改部分）</em>
        ForEach(this.data, (item: number, i: number) => {
          Stack() {
            <em>// 开发者需自行配置媒体资源文件</em>
            Image($r('app.media.vip_sn_star'))
              .width('100%')
              .height('100%');
            Text(item.toString())
              .fontSize(14)
              .fontColor('#FF61240D')
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%');
          }
          .animation({ duration: 200, curve: Curve.EaseInOut })
        <em>  // 根据位置透明度递减，具体数值需要根据具体情况调整</em>。
          .opacity(1 - 0.4 * (69 +
            (this.getStarPosition(i + this.moveDistance).y - this.maxSize * this.getScale(i + this.moveDistance) / 2)) /
            324)
          .rotate({ angle: -90 }) // 保持文字端正
          .width(this.maxSize * this.getScale(i + this.moveDistance))
          .height(this.maxSize * this.getScale(i + this.moveDistance))
        <em>  // 位置信息需要添加位移变量（修改部分）</em>
          .position({
            x: this.getStarPosition(i + this.moveDistance).x - this.maxSize * this.getScale(i + this.moveDistance) / 2,
            y: this.getStarPosition(i + this.moveDistance).y - this.maxSize * this.getScale(i + this.moveDistance) / 2
          });
        });
      }
      .margin({ left: -this.radius })
      .width(this.radius * 2)
      .height(this.radius * 2)
      .rotate({ angle: 90 });<em> // 组件旋转90，才符合UI需求。</em>


    <em>  // 增加一层覆盖在上面处理手势</em>
      Stack() {
      }
      .width(this.radius * 2)
      .height(this.radius * 2)
      .gesture(
      <em>  // 手势需要触发位移变量的改变（修改部分）</em>
        PanGesture({ direction: PanDirection.Vertical, distance: 20 })
          .onActionUpdate((event: GestureEvent) => {
            console.info(`月亮图片：onActionUpdate event.offsetY = + event.offsetY`);
            if (event.offsetY < -20) {
              this.uiContext?.animateTo({ duration: 200 }, () => {
                this.moveDistance -= 0.1;
              });
            } else if (event.offsetY > 20) {
             <em> // 向下滑：回退</em>
              this.uiContext?.animateTo({ duration: 200 }, () => {
                this.moveDistance += 0.1;
              });
            }
          })
          .onActionEnd((event: GestureEvent) => {
            console.info(`event: ${event}`);
          })
      );
    }
    .width('100%')
    .height('100%');
  }
}
```
 
改动后效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Z09cAhf7Szu7RdMC68rxqg/zh-cn_image_0000002658915011.png?HW-CC-KV=V1&HW-CC-Date=20260723T013112Z&HW-CC-Expire=86400&HW-CC-Sign=12BD18B9DA5CC0DC2611996F777422465A208CAEDD3863BC9C326038359EFA4C)
