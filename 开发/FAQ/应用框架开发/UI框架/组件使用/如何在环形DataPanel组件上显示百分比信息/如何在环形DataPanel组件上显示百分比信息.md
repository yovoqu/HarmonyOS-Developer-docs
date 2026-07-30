# 如何在环形DataPanel组件上显示百分比信息

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-981

#### 问题现象

如何在环形DataPanel组件上显示百分比信息，即DataPanel组件与百分比联动。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/lMLTCnI4Q8WUpC-51YY-eg/zh-cn_image_0000002658801071.png?HW-CC-KV=V1&HW-CC-Date=20260730T072336Z&HW-CC-Expire=86400&HW-CC-Sign=E853E3D89EDCED1BBCEB1CFC991483573E75F9BE33978EF1AE39DC5ACA920D05)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/m02YrxjZSsaP4quNJGQEfg/zh-cn_image_0000002628401804.png?HW-CC-KV=V1&HW-CC-Date=20260730T072336Z&HW-CC-Expire=86400&HW-CC-Sign=E8E36FC62AD42C181EC9467C2F7D70E98668F3FA5F0939FB6E0E62FEC5EDE8ED)

 
 

#### 背景知识

- [DataPanel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel)数据面板组件，用于将多个数据占比情况使用占比图进行展示。
- [DataPanelOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel#datapaneloptions对象说明)对象可以设置数据面板的数据源、最大值和类型。当类型为[DataPanelType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel#datapaneltype8枚举说明).Circle（环形数据面板）时可以设置[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel#strokewidth10)控制圆环粗细。当圆环粗细设置value大于圆环半径时，圆环粗细会自动设置为圆环半径的12%。
- [reduce](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array#reduce)对数组中的每个元素执行回调函数，将其结果作为累加值，并返回最终的结果。

 
 

#### 解决方案

可以使用[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)堆叠布局将百分比文本信息和DataPanel组件居中显示，让百分比文本刚好在环形数据面板中心。通过sin/cos还有距离和角度计算出文本相对圆环中心的坐标，[offset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#offset)控制文本根据坐标偏移。刚好让百分比信息显示在环形DataPanel组件上对应的位置。文本和坐标信息计算步骤如下：
 1. 通过reduce计算从0到每段数据结尾的总和，用该总和/圆环整体的值得到当前数据结尾所在的弧度。
```text
<em>// </em><em>获取从0到各个数据段结尾的弧度</em>
getRadian() {
  for (let i = 0; i < this.dataPanelList.length; i++) {
    let count = this.dataPanelList.reduce((accumulator, value, index) => {
      if (index <= i) {
        return accumulator + value;
      } else {
        return accumulator;
      }
    });
    this.radianList[i] = count / this.sum * Math.PI * 2;
  }
}
```

2. 获取每段数据的百分比文本。
```text
<em>// </em><em>获取百分比的文本</em>
getText() {
  let count = 0;
  for (let i = 0; i < this.dataPanelList.length - 1; i++) {
    this.textList[i] = Math.round(this.dataPanelList[i] / this.sum * 100);
    count += this.textList[i];
  }
  this.textList[this.dataPanelList.length-1] = 100 - count;
}
```

3. 通过DataPanel组件的尺寸的一半减去strokeWidth可以得到圆环的半径。
4. sin(弧度)*圆环半径和cos(弧度)*圆环半径的方式可以得到当前弧度下圆环外层的坐标信息，向内偏移半个strokeWidth就是百分比信息文本显示的位置。
```text
<em>// x</em><em>坐标：sin(弧度)*半径，y坐标：-cos(弧度)*半径</em>
.offset({
  x: Math.sin(item) * (this.dataPaneRadius - this.strokeWidth / 2),
  y: -Math.cos(item) * (this.dataPaneRadius - this.strokeWidth / 2)
})
```

 
完整示例参考如下：
 
```text
@Entry
@Component
struct DataPanelExample {
  @State dataPanelList: number[] = [10, 20, 40, 30];
  sum: number = this.dataPanelList.reduce((accumulator, value) => accumulator + value);
  @State radianList: number[] = [];<em> </em><em>// 从0到各个分段结尾的弧度</em>
  @State textList: number[] = [];<em> </em><em>// 每个数据分段的百分比文本</em>
  dataPanelSize: number = 300; <em>// 数据面板组件宽度</em>
  strokeWidth: number = 40; <em>// </em><em>圆环粗细，不能超过dataPanelSize/4</em>
  dataPaneRadius: number = this.dataPanelSize / 2 - this.strokeWidth; <em>// 数据面板中圆环的半径</em>

  aboutToAppear(): void {
    this.getRadian();
    this.getText();
  }

 <em> // 获取从0到各个数据段结尾的弧度</em>
  getRadian() {
    for (let i = 0; i < this.dataPanelList.length; i++) {
      let count = this.dataPanelList.reduce((accumulator, value, index) => {
        if (index <= i) {
          return accumulator + value;
        } else {
          return accumulator;
        }
      });
      this.radianList[i] = count / this.sum * Math.PI * 2;
    }
  }

  <em>// 获取百分比的文本</em>
  getText() {
    let count = 0;
    for (let i = 0; i < this.dataPanelList.length - 1; i++) {
      this.textList[i] = Math.round(this.dataPanelList[i] / this.sum * 100);
      count += this.textList[i];
    }
    this.textList[this.dataPanelList.length-1] = 100 - count;
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.Center }) {
        DataPanel({ values: this.dataPanelList, max: 0, type: DataPanelType.Circle })
          .width(this.dataPanelSize)
          .height(this.dataPanelSize)
          .strokeWidth(this.strokeWidth)
          .backgroundColor('#ffd6f7ff');
        ForEach(this.radianList, (item: number, index: number) => {
          Text(`${this.textList[index]}%`)
        <em>  // x坐标：sin(弧度)*半径，y坐标：-cos(弧度)*半径</em>
            .offset({
              x: Math.sin(item) * (this.dataPaneRadius - this.strokeWidth / 2),
              y: -Math.cos(item) * (this.dataPaneRadius - this.strokeWidth / 2)
            })
            .fontColor('#fff')
            .fontSize(this.strokeWidth / 2.5); <em>// 文本大小根据圆环粗细设置</em>
        });
      };
    }
    .width('100%')
    .height('100%');
  }
}
```
