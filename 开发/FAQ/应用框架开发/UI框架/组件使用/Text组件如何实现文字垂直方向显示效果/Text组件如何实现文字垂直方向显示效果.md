# Text组件如何实现文字垂直方向显示效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1128

#### 问题现象

页面文字需要垂直方向显示，使用Text组件怎样实现这种效果？
 
 

#### 背景知识

- [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)：显示一段文本的组件。
- [@BuilderParam装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam)：引用@Builder函数。

 
 

#### 解决方案

针对Text组件如何实现文字垂直方向显示，有以下解决方案：
 
- 方案一：可通过封装样式方法实现，使用ForEach()方法对Text组件文本内容进行遍历，再使用.split('')属性对文本内容进行分割然后各行显示。详情请参考如下示例代码：
```text
class Tmp {
  label: string = '';
}


// 封装一个方法
@Builder
function overBuilder(params: Tmp) {
  // 用ForEach()方法对Text组件文本内容进行遍历，再使用.split('')属性对文本内容进行分割
  ForEach(params.label.split(''), (item: string) => {
    Text(item)
      .fontSize(30);
  });
}


@Entry
@Component
struct VerticalDemo {
  @BuilderParam customOverBuilderParam: (params: Tmp) => void = overBuilder;


  build() {
    Column() {
      this.customOverBuilderParam({ label: '设置页面文字垂直方向显示' });
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center);
  }
}
```

- 方案二：通过设置Text组件宽度width与字号一致的方式实现，可参考[如何实现文本竖向排列](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-91)。效果如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/x49-xND9QSa7ohmsIVdfSQ/zh-cn_image_0000002628569422.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=7A119FD484C22047949E7D86A696EB704EE544DEBBFB268468ACA625824C6DEE)
