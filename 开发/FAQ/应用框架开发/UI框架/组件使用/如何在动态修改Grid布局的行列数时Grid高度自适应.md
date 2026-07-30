# 如何在动态修改Grid布局的行列数时Grid高度自适应

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1189

#### 问题现象

使用Grid组件渲染时，如何在修改Grid行列数时Grid高度能够自适应？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6ZXdxzeyRhqpCTYNuipfbA/zh-cn_image_0000002628752864.png?HW-CC-KV=V1&HW-CC-Date=20260701T041303Z&HW-CC-Expire=86400&HW-CC-Sign=B129871533AF0BD523329EE453407E9540671BDF8A995B0DAF62F63B3C6D4B3D)

 
 

#### 背景知识

- [rowsTemplate属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#rowstemplate)、[columnsTemplate属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#columnstemplate)：设置当前网格布局行、列的数量。参数为'1fr 1fr 1fr'字符串形式，代表均分为3行或3列，不设置时默认1行或1列。
- [maxCount属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#maxcount8)、[minCount属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#mincount8)：设置Grid组件能显示的最大或最小行列数。
- [cellLength属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#celllength8)：可设置1行的高度或1列的宽度。
- [layoutDirection属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#layoutdirection8)：可设置布局的主轴方向。

 
 

#### 解决方案

当Grid组件不设置height、width属性或者将其设置为auto时，会自适应GridItem的总高度和总宽度，设置maxCount属性、minCount属性设定最大最小行列数，通过cellLength属性设置行列的宽高。
 
> [!NOTE]
> 当Grid组件的rowsTemplate属性、columnsTemplate属性都不设置时，layoutDirection属性、cellLength属性、maxCount属性、minCount属性才可生效。

 
完整示例代码如下：
 
```text
@Entry
@Component
struct GridExample {
  @State numbers: string[] = [];
  @State rowMaxCount: number = 5;
  @State cellHeight: number = 50;
  @State itemNumber: number = 30;

  aboutToAppear() {
    for (let i = 1; i <= 30; i++) {
      this.numbers.push(i.toString());
    }
  }

  build() {
    Scroll() {
      Column({ space: 5 }) {
        Text('修改一行最大显示个数+1')
          .fontSize(15)
          .onClick(() => {
          <em>  // 当单行最大的个数超出屏幕宽度时，即使最大个数增加也不会改变布局。</em>
            this.rowMaxCount += 1;
          });
        Text('修改一行最大显示个数-1')
          .fontSize(15)
          .onClick(() => {
           <em> // 避免单行最大个数小于最小个数，该示例一行最小设置两个GridItem。</em>
            if (this.rowMaxCount > 2) {
              this.rowMaxCount -= 1;
            }
          });
        Text('修改一行行高-10')
          .fontSize(15)
          .onClick(() => {
         <em>   // 限制最小行高为40</em>
            if (this.cellHeight > 40) {
              this.cellHeight -= 10;
            }
          });
        Text('修改一行行高+10')
          .fontSize(15)
          .onClick(() => {
            this.cellHeight += 10;
          });
        Text('增加Item个数')
          .fontSize(15)
          .onClick(() => {
            this.itemNumber += 1;
            this.numbers.push(this.itemNumber.toString());
          });
        Grid() {
          ForEach(this.numbers, (day: string) => {
            GridItem() {
              Text(day)
                .fontSize(16);
            }
            .width(40)
            .height(40)
            .borderWidth(2)
            .borderColor(Color.Black);
          }, (day: string) => day);
        }
        .columnsGap(5)
        .rowsGap(5)
        .backgroundColor(0xAFEEEE)
        .maxCount(this.rowMaxCount)
        .minCount(2) <em>// GridDirection.Row的模式下，该属性表示一行最少放置的个数，本示例为两个。</em>
        .cellLength(this.cellHeight)
        .layoutDirection(GridDirection.Row);
      }
      .width('100%')
      .margin({ top: 5 })
      .align(Alignment.Center);
    };
  }
}
```
