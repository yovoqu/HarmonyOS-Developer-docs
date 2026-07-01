# Map Kit地图服务如何设置我的位置图标实时指向当前设备移动方向

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-20

#### 问题现象

Map Kit地图中，我的位置当前可以通过设置mapCommon.MyLocationDisplayType.FOLLOW_ROTATE，实现我的位置图标实时指向设备旋转方向。
 
如何实现我的位置图标实时指向设备的移动方向，比如在跑步场景，我的位置实时指向跑步的方向。
 
 

#### 背景知识

- [MyLocationDisplayType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section78428244375)：定位图标的展示模式。类型设置为FOLLOW时，表示连续定位，且将相机移动到地图中心点，定位蓝点跟随设备移动。
- [setMyLocationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#section126791641317)：设置用户的位置样式。设置icon参数可以自定义我的位置图标样式。displayType参数设置可以设置定位图标的展示样式，可以设置相机是否跟随移动、我的位置图标是否跟随设备旋转等。
- [setMyLocation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#section1165002535516)：Map Kit默认使用系统的连续定位能力显示用户位置，如果希望定制显示频率或者精准度等，可以调用此接口设置“我的位置”坐标。
- [geoLocationManager.on('locationChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanageronlocationchange)：开启位置变化订阅，并发起定位请求。可实时监听当前设备的位置信息，其中包括设备的移动方向信息。

 
 

#### 解决方案

前提条件：
 
- 需要申请"ohos.permission.LOCATION"和"ohos.permission.APPROXIMATELY_LOCATION"位置权限。
- 需要[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。

1. 设置我的位置图标自定义样式和移动效果，此方案场景，需设置displayType参数为mapCommon.MyLocationDisplayType.FOLLOW（我的位置图标不跟随或设备方向旋转）。
```text
let <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MyLocationStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">anchorU</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">anchorV</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">icon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">此处替换为自定义的我的位置图标</span></em>
  <span style="color: rgb(255,255,255);">displayType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MyLocationDisplayType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FOLLOW</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">style</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationEnabled</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```

2. 通过geoLocationManager.on('locationChange')监听当前设备的位置信息[Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#location)，其中包括设备的移动方向信息（direction）。在监听回调中通过setMyLocation接口设置地图上我的位置图标的位置信息，其中包括显示我的位置图标方向为direction设备移动方向。
```text
let <span style="color: rgb(255,255,255);">requestInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(132,63,161);">'priority'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequestPriority</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FIRST_FIX</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">'scenario'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequestScenario</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UNSET</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">'timeInterval'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">'distanceInterval'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">'maxAccuracy'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(255,255,255);">locationChange </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">location</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Location</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">location</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">accuracy </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setMyLocation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">location</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
try <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'locationChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">requestInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">locationChange</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"errCode:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">", message:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
> [!NOTE]
> direction设备移动方向只有在使用GPS定位时才返回有效值，请在空旷的室外进行测试验证。

 
完整示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">MapComponent</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">map </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AsyncCallback </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">geoLocationManager </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.LocationKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MyLocationDirection </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">mapOptions</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化参数，设置地图中心点坐标及层级</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">39.9</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">116.4</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>

   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图初始化的回调</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取地图的控制器类，用来操作地图</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MyLocationStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">anchorU</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">anchorV</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">icon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span></em><em>此处替换为自定义的我的位置图标</em>
          <span style="color: rgb(255,255,255);">displayType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MyLocationDisplayType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FOLLOW</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">style</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMyLocationEnabled</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

        let <span style="color: rgb(255,255,255);">requestInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(132,63,161);">'priority'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequestPriority</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FIRST_FIX</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(132,63,161);">'scenario'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LocationRequestScenario</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UNSET</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(132,63,161);">'timeInterval'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(132,63,161);">'distanceInterval'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(132,63,161);">'maxAccuracy'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(255,255,255);">locationChange </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">location</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Location</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">location</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">accuracy </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setMyLocation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">location</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        try <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">geoLocationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'locationChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">requestInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">locationChange</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"errCode:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">", message:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">MapComponent</span><span style="color: rgb(128,128,128);">组件初始化地图</span></em>
      <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mapOptions</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">callback</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
