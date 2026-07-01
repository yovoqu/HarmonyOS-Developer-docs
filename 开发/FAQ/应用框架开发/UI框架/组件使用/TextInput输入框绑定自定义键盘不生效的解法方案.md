# TextInput输入框绑定自定义键盘不生效的解法方案

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1649

#### 问题现象

使用customKeyboard属性绑定不同的自定义键盘到输入框时不生效，问题代码如下：
 
```text
@Entry
@Component
struct TextInputClearFocusExample {
  @State index: number = 0;


  @Builder
  keyboard() {
    Column() {
      Text('键盘0');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }


  @Builder
  keyboard1() {
    Column() {
      Text('键盘1');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }


  @Builder
  keyboard2() {
    Column() {
      Text('键盘2');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }


  build() {
    Column({ space: 10 }) {
      TextInput({ placeholder: 'input your word...' }) <em>// 绑定自定义键盘</em>
        .customKeyboard(this.index === 0 ? this.keyboard() : (this.index === 1 ? this.keyboard1() : this.keyboard2()))
        .margin(10)
        .border({ width: 1 })
        .height('48vp');


      Button('切换键盘0')
        .onClick(() => {
          this.index = 0;
        });
      Button('切换键盘1')
        .onClick(() => {
          this.index = 1;
        });
      Button('切换键盘2')
        .onClick(() => {
          this.index = 2;
        });
    };
  }
}
```
 
问题现象见下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/749RjSjeTLqK1LwSYIbA8g/zh-cn_image_0000002628660998.png?HW-CC-KV=V1&HW-CC-Date=20260701T041251Z&HW-CC-Expire=86400&HW-CC-Sign=74A32E7D31B48FBF4E7E0BBE522C0BEE1A4AF8C373604AAFFBF4A382BA4E39F7)

 
 

#### 背景知识

[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)是单行文本输入框组件，常用于响应用户的输入操作，比如手机号输入，表单的输入等。组件的[customKeyboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#customkeyboard10)属性可以设置自定义键盘。
 
 

#### 解决方案

[customKeyboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#customkeyboard10)属性不支持使用响应式，将三元表达式替换为正常的if-else语句可以正常绑定不同的自定义键盘。示例代码如下：
 
```text
@Entry
@Component
struct TextInputClearFocusExample {
  @State index: number = 0;


  @Builder
  keyboard() {
    Column() {
      Text('样式 0');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }


  @Builder
  keyboard1() {
    Column() {
      Text('样式 1');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }


  @Builder
  keyboard2() {
    Column() {
      Text('样式 2');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }


  build() {
    Column() {
      if (this.index === 0) {
        TextInput({ placeholder: 'input your word...' }) <em>// 绑定自定义键盘</em>
          .customKeyboard(this.keyboard())
          .margin(10)
          .height('48vp');
      } else if (this.index === 1) {
        TextInput({ placeholder: 'input your word...' }) /<em>/ 绑定自定义键盘</em>
          .customKeyboard(this.keyboard1())
          .margin(10)
          .height('48vp');
      } else {
        TextInput({ placeholder: 'input your word...' }) <em>// 绑定自定义键盘</em>
          .customKeyboard(this.keyboard2())
          .margin(10)
          .height('48vp');
      }


      Button('切换键盘 样式0')
        .onClick(() => {
          this.index = 0;
        })
        .margin({ top: 10, bottom: 10 });
      Button('切换键盘 样式1')
        .onClick(() => {
          this.index = 1;
        })
        .margin({ top: 10, bottom: 10 });
      Button('切换键盘 样式2')
        .onClick(() => {
          this.index = 2;
        })
        .margin({ top: 10, bottom: 10 });
    };
  }
}
```
 
 

#### 常见FAQ

Q：在[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)中使用[.customKeyboard()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#customkeyboard10)方法自定义了键盘，请问如何触发TextInput的onSubmit事件？
 
A：目前自定义键盘无法触发onSubmit事件。
