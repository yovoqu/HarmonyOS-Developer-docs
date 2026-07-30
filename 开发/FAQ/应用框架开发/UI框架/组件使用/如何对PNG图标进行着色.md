# 如何对PNG图标进行着色

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1328

#### 问题现象

如何对PNG图标进行着色，仅更改图标内容部分的颜色，空白部分保持不变？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/GCCDFgw7Tb2KqiSNj1D72A/zh-cn_image_0000002658839133.png?HW-CC-KV=V1&HW-CC-Date=20260701T041310Z&HW-CC-Expire=86400&HW-CC-Sign=F8DC3892DD5056572CFB5BFCE7B72E7D64F6F43B3F48A6066C96898234073C7C)

 
 

#### 背景知识

[colorBlend](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#colorblend18)：为组件添加颜色叠加效果。colorBlend属性会将指定的颜色与图像原始像素进行叠加混合，仅作用于非透明区域。透明区域因alpha通道值为0，不会参与混合计算。
 
 

#### 解决方案

采用colorBlend属性结合Image组件的声明式语法实现。
 
```text
@Entry
@Component
struct Page {
  build() {
    Column({ space: 20 }) {
      Row({ space: 20 }) {
        Text('修改过图标');
        Image($r('app.media.startIcon'))
          .colorBlend(Color.Red)
          .height(50)
          .width(50);
      };

      Row({ space: 20 }) {
        Text('原始的图标');
        Image($r('app.media.startIcon'))
          .height(50)
          .width(50);
      };
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
 
 

#### 常见FAQ

Q：使用colorBlend更改颜色，背景由透明变为白色。
 
A：colorBlend为颜色叠加，不支持仅设置非透明通道颜色，可以采用[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#colorfilter14)进行替代。
