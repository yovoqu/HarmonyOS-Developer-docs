# 地图添加标记返回undefined如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-20

#### 问题现象

在地图的指定位置添加标记，但地图没有显示标记，添加标记返回undefined，如何解决？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/xV01HIRNR3e9AjMLY6Xf-A/zh-cn_image_0000002658913755.png?HW-CC-KV=V1&HW-CC-Date=20260723T013810Z&HW-CC-Expire=86400&HW-CC-Sign=B0C76C27ECB0C95D08ED85F8E30D6698BF9CD4FDEAC6E3BD9BFE8628CED9F031)

 
 
问题代码示例如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MarkerPage </span><span style="color: rgb(255,0,170);">{</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">myLocationControlsEnabled</span><span style="color: rgb(181,106,1);">: </span>true
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEventManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationControlsEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        let <span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"mapLoad"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span>
        let <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">LatLng </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">markerOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MarkerOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">position</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">marker </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">addMarker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">markerOptions</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7lWGEMfKTAOyWuKrDPYK5A/zh-cn_image_0000002658793809.png?HW-CC-KV=V1&HW-CC-Date=20260723T013810Z&HW-CC-Expire=86400&HW-CC-Sign=0E1BB3F80CE4F6B9B275502FD1012C3F18813ADF609CF67F89C08A1E4B81C8AA)

 
 

#### 背景知识

点标记用来在地图上标记任何位置，例如用户位置、车辆位置、店铺位置等一切带有位置属性的事物，具体实现可参考：[开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-marker#section1564972414506)。
 
 

#### 问题定位
1. 从代码中看出，添加marker的代码是在NavDestination组件的onReady()方法中实现。
2. NavDestination组件即将构建完时会触发onReady()方法，而这时并不能保证Mapkit的callback回调方法已经执行完了，如果执行onReady()方法之前，Mapkit的callback回调方法还没有被触发，那么在onReady()方法中调用mapController对象就会是undefined。
 
 

#### 分析结论

在调用this.mapController对象之前要保证callback回调方法已经执行完成，另外callback回调方法是地图组件MapComponent加载完成之后才会触发。
 
 

#### 修改建议

将this.marker = await this.mapController?.addMarker(markerOptions)相关的代码挪到Mapkit的callback方法里执行，代码示例如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">map </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AsyncCallback </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MarkerPage </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapEventManager</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">myLocationControlsEnabled</span><span style="color: rgb(181,106,1);">: </span>true
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化的回调</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取地图的控制器类，用来操作地图</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEventManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationControlsEnabled</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'mapLoad'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        let <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">LatLng </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">31.984410259206815</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.76625379397866</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(0,0,255);">markerOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MarkerOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">position</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        try <span style="color: rgb(255,0,170);">{</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">addMarker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">markerOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'addMarker error'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">MapComponent</span><span style="color: rgb(128,128,128);">组件初始化地图</span>
        <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'75%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideTitleBar</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onShown</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">show</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onHidden</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hide</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
