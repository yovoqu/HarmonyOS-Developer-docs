# 如何解决Scroll嵌套地图组件时的滚动冲突问题

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1555

#### 问题现象

将地图组件，内嵌到了Scroll里面，会出现上下滑动时同时滚动的问题，如何控制滑动地图时Scroll不响应？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/iAEYrLD3RAaFgnLFq-zyog/zh-cn_image_0000002658848495.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005816Z&HW-CC-Expire=86400&HW-CC-Sign=EBA458C01031406160CE44DE7DFBD23A23219A6C85ADBDDF9CAFD0AB0039CC49)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Xu2a8_hETw2cCdf-njcxiA/zh-cn_image_0000002628609232.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005816Z&HW-CC-Expire=86400&HW-CC-Sign=49088D7C0FD20FEAFE7F41BEEAB28C16FB876794098C4F3AB8F3AE92BCFC5CF4)

 
 

#### 背景知识

- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，若子组件尺寸不超过父组件则Scroll不提供滚动能力。
- [滚动组件通用接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common)滚动组件通用属性和事件目前只支持List、Grid、Scroll和WaterFlow组件。提供了诸如滚动条、摩擦系数、滚动到组件最后触发的回调注册等。
- 在使用地图服务之前，需要先通过DevEco Studio或AppGallery Connect网站开通地图服务，详情可见官网指南[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc)。

 
 

#### 解决方案

Scroll中嵌套地图组件的情况，可以在MapComponent的onTouch事件中确认父组件Scroll的滑动状态，若点击到地图则Scroll不响应滑动，松开时恢复。
 
在onTouch回调函数中，使用switch语句根据触摸事件的类型来更新地图组件的滚动方向：
 
- 当触摸事件类型为TouchType.Down时，表示开始触摸，此时设置this.scrollable为ScrollDirection.None，表示停止滚动。
- 当触摸事件类型为TouchType.Up或TouchType.Cancel时，表示停止触摸或取消操作，此时设置this.scrollable为ScrollDirection.Vertical，表示允许垂直滚动。

 
> [!NOTE]
> 地图组件在 开通地图服务 后才可以正常加载地图信息。

 
在EntryAbility中配置沉浸式，示例代码如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    try <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">COLOR_MODE_NOT_SET</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to set colorMode. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Main window is created, set main page for this ability</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getLastWindow</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">lastWindow</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">lastWindow</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowLayoutFullScreen</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pages/MapDemo'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onForeground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <em><span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onBackground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">map </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AsyncCallback </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MapDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">scrollable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ScrollDirection </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ScrollDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Vertical</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapEventManager</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">TAG </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'HuaweiMapDemo'</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapOption</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化参数，设置地图中心点坐标及层级</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOption </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">39.9</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">116.4</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化的回调</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取地图的控制器类，用来操作地图</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEventManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`on-mapLoad`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'mapLoad'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">MapComponent</span><span style="color: rgb(128,128,128);">组件初始化地图</span></em>
          <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOption</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'60%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              switch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                case <span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(181,106,1);">:</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ScrollDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">None</span><span style="color: rgb(181,106,1);">;</span>
                  break<span style="color: rgb(181,106,1);">;</span>
                case <span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Up</span><span style="color: rgb(181,106,1);">:</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ScrollDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Vertical</span><span style="color: rgb(181,106,1);">;</span>
                  break<span style="color: rgb(181,106,1);">;</span>
                case <span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Cancel</span><span style="color: rgb(181,106,1);">:</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ScrollDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Vertical</span><span style="color: rgb(181,106,1);">;</span>
                  break<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用于观测是否跟随滑动</span></em>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">测试是否可以滑动</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
