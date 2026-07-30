# 如何解决List组件部分分割线不显示的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-948

#### 问题现象

为List组件添加divider属性，部分分割线不显示，该如何解决？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct Index {
  scroller: Scroller | undefined;
  @State outBoxList: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

  build() {
    Column() {

      List({ scroller: this.scroller }) {
        ForEach(this.outBoxList, (item: string, index) => {
          ListItem() {
            Row() {
              Column() {
                Text('名字').fontSize(15)
                Text('数字').fontSize(12).fontColor(Color.Blue).margin({ top: 6 })
              }.layoutWeight(1).margin({ left: 12, right: 12 }).alignItems(HorizontalAlign.Start)
            }
            .height(70)
            .backgroundColor(Color.White)
            .width('100%')
            .padding({ left: 12, right: 12 })
            .onClick(() => {
            })
          }
        })
      }
     <em> // 设置分割线</em>
      .divider({
        strokeWidth: 0.4,
        color: Color.Black,
        startMargin: 0,
        endMargin: 0
      })
      .edgeEffect(EdgeEffect.None)
      .scrollBarWidth(0)
      .width('100%')
    }
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/LezhEN8_QeSh9_G6YB3xyw/zh-cn_image_0000002628401240.png?HW-CC-KV=V1&HW-CC-Date=20260701T041210Z&HW-CC-Expire=86400&HW-CC-Sign=EDD25E07C41ACF6CBFB3995C717271A0928A36F227EF9F578346ADAB603EDF82)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/zMEsZvnUQSyZJXnato99mw/zh-cn_image_0000002658800511.png?HW-CC-KV=V1&HW-CC-Date=20260701T041210Z&HW-CC-Expire=86400&HW-CC-Sign=0DF2871F5B31A0C33B53EA013A5ED957DB1C06B7B6A3356E5880C40C3DF01E61)

 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
- [divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#divider)：设置ListItem分割线样式，默认无分割线。
- [strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdivideroptions18对象说明)：分割线的线宽。
- [Divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider)：提供分隔器组件，分隔不同内容块/内容元素。

 
 

#### 问题定位
1. 查看代码中分割线基础配置是否正确：自定义divider属性时需要明确样式，否则可能不显示。
2. 使用DevEco Studio中的ArkUI Inspector排查列表项布局是否有冲突：避免列表项覆盖分割线。
3. 是否是属性本身规格。
4. 模拟器和真机运行问题代码出现的现象不一致，是否是其他问题影响。
 
 

#### 分析结论
1. 分割线基础配置正确。
2. 无布局冲突。
3. 默认设计隐藏了List组件首尾项的分割线。
4. divider属性的strokeWidth值设置为低于1时，模拟器和真机运行出现差异是因为分辨率等问题导致看不清晰。
 
 

#### 修改建议

模拟器和真机运行问题代码出现的现象不一致，divider属性的strokeWidth值设置为低于1时，模拟器由于分辨率问题导致看不清晰，真机的渲染逻辑更贴近实际环境，优先使用真机进行调试。解决方案如下：可以将divider中的strokeWidth值修改为1。也可以不使用divider属性，手动添加一个Divider组件作为分割线。
 
```text
@Entry
@Component
struct demo1 {
  scroller: Scroller | undefined;
  @State outBoxList: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

  build() {
    Column() {
      List({ scroller: this.scroller }) {
        ForEach(this.outBoxList, (item: string, index) => {
          ListItem() {
            Column() {
              Row() {
                Column() {
                  Text('名字').fontSize(18);
                  Text('数字').fontSize(16).fontColor(Color.Blue).margin({ top: 6 });
                }.layoutWeight(1).margin({ left: 12, right: 12 }).alignItems(HorizontalAlign.Start);
              }
              .height(70)
              .backgroundColor(Color.White)
              .width('100%')
              .padding({ left: 12, right: 12 });

              Column() {
            <em>    // 最后一项不加分割线，其余都加</em>
                if (index !== (this.outBoxList.length - 1)) {
                  Divider()
                    .strokeWidth(1)
                    .color('#e5e5e5')
                    .margin({ left: 16, right: 16 }); <em>// </em><em>与设计保持一致</em>
                }
              };
            };
          };
        });
      }
      .edgeEffect(EdgeEffect.None)
      .scrollBarWidth(0)
      .width('100%');
    };
  }
}
```
