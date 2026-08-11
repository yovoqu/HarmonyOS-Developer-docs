# 自定义弹窗如何使用WrappedBuilder封装的样式实现倒计时效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-510

#### 问题现象

需要实现以下场景：页面中有个按钮，点击按钮弹出弹窗，弹窗中有个10s倒计时，文案显示的是10到0的数字，显示为0时弹窗消失。
 
 

#### 背景知识

- [ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)：ComponentContent表示组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。
- [update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#update)：用于更新WrappedBuilder对象封装的builder函数参数，与constructor传入的参数类型保持一致。
- [setInterval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#setinterval)：重复调用一个函数，在每次调用之间具有固定的时间延迟。

 
 

#### 解决方案

实现弹窗倒计时效果可以参考如下方案进行，其中更新WrappedBuilder对象封装的builder函数参数要用update()方法实现。具体步骤如下：
 1. 使用ComponentContent创建自定义组件内容。
2. 通过openCustomDialog打开弹窗。
3. 设置timer定时器，并通过update()方法更新builder函数参数。
 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos.base'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ComponentContent </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos.arkui.node'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Params </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">buildText</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#FFF0F0F0'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TimeIndex </span><span style="color: rgb(255,0,170);">{</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">@State</span><span style="color: rgb(128,128,128);">装饰器管理状态，记录动态更新的数值</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isEnabled</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">intervalID </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setInterval</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">update</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">--</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">update</span><span style="color: rgb(128,128,128);">方法更新对话框内容</span></em>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">|| </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isEnabled </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">clearInterval</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">intervalID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭对话框并重置状态</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'click me'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isEnabled</span><span style="color: rgb(0,0,255);">)</span>

          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">promptAction </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建自定义组件内容，包含渲染函数和参数</span></em>
            let <span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">wrapBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buildText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
            try <span style="color: rgb(255,0,170);">{</span>

              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打开自定义对话框</span></em>
              <span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">onWillAppear</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isEnabled </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">onWillDismiss</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isEnabled </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">onDidDisappear</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>

                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              let <span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">code </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`OpenCustomDialog args error code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
