# Select组件默认加粗字体

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1434

#### 问题现象

在字体大小一致的前提下，Select组件中显示的文本相较Text组件中的文本，视觉上更为粗重。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct SelectExample {
  @State text: string = '这是实验组';
  @State index: number = 0;

  build() {
    Column({ space: 10 }) {
    <em>  // icon可以使用其他有效资源</em>
      Select([{ value: 'aaa', icon: $r('app.media.startIcon') }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 35 })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          this.index = index;
          if (text) {
            this.text = text;
          }
        });
      Text('这是对照组')
        .fontSize(35);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/xzHutsn4TrKpSL57Jyw5OA/zh-cn_image_0000002628603754.png?HW-CC-KV=V1&HW-CC-Date=20260701T041143Z&HW-CC-Expire=86400&HW-CC-Sign=C84E0D4850C57383BF4C5C6A59C16DD3805B6A21380440C49150796653A85BA1)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/RUJ-RIz4Q8miaG3CYu5f0w/zh-cn_image_0000002658843019.png?HW-CC-KV=V1&HW-CC-Date=20260701T041143Z&HW-CC-Expire=86400&HW-CC-Sign=4A70498AC3773FAD224C77FA8D52DAF779912B089AA000090D084D783BD119B3)

 
 

#### 背景知识

- [Select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)是HarmonyOS提供的一种下拉选择菜单组件，可让用户在多个选项间选择。
- [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件的[font](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#font12)属性可用于设置文本的样式，包括字体大小、字体粗细、字体族和字体风格等。

 
 

#### 问题定位

- 当前Select组件和Text组件的文本内容相同，仅在font属性中设置了size大小，并未修改weight属性，但是Select组件中的文本比Text组件中的文本更粗。
- 根据Select组件中的font方法得知，下拉按钮本身的文本样式中weight的默认值为FontWeight.Medium，且后续版本没有相关变动。而Text组件字体默认粗细为FontWeight.Normal。

 
 

#### 分析结论

Select组件默认会加粗字体，值默认为FontWeight.Medium，若需要修改字体粗细样式，则应该显式地定义其weight参数。
 
 

#### 修改建议

为Select组件的font属性添加weight参数，并将值设置为FontWeight枚举类型的Normal。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct SelectBold {
  @State text: string = '这是实验组';
  @State index: number = 0;

  build() {
    Column({ space: 10 }) {
    <em>  // icon可以使用其他有效资源</em>
      Select([{ value: 'aaa', icon: $r('app.media.startIcon') }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 35, weight: FontWeight.Normal })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          this.index = index;
          if (text) {
            this.text = text;
          }
        });
      Text('这是对照组')
        .fontSize(35);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
