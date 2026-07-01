# Canvas实现六边形雷达图

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-29

## Canvas实现六边形雷达图
 


##### 问题现象

如何基于Canvas实现六边形雷达图以展示不同能力的数据？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/w4hzU0C5S7yXAbsKNjFTKw/zh-cn_image_0000002628393358.png?HW-CC-KV=V1&HW-CC-Date=20260701T025834Z&HW-CC-Expire=86400&HW-CC-Sign=D62AA015C956C480521CF1A3CB5BA3B78B43EA957350922E00B072C939981B73)

 
 

##### 背景知识

- [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)组件用于自定义绘制图形，[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#onready)事件之后可使用Canvas相关API进行绘制。
- [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)可在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
- [Path2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d)支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

 
 

##### 解决方案

- 根据画布的中心点以及雷达图的半径，计算雷达图各点对应的坐标，并将这些坐标点存入positionList中。利用Path2D对象的moveTo方法和lineTo方法绘制折线图，并通过closePath方法闭合路径，最后使用stroke方法绘制边框。整个过程需绘制五个具有不同半径的六边形：
```text
for (let index = 0; index  // 背景
  private path2Db: Path2D = new Path2D();
  // 能力值展示
  private ratePath2Db: Path2D = new Path2D();
  // 计算正六边形的顶点坐标
  private baseRadius: number = 150;
  // 画布半径
  private canvasRadius: number = 200;
  private angleOffset: number = (Math.PI * 2) / 6;
  // 圈数
  private count: number = 5;
  // 各能力值
  private rateArray: number[] = [0.5, 1.0, 0.15, 0.7, 0.4, 0.65];
  // 各能力名称
  private nameList: string[] = ['推进', '战绩', '生存', '团战', '发育', '输出'];
  // 各能力对应的坐标点
  private positionList: PositionModel[] = [];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('400')
        .height('400')
        .backgroundColor(Color.White)
        .onReady(() => {
          // 绘制背景
          for (let index = 0; index   // 绘制能力值对应的路径
          for (let index = 0; index   // 绘制各坐标对应的名称
          this.context.font = '50px sans-serif';
          this.context.fillStyle = '#333333';
          for (let i = 0; i 
##### 总结

在需要对不同能力的数据进行更为直观展示与对比的场景中，可以利用Canvas组件进行自定义图形的绘制，从而实现上述雷达图的构建。
