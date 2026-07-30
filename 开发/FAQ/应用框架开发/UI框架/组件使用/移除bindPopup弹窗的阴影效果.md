# 移除bindPopup弹窗的阴影效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1216

#### 问题现象

如何移除bindPopup弹窗的阴影效果？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/GYAkKrglSB-QG4guufHuEg/zh-cn_image_0000002628753486.png?HW-CC-KV=V1&HW-CC-Date=20260701T041327Z&HW-CC-Expire=86400&HW-CC-Sign=0740C449648638E874F6ADF4FC0F85DE20C2A647FC91125850E103C2C372BC0C)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/J_AaYqGZT26F9YrxUV2Njg/zh-cn_image_0000002658952799.png?HW-CC-KV=V1&HW-CC-Date=20260701T041327Z&HW-CC-Expire=86400&HW-CC-Sign=98F57EFC123CC5998BB215EF64C11B3A17BE5EC400AB048F167B7FE534ADB11A)

 
 

#### 背景知识

- [ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明)：阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。
- [阴影效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect)：阴影接口shadow可以为当前组件添加阴影效果。

 
 

#### 解决方案

通过配置ShadowOptions实现阴影效果的灵活控制。在ShadowOptions模式中，当满足radius设置为0时，即可实现无阴影效果。
 
```text
@Entry
@Component
struct PopupExample {
  @State customPopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button('popup')
        .margin({ top: 50 })
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          message: 'this is a popup',
          arrowHeight: 20,
          arrowWidth: 20,
          radius: 20,
          shadow: {
            radius: 0
          },
        });
    }
    .width('100%');
  }
}
```
