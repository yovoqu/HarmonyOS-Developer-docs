# 如何设置Text组件的缩进避让

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-625

#### 问题现象

当Text组件与其他组件堆叠出现时，Text的文字内容需获取其他组件的宽高数据，进行缩进避让。
 
 

#### 背景知识

- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
- [RelativeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer)，相对布局，子组件间通过相对位置的布局，实现多个组件层叠显示的效果。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)，获取组件的组件大小、位置信息。
- [textIndent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textindent10)，设置Text组件首行文本缩进。
- [ContainerSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan)组件为Text组件的子组件，用于统一管理多个Span、ImageSpan的背景色及圆角弧度。可以包含Span、ImageSpan子组件。

 
 

#### 解决方案

- **方案一**：问题描述提到组件堆叠，则可用Stack布局，通过设置缩进，为文本标签留下空间。
```text
@Entry
@Component
struct ExampleOne {
  private dynamicText: string = '标签';

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Text('这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容')
        .fontSize(30)
        .textIndent(60)
        .width('100%')

      Text(this.dynamicText)
        .fontSize(20)
        .width(50)
        .border({ width: 1, color: Color.Black, radius: 10 })
        .textAlign(TextAlign.Center)
    }
    .padding(20)
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XXMdXGLxSpyXpdpGr_RXxw/zh-cn_image_0000002658913485.png?HW-CC-KV=V1&HW-CC-Date=20260701T041213Z&HW-CC-Expire=86400&HW-CC-Sign=61F3F0C6DAC30776BBAB7918C8A75C1116F3EC36BED20731E9B8BCFE05330E16)

- **方案二**：获取其他组件宽度并设置Text组件的缩进避让。1. 在通过RelativeContainer相对布局，实现标题Row组件和内容Text组件的相同位置显示，但此时两个组件内容会有重叠遮挡。

2. 通过onAreaChange获取标题Row组件的宽度信息（this.titleWidth），转换为number类型。
```json
Row() {
  Text('短剧·中国版教父')
}
.justifyContent(FlexAlign.Center)
.backgroundColor('#a3cf62')
.padding(4)
.borderRadius(4)
.id('row1')
.alignRules({
  top: { anchor: 'text', align: VerticalAlign.Top },
  left: { anchor: 'text', align: HorizontalAlign.Start }
})
.onAreaChange((oldValue: Area, newValue: Area) => {
  this.sizeValue = JSON.stringify(newValue);
  this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); <em>// </em><em>获取标题组件的宽度</em>
})
```


3. 配置Text组件的首行缩进长度为第二步获取的Row组件的宽度（this.titleWidth），实现文字避让。
```text
Text(this.message)
  .key('text')
  .maxLines(this.lines)
  .lineHeight(26)
  .textIndent(this.titleWidth + 2)
```


  完整示例参考如下：

  
```json
const COLLAPSE_LINES: number = 2;

@Entry
@Component
struct ExampleTwo {
  private lines: number = COLLAPSE_LINES;
  @State sizeValue: string = '';
  @State titleWidth: number = 0;
  private message: string = '这里是详情内容，这里是详情内容，这里是详情内容，这里是详情内容';

  build() {
    RelativeContainer() {
      Text(this.message)
        .key('text')
        .maxLines(this.lines)
        .lineHeight(26)
        .textIndent(this.titleWidth + 2)
      Row() {
        Text('短剧·中国版教父')
      }
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#a3cf62')
      .padding(4)
      .borderRadius(4)
      .id('row1')
      .alignRules({
        top: { anchor: 'text', align: VerticalAlign.Top },
        left: { anchor: 'text', align: HorizontalAlign.Start }
      })
      .onAreaChange((oldValue: Area, newValue: Area) => {
        this.sizeValue = JSON.stringify(newValue);
        this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); <em>// </em><em>获取标题组件的宽度</em>
      })
    }
    .height('auto')
    .borderWidth(1)
    .margin({ top: 100, left: 8, right: 8 })
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/dLtkq2N1TuCblRA-N2Qsew/zh-cn_image_0000002658793535.png?HW-CC-KV=V1&HW-CC-Date=20260701T041213Z&HW-CC-Expire=86400&HW-CC-Sign=4E062853368C36CDBE7D158CE81490F38FA20770F7F0A8E62FE4995AE39EC5B3)


 
- **方案三**：可以使用ContainerSpan组件，作为设置Text组件的缩进避让的替代方案，可参考官方文档[通过attributemodifier设置背景样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan#示例2通过attributemodifier设置背景样式)。可在组件内使用Span、ImageSpan组件。但此方法不支持通用属性和通用事件，有一定局限性。
