# TextInput组件如何实现文本默认选中效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1362

#### 问题现象

页面初次构建完成时，如何使TextInput组件获取焦点并且默认文本全部选中？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/i9MWexYBQmWr8SnFbIBhkA/zh-cn_image_0000002658841263.png?HW-CC-KV=V1&HW-CC-Date=20260701T041146Z&HW-CC-Expire=86400&HW-CC-Sign=C175AEA82258D4549889B5BA443CBAF9EB6C57DDC1BE4B53B4AB9FC2AC5DD3FC)

 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)：单行文本输入框组件。
- [defaultFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#defaultfocus9)：设置当前组件是否为当前页面上的默认焦点。
- [setTextSelection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#settextselection10)：设置文本选择区域并高亮显示。

 
 

#### 解决方案
1. 使用defaultFocus属性可使TextInput组件在页面初次构建完成时自动获取焦点。
2. 配合setTextSelection方法设置文本选择区域并高亮显示实现文本默认选中效果。
 
示例参考如下：
 
```text
@Entry
@Component
struct SelectedIndex {
  text: string = 'Hello World';
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      TextInput({
        text: '选中默认文本内容',
        placeholder: 'input your word...',
        controller: this.controller
      })
        .width('100%')
        .defaultFocus(true) <em>// 默认获取焦点</em>
        .onFocus(() => {
          this.controller.setTextSelection(0, this.text.length);<em> </em><em>// 选择文本区域</em>
        });
    }
    .padding({ left: 16, right: 16 })
    .width('100%')
    .height('100%');
  }
}
```
 
 

#### 总结

setTextSelection要在TextInput组件获焦时执行才能生效。
