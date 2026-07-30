# 如何使用Canvas绘制饼状图

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-650

#### 问题现象

如何使用Canvas绘制饼状图以展示不同类型的数据占比？问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/9Hi6rLyPSoa4qhkEAdXibg/zh-cn_image_0000002628554406.png?HW-CC-KV=V1&HW-CC-Date=20260730T072500Z&HW-CC-Expire=86400&HW-CC-Sign=2B73AD884AFB2B59AAE854256A879B68A011ACF199BA5E6AB752B33A9FB21B72)

 
 

#### 背景知识

- [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)：是一种画布组件，用于自定义绘制图形，绘制对象可以是基础形状、文本、图片等。
- [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)：是Canvas组件的参数，可使用它在Canvas画布上进行绘制，绘制对象可以是矩形、文本、图片等。

 
 

#### 解决方案

使用Canvas，根据各个分类对应的占比，绘制扇形，最后组成饼状图。具体步骤如下：
 1. 根据指定数组填装数据，并且计算出总量。
```text
class SectorInfo {
  name: string = ''; <em>// </em><em>名称</em>
  data: number = 0; <em>// </em><em>数据</em>
  color: string = ''; <em>// 颜色</em>
  fontSize: number = 14;<strong style="color: rgb(181,106,1);"> </strong><em>// 字体大小</em>
  radius: number = 40;<em> </em><em>// 半径</em>
}
```
 
```text
aboutToAppear(): void {
 <em> // 装载模拟数据</em>
  const categories = ['视频广告', '搜索引擎', '直接访问', '邮件营销', '联盟广告'];
  const dataCount = [1, 2, 1, 3, 1];
  const colorArr =
  ['#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6 '];
  for (let index = 0; index < categories.length; index++) {
    let sectorInfo = new SectorInfo();
    sectorInfo.name = categories[index];
    sectorInfo.data = dataCount[index];
    sectorInfo.color = colorArr[index];
    this.allData += dataCount[index];
    this.sectorInfoArr.push(sectorInfo);
    if (this.maxData < dataCount[index]) {
      this.maxData = dataCount[index];
    }
    if (this.minData > dataCount[index]) {
      this.minData = dataCount[index];
    }
  }
}
```

2. 根据当前分类的数据和总数据占比，计算出扇形的起始角度和终点角度。
```text
drawChart() {
  this.context.clearRect(0, 0, this.centerX * 2, this.centerY * 2);
 <em> // 上一个扇形的结束角度</em>
  let lastEndAngle: number = -Math.PI / 2;
  for (let index = 0; index < this.sectorInfoArr.length; index++) {
    const element = this.sectorInfoArr[index];
   <em> // 计算当前扇形的起始角度和终点角度</em>
    let startAngle: number = lastEndAngle;
    let endAngle: number = lastEndAngle + element.data / this.allData * 2 * Math.PI;
    if (this.isTypeChange) {
      element.radius = this.radius * (0.5 + (element.data - this.minData) / this.maxData / 2);
    } else {
      element.radius = this.radius;
    }
    this.drawSector(startAngle, endAngle, element);
    this.drawBrokenLineAndText(startAngle, endAngle, element);
    lastEndAngle = endAngle;
  }
}
```

3. 根据扇形的起始角度和终点角度，以及对应的数据信息绘制扇形。
```text
drawSector(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
  this.context.beginPath();
  this.context.arc(this.centerX, this.centerY, sectorInfo.radius, startAngle, endAngle);
  this.context.lineWidth = sectorInfo.radius * 2;
  this.context.strokeStyle = sectorInfo.color;
  this.context.stroke();
  this.context.restore();
}
```

