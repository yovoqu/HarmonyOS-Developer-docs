# 如何解决网页发生重定向后JS对象丢失的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-139

#### 问题现象

APP中使用Web组件加载在线网页，网页内部会跳转到新网页，JS交互无法响应，方法不执行。
 
关键代码如下：
 
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onControllerAttached</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerJavaScriptProxy</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webTestObj</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"objTestName"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">"webTest"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"webString"</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
 

#### 背景知识

- [前端页面调用应用侧函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking)：开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的方法，实现在前端页面中调用应用侧方法。
- [onLoadIntercept](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。
- [onControllerAttached](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontrollerattached10)：当Controller成功绑定到Web组件时触发该回调。
- [registerJavaScriptProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#registerjavascriptproxy)：registerJavaScriptProxy提供了应用与Web组件加载的网页之间强大的交互能力。

 
 

#### 问题定位

页面初始化的情况下加载网页A，然后发现网页A内部跳转网页B时，JS对象丢失了。尝试页面直接加载目标链接，不会出现JS丢失情况。当监听到url和之前的url域名不一致，尝试重新注册一遍JS，问题可以解决。
 
 

#### 分析结论

当网页发生整页跳转（非单页应用的路由切换）加载新页面时，原页面上下文会被完全重置。因此，之前注册到H5上的自定义JS对象会丢失。
 
 

#### 修改建议

需要监听页面url是否发生变化，如果发生变化就重新注入对象。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">模拟注入数据，需要根据业务修改注入的对象</span></em>
class <span style="color: rgb(0,0,255);">WebObj </span><span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">webTest</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Web test'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,0,170);">'Web test'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">webString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Web test toString'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebRedirect </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">webTestObj</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WebObj </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">WebObj</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <em><span style="color: rgb(128,128,128);">// src</span><span style="color: rgb(128,128,128);">需替换为相应业务的网址</span></em>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onControllerAttached</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerJavaScriptProxy</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webTestObj</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"objTestName"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">"webTest"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"webString"</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoadIntercept</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">=== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'loginfo: </span><span style="color: rgb(255,0,170);">首次加载</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`loginfo: </span><span style="color: rgb(255,0,170);">两次</span><span style="color: rgb(255,0,170);">url</span><span style="color: rgb(255,0,170);">不一样</span><span style="color: rgb(255,0,170);">——</span><span style="color: rgb(255,0,170);">上次加载</span><span style="color: rgb(255,0,170);"> url</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">== </span>null <span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'null' </span><span style="color: rgb(181,106,1);">:</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> ---- </span><span style="color: rgb(255,0,170);">本次加载</span><span style="color: rgb(255,0,170);"> URL</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <em>// </em><em><span style="color: rgb(128,128,128);">重新注册</span><span style="color: rgb(128,128,128);">JS</span><span style="color: rgb(128,128,128);">对象</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerJavaScriptProxy</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webTestObj</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"objTestName"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">"webTest"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"webString"</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">两次</span><span style="color: rgb(255,0,170);">url</span><span style="color: rgb(255,0,170);">相同，未发生重定向</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          return false<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：ArkWeb如何判断发生了重定向？
 
A：在ArkTS WebView中判断请求是否发生重定向，可以通过[onLoadIntercept](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onloadintercept10)拦截网络请求，再通过[isRedirect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourcerequest#isredirect)请求是否重定向。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebRedirectJudge </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">记录加载的</span><span style="color: rgb(128,128,128);">url</span></em>
  <span style="color: rgb(0,0,255);">isRedirect</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">是否发生重定向</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// scr</span><span style="color: rgb(128,128,128);">需替换为相应业务的网址</span></em>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoadIntercept</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`onLoadIntercept, url is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">=== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">首次加载</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">首次加载</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将此次加载路径保存入变量中，为下次对比做参照</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">非首次加载</span></em>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">和上一次跳转的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">相同</span></em>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">两次</span><span style="color: rgb(255,0,170);">url</span><span style="color: rgb(255,0,170);">相同，未发生重定向</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">和上一次跳转的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">不同</span></em>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断服务器重定向</span></em>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">服务器重定向</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
                if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRequestGesture</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">判断是否发生了交互，未交互就跳转认定为代码重定向，发生了交互认定为正常页面跳转</span></em>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">页面跳转</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">用户交互发生的页面跳转属于正常页面跳转，不属于重定向</span></em>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">客户端页面代码重定向</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">若未发生交互，直接进行页面跳转则认定发生了重定向</span></em>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRequestUrl</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">将此次加载路径保存入变量中，为下次对比做参照</span></em>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
          return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRedirect</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

任何页面跳转或重定向都会导致当前页面的JavaScript上下文被完全销毁并重建，所以监听到此类事件时需要重新注入JS对象。
