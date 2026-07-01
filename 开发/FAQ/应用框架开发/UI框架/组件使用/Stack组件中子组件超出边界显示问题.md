# Stack组件中子组件超出边界显示问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1650

#### 问题现象

- 场景一：Stack组件中Text子组件因边缘约束导致宽度压缩、文字溢出，如何设置Text宽度自适应或调整Stack布局策略，使其保持原始文本宽度并扩展容器边界。代码如下：
```text
@Entry
@Component
struct StackPageOne {
  build() {
    Column() {
      Stack() {
        Text(' 测试 ')
          .borderRadius(10)
          .fontSize(40)
          .margin({ left: 150 })
          .backgroundColor('#989ba1')
          .maxLines(1);
      }
      .width(200)
      .height(100)
      .borderRadius(10)
      .backgroundColor('#f1f3f5');
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
 效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/x7ZF0kadST2_mzfO1wmccA/zh-cn_image_0000002659060259.png?HW-CC-KV=V1&HW-CC-Date=20260701T041248Z&HW-CC-Expire=86400&HW-CC-Sign=CA3EE1357EC4A65FF1BB47E097570C6C8C21DD06CA4EB995D715A1799A689B2D)

- 场景二：如何实现图片超出容器右上角展示效果？

 
 

#### 背景知识

- [position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)：属性属于通用属性，可对适用组件应用绝对定位，使子组件相对于最近的定位组件元素进行精确布局。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
- [margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)：设置组件的外边距属性。在布局计算过程中，外边距被视为组件尺寸的一部分，从而影响组件位置。

 
 

#### 解决方案

- 场景一：Stack容器的默认层叠布局模式限制了Text组件的宽度，通过.margin({ left: 150 })设置的左侧外边距仅调整了文本位置，若需实现Text组件突破父容器边界显示，可通过绝对定位（position）明确设置其位置和宽度，从而使Text组件能够突破Stack容器边界，完整显示内容。

  
```text
@Entry
@Component
struct StackPageTwo {
  build() {
    Column() {
      Stack() {
        Text(' 测试测试 ')
          .borderRadius(10)
          .fontSize(30)
          .backgroundColor('#989ba1')
          .maxLines(1)
          .position({
            top: 25,
            right: 0,
            left: 100
          });
      }
      .width(200)
      .height(100)
      .borderRadius(10)
      .backgroundColor('#f1f3f5');
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
 效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/OMC4pBNYRImseiyxQGEOlQ/zh-cn_image_0000002628820886.png?HW-CC-KV=V1&HW-CC-Date=20260701T041248Z&HW-CC-Expire=86400&HW-CC-Sign=385C9D14A840DC005A95AFC1CA3CBB9A53AF1B2A742FC90E0FAB2A0FDEB52156)

- 场景二：使用Stack容器的默认层叠布局模式结合子组件position属性实现图片超出父组件右上角堆叠效果。示例代码如下：

  
```json
@Entry
@Component
struct StackPageThree {
  num: number[] = [1, 2];

  build() {
    Column() {
      ForEach(this.num, (item: number) => {
        Stack() {
          Text()
            .borderRadius(10)
            .backgroundColor('#989ba1')
            .maxLines(1)
            .width(50)
            .height(50)
            .position({
              top: -20,
              right: 0,
              left: 180
            });

          Text(`${item}`);
        }
        .margin({ top: 50 })
        .width(200)
        .height(100)
        .borderRadius(10)
        .backgroundColor('#f1f3f5');
      }, (item: number) => JSON.stringify(item));
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
 效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/5MzM7zh0R1e6CbDYTDlQTA/zh-cn_image_0000002659020191.png?HW-CC-KV=V1&HW-CC-Date=20260701T041248Z&HW-CC-Expire=86400&HW-CC-Sign=4E937E1D027DE523A1E1BE1522BFBF9A85B5CD29C6567A0B794A3C9884F0AFF9)
