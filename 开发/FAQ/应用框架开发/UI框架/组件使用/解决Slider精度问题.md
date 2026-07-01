# 解决Slider精度问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1280

## 解决Slider精度问题
 


##### 问题现象

Slider组件，step设置为0.1时，滑动时显示的value不是正常的35.1、35.2、35.3，而是35.70000076293945、36.400001525878906这类数值，如何解决？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct Question {
  textTimerController: TextTimerController = new TextTimerController();
  @State tempLatrue: number = 35;

  build() {
    Column() {
      Slider({
        value: this.tempLatrue,
        min: 34.5,
        max: 43.1,
        style: SliderStyle.OutSet,
        step: 0.1
      })
        .width('100%')
        .margin({ top: 15, bottom: 15 })
        .onChange((value: number) => {
          this.tempLatrue = value;
        }).showTips(true, `${this.tempLatrue}`)
    }
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/dKgBOfWTSn6WUObdpDPC1w/zh-cn_image_0000002628757874.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025608Z&HW-CC-Expire=86400&HW-CC-Sign=49714CDA80F1A8C7DC7DF5033BA0F915A236AFE9C59E4DE75D22B70C8372AD57)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6fpeuVJyR2OQYhZeITk6Sg/zh-cn_image_0000002658957189.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025608Z&HW-CC-Expire=86400&HW-CC-Sign=EE59A62A35CF0291CD1B9D44AD294238B3620F5E5799737192D2589DAB80EFDD)

 
 

##### 背景知识

[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-slider)：滑动条组件，用来快速调节设置值，如音量、亮度等。
 
 

##### 解决方案

浮点数在计算机中是通过二进制形式存储的，某些十进制浮点数在二进制中无法精确表示，导致了运算结果的精度问题。
 
- 使用toFixed(3)将数值转换为十进制定点模式表示的字符串，并保留小数点后3位。
- 使用slice(0, -1)截取字符串。
- 使用parseFloat返回一个新的浮点数，并展示。

 
```text
@Entry
@Component
struct TextTimerExample {
  textTimerController: TextTimerController = new TextTimerController();
  @State tempLatrue: number = 35;

  build() {
    Column() {
      Slider({
        value: this.tempLatrue,
        min: 34.5,
        max: 43.1,
        style: SliderStyle.OutSet,
        step: 0.1
      })
        .width('100%')
        .margin({ top: 15, bottom: 15 })
        .onChange((value: number) => {
          this.tempLatrue = Number.parseFloat(value.toFixed(3).slice(0, -1));
        }).showTips(true, `${this.tempLatrue}`)
    }
  }
}
```
