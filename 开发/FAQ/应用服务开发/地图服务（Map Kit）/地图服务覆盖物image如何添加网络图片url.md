# 地图服务覆盖物image如何添加网络图片url

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-19

#### 问题现象

Map Kit地图服务开发需要添加覆盖物，ImageOverlayParams参数中image只支持ResourceStr和image.PixelMap两种格式，如何将网络图片url添加到image中？
 
 

#### 背景知识

- [Map Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-introduction)：Map Kit（地图服务）为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。
- [覆盖物](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-coverings)：覆盖物是一种位于底图和底图标注层之间的特殊Overlay，该图层不会遮挡地图标注信息。通过[ImageOverlayParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section12537418218)类来设置，开发者可以通过[ImageOverlayParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section12537418218)类设置一张图片，该图片可随地图的平移、缩放、旋转等操作做相应的变换。
- [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)：图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)创建一个PixelMap实例。

 
 

#### 解决方案

[ImageOverlayParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section12537418218)类中image参数只支持ResourceStr和image.PixelMap，无法直接添加网络图片url，可以把网络图片的url转换成[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型显示。
 1. 通过http的request下载网络图片资源，并把网络图片url下载的ArrayBuffer类型的图片转换为[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型数据。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">http</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">request</span><span style="color: rgb(128,128,128);">方法从网络下载图片资源</span></em>
<span style="color: rgb(0,0,255);">async </span><span style="color: rgb(0,0,255);">getPicture</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">请填写一个具体的网络图片地址</span></em>
  <span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'xx.xx.xx.xx.png'</span><span style="color: rgb(181,106,1);">,</span>
    async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpResponse</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'get network picture error:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200 </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">responseCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        const <span style="color: rgb(0,0,255);">imageData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">result </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">创建图片源实例</span></em>
        const <span style="color: rgb(0,0,255);">imageSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ImageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">imageData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        const <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InitializationOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(255,0,170);">'alphaType'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,0,170);">'editable'</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,0,170);">'pixelFormat'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,0,170);">'scaleMode'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,0,170);">'size'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过属性创建</span><span style="color: rgb(128,128,128);">PixelMap</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageMap </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

1. 将转换后的[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)图片添加到[ImageOverlayParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section12537418218)的image参数中。
```text
<span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">添加网络图片覆盖物</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">imageOverlayParams</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ImageOverlayParams </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">覆盖物范围</span></em>
    <span style="color: rgb(0,0,255);">bounds</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">southwest</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">northeast</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32.4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.4 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">,</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">转换过后的</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">图片</span></em>
    <span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageMap</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">transparency</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.3</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">101</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">anchorU</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">anchorV</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">clickable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">visible</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">bearing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <em>// </em><em><span style="color: rgb(128,128,128);">添加覆盖物</span></em>
  await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">addImageOverlay</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">imageOverlayParams</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```

 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">http </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">image </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AsyncCallback</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">MapComponent </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
<span style="color: rgb(181,106,1);">@Entry</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">imageMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PixelMap </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapOptions</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">AsyncCallback</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapComponentController</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mapEventManager</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapEventManager</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">http</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">request</span><span style="color: rgb(128,128,128);">方法从网络下载图片资源</span></em>
  async <span style="color: rgb(0,0,255);">getPicture</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">请填写一个具体的网络图片地址</span></em>
    <span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'xx.xx.xx.xx.png'</span><span style="color: rgb(181,106,1);">,</span>
      async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpResponse</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'get network picture error:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200 </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">responseCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          const <span style="color: rgb(0,0,255);">imageData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">result </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
      <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">创建图片源实例</span></em>
          const <span style="color: rgb(0,0,255);">imageSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ImageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">imageData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InitializationOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(255,0,170);">'alphaType'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'editable'</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'pixelFormat'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'scaleMode'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'size'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(181,106,1);">;</span>
      <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过属性创建</span><span style="color: rgb(128,128,128);">PixelMap</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageMap </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>


  async <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置地图属性模型</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32.2</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.2</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">地图回调</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapEventManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEventManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPicture</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">地图初始化失败</span><span style="color: rgb(255,0,170);">, code is</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">添加网络图片覆盖物</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">imageOverlayParams</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ImageOverlayParams </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">覆盖物范围</span></em>
            <span style="color: rgb(0,0,255);">bounds</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">southwest</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">northeast</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32.4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">118.4 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">,</span>
       <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">转换过后的</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">图片</span></em>
            <span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageMap</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">transparency</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.3</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">101</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">anchorU</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">anchorV</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">clickable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">visible</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">bearing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">添加覆盖物</span></em>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapController</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">addImageOverlay</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">imageOverlayParams</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(0,0,255);">MapComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mapOptions</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mapCallback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：MapKit绘制中是否支持自定义覆盖物，比如图文覆盖和自定义排版？
 
A：当前地图覆盖物仅支持图片，不支持图文覆盖和自定义排版。
