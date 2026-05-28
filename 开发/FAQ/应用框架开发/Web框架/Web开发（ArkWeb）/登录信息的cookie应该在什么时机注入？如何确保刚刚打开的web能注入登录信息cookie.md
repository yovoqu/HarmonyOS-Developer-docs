# 登录信息的cookie应该在什么时机注入？如何确保刚刚打开的web能注入登录信息cookie

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-26

[webview.once](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-f#webviewonce)可以订阅一次指定类型Web事件的回调。一般在web初始化完成后可以注入。
 
```ArkTS
import { webview } from '@kit.ArkWeb'

webview.once("webInited", () => {
  console.log("setCookie");
  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b,c=d,e=f');
})

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