4. 根据扇形的起始角度和终点角度，以及对应的数据信息绘制折线和文字。
```text
drawBrokenLineAndText(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
  let angle = endAngle - startAngle;
  let brokenLineLength: number = 20;
  let brokenLineLengthTemp: number = 15;
 <em> // 计算扇形中心角度</em>
  let centerAngle = startAngle + angle / 2;
  let r = sectorInfo.radius * 2 + brokenLineLength / 2;
 <em> // 计算折线起始点</em>
  let startX = this.centerX + (r - brokenLineLength) * Math.cos(centerAngle);
  let startY = this.centerY + (r - brokenLineLength) * Math.sin(centerAngle);
 <em> // 计算折线转折点</em>
  let brokenX = this.centerX + r * Math.cos(centerAngle);
  let brokenY = this.centerY + r * Math.sin(centerAngle);
  let endX = brokenX;
  let endY = brokenY;
 <em> // 添加文字属性</em>
  this.context.textBaseline = 'middle';
  this.context.fillStyle = sectorInfo.color;
  this.context.font = this.getUIContext().fp2px(sectorInfo.fontSize) + 'px sans-serif';
<em>  // 获取文本</em>
  let textWidth = this.context.measureText(sectorInfo.name).width;
  let textHeight = this.context.measureText(sectorInfo.name).height;
  let textX = endX;
  let textY = endY - textHeight + 5;
  let lastX = 0;
<em>  // 根据文字计算折线终点，根据角度单位判断折线左右方向，以及文字的起点</em>
  if (centerAngle < Math.PI / 2) {
    this.context.textAlign = 'right';
    endX = brokenX + brokenLineLengthTemp + textWidth;
    textX = brokenX + brokenLineLengthTemp + textWidth;
    lastX = endX - 27;
  } else {
    this.context.textAlign = 'left';
    endX = brokenX - brokenLineLengthTemp - textWidth;
    textX = endX;
    lastX = endX + 27;
  }
 <em> // 绘制折线</em>
  this.context.beginPath();
  this.context.lineWidth = 2;
  this.context.strokeStyle = sectorInfo.color;
  this.context.moveTo(startX, startY);
  this.context.lineTo(brokenX, brokenY);
  this.context.lineTo(lastX, endY);
 <em> // 填充文字</em>
  this.context.fillText(sectorInfo.name, textX, textY);
  this.context.stroke();
}
```

