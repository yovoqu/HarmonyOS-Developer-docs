# Web组件如何实现屏幕共享功能

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-150

#### 问题现象

Web组件加载的H5中使用navigator.mediaDevices.getDisplayMedia后出现没有权限的问题，如何实现屏幕共享功能？
 
 

#### 背景知识

- 当H5中的JavaScript代码调用getDisplayMedia尝试进行屏幕捕获时，会触发Web组件的[onScreenCaptureRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onscreencapturerequest10)回调。
- [grant](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler#grant10)：对网页访问的屏幕捕获操作进行授权。
- [deny](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler#deny10)：拒绝网页所请求的屏幕捕获操作。

 
 

#### 解决方案

在H5中调用getDisplayMedia发起屏幕共享，触发Web组件中onScreenCaptureRequest回调，在回调中通过event.handler.grant完成屏幕捕获权限申请。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">webview </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'refresh'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            try <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refresh</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`ErrorCode: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">,  Message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'screenCapture.html'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">databaseAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onlineImageAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScreenCaptureRequest</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              return<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`on onScreenCaptureRequest Origin:  </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handler</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getOrigin</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showAlertDialog</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'title'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">请求权限</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handler</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getOrigin</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">primaryButton</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'deny'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,255,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handler</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deny</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">secondaryButton</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'onConfirm'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,255,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handler</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">grant</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">captureMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">WebCaptureMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HOME_SCREEN </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">cancel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handler</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deny</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
screenCapture.html：
 
```text
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">!doctype </span><span style="color: rgb(128,128,128);">html</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">html </span><span style="color: rgb(128,128,128);">lang</span><span style="color: rgb(80,160,79);">="en"</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">head</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">charset</span><span style="color: rgb(80,160,79);">="UTF-8"</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">name</span><span style="color: rgb(80,160,79);">="viewport"</span>
          <span style="color: rgb(128,128,128);">content</span><span style="color: rgb(80,160,79);">="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">http-equiv</span><span style="color: rgb(80,160,79);">="X-UA-Compatible" </span><span style="color: rgb(128,128,128);">content</span><span style="color: rgb(80,160,79);">="ie=edge"</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">title</span><span style="color: rgb(181,106,1);">></span>Document<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/title</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">style</span><span style="color: rgb(181,106,1);">></span>
        #video {
            width: 200px;
            height: 400px;
            border: 2px solid red;
        }
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/style</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/head</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">body</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">script</span><span style="color: rgb(181,106,1);">></span>
    function share() {
        navigator.mediaDevices.getDisplayMedia({video: true}).then(stream => {
            document.getElementById('res').innerText = '';
          <em>  // 创建一个video元素</em>
            let video = document.getElementById('video');
         <em>   // 设置video元素的srcObject为获取到的流</em>
            video.srcObject = stream;
            video.play();
        }).catch(res => {
            document.getElementById('res').innerText = res;
        })
    }
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/script</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">button </span><span style="color: rgb(128,128,128);">onclick</span><span style="color: rgb(80,160,79);">="share()"</span><span style="color: rgb(181,106,1);">></span>投屏<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/button</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">video </span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(80,160,79);">="video"</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/video</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">span </span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(80,160,79);">="res"</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/span</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/body</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/html</span><span style="color: rgb(181,106,1);">></span>
```
