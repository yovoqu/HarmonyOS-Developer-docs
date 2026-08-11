# 如何实现基于StyledString的气泡动态适配

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-670

#### 问题现象

如何根据StyledString文本高度动态调整气泡的高度？
 
 

#### 效果预览

可以看到气泡大小会跟随StyledString而变化。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/2cEfcK1WT8GXWfg-lwesmQ/zh-cn_image_0000002628394678.png?HW-CC-KV=V1&HW-CC-Date=20260811T005809Z&HW-CC-Expire=86400&HW-CC-Sign=115AFE3F3A783A36884D576A65E1B1DB7B6406AC3C9A32FE7A6876762E113965)

 
 

#### 背景知识

- [StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#styledstring)对象支持灵活设置文本样式，可通过TextController的[setStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#setstyledstring12)方法与Text组件绑定，也可通过RichEditor组件的控制器方法与RichEditor组件关联。
- [objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)方法用于设置图片的填充效果。

 
 

#### 解决方案

气泡高度的动态调整可通过Column自适应Text内容实现，StyledString提供样式化文本内容，其高度由Text组件渲染后自动传递给Column。
 
```text
@Builder
function bubbleBackgroundOne() {
  Image($r('app.media.backgroundcolorgray')) <em>// 此处'backgroundcolorgray'仅作示例，请开发者自行替换。</em>
    .objectFit(ImageFit.Fill)
    .width('100%')
    .height('100%');
}

@Entry
@Component
struct StyledStringDemo {
  styledString1: StyledString = new StyledString('运动45分钟');
  mutableStyledString1: MutableStyledString = new MutableStyledString('运动35分钟');
  controller1: TextController = new TextController();
  controller2: TextController = new TextController();

  async onPageShow() {
    this.controller1.setStyledString(this.styledString1);
    this.controller2.setStyledString(this.mutableStyledString1);
  }

  build() {
    Row() {
      Column() {
    <em>    // 显示属性字符串</em>
        Text(undefined, { controller: this.controller1 });
        Text(undefined, { controller: this.controller2 });
        Text('测试')
          .onClick(async () => {
            this.styledString1 = new StyledString('运动45分钟XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
            this.controller1.setStyledString(this.styledString1);
          })
      }
      .background(bubbleBackgroundOne)
      .padding(10)
      .borderRadius(5)
      .width('100%');
    }
    .height('100%')
    .width('100%')
    .padding(10);
  }
}
```
