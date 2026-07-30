# 使用customKeyboard设置自定义键盘时，弹出失败

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1161

#### 问题现象

自定义键盘通过focusController获取焦点的时候，弹出的键盘是系统键盘，而不是预期的自定义键盘。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController()
  @State keyboardVisible: boolean = false
  customKeyboard: CustomBuilder = () => {
    this.buildCustomKeyboard()
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined)<em> </em><em>// 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘</em>
      Button('切换自定义键盘').onClick(() => {
        this.keyboardVisible = true
        this.getUIContext().getFocusController().requestFocus('RichEditor')
      })
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false
        })
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }

<em>  // 自定义键盘</em>
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘')
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd')
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/0nSRHe54Tny6hhf5R3VMMg/zh-cn_image_0000002628569772.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072456Z&HW-CC-Expire=86400&HW-CC-Sign=3819FD707BF825DBCCE9246F080277FE75EF56533926758B278D7C25CF8AE773)

 
 

#### 背景知识

- [@Builder装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)：ArkUI提供了一种轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。
- [customKeyboard属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#customkeyboard)：该属性可用于设置自定义键盘。其第一个参数[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)用于自定义UI描述，必须结合@Builder使用。
- [@ohos.arkui.UIContext(UIContext)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uicontext)与通用[焦点事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus)获取焦点差异：[this.getUIContext().getFocusController().requestFocus()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#requestfocus12)：通过组件的id将焦点转移到组件树对应的实体节点。在当前帧生效。

  [focusControl.requestFocus()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9)：此接口可以主动让焦点转移至参数指定的组件上。非当前帧生效，在下一帧才生效。

 
 

#### 问题定位
1. this.customKeyboard函数未用@Builder装饰器修饰。customKeyboard属性的第一个参数[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)用于自定义UI描述，必须结合@Builder使用。
2. 由于customKeyboard属性不是实时渲染，在更改this.keyboardVisible变量后，customKeyboard需要更新渲染。该问题代码中this.getUIContext().getFocusController().requestFocus("RichEditor")是在当前帧生效。更改this.keyboardVisible变量后，customKeyboard还没有完成渲染，因此第一次依旧会弹出系统键盘。使用focusControl.requestFocus("RichEditor")让控件在下一帧获取焦点即可，此时customKeyboard已完成渲染。
 
 

#### 分析结论

该问题代码存在以下两个问题：
 1. customKeyboard属性内this.customKeyboard函数未使用@Builder装饰器修饰，导致customKeyboard属性设置失效，无法弹出自定义键盘。
2. this.getUIContext().getFocusController().requestFocus("RichEditor")获取焦点是在当前帧生效，由于更改keyboardVisible变量后，customKeyboard未更新渲染完成，导致第一次获取焦点无法弹出自定义键盘。
 
 

#### 修改建议
1. 采用@Builder装饰器自定义构建函数。修改customKeyboard函数代码：
```text
@Builder
customKeyboard() {
  this.buildCustomKeyboard();
}
```

2. customKeyboard属性更新后再获取焦点。采用focusControl.requestFocus方法代替this.getUIContext().getFocusController().requestFocus方法获取组件焦点。
```text
Button('切换自定义键盘')
  .onClick(() => {
    this.keyboardVisible = true;
    focusControl.requestFocus('RichEditor');
  });
```

 
完整示例参考如下：
 
```text
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController();
  @State keyboardVisible: boolean = false;

  @Builder
  customKeyboard() {
    this.buildCustomKeyboard();
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined); <em>// 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘</em>
      Button('切换自定义键盘')
        .onClick(() => {
          this.keyboardVisible = true;
          focusControl.requestFocus('RichEditor');
        });
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false;
        });
    }
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }

 <em> // 自定义键盘</em>
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘');
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd');
  }
}
```
