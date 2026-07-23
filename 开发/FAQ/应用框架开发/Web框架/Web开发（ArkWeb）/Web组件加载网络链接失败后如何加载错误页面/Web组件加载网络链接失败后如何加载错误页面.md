# Web组件加载网络链接失败后如何加载错误页面

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-173

#### 问题现象

如果网络或者在线链接有问题时，Web组件加载网络链接会失败，此时如何加载本地缺省页面（指定失败页面）并进行页面刷新？
 
- 场景一：使用ArkTS页面实现缺省页面。
- 场景二：使用html页面实现缺省页面。
- 场景三：使用html格式的文本数据实现缺省页面。

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5iM-PFp8Q-Gc-1sdujm9Ow/zh-cn_image_0000002659258391.png?HW-CC-KV=V1&HW-CC-Date=20260723T013349Z&HW-CC-Expire=86400&HW-CC-Sign=15B332EFF1D1CE90BF7F05F0F50E51957AAAF0BE428C37802AC23D4BDC42A70C)

 
 

#### 背景知识

- [onErrorReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onerrorreceive)：网页加载遇到错误或无网络的情况下触发该回调。主资源与子资源出错都会回调该接口，可以通过isMainFrame来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。错误码范围：[ArkWeb的网络协议栈错误列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist)。
- [javaScriptProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#javascriptproxy)：将javaScriptProxy中的ArkTS对象注册到Web组件中。
- [visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
Hidden：隐藏，但参与布局进行占位。
- Visible：显示。
- None：隐藏，但不参与布局，不进行占位。

 - [loadUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)：加载指定的URL。
- [loadData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loaddata)：加载指定的数据。
- [onOverrideErrorPage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onoverrideerrorpage20)：网页加载遇到错误时触发，只有主资源出错才会回调该接口，可以使用该接口自定义错误展示页。该功能需通过调用[setErrorPageEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#seterrorpageenabled20)接口启用默认错误页后，才会生效。

 
 

#### 解决方案

- **场景一**：ArkWeb的网络协议栈错误列表中，errorCode为0表示正常加载，其他值表示异常加载。

  定义successLoad变量控制页面显示，当加载失败后把errorCode赋值给successLoad变量，重新刷新页面时设置successLoad的值为0（若不设置为0，则缺省页面一直展示）。页面采用Stack布局，包含缺省页面层和Web页面层，当successLoad为0时展示Web页面，successLoad为其他值展示缺省页面。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">请换成实际应用的在线地址</span></em>
const <span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebLoadErrorPage1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">successLoad</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">缺省页</span></em>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">重新加载</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">successLoad </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">successLoad </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Visible </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">None</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><em>// Web</em><em><span style="color: rgb(128,128,128);">页面</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">successLoad </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Visible </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Hidden</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onErrorReceive</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorCode</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">successLoad </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorCode</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **场景二**：

  ArkTS侧实现Web加载H5页面的功能，当加载失败后onErrorReceive回调的errorCode不为0时，使用loadUrl加载本地H5页面，并通过javaScriptProxy接口给H5注入对应的对象和方法，以便H5侧能调用。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">请换成实际应用的在线地址</span></em>
const <span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebLoadErrorPage2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">WebManager</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'WebManager'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'refresh'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onErrorReceive</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorCode</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'index.html'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


  在加载的本地H5侧触发重新加载的方法。

  html示例代码：

  
```text
<em><!-- index.html --></em>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
        body {
          height: 100vh;
          display: flex;
          justify-content: center;<em>  /* 水平居中 */</em>
          align-items: center; <em>     /* 垂直居中 */</em>
        }
        .btn {
          border: none;  <em> /* 移除边框 */</em>
          border-radius: 30px; <em> /* 添加圆角 */</em>
          padding: 12px 30px;
          font-size: 16px;
          background-color: #0A59F7;
          color: white;
          cursor: pointer;
        }
    </style>
</head>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover"/>
<body>
<button class="btn" onclick="refresh()">重新加载</button>
</body>
</html>
<script>
    function refresh() {
      console.info('refresh')
      return window.WebManager.refresh()
    }
</script>
```

- **场景三**：
**方案一**：ArkTS侧实现Web加载H5页面的功能，当加载失败后onErrorReceive回调的errorCode不为0时，使用loadData加载本地html格式的文本数据，并通过javaScriptProxy接口给H5注入对应的对象和方法，以便H5侧能调用。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">请换成实际应用的在线地址</span></em>
const <span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>


<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebLoadErrorPage3 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">WebManager</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'WebManager'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'refresh'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onErrorReceive</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorCode</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(0,0,255);">(</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">html</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">head</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta charset=</span>\"<span style="color: rgb(255,0,170);">UTF-8</span>\"<span style="color: rgb(255,0,170);"> /</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'   </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta name=</span>\"<span style="color: rgb(255,0,170);">viewport</span>\"<span style="color: rgb(255,0,170);"> content=</span>\"<span style="color: rgb(255,0,170);">width=device-width, initial-scale=1.0</span>\"<span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">style</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'        body {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          height: 90vh;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          display: flex;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          justify-content: center;  /* </span><span style="color: rgb(255,0,170);">水平居中</span><span style="color: rgb(255,0,170);"> */</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          align-items: center;      /* </span><span style="color: rgb(255,0,170);">垂直居中</span><span style="color: rgb(255,0,170);"> */</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'        }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'        .btn {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          border: none;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          border-radius: 30px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          padding: 12px 30px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          font-size: 16px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          background-color: #0A59F7;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          color: white;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'          cursor: pointer;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'        }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/style</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/head</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta name=</span>\"<span style="color: rgb(255,0,170);">viewport</span>\"<span style="color: rgb(255,0,170);"> content=</span>\"<span style="color: rgb(255,0,170);">width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover</span>\"<span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">body</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">button class=</span>\"<span style="color: rgb(255,0,170);">btn</span>\"<span style="color: rgb(255,0,170);"> onclick=</span>\"<span style="color: rgb(255,0,170);">refresh()</span>\"<span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">重新加载</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/button</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/body</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/html</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">script</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    function refresh() {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'      console.info("refresh")</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'      return window.WebManager.refresh()</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/script</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">'text/html'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">'UTF-8'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// baseUrl</span><span style="color: rgb(128,128,128);">设置为空格</span></em>
              <span style="color: rgb(255,0,170);">' ' </span><em><span style="color: rgb(128,128,128);">// historyUrl</span><span style="color: rgb(128,128,128);">设置为空格</span></em>
            <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案二**：如果在API20及以上版本，可以在onControllerAttached回调中将setErrorPageEnabled设置为true启用默认错误页。当加载网络页面加载失败后会回调onOverrideErrorPage接口，该接口是一个用于处理错误页面的机制，将需要实现html文本return后，就会把内容渲染在该页面上。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">请换成实际应用的在线地址</span></em>
const <span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'www.baidu.com'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebLoadErrorPage4 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WebManager </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">WebManager</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WEB_URL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onControllerAttached</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setErrorPageEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorPageEnabled</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setErrorPageEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webManager</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'WebManager'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'refresh'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onOverrideErrorPage</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getErrorCode</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">htmlStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">html</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">head</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta charset=</span>\"<span style="color: rgb(255,0,170);">UTF-8</span>\"<span style="color: rgb(255,0,170);"> /</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'   </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta name=</span>\"<span style="color: rgb(255,0,170);">viewport</span>\"<span style="color: rgb(255,0,170);"> content=</span>\"<span style="color: rgb(255,0,170);">width=device-width, initial-scale=1.0</span>\"<span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">style</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'        body {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          height: 100vh;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          display: flex;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          justify-content: center;  /* </span><span style="color: rgb(255,0,170);">水平居中</span><span style="color: rgb(255,0,170);"> */</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          align-items: center;      /* </span><span style="color: rgb(255,0,170);">垂直居中</span><span style="color: rgb(255,0,170);"> */</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'        }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'        .btn {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          border: none;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          border-radius: 30px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          padding: 12px 30px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          font-size: 16px;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          background-color: #0A59F7;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          color: white;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'          cursor: pointer;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'        }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'    </span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/style</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/head</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">meta name=</span>\"<span style="color: rgb(255,0,170);">viewport</span>\"<span style="color: rgb(255,0,170);"> content=</span>\"<span style="color: rgb(255,0,170);">width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover</span>\"<span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">body</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">button class=</span>\"<span style="color: rgb(255,0,170);">btn</span>\"<span style="color: rgb(255,0,170);"> onclick=</span>\"<span style="color: rgb(255,0,170);">refresh()</span>\"<span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">重新加载</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/button</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/body</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/html</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">script</span><span style="color: rgb(255,0,170);">></span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'    function refresh() {</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'      console.info("refresh")</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'      return window.WebManager.refresh()</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'    }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">/script</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
            return <span style="color: rgb(0,0,255);">htmlStr</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          return null<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
> [!NOTE]
> 加载在线网址时需在module.json5中声明ohos.permission.INTERNET权限，确保在线跳转可用。  CODE5 


 
 
 

#### 常见FAQ

Q：为什么加载视频的网页一直触发onErrorReceive？
 
A：在onErrorReceive回调中，查看getErrorCode获取的错误码为-2。-2表示ERR_FAILED，是一个通用的错误代码，表明产生了一般性的错误。错误产生与多种原因有关，可以表示网络错误、文件传输失败、协议栈错误等。接着分析网页的网络请求，发现网页发出了多个请求，而多个响应的HTTP状态码为206。
 
HTTP的206状态码用于表示服务器已成功处理部分Get请求，常见于视频加载和文件下载，尤其是断点续传场景。从错误码和状态码验证可知，一直触发onErrorReceive的原因是，网页中请求了视频资源，而视频使用了断点续传技术，就会导致资源请求多次。因为每一次只处理部分请求，没有完成整个文件的传输，就会引起onErrorReceive回调一次或者多次。
 
 

#### 总结

可以根据缺省页面的实现形式选择实现方案：
  
| 缺省页面的实现形式 | 方案的主要实现方法 | 优点 | 缺点 |
| --- | --- | --- | --- |
| ArkTS页面 | onErrorReceive回调+visibility控件显示状态。 | 加载速度极快，ArkTS渲染，无加载延迟。 | 需要编写缺省页ArkTS页面布局。 |
| html页面 | onErrorReceive回调+loadUrl加载本地html页面。 | 可模块化管理，便于调试，可复用其他端html页面。 | 需要将html文件放在资源目录下，需要文件系统IO，首次加载有延迟。 |
| html格式的文本数据 | 方案一： onErrorReceive回调+loadData加载html格式的文本数据。 | 从内存解析，启动瞬间完成。 | 复杂页面难以维护，全部写成字符串很臃肿。 |
| html格式的文本数据 | 方案二：setErrorPageEnabled+onOverrideErrorPage回调中添加html格式的字符串。 | 系统自定义页面，可以直接将html内容渲染在页面上，用户体验感相对于loadData更好。 | 复杂页面难以维护，全部写成字符串很臃肿。 |
 
 
- 优先推荐使用ArkTS页面实现缺省页，ArkTS渲染，体验感最佳。
- 如果缺省页页面逻辑简单，且需要使用html实现，在API20及以上版本推荐使用onOverrideErrorPage回调方法，API20以下版本推荐使用loadData方法。
- 页面复杂并已有html页面，推荐使用loadUrl方法。
