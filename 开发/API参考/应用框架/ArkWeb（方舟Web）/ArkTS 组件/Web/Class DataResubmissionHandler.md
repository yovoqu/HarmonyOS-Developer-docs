# Class (DataResubmissionHandler)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-dataresubmissionhandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通过DataResubmissionHandler可以重新提交表单数据或取消提交表单数据。


## constructor9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

DataResubmissionHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## resend9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

resend(): void

重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onDataResubmitted((event) => {
        console.info('onDataResubmitted');
        event.handler.resend();
      })
    }
  }
}
```


## cancel9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

cancel(): void

取消重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onDataResubmitted((event) => {
        console.info('onDataResubmitted');
        event.handler.cancel();
      })
    }
  }
}
```
