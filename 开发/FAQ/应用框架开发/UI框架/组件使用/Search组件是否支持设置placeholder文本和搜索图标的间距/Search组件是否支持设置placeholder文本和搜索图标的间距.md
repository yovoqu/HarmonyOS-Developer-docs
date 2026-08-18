# Search组件是否支持设置placeholder文本和搜索图标的间距

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1338

#### 问题现象

无法设置Search组件的placeholder文本和搜索图标的间距，应该如何实现？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/Me67imMURAufdMCZOjqJ9A/zh-cn_image_0000002658840775.png?HW-CC-KV=V1&HW-CC-Date=20260811T005750Z&HW-CC-Expire=86400&HW-CC-Sign=7133769854AC3E4A6792157F516261392F077B018DCA4C8E56DBC8134BECEB06)

 
 

#### 背景知识

[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)组件支持设置[placeholder文本颜色](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search#placeholdercolor)和[placeholder文本样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search#placeholderfont)，包括字体大小，字体粗细，字体族，字体风格。暂不支持设置placeholder文本和搜索图标的间距。
 
 

#### 解决方案

Search组件不支持设置placeholder文本和搜索图标的间距，可以自定义搜索框组件实现该效果：
 
```text
@Entry
@Component
struct searchTest {
  @State searchText: string = '';

  build() {
    Row() {
      Column({ space: 10 }) {
        Row({ space: 5 }) {
          Row() {
            Image($r('sys.media.ohos_ic_public_search_filled'))
              .size({ width: 18, height: 18 })
              .opacity(0.5)
              .margin({ left: 10, right: 0 })
            TextInput({ placeholder: '搜索', text: this.searchText })
              .padding({ left: 4 })
              .layoutWeight(1)
              .backgroundColor(Color.Transparent)
              .height('100%')
          }
          .layoutWeight(1)
          .backgroundColor('#f2f3f5')
          .borderRadius('50%')
        }.width('100%')
        .height(40)
      }
      .width('100%')
      .padding({ top: 20, left: 20, right: 20 })
      .height('100%')
    }
    .height('100%')
    .backgroundColor(Color.White)
  }
}
```
 
 

#### 常见FAQ

Q：如何设置Search组件删除按钮颜色？
 
A：参考示例[设置symbol类型清除按钮](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search#示例11设置symbol类型清除按钮)。
 
Q：Search组件点击旁边的‘x’号会触发什么回调？
 
A：会触发onChange()、onWillChange()、onTextSelectionChange等回调。
