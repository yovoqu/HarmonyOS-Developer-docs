# List组件实现自定义时间选择器

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1415

#### 问题现象

目前HarmonyOS官方提供的TextPicker组件没有横向滑动的能力，怎样实现横向滑动的时间选择器？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4EU6zWyDTXawMr-uLawZLw/zh-cn_image_0000002628763170.png?HW-CC-KV=V1&HW-CC-Date=20260730T072359Z&HW-CC-Expire=86400&HW-CC-Sign=E23FB56ECAC230FAC53E78AE55561074D9FA6856963D0F6D4481A7E25707F569)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/KwCOIg0sTcih3C14YNqXkA/zh-cn_image_0000002658962483.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072359Z&HW-CC-Expire=86400&HW-CC-Sign=EE4B4FC99A98DA4DA94AA16F1C0F734448169F8FB9082F9E2AA3AB186B16625B)

 
 

#### 背景知识

- [TextPicker组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)：滑动选择文本内容的组件，但是没有横向滑动的能力，目前只支持竖向滑动。
- [List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：是官方提供的常用的滚动组件之一，其接口[listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)可设置List组件排列方向，其Axis参数如下：

  
| 序号 | 名称 | 说明 |
| --- | --- | --- |
| 1 | Vertical | 方向为纵向。 |
| 2 | Horizontal | 方向为横向。 |
 
 
 

#### 解决方案

由于TextPicker组件没有横向滑动的能力，因此可以采用List滑动组件，实现横向滚动的时间选择器，采用[scrollSnapAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#scrollsnapalign10)属性使List中间项对齐，同时将中间的Item差异化处理来进行突出显示。
 
```text
@Entry
@Component
struct ListCustomTimePicker {
  private arr: string[] = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60'];
  @State centerIndex: number = 0;

  build() {
    Row() {
      List() {
        ForEach(this.arr, (item: number, index: number) => {
          ListItem() {
            Row() {
              Text('' + item)
              <em>  // 判断语句,当索引位置在显示的中间时，对该时间放大处理</em>
                .fontSize(index === this.centerIndex ? 30 : 18)
                .fontColor(index === this.centerIndex ? Color.Black : Color.Gray)
                .textAlign(TextAlign.Center);
            }
            .width('20%') <em>// 单行显示5个item</em>
            .height(50)
            .justifyContent(FlexAlign.Center);
          };
        }, (item: string) => item);
      }
      .scrollSnapAlign(ScrollSnapAlign.CENTER)<em> </em><em>// 中间项对齐</em>
      .listDirection(Axis.Horizontal)<em> </em><em>// List组件设置横向滚动</em>
      .scrollBar(BarState.Off)
      .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
        <em>// 获取屏幕中间item的索引值</em>
        this.centerIndex = centerIndex;
        console.info(`firstIndex：${firstIndex},lastIndex：${lastIndex}`);
      })
      .width('100%');
    }
    .width('100%')
    .height(50)
    .backgroundColor(0xDCDCDC);
  }
}
```
