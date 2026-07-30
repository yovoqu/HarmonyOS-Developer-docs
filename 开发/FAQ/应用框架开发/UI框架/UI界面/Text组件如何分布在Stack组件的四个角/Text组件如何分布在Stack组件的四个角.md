# Text组件如何分布在Stack组件的四个角

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-816

#### 问题现象

Stack组件中有四个Text组件，如何使子组件分别分布在Stack组件的左上角，右上角，左下角，右下角？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/3kCfrW2LShGLORetb4SYfQ/zh-cn_image_0000002628557804.png?HW-CC-KV=V1&HW-CC-Date=20260730T072448Z&HW-CC-Expire=86400&HW-CC-Sign=8A6D1C0C3FC401FB89F7930495534E9BF04FB8058F2C486A5E26148907F90223)

 
 

#### 背景知识

[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)：设置子组件在水平或垂直方向上的对齐格式。
 
 

#### 解决方案

首先将左上角、右上角的两个Text组件外层嵌套一个Row组件，左下角、右下角的两个Text组件外层嵌套一个Row组件，再将两个Row组件外层嵌套一个Column组件，最后给Row组件和Column组件添加justifyContent属性即可实现。
 
```text
@Entry
@Component
struct StackDemo {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        Row() {
          Text('左上角')
          Text('右上角')
        }.width('100%')
        .justifyContent(FlexAlign.SpaceBetween)<em> </em><em>// 设置子组件在水平方向上的对齐格式。</em>

        Row() {
          Text('左下角')
          Text('右下角')
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceBetween) <em>// 设置子组件在水平方向上的对齐格式。</em>
      }
      .justifyContent(FlexAlign.SpaceBetween)<em> </em><em>// 设置子组件在垂直方向上的对齐格式。</em>
      .width('100%')
      .height('100%')
    }
  }
}
```
