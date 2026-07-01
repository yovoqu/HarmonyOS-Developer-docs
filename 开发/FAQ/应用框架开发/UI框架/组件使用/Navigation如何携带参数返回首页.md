# Navigation如何携带参数返回首页

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-708

#### 问题现象

使用Navigation实现页面导航功能，从首页跳转到其他非首页之后，再次返回首页，如何将数据传递回首页？
 
 

#### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部可分为首页和子页。首页又称为导航栏（NavBar），由三部分组成：标题栏、内容区（Navigation子组件）、工具栏。

  子页则通过[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)承载，由两部分组成：标题栏、内容区（NavDestination子组件）。
- Navigation路由相关的操作都是基于页面栈[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)提供的方法进行，每个Navigation都需要创建并传入一个NavPathStack对象，用于管理页面。主要涉及页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能。
> [!NOTE]
> 首页并不属于路由栈（NavPathStack）管理，路由栈只能控制NavDestination页面的入栈出栈。

- [pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname11)：将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。
- [@ohos.events.emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter)：支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。
- [hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)：设置是否隐藏导航栏。设置为true时，隐藏Navigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

 
返回首页一般存在两种方式：
 1. 通过NavPathStack的pop方法一步步回退至首页，最简单的场景是：首页->PageOne->首页。
2. 首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。一个简单的场景是：首页->PageOne->PageTwo->首页。
 
 

#### 解决方案

- **场景一：**从其他页面一步步回退至首页。直接在首页通过pushPathByName等方法跳转到PageOne页面，同时添加onPop回调接收PageOne页面返回的参数即可。

  
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavPopSolution </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">展示返回参数</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转到</span><span style="color: rgb(132,63,161);">PageOne'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
         <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用于页面出栈时触发该回调处理返回结果。</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">首页</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageMap</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">携带参数回退首页</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">'content'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'c' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2FJuhdcmTFezVGRJYS3BCA/zh-cn_image_0000002628394992.png?HW-CC-KV=V1&HW-CC-Date=20260701T041244Z&HW-CC-Expire=86400&HW-CC-Sign=A1B602D16303DF38ACF668F8694221E8FAB7DF8B1A055A603169B57555FB06EC)

- **场景二**：首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。由于需要立马返回首页，无法一步步将路由栈中页面逐个出栈，所以无法通过出栈时的onPop回调，拿到上一个页面出栈时携带的参数。且首页无法推入路由栈，不能使用push类方法跳转，也没有onReady生命周期，所以也无法在onReady接收其他子页的传参。

  现提供两种方式完成跳转，并将参数携带回首页。

  
**方案一**：不使用默认的首页，将一个NavDestination自定义为首页。在返回自定义首页MainPage时，先调用[clear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#clear10)方法清除路由栈中的页面，然后重新将MainPage页入栈，即可在MainPage页[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)方法中接收返回的参数。1. 在Navigation首页设置hideNavBar为true，在aboutToAppear方法中将MainPage入栈，设置为自定义首页。通过[setInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#setinterception12)拦截所有返回到Navigation首页的操作，重定向到自定义首页。

2. 从PageTwo页面跳转至MainPage，先使用clear()清除路由栈，再主动调用pushPath跳转到自定义首页MainPage。MainPage页面通过onReady方法获取传递参数。
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavMainPageExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">MainPage</span><span style="color: rgb(128,128,128);">设置成自定义首页</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">Navigation</span><span style="color: rgb(128,128,128);">页面跳转拦截回调</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setInterception</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">willShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(132,63,161);">'navBar'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(132,63,161);">'navBar'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">operation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavigationOperation</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">animated</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">from</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">to</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">operation</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">animated</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果要返回到首页，就</span><span style="color: rgb(128,128,128);">push</span><span style="color: rgb(128,128,128);">名为</span><span style="color: rgb(128,128,128);">MainPage</span><span style="color: rgb(128,128,128);">的子页面</span></em>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">to </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'navBar'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">MainPage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'PageTwo'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">PageTwo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideNavBar</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">隐藏首页</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageMap</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// NavDestination</em><em><span style="color: rgb(128,128,128);">作为首页</span></em>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MainPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转到</span><span style="color: rgb(132,63,161);">PageOne'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getParamByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转到</span><span style="color: rgb(132,63,161);">PageTwo'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageTwo'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">携带参数回退首页</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">清除路由栈</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'MainPage'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'context' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">跳转到自定义首页</span></em>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageTwo'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
> [!NOTE]
> 连续调用多个页面栈操作方法时，中间过程会被忽略，显示最终的栈操作结果。


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/1jlaw3eJReKa3dUO_V3C8A/zh-cn_image_0000002658794257.png?HW-CC-KV=V1&HW-CC-Date=20260701T041244Z&HW-CC-Expire=86400&HW-CC-Sign=F643295094EC00EDF053B19A5E824332F65EE9F326550677EF876F1273008D8F)

- **方案二**：在首页的aboutToAppear订阅事件，在clear清除路由栈时通过订阅的事件将参数传递回首页。
```json
import <span style="color: rgb(255,255,255);">emitter </span>from <span style="color: rgb(132,63,161);">'@ohos.events.emitter'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">EmitterSolution </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EventData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">back</span><span style="color: rgb(128,128,128);">事件，获取参数</span></em>
    <span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'back'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'back'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">取消监听</span></em>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'PageTwo'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">PageTwo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转到</span><span style="color: rgb(132,63,161);">PageOne'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">首页</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageMap</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转到</span><span style="color: rgb(132,63,161);">PageTwo'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageTwo'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PageOne'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">回退到首页，通过</span><span style="color: rgb(132,63,161);">emitter</span><span style="color: rgb(132,63,161);">传递参数</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EventData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">'content'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'c'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'1' </span><span style="color: rgb(181,106,1);">} }</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">emit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'back'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传递</span><span style="color: rgb(128,128,128);">back</span><span style="color: rgb(128,128,128);">事件给首页</span></em>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pageTwo'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavDestinationContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bLvbPWA5TIiOu1Yzk-pO_Q/zh-cn_image_0000002628554896.png?HW-CC-KV=V1&HW-CC-Date=20260701T041244Z&HW-CC-Expire=86400&HW-CC-Sign=3020E09ED797922E7ED5C8382298B083DDFC7B00AFF1A43282CA7EE63074F2CD)


 
 
 

#### 常见FAQ

Q：Navigation如何直接返回首页？
 
A：首页不存在页面栈中，可看作在栈中的位置为-1，使用this.pathStack.clear()清空栈即可返回首页。
 
 

#### 总结
 
| 场景 | 方案 | 说明 |
| --- | --- | --- |
| 从其他页面一步步回退至首页 | 使用onPop回调链式接收 | 适合页面逐级返回的场景。 |
| 多次跳转之后立马返回 | 自定义首页 | 无法适配导航栏分栏显示模式。需要对自定义首页进行路由管理。导航栏等需要自定义实现。 |
| 多次跳转之后立马返回 | 事件订阅 | 页面销毁时未正确销毁监听，可能会导致内存泄露。需要新增一个订阅事件，造成订阅事件过多。 |
