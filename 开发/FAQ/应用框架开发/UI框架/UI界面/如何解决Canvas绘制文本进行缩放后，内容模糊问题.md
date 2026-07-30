# 如何解决Canvas绘制文本进行缩放后，内容模糊问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-914

#### 问题现象

当对组件添加scale以实现放大效果时，Text组件所渲染的文本仍能保持清晰可辨，而通过Canvas组件绘制的文本则会出现模糊现象。
 
```text
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State textScale: number = 1

  build() {
    Column() {
      Button('点击').onClick(() => {
        this.textScale = 5
      })
      Text('hello')
        .scale({ x: this.textScale, y: this.textScale })
        .margin({top:50})
      Column() {
        Canvas(this.context)
          .width('100%')
          .height(400)
          .onReady(() => {
            this.context.font = '70px sans-serif';
           <em> // 描边宽度</em>
            this.context.lineWidth = 4;
           <em> // 填充颜色</em>
            this.context.fillStyle = 'black';
            <em>// </em><em>填充文本</em>
            this.context.fillText('hello', 180,200);
          })
      }
      .scale({ x: this.textScale, y: this.textScale })

    }
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/yv_EW9lLRAeNBwXne_4Kog/zh-cn_image_0000002628399762.png?HW-CC-KV=V1&HW-CC-Date=20260701T041209Z&HW-CC-Expire=86400&HW-CC-Sign=43F6E4A2166EE1EC21F0DC27DE19DE84F984343F67396BD459D3A1AA860225DA)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_tiLkGp5QuWMwLZ6ejpzPg/zh-cn_image_0000002658799031.png?HW-CC-KV=V1&HW-CC-Date=20260701T041209Z&HW-CC-Expire=86400&HW-CC-Sign=B32BEBE7624D3C9F9CC8A9C79608FA967F38D972537E93086BD80727DCCD20DF)

 
 

#### 背景知识

[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)对象和[OffscreenCanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
 
 

#### 解决方案

上述现象的出现是由于对Canvas画布进行了整体缩放操作，导致文字显示模糊。为解决此问题，需先使用[clearRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d#clearrect)方法清除当前画布内容，随后在放大比例下重新绘制文字内容，从而保证文字的清晰度。
 
```text
@Entry
@Component
struct Solution {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State textScale: number = 1;

  onDrawText() {
   <em> // 文本字体大小</em>
    this.context.font = `${70 * this.textScale}px sans-serif`;
    <em>// </em><em>填充颜色</em>
    this.context.fillStyle = 'black';
  <em>  // 填充文本</em>
    this.context.fillText('hello', 180, 200);
  }

  build() {
    Column() {
      Button('点击').onClick(() => {
        this.textScale = 4;
        <em>// </em><em>清除画布</em>
        this.context.clearRect(0, 0, 500, 200);
        this.onDrawText();
      })
      Text('hello')
        .scale({ x: this.textScale, y: this.textScale })
        .margin({ top: 50 })
      Column() {
        Canvas(this.context)
          .width(500)
          .height(200)
          .onReady(() => {
            this.onDrawText();
          })
      }
    }
  }
}
```
