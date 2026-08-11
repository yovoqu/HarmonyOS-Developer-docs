# 地图如何实现添加折线显示在地点名称和图标（底图POI）上层

更新时间：2026-07-30 01:03:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-27

#### 问题现象

地图添加折线后，折线显示在了地点名称和图标（底图POI）的下层，对折线有遮挡，如何让折线显示在上层。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/TTW8dMxeTPuDBqZ-mAxbPQ/zh-cn_image_0000002658913579.png?HW-CC-KV=V1&HW-CC-Date=20260811T005611Z&HW-CC-Expire=86400&HW-CC-Sign=5B9E16D64C058D2D321E0A280B3424563FE93EB0CF9E3B24D6790F3BAB8C3E63)

 
 

#### 背景知识

- 开发准备：使用地图服务，需要先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。
- [setDisplayOrder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#setdisplayorder)：设置地图元素的显示顺序，按照从低到高排列，即后面的覆盖物会压盖前面的覆盖物。从底层到上层，默认顺序为：OVERLAY（覆盖物，包括折线、动态轨迹等）、POI（底图POI）、CUSTOM_POI（点注释、气泡）、MARKER。

 
 

#### 解决方案

调整元素显示顺序，让OVERLAY（包括折线）元素显示在POI的上层。
 
```text
let <span style="color: rgb(0,0,255);">mapElementTypeArr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[</span>
  <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">POI</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OVERLAY</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CUSTOM_POI</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MARKER</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setDisplayOrder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mapElementTypeArr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
完整代码：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">MapComponent </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AsyncCallback </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">AddPolylineOrder </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化参数</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">mapElementTypeArr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[</span>
          <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">POI</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OVERLAY</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CUSTOM_POI</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapElementType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MARKER</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setDisplayOrder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mapElementTypeArr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        let <span style="color: rgb(0,0,255);">polylineOption</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapPolylineOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">points</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
            <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.979410259206815</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.75625379397866 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">clickable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">startCap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CapStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BUTT</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">endCap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CapStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BUTT</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">jointType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">JointType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BEVEL</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">0xFF0A59F7</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">polyline </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">addPolyline</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">polylineOption</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`add polyline success, polyline is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">polyline</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
