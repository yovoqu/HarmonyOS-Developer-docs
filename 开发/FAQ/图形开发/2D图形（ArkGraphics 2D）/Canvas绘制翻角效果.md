# Canvas绘制翻角效果

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-19

#### 问题现象

如何使用Canvas实现翻角效果，类似于书籍装帧的折角设计，使页面的翻角效果更加生动。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/o7UTOr17TL26s-xhPLgSZg/zh-cn_image_0000002628393352.png?HW-CC-KV=V1&HW-CC-Date=20260701T041025Z&HW-CC-Expire=86400&HW-CC-Sign=9DC37112CBB8ACE8000DF7676390AFDF59AF27DDD78E3AB356B274E4C480949A)

 
 

#### 背景知识

- [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)：提供画布组件，用于自定义绘制图形。
- [RenderingContextSettings](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#renderingcontextsettings)：用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。
- [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#renderingcontextsettings)：使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
- [quadraticCurveTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#quadraticcurveto)：创建二次贝赛尔曲线的路径。
- [arc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#arc)：绘制弧线路径。

 
 

#### 解决方案

使用CanvasRenderingContext2D中的moveTo，lineTo等函数绘制各个部分的线条，最后将线条连接回起点完成翻角效果。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Canvas(this.context)
        .height(200)
        .width('100%')
        .onReady(() => {
          this.context.moveTo(50, 0);
          this.context.quadraticCurveTo(55, 5, 55, 25); <em>// </em><em>左上角向右下的弧线</em>
          this.context.lineTo(55, 40); <em>// 竖直向下的竖线</em>
          this.context.arc(60, 40, 5, Math.PI, Math.PI / 2, true); <em>// 左下角的半圆弧线</em>
          this.context.lineTo(75, 45); <em>// 绘制水平横线</em>
          this.context.quadraticCurveTo(95, 45, 100, 50); <em>// </em><em>右下角的弧线</em>
          this.context.lineTo(50, 0);
          let gradient = this.context.createLinearGradient(50, 50, 75, 75);
          gradient.addColorStop(0, '#ccc');
          gradient.addColorStop(0.7, '#111');
          gradient.addColorStop(1, '#000');
          this.context.fillStyle = gradient;
          this.context.fill(); <em>// </em><em>对封闭的路径进行填充</em>
          this.context.beginPath(); <em>// </em><em>新建路径</em>
          this.context.moveTo(50, 0);
          this.context.lineTo(100, 50);
          this.context.lineTo(100, 0);
          this.context.lineTo(50, 0);
          this.context.closePath(); <em>// 闭合路径</em>
          this.context.fillStyle = '#ff6600';
          this.context.fill();
        });
    }
    .margin({ top: 200, left: 120 })
    .width('100%')
    .height('100%')
  }
}
```
