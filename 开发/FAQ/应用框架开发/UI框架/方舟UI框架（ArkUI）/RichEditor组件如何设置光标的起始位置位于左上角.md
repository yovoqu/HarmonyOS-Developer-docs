# RichEditor组件如何设置光标的起始位置位于左上角

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-14

可以通过align属性传入参数Alignment.TopStart，来设置光标位置位于左上角。示例代码如下：

```ts
// xxx.ets
@Entry
@Component
struct RichEditorExample {
controller: RichEditorController = new RichEditorController();

build() {
Column() {
RichEditor({ controller: this.controller })
.align(Alignment.TopStart) // Set the starting position of the cursor to the upper left corner
.height(200)
.borderWidth(1)
.borderColor(Color.Red)
.width('100%')
}
}
}
```
