# Flex布局Text自动换行时显示不全

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-946

#### 问题现象

在下面代码中，Flex布局使用alignItems: ItemAlign.Stretch进行拉伸，并使用clip进行裁剪时会出现部分字符被裁切显示不全。
 
```text
@Entry
@Component
struct Index {
  @State text: string = '1234567890123456789012345678901234567890123456789012345678901234567890123344';

  build() {
    Column() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Stretch }) {
          Column() {
            Text('xxxx')
          }
          .width(96)
          .flexShrink(0)

          Column() {
            Text('yyyy')
            Text('yyyy')
            Text(this.text) <em>// 这里在自动换行时，最后一行的字符被部分遮挡</em>
          }
          .flexGrow(1)
          .flexShrink(1)
          .padding(10)
          .borderWidth(1)
          .alignItems(HorizontalAlign.Start)
        }.width('90%')
        .border({
          width: 1,
          color: '#000000'
        })
      }.height('auto').clip(true)
      .justifyContent(FlexAlign.Center)

      Row() {
        Text(this.text)
      }.padding(12)
    }
  }
}
```
 
下面是字符显示不全的效果图。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/2SEPNyy0S1eVsr7otmjPEQ/zh-cn_image_0000002628401232.png?HW-CC-KV=V1&HW-CC-Date=20260811T005743Z&HW-CC-Expire=86400&HW-CC-Sign=51D2AE17C854965BA6431346F76BC14E0FC8C0CC2A900D468D903C55C2341CC3)

 
 

#### 背景知识

[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)组件可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。子元素的[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。
 
 

#### 问题定位

父组件设置的alignItems属性为[ItemAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#itemalign).Stretch时，子组件在交叉轴方向拉伸填充，拉伸效果由系统进行一个先期布局，不设置子组件的宽高时，会出现子组件溢出Flex区域的情况。
 
 

#### 分析结论

在Flex容器的子组件设置alignSelf属性，可使该子组件不应用父组件的alignItems属性，从而防止子组件被过度拉伸导致溢出。
 
 

#### 修改建议

可以给Flex容器中的Column组件增加alignSelf属性，Text子组件在Column父组件交叉轴的对齐格式会覆盖其alignItems设置，可以使Text子组件中的文本内容完整显示。
 
示例代码：
 
```text
@Entry
@Component
struct StretchDemo {
  text: string = '1234567890123456789012345678901234567890123456789012345678901234567890123344';

  build() {
    Column() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Stretch }) {
          Column() {
            Text('xxxx');
          }
          .width(96)
          .flexShrink(0);

          Column() {
            Text('yyyy');
            Text('yyyy');
            Text(this.text); <em>// 这里在自动换行时，最后一行的字符被部分遮挡</em>
          }
          .flexGrow(1)
          .flexShrink(1)
          .padding(10)
          .borderWidth(1)
          .alignItems(HorizontalAlign.Start)
          .alignSelf(ItemAlign.Start);
        }.width('90%')
        .border({
          width: 1,
          color: '#000000'
        });
      }.height('auto').clip(true)
      .justifyContent(FlexAlign.Center);

      Row() {
        Text(this.text);
      }.padding(12);
    };
  }
}
```
 
 
效果图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/f7PCnLzqQISMVYjs2Kn1QQ/zh-cn_image_0000002658800497.png?HW-CC-KV=V1&HW-CC-Date=20260811T005743Z&HW-CC-Expire=86400&HW-CC-Sign=9F55C8F30B4620CD15B2BB0AD997890CDC8C828A45FF4950BB30EE0DFFA9BC33)
