# 如何封装bindPopup的options

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-738

#### 问题现象

如何封装bindPopup的PopupOptions以实现复用？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DL0HzdB6SrmMFwUzcHdIMg/zh-cn_image_0000002628555358.png?HW-CC-KV=V1&HW-CC-Date=20260701T041207Z&HW-CC-Expire=86400&HW-CC-Sign=9A29C6DD4CDB6E3D123A2D86947DF4C73B81C21419350B0F766C3E0BA9D3306A)

 
 

#### 背景知识

- [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)可以为组件绑定气泡弹窗，其参数[PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup#popupoptions)可以被封装以提高复用性。
- [emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter)是一个在HarmonyOS Next中用于进程内或同一线程间的事件处理机制，它允许应用程序进行事件的订阅、发布和取消订阅。

 
 

#### 解决方案
1. 在CustomPopUtility.ets中定义气泡弹窗的显示内容，并封装气泡弹窗的配置属性。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">emitter </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">csPopupBuilder</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">Resource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">title</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDisAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// Pop</span><span style="color: rgb(128,128,128);">消失时发送</span><span style="color: rgb(128,128,128);">emitter</span><span style="color: rgb(128,128,128);">事件。</span></em>
        <span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">emit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">eventId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">priority</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EventPriority</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HIGH</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">13</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

export function <span style="color: rgb(0,0,255);">buildOptionsParams</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">that</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Object</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">customPopup</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomPopupOptions </span><span style="color: rgb(181,106,1);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">想在此处解析皮肤配置</span><span style="color: rgb(128,128,128);">title</span><span style="color: rgb(128,128,128);">，字体颜色、背景颜色、气泡描边色</span><span style="color: rgb(128,128,128);">offset</span><span style="color: rgb(128,128,128);">等</span></em>
  return <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">csPopupBuilder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bind</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">that</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'#FFFFFF'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">placement</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Placement</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">y</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">6 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">arrowWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">arrowHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">6</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NONE</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">popupColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#5291FF'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isVisible</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'res='</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">customPopup</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 在Index.ets中调用CustomPopUtility.ets中封装的弹窗配置属性,并使用emitter进行监听Pop的消失事件，以此达到一次封装可多次复用的效果。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">emitter </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">buildOptionsParams </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./CustomPopUtility'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">收到</span><span style="color: rgb(128,128,128);">eventId</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">的事件后执行回调函数修改</span><span style="color: rgb(128,128,128);">Pop</span><span style="color: rgb(128,128,128);">的状态变量</span></em>
    <span style="color: rgb(255,255,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">eventId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EventData</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">温馨提示</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">25</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bold</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
       <em> <span style="color: rgb(128,128,128);">//Pop</span><span style="color: rgb(128,128,128);">封装后只需一行代码即可实现调用。</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buildOptionsParams</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">国庆中秋假期</span><span style="color: rgb(132,63,161);">10</span><span style="color: rgb(132,63,161);">月</span><span style="color: rgb(132,63,161);">1</span><span style="color: rgb(132,63,161);">日至</span><span style="color: rgb(132,63,161);">8</span><span style="color: rgb(132,63,161);">日放假调休，共</span><span style="color: rgb(132,63,161);">8</span><span style="color: rgb(132,63,161);">天。所有收费公路（含机场高速、收费桥梁和隧道）免征小型客车通行费</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShowSchedulePopupGuide</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
