# 如何实现在NavDestination子页面中动态调整公共组件的样式

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1170

#### 问题现象

在NavDestination子页面中抽离出公共组件，如何动态调整公共组件的样式？比如，在NavDestination的A子页面中，组件使用红色背景色，而在B子页面中，组件使用蓝色背景色。
 
 

#### 背景知识

- [组件导航（Navigation）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)主要用于实现Navigation页面（NavDestination）间的跳转，支持在不同Navigation页面间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
- 自定义组件提供[queryNavDestinationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api#querynavdestinationinfo)方法，可以在NavDestination内部查询到当前所属页面的信息，返回值为[NavDestinationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#navdestinationinfo)，若查询不到则返回undefined。

 
 

#### 解决方案

整体上来看，首先需要使用Navigation组件构建路由导航的根视图容器，然后使用NavDestination构建子页面。在子页面中，将公共组件抽离，并利用queryNavDestinationInfo方法查询组件所属的页面，进行动态调整。
 1. 使用Navigation组件构建路由导航的根视图容器。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">根容器</span></em>
<span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转第一个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'one'</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转第二个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'two'</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">myDestination</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```

2. 使用NavDestination构建子页面。
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">One </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'navPathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">第一个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Common</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Two </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'navPathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">第二个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Common</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

3. 抽离公共组件，利用queryNavDestinationInfo方法查询组件所属的页面，进行动态调整。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">公共组件</span></em>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Common </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NavDestinationInfo </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">queryNavDestinationInfo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">这里是公共的组件</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(132,63,161);">所属页面</span><span style="color: rgb(132,63,161);">Name: " </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据</span><span style="color: rgb(128,128,128);">NavDestinationInfo</span><span style="color: rgb(128,128,128);">动态调整样式</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(132,63,161);">'one' </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Red</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
完整示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">uiObserver </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
<span style="color: rgb(181,106,1);">@Entry</span>
struct <span style="color: rgb(0,0,255);">DynamicallyAdjustPublicComponents </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'navPathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">myDestination</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(132,63,161);">'one'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">One</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(132,63,161);">'two'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Two</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根容器</span></em>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转第一个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'one'</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转第二个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'two'</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">myDestination</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">One </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'navPathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">第一个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Common</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Two </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'navPathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">第二个页面</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Common</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">公共组件</span></em>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Common </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">uiObserver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NavDestinationInfo </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">queryNavDestinationInfo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">这里是公共的组件</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(132,63,161);">所属页面</span><span style="color: rgb(132,63,161);">Name: " </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据</span><span style="color: rgb(128,128,128);">NavDestinationInfo</span><span style="color: rgb(128,128,128);">动态调整样式</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">navDesInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(132,63,161);">'one' </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Red</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
