# Web组件加载链接，如何修改链接网页中的文本

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-147

#### 问题现象

使用Web组件加载第三方的网页时，需要修改网页中的文本信息，如何实现？
 
 

#### 背景知识

- 在H5（HTML5）中，可以使用getElementById获取到指定ID的标签：
根据ID获取指定的Span标签：
```text
const <span style="color: rgb(255,255,255);">spanElement </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">document</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getElementById</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'mySpan'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 也可以通过getElementsByTagName获取到指定名称标签的集合：
```text
const <span style="color: rgb(255,255,255);">spanElements </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">document</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getElementsByTagName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'span'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```


 - [runJavaScriptExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascriptext10)：WebView提供了runJavaScriptExt实现异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。

 
 

#### 解决方案
1. 可以通过runJavaScriptExt注入脚本实现修改三方网页中文本。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">webview </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">Context</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">initJavaScrip</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注入本地的</span><span style="color: rgb(128,128,128);">js</span><span style="color: rgb(128,128,128);">脚本</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'index.js'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ESObject</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">js</span><span style="color: rgb(128,128,128);">脚本的</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">数据</span></em>
        let <span style="color: rgb(255,255,255);">rawfile</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始注入脚本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">runJavaScriptExt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">rawfile</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始注入脚本成功</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始注入脚本失败</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'span.html'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPageEnd</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">initJavaScrip</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">3000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 在js中通过getElementById获取指定ID的标签，并修改其文本内容。index.js：

  
```text
let <span style="color: rgb(255,255,255);">spanLabels </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">document</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getElementById</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'mySpan'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`mySpan:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">spanLabels</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">innerHTML</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,255,255);">spanLabels</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">innerHTML </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(132,63,161);">修改后的文本</span><span style="color: rgb(132,63,161);">"</span>
```

3. 加载的本地页面。span.html：

  
```text
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">!DOCTYPE </span><span style="color: rgb(128,128,128);">html</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">html</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">body</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">name</span><span style="color: rgb(80,160,79);">="viewport" </span><span style="color: rgb(128,128,128);">content</span><span style="color: rgb(80,160,79);">="width=device-width, initial-scale=1.0"</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">h1 </span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(80,160,79);">="example"</span><span style="color: rgb(181,106,1);">></span>示例文本<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/h1</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">span </span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(80,160,79);">="mySpan"</span><span style="color: rgb(181,106,1);">></span>这是默认文本<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/span</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/body</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/html</span><span style="color: rgb(181,106,1);">></span>
```

 
 

#### 常见FAQ

Q：runJavaScript()和runJavaScriptExt()有什么区别？
 
A：[runJavaScript()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)和runJavaScriptExt()的区别主要体现在参数和返回值的类型上。runJavaScript()仅支持string类型参数，而runJavaScriptExt()支持string和ArrayBuffer类型参数；runJavaScript()返回脚本执行的结果只能是string，而runJavaScriptExt()可以返回的类型支持[JsMessageType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-jsmessageext)，包括字符串、数组类型等。
