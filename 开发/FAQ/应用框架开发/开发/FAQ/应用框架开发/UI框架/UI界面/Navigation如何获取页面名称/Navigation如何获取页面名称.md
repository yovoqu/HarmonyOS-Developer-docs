# Navigation如何获取页面名称

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1399

#### 问题现象

Navigation路由跳转场景下，如何获取当前所在页面的页面名称或者信息？
 
 

#### 背景知识

- NavPathStack页面路由栈，此对象下保存了当前的路由过程，其中[getAllPathName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#getallpathname10)返回路由栈中所有NavDestination页面名称的数组，最后一项即为当前页面名称。
- NavDestination：进行路由跳转的时候，NavDestination会响应[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)方法，其响应参数为NavDestinationContext，其包含了页面名称等信息。
- setInterception：Navigation提供的页面跳转拦截回调方法，可以在[setInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#setinterception12)中拦截页面跳转操作，也可以获取到NavDestinationContext的内容。

 
 

#### 解决方案

获取页面名称的方案有三种：
 
- 通过NavPathStack的getAllPathName方法拿到所有页面的名称，最后一项即为当前页面名称。
- 在NavDestination的onReady回调中通过NavDestinationContext中的pathInfo拿到页面名称。
- 通过setInterception拦截页面跳转，获取到跳转目标页面名称。

 
Navigation页面：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">NaviDesPagBuilder </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./SubPage'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">setInterception</span><span style="color: rgb(128,128,128);">跳转拦截获取目标页面名称</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setInterception</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">willShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,0,170);">'navBar'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,0,170);">'navBar'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>typeof <span style="color: rgb(0,0,255);">from </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'string'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`from: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        if <span style="color: rgb(0,0,255);">(</span>typeof <span style="color: rgb(0,0,255);">to </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'string'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'target page is navigation home'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        let <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">to </span>as <span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`setInterception currentPageName = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'GetNaviPageName_NaviDesPage'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">NaviDesPagBuilder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转</span><span style="color: rgb(255,0,170);">NavDestination'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'20fp'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50vp' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'GetNaviPageName_NaviDesPage' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageMap</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
NavDestination页面：
 
```text
<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">NaviDesPagBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">GetNaviPageName_NaviDesPage</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">GetNaviPageName_NaviDesPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'GetName'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">getAllPageName</span><span style="color: rgb(128,128,128);">，拿到所有页面名字，最后一项即为当前页面名称</span></em>
          let <span style="color: rgb(0,0,255);">names </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navPathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAllPathName</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">pageName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">names</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">names</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`last page of getAllPathName: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pageName</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">onReady</span><span style="color: rgb(128,128,128);">回调的</span><span style="color: rgb(128,128,128);">NavDestinationContext</span><span style="color: rgb(128,128,128);">获取当前页面名称</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navPathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`onReady: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：Navigation获取页面参数getParamByName获取的返回值为什么是Array？
 
A：getParamByName是路由栈NavPathStack的实例方法，路由栈中一个页面可以入栈多次。例如在页面A中push一个页面A，此时路由栈中就有两个页面A，每次跳转到页面A可能携带不同的参数，所以getParamByName方法的返回值是数组。
