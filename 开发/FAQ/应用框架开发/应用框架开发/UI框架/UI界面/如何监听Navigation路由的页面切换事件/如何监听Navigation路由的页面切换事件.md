# 如何监听Navigation路由的页面切换事件

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-573

#### 问题现象

如何监听Navigation的页面切换，以便在页面转场过程中执行自定义操作？如获取进退场页面的相关信息、拦截切换等。
 
 

#### 背景知识

- [@ohos.arkui.observer(无感监听)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer)提供UI组件行为变化的无感监听能力。如页面生命周期、组件显隐状态、滚动事件等。其中[uiObserver.on('navDestinationSwitch')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserveronnavdestinationswitch12)可以监听Navigation的页面切换事件并执行自定义操作。
- [setInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#setinterception12)：用于设置Navigation页面跳转拦截回调。通过setInterception方法实现路由拦截，可用于统一处理页面跳转前的逻辑校验（如登录态验证、页面状态管理等）。

 
 

#### 解决方案

- **方案一**：使用uiObserver.on('navDestinationSwitch')方法订阅Navigation页面切换事件，并在参数中传入回调函数，用于执行相应的逻辑处理。
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">uiObserver </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">callBackFunc</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NavDestinationSwitchInfo</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">from </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">to </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`from:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> to: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavObserverDemo </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">stack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">Page</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'navDestinationSwitch'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callBackFunc</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注册页面切换的监听</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'navDestinationSwitch'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callBackFunc</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'pageOne' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Navigation'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Page</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageOne'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageOne'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案二**：使用导航控制器NavPathStack的setInterception方法，在入参[NavigationInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationinterception12)中可以设置页面跳转前后的拦截回调。

  以跳转前拦截为例：在页面跳转前打印跳转目标页面的信息。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setInterception</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">willShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,0,170);">'navBar'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,0,170);">'navBar'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>typeof <span style="color: rgb(0,0,255);">from </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'string'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">target </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">to </span>as <span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`from page is navigation home -</span><span style="color: rgb(255,0,170);">></span> <span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span>typeof <span style="color: rgb(0,0,255);">to </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'string'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">target </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">from </span>as <span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> -</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);"> to page is navigation home`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'PageOne'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'PageOne'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'PageOne'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'PageOne'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 常见FAQ

Q：无感监听有哪些常见事件？
 
A：监听滚动事件[uiObserver.on('scrollEvent')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserveronscrollevent12)、监听NavDestination组件的状态变化[uiObserver.on('navDestinationUpdate')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserveronnavdestinationupdate)、监听TabContent页面的切换事件[uiObserver.on('tabContentUpdate')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserverontabcontentupdate12)等。
