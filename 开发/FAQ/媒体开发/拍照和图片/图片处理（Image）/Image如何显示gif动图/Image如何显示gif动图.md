# Image如何显示gif动图

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-42

#### 问题现象

gif图解码出来的PixelMap放到Image组件中只显示静态图，怎么显示动图？
 
 

#### 背景知识

- [Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display)支持图片的显示，支持加载存档图类型的数据源，包括本地资源、网络资源、Resource资源、媒体库资源和base64，也支持加载PixelMap像素图。
- [ImageSource.createPixelMapList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource#createpixelmaplist10)支持图片解码并返回PixelMap数组。针对动图如gif、Webp，此接口返回每帧图片数据；针对静态图，此接口返回唯一的一帧图片数据。

 
 

#### 解决方案

gif图片可以通过createPixelMapList创建PixelMap数组，然后传入[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)类型播放PixelMap数组动画。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AnimationOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">AnimatedDrawableDescriptor </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">image </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ImageGifDemo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">animationOpt</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimationOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">animated</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimatedDrawableDescriptor </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AnimatedDrawableDescriptor</span><span style="color: rgb(255,0,170);">([]</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animationOpt</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// app.media.gif1</span><span style="color: rgb(128,128,128);">是</span><span style="color: rgb(128,128,128);">gif</span><span style="color: rgb(128,128,128);">文件，需要自行配置</span></em>
          let <span style="color: rgb(255,255,255);">pixelMaps </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixmapFromMedia</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.gif1'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animated </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AnimatedDrawableDescriptor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pixelMaps</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animationOpt</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>

      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animated</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'200'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'200'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">读取资源文件返回</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">数组</span></em>
  private async <span style="color: rgb(0,0,255);">getPixmapFromMedia</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">resource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Resource</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMediaContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">resource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">imageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">uint8Array</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">uint8Array</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">byteLength</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">pixelMapList </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMapList</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">desiredPixelFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PixelMapFormat</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RGBA_8888</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">pixelMapList</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 总结

Image组件通过AnimatedDrawableDescriptor类型传入PixelMap数组即可实现gif动画的播放。
