# 禁止编辑TextInput内容

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-745

## 禁止编辑TextInput内容
 


##### 问题现象

如何实现禁止编辑TextInput组件中的内容的功能？
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/_eGfSOrwTHW_Hh2r5oYu5w/zh-cn_image_0000002628555362.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025658Z&HW-CC-Expire=86400&HW-CC-Sign=4E71F97B2E42DB54C6FB2248E2AE89983D1D08425BAA1802A1E5A0CE8FE74766)

 
 

##### 背景知识

- [enabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable#enabled)是一种组件通用属性，可用于设置组件是否可交互。
- [focusOnTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusontouch9)用于设置当前组件是否支持点击获焦功能。
- [focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)用于设置当前组件是否可以获焦。

 
 

##### 解决方案

- 方案一：添加enabled属性。当设置enabled属性的值为false后，系统会自动为相关组件添加灰度效果，会改变原来组件的样式。
- 方案二：添加focusOnTouch属性。当focusOnTouch属性为true时，仅在组件可点击时才能正常获取焦点，更适合具有点击功能的组件，如TextInput。
- 方案三：添加focusable属性。该属性是一种更通用的获焦方法，适合大部分组件。当它设置为false时，组件无法获得焦点。

 
```text
@Entry
@Component
struct TextInputColorPage {
  message: string = 'Hello World';

  build() {
    Column({ space: 16 }) {
      TextInput({ text: this.message }).enabled(false).fontColor(Color.Blue);
      TextInput({ text: this.message }).focusOnTouch(false).fontColor(Color.Gray);
      TextInput({ text: this.message }).focusable(false).fontColor(Color.Brown);
    }
    .padding(10);
  }
}
```
