# 实现Image组件的渐变模糊效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-850

#### 问题现象

Image组件如何基于图片内容实现模糊渐变和纯颜色遮罩渐变效果。
 
 

#### 背景知识

- [linearGradientBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#lineargradientblur12)为组件添加内容线性渐变模糊效果。
- [linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color#lineargradient)设置组件的颜色渐变效果，支持方向控制和多颜色配置。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

方案一：可以通过linearGradientBlur设置组件的内容线性渐变模糊效果，具体可以参考官网案例[设置组件线性渐变模糊效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#示例2设置组件线性渐变模糊效果)。
 
方案二：通过视觉叠加效果，使用Stack组件将线性渐变遮罩层叠加于图片之上，实现底部透明至不透明的视觉融合效果（可叠加多个渐变层）。
 
示例代码如下：
 
 
```text
@Entry
@Component
struct demo {
  build() {
    Column({ space: 5 }) {
      Column() {
        Text('原始图片')
          .fontSize(30);
      <em>  // 本地资源，需自行替换</em>
        Image($r('app.media.startIcon'))
          .width('100%')
          .height(300)
          .objectFit(ImageFit.Auto);
      };


      Text('渐变图片')
        .fontSize(30);
      Stack() {
        <em>// 本地资源，需自行替换</em>
        Image($r('app.media.startIcon'))
          .width('100%')
          .height(300)
          .objectFit(ImageFit.Auto);
        Row()
          .width('100%')
          .height(300)
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [
              [0x1000000, 0],
              [0x1000000, 0.2],
              [0x2000000, 0.3],
              [0x2000000, 0.4],
              [0x2000000, 0.5],
              [0x2000000, 0.6],
              [0x0100000, 0.9],
              [0x0000000, 1.0]
            ]
          });
      }
      .alignContent(Alignment.Bottom);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
 
运行效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Cp5-Fv4cRjqGln_xfhkxOQ/zh-cn_image_0000002628398642.png?HW-CC-KV=V1&HW-CC-Date=20260701T041215Z&HW-CC-Expire=86400&HW-CC-Sign=4F5C6DA00E32C4EF519B57C688C38A9D93EF9476C2475914C98F56C879C14D4A)

 

#### 总结

方案一可以为组件添加内容线性渐变模糊效果，实现类似毛玻璃的景深效果（如近实远虚、半透明模糊背景）；方案二为纯颜色渐变效果，实现两种或多种颜色的平滑过渡（如从白色渐变到黑色）。
