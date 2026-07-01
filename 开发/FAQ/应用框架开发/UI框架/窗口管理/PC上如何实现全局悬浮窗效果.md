# PC上如何实现全局悬浮窗效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-995

#### 问题现象

在PC上如何实现全局悬浮窗的效果？
 
 

#### 背景知识

- [startAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability)方法：启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。
- [resize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#resize9-1)方法：基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。
- [setWindowDecorVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowdecorvisible11)方法：设置窗口标题栏是否可见。
- [setWindowTitleButtonVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowtitlebuttonvisible14)方法：设置标题栏上最大化、最小化、关闭按钮是否可见。
- [setWindowTopmost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowtopmost14)方法：将窗口置于其他应用窗口之上不被遮挡。使用该接口需要配置权限：[ohos.permission.WINDOW_TOPMOST](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionwindow_topmost)。
- 窗口不响应拖拽到屏幕边缘最大化、分屏等效果：应用配置文件[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)中设置supportWindowMode属性，可参考[应用声明支持智慧多窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-support)。

 
 

#### 解决方案

实现悬浮窗有设置全局悬浮窗和多开Ability窗口这两种方案。
 
方法一：可以参考官方文档[设置全局悬浮窗（受限开放）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage#设置全局悬浮窗受限开放)，需要申请受限权限[ohos.permission.SYSTEM_FLOAT_WINDOW](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionsystem_float_window)。
 
方法二：使用多开Ability的方案，拉起新的Ability窗口，悬浮窗口需要满足如下特点：无窗口标签栏；无最大化、最小化、关闭窗口按钮；悬浮窗口保持全局置顶效果；主窗口最小化之后，悬浮窗口不跟随最小化；悬浮窗口不响应拖拽到屏幕边缘最大化、分屏等效果。
 1. 新建独立窗口的代码“src/main/ets/pages/pageTwo.ets”并在配置文件“src/main/resources/base/profile/main_pages.json”中新增路径：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Float Window'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
```json
{
  <span style="color: rgb(132,63,161);">"src"</span><span style="color: rgb(181,106,1);">: </span>[
    <span style="color: rgb(80,160,79);">"pages/Index"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(80,160,79);">"pages/pageTwo"</span>
  ]
}
```

2. 在“src/main/module.json5”中配置窗口全局置顶权限：
```json
<span style="color: rgb(80,160,79);">"requestPermissions"</span><span style="color: rgb(181,106,1);">: </span>[
  {
    <span style="color: rgb(80,160,79);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"ohos.permission.WINDOW_TOPMOST"</span>
  }
]<span style="color: rgb(181,106,1);">,</span>
```

3. 新增文件“src/main/ets/entryability/FloatWindowAbility.ets”，声明FloatWindowAbility类，继承自UIAbility，在接口[onWindowStageCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle#onwindowstagecreate)中[loadContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage#loadcontent9)之后获取主窗口对象。对该窗口设置标题栏不可见，最大化、最小化、关闭按钮不可见，设置窗口全局置顶等属性：
```text
export default class <span style="color: rgb(0,0,255);">FloatWindowAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(181,106,1);">{</span>
  private async <span style="color: rgb(0,0,255);">resizeWindow</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      await <span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Succeeded in resizing window.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`resize window failed: </span><span style="color: rgb(132,63,161);"><</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">setDecorVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowDecorVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isVisible</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'set window decor visible success.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`set window decor visible failed: </span><span style="color: rgb(132,63,161);"><</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">setTitleButtonVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isMaxVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">isMinVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isCloseVisible</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowTitleButtonVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isMaxVisible</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isMinVisible</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isCloseVisible</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'set window title button visible success.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`set window title button visible failed: </span><span style="color: rgb(132,63,161);"><</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private async <span style="color: rgb(0,0,255);">setTopmost</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">isWindowTopmost</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      await <span style="color: rgb(255,255,255);">win</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowTopmost</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isWindowTopmost</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'set window topmost success.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`set window topmost failed: </span><span style="color: rgb(132,63,161);"><</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WindowStage</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">加载主窗口对应的页面。</span></em>
    <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pages/pageTwo'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">mainWindow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取应用主窗口。</span></em>
      <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(255,255,255);">mainWindow </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置窗口大小</span></em>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resizeWindow</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mainWindow</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置窗口标题可见</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setDecorVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mainWindow</span><span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置窗口最大化、最小化、关闭按钮可见</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setTitleButtonVisible</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mainWindow</span><span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置窗口置顶</span></em>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setTopmost</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mainWindow</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to obtain the main window. Cause code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

4. 在应用配置文件“src/main/module.json5”的abilities属性中，新增FloatWindowAbility配置项以及supportWindowMode属性为floating：
```ArkTS
{
  <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"FloatWindowAbility"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"srcEntry"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"./ets/entryability/FloatWindowAbility.ets"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"description"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$string:EntryAbility_desc"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"icon"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$media:layered_image"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"label"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$string:EntryAbility_label"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"supportWindowMode"</span><span style="color: rgb(181,106,1);">: </span>[<span style="color: rgb(80,160,79);">"floating"</span>]<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"startWindowIcon"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$media:startIcon"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"startWindowBackground"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$color:start_window_background"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"exported"</span><span style="color: rgb(181,106,1);">: true,</span>
  <span style="color: rgb(132,63,161);">"skills"</span><span style="color: rgb(181,106,1);">: </span>[
    {
      <span style="color: rgb(132,63,161);">"entities"</span><span style="color: rgb(181,106,1);">: </span>[
        <span style="color: rgb(80,160,79);">"entity.system.home"</span>
      ]<span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"actions"</span><span style="color: rgb(181,106,1);">: </span>[
        <span style="color: rgb(80,160,79);">"ohos.want.action.home"</span>
      ]
    }
  ]
}
```

5. 在主界面配置拉起FloatWindowAbility窗口按钮：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Want </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">abilityContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">拉起悬浮窗</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          let <span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处需要根据实际包名进行更改</span></em>
            <span style="color: rgb(255,255,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'com.example.myapplication'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'FloatWindowAbility'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">moduleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'entry'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">abilityContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'start ability success'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`start ability failed, code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
