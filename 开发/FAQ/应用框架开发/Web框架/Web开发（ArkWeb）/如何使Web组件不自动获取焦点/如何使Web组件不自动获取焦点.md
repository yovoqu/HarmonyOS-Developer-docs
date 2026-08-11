# 如何使Web组件不自动获取焦点

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-156

#### 问题现象

Web组件调用loadUrl方法后如何设置不自动获取焦点？
 
 

#### 背景知识

- [loadUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)：用于加载指定的URL，该API除了指定需要加载的URL外，还可以设置URL的附加HTTP请求头。
- [焦点事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event)：指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。
- [onFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event#onfocus)：当前组件获取焦点时触发的回调。
- [onBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event#onblur)：当前组件失去焦点时触发的回调。
- [focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)：为通用属性，设置当前组件是否可以获焦。
当focusable设置为false时为失焦状态，并触发失焦回调onBlur。
- 当focusable设置为true时为获焦状态，并触发获焦回调onFocus。

 
 
 

#### 解决方案

Web组件调用loadUrl方法后，将focusable属性设置为false时就可以不自动获取焦点，通过onBlur和onFocus回调获取当前焦点状态。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">webBorderColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Yellow</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isFocus</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'loadUrl</span><span style="color: rgb(255,0,170);">调用按钮</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            try <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isFocus </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,  Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">获取焦点按钮</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            try <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isFocus </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,  Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span> <em>// </em><em><span style="color: rgb(128,128,128);">监听获焦事件，获焦后改变颜色</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webBorderColor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Red</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span> <em>// </em><em><span style="color: rgb(128,128,128);">监听失焦事件，失焦后改变颜色</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBlur</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webBorderColor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Yellow</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webBorderColor</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isFocus</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'45%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
