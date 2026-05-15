# 通过\$r访问应用资源是否支持嵌套形式

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102

\$r当前不支持嵌套。第二个参数需使用ResourceManager获取应用资源的字符串。参考代码如下：

```ts
@Entry
@Component
struct Page16 {
context = this.getUIContext();

build() {
Row() {
Column() {
Text($r('app.string.EntryAbility1_label2',
this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility_label'))))// path: resources\base\element\string.json
.fontSize(50)
.fontWeight(FontWeight.Bold)
}
.width('100%')
}
.height('100%')
}
}
```

参考链接

ResourceManager
