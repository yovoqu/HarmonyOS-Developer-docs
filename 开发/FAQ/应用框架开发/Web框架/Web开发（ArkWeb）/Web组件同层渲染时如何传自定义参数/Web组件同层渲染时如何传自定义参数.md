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
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebRender </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'render.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enableNativeEmbedMode</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerNativeEmbedRule</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'object'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'test/input'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onNativeEmbedLifecycleChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'NativeEmbedParams: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'testName'</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
HTML示例代码如下：
 
```text
<em><!--src/main/resources/rawfile/render.html--></em>
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/6z5ozQZPS0OPfwKbBtCjqA/zh-cn_image_0000002659138435.png?HW-CC-KV=V1&HW-CC-Date=20260723T013351Z&HW-CC-Expire=86400&HW-CC-Sign=DDB8227EA387D24FD320DBE2E820D2E6BD76ABE30F920FCDA93D7B7B8B3E0690)
