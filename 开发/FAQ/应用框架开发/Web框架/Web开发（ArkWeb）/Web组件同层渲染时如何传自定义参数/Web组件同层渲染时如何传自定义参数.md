# Web组件同层渲染时如何传自定义参数

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-177

#### 问题现象

在Web组件同层渲染场景下，H5中的object标签如何传自定义参数并通过onNativeEmbedLifecycleChange回调接收参数？
 
 

#### 背景知识

- [同层渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-same-layer)：在系统中，应用可以使用Web组件加载Web网页。当非系统框架的UI组件功能或性能不如系统组件时，可使用同层渲染技术，通过ArkUI组件渲染这些组件（简称为同层组件）。
支持embed标签：在开启同层渲染后，仅支持type类型为native前缀的标签识别为同层组件，不支持自定义属性。
- 支持object标签：在开启同层渲染后，支持将非标准MIME type的object标签识别为同层组件，支持通过param/value的自定义属性解析。

 - [onNativeEmbedLifecycleChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedlifecyclechange11)：当同层标签生命周期变化时触发该回调。
- [enableNativeEmbedMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enablenativeembedmode11)：设置是否开启同层渲染功能。当属性没有显式调用时，默认不开启同层渲染功能。
- [registerNativeEmbedRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#registernativeembedrule12)：注册使用同层渲染的HTML标签名和类型。标签名仅支持使用object和embed。标签类型只能使用ASCII可显示字符。

 
 

#### 解决方案

object标签支持param/value的自定义属性传值，使用时需要将enableNativeEmbedMode属性设置为true，调用registerNativeEmbedRule注册同层渲染的HTML标签名和类型，最后通过onNativeEmbedLifecycleChange回调中获取到自定义属性值。
 
应用侧示例代码如下：
 
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebRender {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('render.html'), controller: this.controller })
        .domStorageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false)
        .enableNativeEmbedMode(true)
        .registerNativeEmbedRule('object', 'test/input')
        .onNativeEmbedLifecycleChange((event) => {
          if (event.info) {
            console.info('NativeEmbedParams: ' + event.info.params?.['testName']);
          }
        });
    };
  }
}
```
 
HTML示例代码如下：
 
```text
<!--src/main/resources/rawfile/render.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染html</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="background:white">
<object id = "input1" type="test/input" style="width: 300px; height: 100px">
    <param name="testName" value="testValue">
</object>
</body>
</html>
```
 
打印结果如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/6z5ozQZPS0OPfwKbBtCjqA/zh-cn_image_0000002659138435.png?HW-CC-KV=V1&HW-CC-Date=20260811T005837Z&HW-CC-Expire=86400&HW-CC-Sign=D1010349C3C95E289E162BAE95DD28F48AC8564901B734BCBAE5369CCD4E31A7)
