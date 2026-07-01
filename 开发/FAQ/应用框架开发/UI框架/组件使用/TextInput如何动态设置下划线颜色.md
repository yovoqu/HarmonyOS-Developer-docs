# TextInput如何动态设置下划线颜色

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1047

## TextInput如何动态设置下划线颜色
 


##### 问题现象

TextInput设置InputType.NUMBER_DECIMAL类型后，切换焦点，如何解决showUnderline下划线的状态颜色无变化的问题？
 
 

##### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)单行文本输入框组件。
- [showUnderline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showunderline10)：设置是否开启下划线。
- [outline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline#outline)属性是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

 
 

##### 解决方案

 
TextInput设置showUnderline下划线只支持InputType.Normal类型，其他类型不生效。可通过outline属性实现动态设置下划线颜色的效果。
 
- 创建颜色变量bottomLineColor，设置为outline属性的color。
- 在onFocus、onBlur设置切换焦点时的颜色即可。

 
```text
@Entry
@Component
struct TextInputExample {
  @State bottomLineColor: string = '#F1F3F5';

  build() {
    Column({ space: 20 }) {
      TextInput({ placeholder: '请输入文本内容' })
        .width('100%')
        .type(InputType.NUMBER_DECIMAL)
        .showUnderline(true)
        .borderRadius(0)
        .backgroundColor(Color.White)
        // 设置下划线
        .outline({
          width: { bottom: 1 },
          color: this.bottomLineColor
        })
        .onFocus(() => {
          // 获焦设置蓝色
          this.bottomLineColor = '#0A59F7';
        })
        .onBlur(() => {
          // 失焦设置灰
          this.bottomLineColor = '#F1F3F5';
        })
      TextInput({ placeholder: '提示文本内容' })
        .width('100%')
        .type(InputType.NUMBER_DECIMAL)
        .showUnderline(true)
        .borderRadius(0)
        .backgroundColor(Color.White)
    }
    .width('100%')
    .padding(16)
  }
}
```
 
运行效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/FXxgLN3bQF6QE5O2UxH0cw/zh-cn_image_0000002658804821.png?HW-CC-KV=V1&HW-CC-Date=20260701T025557Z&HW-CC-Expire=86400&HW-CC-Sign=C4A9FFE35BA3D1AF74AD0A676AFC6012B3A4301D7BC8A1467CF232C4208FFFED)
