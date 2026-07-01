# 通过页面跳转将CardRecognition控件拍照界面关闭

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-2

#### 问题现象

通过设置了两个[setTimeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#settimeout)定时器控制[CardRecognition（卡证识别控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition)实现拍照界面关闭，预期效果是进入页面五秒后，会渲染CardRecognition控件，在进入页面十秒后，会销毁CardRecognition控件。
 
 

#### 背景知识

当前系统已支持卡证识别控件提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。CardRecognition控件会拉起的是一个系统的全模态弹窗，页面组件的显隐状态无法关闭该弹窗。
 
 

#### 解决方案

将CardRecognition控件单独放在一个页面，设置定时器通过页面路由跳转来实现自主关闭卡证识别拍摄功能。核心代码参考如下：
 
- Index.ets：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">卡证识别入口按钮</span></em>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'CardRecognition'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'cardDemoPage'</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">卡证识别控件</span><span style="color: rgb(255,0,170);">demo'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">NavigationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
- CardDemoPage.ets
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">CardRecognition</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">CardRecognitionResult</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">CardType</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">CardSide</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ShootingMode </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.VisionKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'CardRecognitionPage'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">CardDemoPageBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">CardDemoPage</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">卡证识别页，用于加载</span><span style="color: rgb(128,128,128);">uiExtensionAbility</span></em>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">CardDemoPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">timerId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">子页面销毁时清除定时器</span></em>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timerId </span><span style="color: rgb(181,106,1);">!== -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">clearTimeout</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timerId</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">CardRecognition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处选择身份证类型作为示例</span></em>
        <span style="color: rgb(0,0,255);">supportType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CardType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CARD_ID</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">cardSide</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CardSide</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DEFAULT</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">cardRecognitionConfig</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">defaultShootingMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ShootingMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MANUAL</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">isPhotoSelectionSupported</span><span style="color: rgb(181,106,1);">: </span>true
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">onResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CardRecognitionResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`params code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`params cardInfo front: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">front</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`params cardInfo back: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">back</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手动返回或扫描到结果返回上个页面</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">goBack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideTitleBar</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`current page config info is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getConfigInRouteMap</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onShown</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当该</span><span style="color: rgb(128,128,128);">NavDestination</span><span style="color: rgb(128,128,128);">页面显示时设置定时器，定时触发路由返回</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timerId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">goBack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">5000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * 1.</span><span style="color: rgb(128,128,128);">如果返回的是</span><span style="color: rgb(128,128,128);">Navigation</span><span style="color: rgb(128,128,128);">根页面需要使用</span><span style="color: rgb(128,128,128);">getRouter()</span><span style="color: rgb(128,128,128);">返回</span></em>
<em><span style="color: rgb(128,128,128);">   * 2.</span><span style="color: rgb(128,128,128);">如果返回的是</span><span style="color: rgb(128,128,128);">NavDestination</span><span style="color: rgb(128,128,128);">子页面可使用</span><span style="color: rgb(128,128,128);">NavPathStack</span><span style="color: rgb(128,128,128);">返回</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">goBack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRouter</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">replaceUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'pages/Index' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- router_map.json：
```ArkTS
{
  "routerMap": [
    {
      "name": "cardDemoPage",
      "pageSourceFile": "src/main/ets/pages/CardDemoPage.ets",
      "buildFunction": "CardDemoPageBuilder",
      "data": {
        "description": "this is cardDemoPage"
      }
    }
  ]
}
```


 
> [!NOTE]
> 不要在同一界面设置两个定时器，否则第二个定时器执行后也不会关闭拍照界面。
