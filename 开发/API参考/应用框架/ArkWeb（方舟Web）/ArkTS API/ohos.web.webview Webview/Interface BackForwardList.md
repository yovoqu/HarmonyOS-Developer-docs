# Interface (BackForwardList)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardlist
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

当前Webview的历史信息列表。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { webview } from '@kit.ArkWeb';
```


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力：** SystemCapability.Web.Webview.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentIndex | number | 否 | 否 | 当前在页面历史列表中的索引。 |
| size | number | 否 | 否 | 历史列表中索引的数量，最多保存50条，超过时起始记录会被覆盖。 |


## getItemAtIndex
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getItemAtIndex(index: number): HistoryItem

获取历史列表中指定索引的历史记录项信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定历史列表中的索引。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [HistoryItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i#historyitem) | 历史记录项。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State icon: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Button('getBackForwardEntries')
      .onClick(() => {
        try {
          let list = this.controller.getBackForwardEntries();
          let historyItem = list.getItemAtIndex(list.currentIndex);
          console.info("HistoryItem: " + JSON.stringify(historyItem));
          this.icon = historyItem.icon;
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
