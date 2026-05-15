# 如何解决Web与List的嵌套滑动冲突

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-18

可以设置组件的hitTestBehavior来避免这种情况，参考代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct SlidingConflictBetweenWebAndList {
webviewController: webview.WebviewController = new webview.WebviewController();

build() {
List() {
ListItem() {
Web({
src: $rawfile('index.html'),
controller: this.webviewController
})
.width('100%')
.height(220)
}.hitTestBehavior(HitTestMode.Block)
ListItem() {
Web({
src: $rawfile('index.html'),
controller: this.webviewController
})
.width('100%')
.height(220)
}
ListItem() {
Text('1')
}
.height(220)
ListItem() {
Text('2')
}
.height(220)
}
.backgroundColor(Color.Blue)
.width('100%')
.height('100%')
}
}
```

参考链接

触摸测试控制