5. 完整示例参考如下：
```text
class SectorInfo {
  name: string = ''; <em>// 名称</em>
  data: number = 0; <em>// </em><em>数据</em>
  color: string = ''; <em>// 颜色</em>
  fontSize: number = 14;<em> </em><em>// 字体大小</em>
  radius: number = 40;<em> </em><em>// 半径</em>
}

@Entry
@Component
struct drawPieChart {
  @State sectorInfoArr: Array<SectorInfo> = [];
  @State @Watch('drawChart') isTypeChange: boolean = false;
 <em> // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。</em>
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  <em>// 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。</em>
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private centerX: number = 0;
  private centerY: number = 0;
  private radius: number = 40;
  private allData: number = 0;<em> </em><em>// 总数</em>
  private maxData: number = 40;<em> </em><em>// 最大值</em>
  private minData: number = 20; <em>// </em><em>最小值</em>

 <em> // 绘制扇形</em>
  drawSector(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
    this.context.beginPath();
    this.context.arc(this.centerX, this.centerY, sectorInfo.radius, startAngle, endAngle);
    this.context.lineWidth = sectorInfo.radius * 2;
    this.context.strokeStyle = sectorInfo.color;
    this.context.stroke();
    this.context.restore();
  }

 <em> // 绘制折线和文字</em>
  drawBrokenLineAndText(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
    let angle = endAngle - startAngle;
    let brokenLineLength: number = 20;
    let brokenLineLengthTemp: number = 15;
  <em>  // 计算扇形中心角度</em>
    let centerAngle = startAngle + angle / 2;
    let r = sectorInfo.radius * 2 + brokenLineLength / 2;
   <em> // 计算折线起始点</em>
    let startX = this.centerX + (r - brokenLineLength) * Math.cos(centerAngle);
    let startY = this.centerY + (r - brokenLineLength) * Math.sin(centerAngle);
  <em>  // 计算折线转折点</em>
    let brokenX = this.centerX + r * Math.cos(centerAngle);
    let brokenY = this.centerY + r * Math.sin(centerAngle);
    let endX = brokenX;
    let endY = brokenY;
  <em>  // 添加文字属性</em>
    this.context.textBaseline = 'middle';
    this.context.fillStyle = sectorInfo.color;
    this.context.font = this.getUIContext().fp2px(sectorInfo.fontSize) + 'px sans-serif';
   <em> // 获取文本</em>
    let textWidth = this.context.measureText(sectorInfo.name).width;
    let textHeight = this.context.measureText(sectorInfo.name).height;
    let textX = endX;
    let textY = endY - textHeight + 5;
    let lastX = 0;
  <em>  // 根据文字计算折线终点，根据角度单位判断折线左右方向，以及文字的起点</em>
    if (centerAngle < Math.PI / 2) {
      this.context.textAlign = 'right';
      endX = brokenX + brokenLineLengthTemp + textWidth;
      textX = brokenX + brokenLineLengthTemp + textWidth;
      lastX = endX - 27;
    } else {
      this.context.textAlign = 'left';
      endX = brokenX - brokenLineLengthTemp - textWidth;
      textX = endX;
      lastX = endX + 27;
    }
   <em> // 绘制折线</em>
    this.context.beginPath();
    this.context.lineWidth = 2;
    this.context.strokeStyle = sectorInfo.color;
    this.context.moveTo(startX, startY);
    this.context.lineTo(brokenX, brokenY);
    this.context.lineTo(lastX, endY);
 <em>   // 填充文字</em>
    this.context.fillText(sectorInfo.name, textX, textY);
    this.context.stroke();
  }

  aboutToAppear(): void {
  <em>  // 装载模拟数据</em>
    const categories = ['视频广告', '搜索引擎', '直接访问', '邮件营销', '联盟广告'];
    const dataCount = [1, 2, 1, 3, 1];
    const colorArr =
      ['#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6 '];
    for (let index = 0; index < categories.length; index++) {
      let sectorInfo = new SectorInfo();
      sectorInfo.name = categories[index];
      sectorInfo.data = dataCount[index];
      sectorInfo.color = colorArr[index];
      this.allData += dataCount[index];
      this.sectorInfoArr.push(sectorInfo);
      if (this.maxData < dataCount[index]) {
        this.maxData = dataCount[index];
      }
      if (this.minData > dataCount[index]) {
        this.minData = dataCount[index];
      }
    }
  }

  drawChart() {
    this.context.clearRect(0, 0, this.centerX * 2, this.centerY * 2);
  <em>  // 上一个扇形的结束角度</em>
    let lastEndAngle: number = -Math.PI / 2;
    for (let index = 0; index < this.sectorInfoArr.length; index++) {
      const element = this.sectorInfoArr[index];
    <em>  // 计算当前扇形的起始角度和终点角度</em>
      let startAngle: number = lastEndAngle;
      let endAngle: number = lastEndAngle + element.data / this.allData * 2 * Math.PI;
      if (this.isTypeChange) {
        element.radius = this.radius * (0.5 + (element.data - this.minData) / this.maxData / 2);
      } else {
        element.radius = this.radius;
      }
      this.drawSector(startAngle, endAngle, element);
      this.drawBrokenLineAndText(startAngle, endAngle, element);
      lastEndAngle = endAngle;
    }
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('90%')
        .height('40%')
        .backgroundColor('#fff5f5f1')
        .onAreaChange((oldArea: Area, newArea: Area) => {
       <em>   // 计算饼图的中心点</em>
          this.centerX = Number(newArea.width) / 2;
          this.centerY = Number(newArea.height) / 2;
          this.drawChart();
        })
        .onReady(() => {
          console.info('onReady');
        })
      Button('切换状态')
        .onClick(() => {
          this.isTypeChange = !this.isTypeChange;
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
