# startAbility启动小窗口后requestFocus原页面组件报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-6

#### 问题现象

在2in1设备上启动小窗口，小窗口中调用requestFocus到原页面组件时报错150003。
 
```text
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">message</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">The component doesn</span>'t <span style="color: rgb(0,0,255);">exist</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">is currently invisible</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">or has been disabled</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">code</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">150003</span>
```
 
 

#### 背景知识

- [UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)：在Stage模型中，WindowStage/Window可以通过loadContent接口加载页面并创建UI的实例，并将页面内容渲染到关联的窗口中，所以UI实例和窗口是一一关联的。
- [requestFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9)：通过组件的id将焦点转移到组件树对应的实体节点，当前帧生效。
- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)：AppStorage支持应用的主线程内多个UIAbility实例间的UI状态数据共享。
- [startAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability)：startAbility接口是将应用链接放入want中，通过调用[隐式want匹配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings#隐式want匹配原理)的方法触发应用跳转。通过startAbility接口启动时，还需要调用方传入待匹配的action和entity。

 
 

#### 问题定位

错误码[150003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-focus#section150003-节点不存在)表示requestFocus传入的id指向不存在、未挂树或者不可见节点。可以排查以下情况：
 
- 检查目标组件id同requestFocus请求参数是否一致。

  如下小窗口修改焦点方法requestFocus('TextInput')：
```text
<span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestFocus'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```


  主窗口获取焦点组件中.id('TextInput')，同小窗口请求的参数一致：
```text
<span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">!!, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Grey</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span>
```


 
- 组件id一致的情况下，需要检查小窗口启动方式，是否与主窗口之间有共享的UI实例，这样才能将焦点转移到主窗口组件树对应的实体节点。

  如下小窗口是由新的startAbility，通过loadContent接口加载页面新创建的UI实例，与主窗口没有关联，无法将焦点转移到主窗口组件树对应的实体节点。
```text
<span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">calculation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打开新</span><span style="color: rgb(128,128,128);">UI</span><span style="color: rgb(128,128,128);">实例</span></em>
  let <span style="color: rgb(0,0,255);">uiAbility</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'@bundle:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'com.example.keyboard' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/entry/ets/pages/KeyboardPage'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'KeyboardAbility onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uiAbility</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 分析结论

小窗口自己的UIContext调用requestFocus无法使主窗口的组件获取焦点，需要先获取主窗口的UIContext，再使用主窗口的UIContext来调用requestFocus方法，使焦点转移到主窗口组件树对应的实体节点。
 
 

#### 修改建议

在主窗口创建UI实例时，获取UIContext存到AppStorage应用全局的UI状态存储中，在小窗口将焦点转移到主窗口组件树对应的实体节点时，获取存储中的主窗口UIContext。示例代码如下：
 1. 在EntryAbility内，主窗口获取并保存UIContext：
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <em><span style="color: rgb(128,128,128);">// Main window is created, set main page for this ability</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Window</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"entryContext"</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to obtain the main window. Cause code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onForeground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onBackground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```

2. Index.ets页面,使用startAbility唤起小窗口。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">componentUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">StartOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">!!, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Grey</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'openSoftKeyboard'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSoftKeyboard</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">openSoftKeyboard</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">安全键盘输入框</span></em>
    let <span style="color: rgb(0,0,255);">modePosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">componentUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ComponentInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getComponentUtils</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRectangleById</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">layoutX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">modePosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">screenOffset</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">layoutY </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">modePosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">screenOffset</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">inputH </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">modePosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">inputW </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">modePosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'com.example.keyboard'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'KeyboardAbility'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">moduleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'entry'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">parameters</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">inputX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">layoutX</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">inputY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">layoutY</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">inputH</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">inputH</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">inputW</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">inputW</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">StartOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">supportWindowModes</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
        <span style="color: rgb(255,0,0);">2</span>
      <span style="color: rgb(0,0,255);">]</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">uiAbilityContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">uiAbilityContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">    }</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 新建KeyboardPage.ets，通过StorageProp获取在主窗口保存的UIContext，可以通过该UIContext对TextInput获取焦点使能。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">KeyboardPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">keyboardText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@StorageProp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'entryContext'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keyboardText</span><span style="color: rgb(181,106,1);">!!, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Grey</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput2'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestFocus success'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestFocus error'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInput'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 新建小窗口的Ability命名为KeyboardAbility，并通过loadContent加载KeyboardPage页面，并且指定小窗口的大小和位置。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">KeyboardAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打开</span></em>
    let <span style="color: rgb(0,0,255);">uiAbility</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'@bundle:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'com.example.keyboard' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/entry/ets/pages/KeyboardPage'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uiAbility</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取应用启动时的窗口尺寸</span></em>
<em>        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注册回调函数，监听窗口尺寸变化</span></em>
        <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">移动位置</span></em>
        <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">moveWindowTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置主窗口或子窗口的布局是否为沉浸式布局</span></em>
        let <span style="color: rgb(0,0,255);">isLayoutFullScreen </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        try <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">promise </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowLayoutFullScreen</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isLayoutFullScreen</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">exception</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span>
        <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowSystemBarEnable</span><span style="color: rgb(0,0,255);">([])</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          } </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">exception</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span>
          try <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'windowTitleButtonRectChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">exception</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">canIUse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'SystemCapability.Window.SessionManager'</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">isTouchable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setWindowDecorVisible</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isTouchable</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```

5. 将KeyboardAbility添加至模块配置的module.json5中abilities里。
```ArkTS
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": [
      "phone"
    ],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          }
        ]
      },
      {
        "name": "KeyboardAbility",
        "srcEntry": "./ets/keyboardability/KeyboardAbility.ets",
        "description": "$string:KeyboardAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:KeyboardAbility_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start_window_background"
      }
    ],
    "extensionAbilities": [
      {
        "name": "EntryBackupAbility",
        "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
        "type": "backup",
        "exported": false,
        "metadata": [
          {
            "name": "ohos.extension.backup",
            "resource": "$profile:backup_config"
          }
        ],
      }
    ]
  }
}
```
