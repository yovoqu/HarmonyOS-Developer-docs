# 如何获取Web组件的宽度

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-154

#### 问题现象

getPageHeight()方法用于获取当前网页的页面高度，如何获取当前Web组件的宽度？
 
 

#### 背景知识

- [getRectangleById](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentutils#getrectanglebyid)：获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。
- [应用侧调用前端页面函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-app-frontend-page-function-invoking)：应用侧可以通过runJavaScript()和runJavaScriptExt()方法调用前端页面的JavaScript相关函数。

 
 

#### 解决方案

**方案一**：获取Web组件的宽度，需要先给Web组件标记一个id，然后通过getRectangleById获取组件信息，根据组件的size.width获取宽度。因为要跟方案二中前端网页获取的宽度对齐，需要使用px2vp将像素（px）转换为视觉像素（vp）。
 
**方案二**：通过runJavaScript方法注入window.innerWidth方法，在回调中即可获取到Web组件的宽度，单位为vp。
 
两种方案示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ComponentUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebGetWidth</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">webResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取组件宽度</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">获取组件宽度</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取组件信息对象，然后获取对象里的</span><span style="color: rgb(128,128,128);">size.width</span><span style="color: rgb(128,128,128);">取得宽度</span>
        let <span style="color: rgb(0,0,255);">componentUtils</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentUtils </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getComponentUtils</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">componentUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRectangleById</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'width is:'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">加载链接需要替换自己业务链接</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPageEnd</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">执行</span><span style="color: rgb(128,128,128);">js</span><span style="color: rgb(128,128,128);">获取页面宽度</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">runJavaScript</span><span style="color: rgb(0,0,255);">(</span>
              <span style="color: rgb(255,0,170);">'function getWidth(){</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    return window.innerWidth;</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    }</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
                <span style="color: rgb(255,0,170);">'    getWidth();'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在回调中获取前端</span><span style="color: rgb(128,128,128);">js</span><span style="color: rgb(128,128,128);">结果</span>
              <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`run JavaScript error, ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,  Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                  return<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
                if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`The width return value is: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
访问在线网页时需添加网络权限：[ohos.permission.INTERNET](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissioninternet)，具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。
 
 

#### 常见FAQ

Q：通过getWindowProperties()系统方法获取的屏幕宽为何与Web加载的H5中通过window.innerWidth方法获取的宽度不一致？
 
A：通过[getWindowProperties()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9)系统方法获取的是当前窗口尺寸，即屏幕分辨率的宽度，单位为px。
 
通过window.innerWidth方法获取的是布局视口的宽度，如果在H5中给viewport的content添加width=device-width，说明当前H5已经适配当前设备尺寸，获取的宽度为Web组件的宽度，单位为vp。如果没有添加，设备上的浏览器都会把默认的viewport设为980px或1024px（这个值由设备决定），单位为px。
 
如果需要在H5中获取到屏幕宽度，可以使用window.screen.width获取，单位为vp。使用[vp2px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#vp2px12)和[px2vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12)方法，px与vp两个单位可以相互转换。
