# 设置RichEditor键盘输入的字体颜色、字间距

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1130

#### 问题现象

使用RichEditor控制器添加绿色双#号文本后，键盘输入的文本颜色也是绿色，如何设置键盘输入文本的字体颜色为黑色并调整字间距？
 
代码如下：
 
```text
onReady(() => {
  this.controller.addTextSpan(`#${this.message}# `, {
    style:
    { fontColor: Color.Green }
  })
})
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/uTHF-dLVRimaO_xzhl1BQA/zh-cn_image_0000002658928735.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072440Z&HW-CC-Expire=86400&HW-CC-Sign=397A56B4EF5C03B1A5333B083004404FEC21F672565CB89DA56837DAF31B8040)

 
 

#### 背景知识

- [addTextSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan)：添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。
- [letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditortextstyle)：设置文本字符间距。

 
 

#### 解决方案

RichEditor组件的字体样式会默认跟随最后TextSpan的样式，所以添加绿色双#号文本后，键盘输入的字体样式也是绿色。设置字间距使用style的letterSpacing属性即可。
 
- 方案一：style设置字体颜色，onReady事件中控制器使用addTextSpan接口添加一个''（引号里有空格），设置其样式为黑色。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/NMm0MErNRkGH_1LkJ8Sqbg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260730T072440Z&HW-CC-Expire=86400&HW-CC-Sign=CF5F73206A493DB1697E4EF53351A42CF8E62231EF310F4BC319496EE0B11A31)
 

  必须添加一个空格字符(' ')，不是''（引号里无空格）。

  
```text
@Entry
@Component
struct RichEditorDemo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  message: string = 'Hello World';

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(`#${this.message}# `, {
            style:
            { fontColor: Color.Green, letterSpacing: 1 }
          });
          this.controller.addTextSpan(' ', {
            style:
            { fontColor: Color.Black }
          });
        });
    }.padding(16);
  }
}
```


 
- **方案二**：使用aboutToIMEInput回调，设置样式。
```text
@Entry
@Component
struct RichEditorText {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  message: string = 'Hello World';

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(`#${this.message}# `, {
            style:
            { fontColor: Color.Green }
          });
        })
        .aboutToIMEInput((value: RichEditorInsertValue) => {
          this.controller.addTextSpan(value.insertValue, {
            offset: value.insertOffset,
            style: {
              fontColor: Color.Black, letterSpacing: 1
            }
          });
          return false;
        });
    }.padding(16);
  }
}
```


 
 

#### 常见FAQ

Q：RichEditor的TextSpan是否可以配置backgroudcolor？
 
A：不可以。
 
Q：RichEditor是否可以通过非index的方式标记span？
 
A：不可以。
