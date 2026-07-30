# 富文本RichEditor能否实现有序标签和无序标签

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-925

#### 问题现象

RichEditor能否实现文本的有序标签和无序标签？如果不能有没有其他办法实现？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/9W7x_ecWTOub1elpy_-daA/zh-cn_image_0000002628400318.png?HW-CC-KV=V1&HW-CC-Date=20260730T072334Z&HW-CC-Expire=86400&HW-CC-Sign=62F7AC35C08663A71E622A8616E2C8095E99263DAD41251732F57D6F380D59F9)

 
 

#### 背景知识

- [Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。
- [@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)装饰的函数也称为“自定义构建函数”。其提供轻量的UI元素复用机制，UI结构固定，仅与使用方进行数据传递。
- [RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor)是支持图文混排和文本交互式编辑的组件，无法支持audio标签和有序无序列表。

 
 

#### 解决方案
1. 使用@Builder装饰器自定义设置一个ListItemBuilder，在文本前面配置圆点大小，实现无序标签Row().width(6).height(6).backgroundColor(Color.Black).borderRadius(3).borderWidth(1)。
2. 使用@Builder装饰器自定义设置一个ListNumBuilder，在文本前面配置数字，实现有序标签。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct test {
<em>  // 编号开头的列表行</em>
  @Builder
  ListNumBuilder(num: number, title: string) {
    Flex() {
      Text(`${num}.`).width(24)
      Text(title)
    }
  }

<em>  // 列表行</em>
  @Builder
  ListItemBuilder(title: string) {
    Flex() {
      Row() {
        Row()
          .width(6)
          .height(6)
          .backgroundColor(Color.Black)
          .borderRadius(3)
          .borderWidth(1)
      }.width(24).height(18).justifyContent(FlexAlign.Center)

      Text(title)
    }
  }

  build() {
    Column() {
      Column() {
        Text('demo').fontSize(20).fontWeight(FontWeight.Bold)
        this.ListItemBuilder('包裹到的时候很惊讶，好大一个箱子但是重量很轻，鞋盒也是很轻的泡沫材质');
        this.ListItemBuilder('鞋子很有科技未来感的音色和灰色相间，内外侧都有镂空设计更透');
        this.ListItemBuilder('特有结构+材料减震，通过结构压缩形变，将储存的能量进行快速反馈，让回弹效果更快、更明显，给跑者带来强劲的回弹动力');
      }.width('100%').padding({ left: 10, right: 10, top: 20 })

      Column() {
        Text('demo').fontSize(20).fontWeight(FontWeight.Bold)
        this.ListNumBuilder(1, '包裹到的时候很惊讶，好大一个箱子但是重量很轻，鞋盒也是很轻的泡沫材质');
        this.ListNumBuilder(2, '鞋子很有科技未来感的音色和灰色相间，内外侧都有镂空设计更透');
        this.ListNumBuilder(3,
          '特有结构+材料减震，通过结构压缩形变，将储存的能量进行快速反馈，让回弹效果更快、更明显，给跑者带来强劲的回弹动力');
      }.width('100%').padding({ left: 15, right: 10, top: 20 })
    }.width('100%')
  }
}
```
