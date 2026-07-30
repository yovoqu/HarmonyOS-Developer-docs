# 如何实现Text字号自适应缩放与省略

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-963

#### 问题现象

如何让Text组件在文字显示时首先自动调整字号以自适应容器大小，当缩小到指定最小字号后仍无法完整显示时，自动触发省略号显示？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/LRU0cDOjQGubexsHdkHQBQ/zh-cn_image_0000002658920895.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072505Z&HW-CC-Expire=86400&HW-CC-Sign=6C5AA6DEE17FB5D9435820824B3A44AC2666F2BD3A76622CB10E957BA8E0F0C9)

 
 

#### 背景知识

- [ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)：设置省略位置。ellipsisMode属性仅在内联模式下生效，需要配合overflow设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。
- [maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes#maxfontsize18)：设置文本最大显示字号。
- [minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes#minfontsize18)：设置文本最小显示字号。

 
 

#### 解决方案

要实现字号缩放与省略号的触发关系。具体步骤如下：
 1. 定义文本组件时，需同时指定最大/最小字号范围。
2. 设置父容器的尺寸限制条件。
3. 配置文本溢出规则以实现单行显示和省略策略。
4. 当缩放至最小字号仍无法完整显示时，触发省略逻辑。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct TextDemo {
  @State message: string = '';

  build() {
    Column({ space: 30 }) {
      TextInput({ text: this.message })
        .onChange((value: string) => {
         <em> // 文本内容发生变化时触发该回调</em>
          this.message = value;
        })
      Row() {
        Text('大')
          .width(40)
          .height(40)
          .backgroundColor(Color.Orange)
          .fontSize(35)
        Text(this.message)
          .maxFontSize(30)
          .minFontSize(15)
          .constraintSize({
            minWidth: 20,
            maxWidth: '100%'
          })
          .ellipsisMode(EllipsisMode.END)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .maxLines(1)
          .textAlign(TextAlign.Center)
          .fontColor(Color.Black)
          .fontWeight(500)
          .layoutWeight(1)
          .height(40)
        Text('小')
          .width(40)
          .height(40)
          .backgroundColor(Color.Orange)
          .fontSize(15)
      }
      .width('100%')
      .height(40)

    }
    .height('100%')
    .width('100%')
  }
}
```
 
 

#### 常见FAQ

Q：为什么使用了EllipsisMode.CENTER会使minFontSize失效？
 
A：为了保证中间省略的视觉效果，系统会强制使用最大字号，即使它会导致文字超出容器，从而触发省略。
 
Q：为什么EllipsisMode.END可以使用minFontSize？
 
A：系统会先尝试缩小字体，直到文字可以完全显示。如果最终仍无法完全显示，才会触发省略，此时使用的是当前实际应用的字号。
 
Q：为什么文本内容未到达Text组件显示末端就提前发生截断省略，导致出现一长段空白？
 
A：该问题是由于默认情况下文本是以字为单位，英文以单词为单位进行截断，当截断处的英文单词过长时被省略后会导致出现留白。可设置属性[wordBreak](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#wordbreak11)为WordBreak.BREAK_ALL使英文单词按字母截断，从而解决以上问题。
