# Web组件加载网页如何获取网页的标题及标题来源

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-157

#### 问题现象

Web组件加载网页可以通过什么方式获取网页的标题以及标题来源？
 
 

#### 背景知识

- [onTitleReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#ontitlereceive)：当页面文档标题&lt;title&gt;元素发生变更时，触发回调。若当前页面未显示设置标题，ArkWeb将在加载完成前基于页面的URL生成标题并返回给应用。
- [getTitle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#gettitle)：获取当前网页的标题。
- [OnTitleReceiveEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#ontitlereceiveevent12)：定义网页document标题更改时触发该回调。

 
 

#### 解决方案
1. 获取网页标题来源：onTitleReceive的callback回调参数OnTitleReceiveEvent中的isRealTitle表示document标题来源，true表示来自网页的title标签，false表示该title是根据URL自动生成，默认返回为false。

  
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
        .domStorageAccess(true)
        .onTitleReceive((event) => {
          if (event) {
            console.info(`title:${event.title}, is from title: ${event?.isRealTitle}`);
          } else {
            console.error('onTitleReceive callback error');
          }
        });
    };
  }
}
```

2. 根据场景，获取网页标题有以下三种方式：
如果当前网页标题发生了改变，可以在onTitleReceive事件中直接获取。
3. 如果是正常网页加载，可以在[onPageEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onpageend)中使用getTitle获取网页的标题。
4. 通过[runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)执行JavaScript代码来获取文档的标题。
 
 

#### 常见FAQ

Q：onTitleReceive或者是通过getTitle获取标题为什么返回的是URL？
 
A：如果加载的页面未设置title元素来指定标题，Web组件将基于URL生成标题并返回给应用程序。
