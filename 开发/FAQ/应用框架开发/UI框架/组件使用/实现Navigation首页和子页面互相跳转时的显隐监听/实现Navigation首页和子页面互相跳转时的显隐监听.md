# 实现Navigation首页和子页面互相跳转时的显隐监听

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-504

#### 问题现象

一个应用的UI页面采用Navigation组件作为根视图，并使用NavPathStack进行页面跳转。在onPageShow事件不支持或不执行的情况下，如何监听Navigation首页和子页面互相跳转的过程中两个页面的显示和隐藏？
 
问题关键代码如下：
 
```ArkTS
<em>// Index.ets</em>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavigationPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageInfos'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从子页返回根页面不会触发</span></em>
  <span style="color: rgb(0,0,255);">onPageShow</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'NavigationPage onPageShow'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
```ArkTS
<em>// PageOne.ets</em>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageInfos'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// onPageShow</span><span style="color: rgb(128,128,128);">不会被触发</span></em>
  <span style="color: rgb(0,0,255);">onPageShow</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'NavDestination PageOne onPageShow'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

- [onPageShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow)和[onPageHide](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpagehide)仅在router路由页面每次显示隐藏时触发。其他[自定义组件生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-lifecycle)无法触发。
- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)是路由导航的根视图容器，一般作为页面（@Entry）的根容器，[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)是Navigation子页面的根容器。
- [@ohos.arkui.observer (无感监听)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer)提供UI组件行为变化的无感监听能力。可通过[uiObserver.on('navDestinationSwitch')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserveronnavdestinationswitch12)监听Navigation的页面切换事件。

 
 

#### 解决方案

Navigation组件通常被用作Page页面的根容器，它内部默认包含标题栏、内容区域和工具栏。在内容区域中，默认情况下，首页会展示导航内容（即Navigation的子组件），而子页面则展示NavDestination的子组件。当从首页跳转至子页面时，实际打开的是NavDestination组件，而不是一个router页面，因此不会触发应用页面特有的onPageShow和onPageHide生命周期方法。
 
- **场景一**：监听NavDestination组件的显示和隐藏。可以使用[onShown](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onshown10)事件和[onHidden](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onhidden10)事件来监听NavDestination组件的显示和隐藏。示例可参考[NavDestination生命周期时序](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#示例8navdestination生命周期时序)。
- **场景二**：监听Navigation首页的显示和隐藏。

  在Navigation不使用[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)隐藏导航栏的场景下，监听Navigation的[onNavBarStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#onnavbarstatechange9)事件。在回调函数中，如果变量isVisible为true，表明首页正在显示。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavBarStateChangePage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">PageB</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">NavDestination</span><span style="color: rgb(255,0,170);">页面</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'PageB' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onNavBarStateChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Navigation</span><span style="color: rgb(255,0,170);">显示</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Navigation</span><span style="color: rgb(255,0,170);">隐藏</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageB </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">返回</span><span style="color: rgb(255,0,170);">Navigation'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 
- **场景三**：监听首页和子页的显示和隐藏。在首页的aboutToAppear函数中使用无感监听uiObserver.on('navDestinationSwitch')监听页面切换。回调函数的入参为[NavDestinationSwitchInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#navdestinationswitchinfo12)，可以根据from和to的信息判断隐藏和显示的页面。

  
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">uiObserver </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavDestinationSwitchPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">navigation</span><span style="color: rgb(128,128,128);">页面切换事件</span></em>
    <span style="color: rgb(0,0,255);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'navDestinationSwitch'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">switchInfo</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可根据</span><span style="color: rgb(128,128,128);">from</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">to</span><span style="color: rgb(128,128,128);">判断显隐的页面，类型为</span><span style="color: rgb(128,128,128);">NavDestinationInfo</span><span style="color: rgb(128,128,128);">表示子页，为</span><span style="color: rgb(128,128,128);">NavBar</span><span style="color: rgb(128,128,128);">表示</span><span style="color: rgb(128,128,128);">Navigation</span><span style="color: rgb(128,128,128);">页面</span></em>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`from </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">switchInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> -</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);"> to </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">switchInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'navDestinationSwitch'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">取消监听</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">PageA</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">NavDestination</span><span style="color: rgb(255,0,170);">页面</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'PageA' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageA </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">返回</span><span style="color: rgb(255,0,170);">Navigation'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 

#### 常见FAQ

Q：Navigation子页面A跳转到子页面B后，重新返回页面A，如何监听A页面重新展示了？
 
A：[onActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onactive17)在NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。当重新返回A页面后会触发onActive函数。
