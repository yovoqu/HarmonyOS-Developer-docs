# Image动态设置圆角大小

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-842

## Image动态设置圆角大小
 


##### 问题现象

使用Slider组件希望实现滑动时控制Image组件圆角的变化，但滑动Slider时圆角没有改变。
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/tIbyrHAPQyuMhQET4FLDwg/zh-cn_image_0000002628558546.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025550Z&HW-CC-Expire=86400&HW-CC-Sign=E4CB1820F3979C74EAFE6353C14785BF48127C2E66B743EFCD854AB941F2866F)

 
 

##### 背景知识

- [clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)：用于对组件进行裁剪、遮罩处理。
- [borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)：设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。
- [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
- [$$语法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)：内置组件双向同步。

 
 

##### 解决方案

针对滑动Slider时圆角没有改变的问题，需要注意以下事项：
 
- 想通过Slider组件值改变来同步改变Image组件的圆角，需要将.borderRadius()属性值和Slider组件的value值双向绑定。
- 实现圆角变化效果后如果需要图片跟随圆角值发生变化，需要给Image组件添加.clip(true)属性。

 
完整示例参考如下：
 
```text
@Entry
@Component
struct ImageChange {
  @State radius: number = 0;

  build() {
    Column() {

      Image($r('app.media.background')) // 可根据具体场景替换为可用资源
        .width(100)
        .borderRadius(this.radius)
        .clip(true) // 裁剪超出Image组件的图片
      Column() {
        Text(this.radius + 'PX')
          .fontColor('#007AFF')
        Slider({
          min: 0,
          max: 60,
          style: SliderStyle.OutSet,
          value: $$this.radius // 双向绑定
        })
          .blockSize({ width: 20, height: 20 })
          .trackColor('#E5E5EA')
          .selectedColor('#007AFF')
          .trackThickness(6)
          .width('100%')
          .margin({
            top: 7,
            bottom: 13
          })
      }
    }
    .padding(50)
    .width('100%')
    .height('100%')
  }
}
```
