# 如何根据单行Item数量动态调整布局

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-674

#### 问题现象

如何使用Grid组件实现布局只有一行，宽度固定，横向排列，当Item数量小于5时，Item宽度按照数量均分，当Item数量大于5时指定宽度且横向可以滚动的效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/I4wuIlR5Ss6BzPr1j81tcw/zh-cn_image_0000002658913891.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072324Z&HW-CC-Expire=86400&HW-CC-Sign=DB9B9D24BA7661DD3F08674CE7BB9A04873DE3F92D0ABD2D47ABF07244FF2937)

 
 

#### 背景知识

- [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
- [rowsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#rowstemplate)：设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。
- [columnsGap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#columnsgap)：设置列与列的间距。设置为小于0的值时，按默认值显示。
- [display.getDefaultDisplaySync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)：获取当前默认的[display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)对象。
- [px2vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12)：将px单位的数值转换为以vp为单位的数值。

 
 

#### 解决方案

获取当前屏幕的宽度，当Item数量大于5时，Item宽度指定为100vp，当Item数量小于5时，动态设置Item宽度。
 
```text
import { display } from '@kit.ArkUI';

@Entry
@Component
struct HorizontalIndex {
  @State screenWidth: number = 0;
  @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7];

  aboutToAppear(): void {
   <em> // 使用display.getDefaultDisplaySync()方法获取当前屏幕宽度</em>
    this.screenWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
  }

  getItemWidth(): number {
  <em>  // 当Item数量大于5时，宽度指定为100</em>
    if (this.arr.length > 5) {
      return 100;
    } else {
    <em>  // 当Item数量小于5时，Item宽度按照数量均分</em>
      return (this.screenWidth - (this.arr.length - 1) * 10) / this.arr.length;
    }
  }

  build() {
    Column() {
      Grid() {
        ForEach(this.arr, (num: number) => {
          GridItem() {
            Column() {
              Text(`${num}`)
                .fontColor(Color.White);
            }
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
            .backgroundColor(Color.Blue)
            .width(this.getItemWidth())
            .height(100);
          };
        });
      }
     <em> // 设置当前网格布局行的数量为1</em>
      .rowsTemplate('1fr')
      .height(100)
    <em>  // 设置列与列的间距为10</em>
      .columnsGap(10)
      .width('100%')
      .backgroundColor('#fafafa');

      Button('数量改变')
        .margin({ top: 20 })
        .onClick(() => {
          this.arr = [0, 1, 2, 3,];
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
