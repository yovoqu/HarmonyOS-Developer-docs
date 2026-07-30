# 组件外层加了Navigation后，该组件的高度不能达到整个屏幕高度

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1272

#### 问题现象

RelativeContainer组件外层添加了Navigation后，该组件的高度不能达到整个屏幕高度。如何将Image组件放到整个手机屏幕最下方？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct PrivatePage34 {
  build() {
    Navigation() {
      RelativeContainer() {
        Row() {
          Image($r('app.media.app_icon'))
            .width('90%')
            .height(200);
        }
        .padding({ top: 20 })
        .justifyContent(FlexAlign.Center)
        .width('100%');
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#ffeceeef');
    }
    .backgroundColor('#DFE1E3');
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/gaeorCjHT0KIuBeT-aOmLw/zh-cn_image_0000002658835379.png?HW-CC-KV=V1&HW-CC-Date=20260701T041223Z&HW-CC-Expire=86400&HW-CC-Sign=8B323472AC70ADFC6C5C1D62C188D499B684403C95CCAE46FB2091396ABC0877)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/dKPd0VKkQ_qGCFJoEokHcQ/zh-cn_image_0000002628756014.png?HW-CC-KV=V1&HW-CC-Date=20260701T041223Z&HW-CC-Expire=86400&HW-CC-Sign=EBFC61898F1E9696A595455B5A3BC2CC22FFC991C8D817941CF54B5EB293EFFF)

 
 

#### 背景知识

[hideTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidetitlebar)：设置是否隐藏标题栏，默认值：false。
 
 

#### 解决方案

Navigation组件是路由导航的根视图容器，一般作为页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏。RelativeContainer组件是在内容区的，因此达不到屏幕高度。需要先将默认显示的标题等隐藏，然后进行页面布局。
 
```text
@Entry
@Component
struct PrivatePage {
  build() {
    Navigation() {
      RelativeContainer() {
        Row() {
          Image($r('app.media.startIcon'))<em> </em><em>// 根据实际情况添加图片</em>
            .width('90%')
            .height(200);
        }
        .padding({ top: 20 })
        .justifyContent(FlexAlign.Center)
        <em>// 设置对齐规则</em>
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        });
      }
      .backgroundColor('#ffeceeef');
    }
    .hideTitleBar(true)
    .backgroundColor('#DFE1E3');
  }
}
```
