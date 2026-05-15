# 如何实现Tabs高度自适应内容

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-475

可以给Tabs设置height('auto')。参考示例如下：

```ts
@Entry
@Component
struct Index {
build() {
Column() {
Tabs() {
TabContent() {
Row() {
Text('hello')
}
.width('100%')
}
}
.height('auto')
.barBackgroundColor(Color.Orange)
.barHeight(0)
}
.height('100%')
.width('100%')
}
}
```
