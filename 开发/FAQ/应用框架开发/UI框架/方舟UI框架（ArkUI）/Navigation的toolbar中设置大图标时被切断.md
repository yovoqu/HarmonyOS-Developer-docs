# Navigation的toolbar中设置大图标时被切断

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-60

当图片尺寸超过toolbar高度时，可通过scale属性进行缩放调整。参考代码如下：

```ts
@Entry
@Component
struct NavigationExample {
build() {
Column() {
Navigation() {
}.toolbarConfiguration(this.navigationToolbar)
}
.height('100%')
.width('100%')
.backgroundColor(Color.Gray)
}

@Builder
navigationToolbar() {
Row() {
Column() {
Image($r('app.media.icon')).width(24)
}.layoutWeight(1)

Column() {
Image($r('app.media.icon')).width(24).scale({ x: 2, y: 2 })
}.layoutWeight(1)

Column() {
Image($r('app.media.icon')).width(24)
}.layoutWeight(1)
}
.height(34)
.width('100%').backgroundColor(Color.White)
}
}
```

参考链接

图形变换
