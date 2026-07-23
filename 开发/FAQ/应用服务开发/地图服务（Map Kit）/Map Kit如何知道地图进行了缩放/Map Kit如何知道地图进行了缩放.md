# Map Kit如何知道地图进行了缩放

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-13

#### 问题现象

应用在用户使用过程中需要知道用户是否进行了地图缩放，是否有地图缩放事件通知？
 
 

#### 背景知识

[Map Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-introduction)：具备丰富地图的细节呈现能力，提供了包括缩放、旋转、移动、倾斜等流畅的交互体验。
 
 

#### 解决方案

通过[on(type: 'cameraChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager#section1488710318220)监听地图相机状态变化事件，回调里通过zoom是否变化来判断是否有缩放行为。zoom获取方式为：this.mapController?.getCameraPosition().zoom。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">map</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">MapComponent </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AsyncCallback </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">geoLocationManager </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.LocationKit'</span><span style="color: rgb(181,106,1);">;</span>

<em>/**</em>
<em><span style="color: rgb(128,128,128);"> *</span></em>
<em><span style="color: rgb(128,128,128);"> * 1</span><span style="color: rgb(128,128,128);">、监听用户是否进行地图缩放</span></em>
<em><span style="color: rgb(128,128,128);"> * 2</span><span style="color: rgb(128,128,128);">、监听</span><span style="color: rgb(128,128,128);">“</span><span style="color: rgb(128,128,128);">我的位置</span><span style="color: rgb(128,128,128);">”</span><span style="color: rgb(128,128,128);">按钮点击事件，并初始化我的位置</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MapOnChangeZoom </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">mapOption</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化参数，设置地图中心点坐标及层级</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapOption </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30.246</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">120.145</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">17</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">zoomControlsEnabled</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">myLocationControlsEnabled</span><span style="color: rgb(181,106,1);">: </span>true
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化的回调</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取地图的控制器类，用来操作地图</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">启用我的位置图层</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setMyLocationEnabled</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

        let <span style="color: rgb(255,255,255);">mapEventManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEventManager</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(255,255,255);">cameraChangeCallback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'cameraChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`callback position = </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">position</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取当前地图缩放级别，通过</span><span style="color: rgb(128,128,128);">zoom</span><span style="color: rgb(128,128,128);">是否变化来判断是否有缩放行为</span></em>
          let <span style="color: rgb(255,255,255);">zoom </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getCameraPosition</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">zoom</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'cameraChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`callback zoom = </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">zoom</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">mapEventManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'cameraChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">cameraChangeCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">“</span><span style="color: rgb(128,128,128);">我的位置</span><span style="color: rgb(128,128,128);">”</span><span style="color: rgb(128,128,128);">按钮点击事件</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'myLocationButtonClick'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'myLocationButtonClick'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`myLocationButtonClick`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMyLocation</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始化我的位置</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMyLocation</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapOption</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">callback </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取当前位置并视图移动过去</span></em>
  <span style="color: rgb(0,0,255);">getMyLocation</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCurrentLocation</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Location </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(132,63,161);">'latitude'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'longitude'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'altitude'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'accuracy'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'speed'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'timeStamp'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'direction'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'timeSinceBoot'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setMyLocation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">position</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">CameraUpdate</span><span style="color: rgb(128,128,128);">对象</span></em>
      let <span style="color: rgb(255,255,255);">gcj02Position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertCoordinate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">latLng</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">gcj02Position</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">gcj02Position</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">longitude</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">zoom </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">17</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">cameraUpdate </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">newLatLng</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">latLng</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">zoom</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">以动画方式移动地图相机</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">animateCamera</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">cameraUpdate</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  async <span style="color: rgb(0,0,255);">convertCoordinate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">wgs84Position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">longitude</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">gcj02Position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LatLng </span><span style="color: rgb(181,106,1);">=</span>
      await <span style="color: rgb(255,255,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertCoordinate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CoordinateType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WGS84</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CoordinateType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">GCJ02</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">wgs84Position</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    return <span style="color: rgb(255,255,255);">gcj02Position</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
