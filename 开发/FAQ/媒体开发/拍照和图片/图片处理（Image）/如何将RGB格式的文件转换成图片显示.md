# 如何将RGB格式的文件转换成图片显示

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-50

#### 问题现象

HarmonyOS中视频流格式转换成的RGB格式的图像文件，如何以图片的形式展示？
 
 

#### 背景知识

[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#pixelmap)是图像解码后的一种无压缩位图格式，图片解码是指将所支持格式的图片文件解码成统一的PixelMap格式，目前支持的图片格式有JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。PixelMap主要用于图像显示或进一步处理，这种格式可以有效地存储图像的原始数据，使其可以方便地进行[图像变换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation)，如裁剪、缩放、偏移、旋转、翻转、设置透明度等。
 
RGB文件是指使用RGB（红、绿、蓝）颜色模式存储图像数据的任何文件，这种模式主要用于显示设备，是基于光的三原色模型。
 
 

#### 解决方案

RGB格式的文件无法直接用Image组件显示，需要使用RGB格式的文件中的数据来创建PixelMap，再使用Image组件来显示，步骤如下：
 1. 读取RGB格式的文件中的数据。
2. 图像数据存入到ArrayBuffer中。
3. 设置创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。
4. 通过图像像素数据和像素的属性[image.createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8-1)创建PixelMap。
5. 使用Image组件显示创建的PixelMap。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">resourceManager </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.LocalizationKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">image </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PixelMap </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">resourceMgr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ResourceManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">openRGB</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// 1</span><span style="color: rgb(128,128,128);">、读取</span><span style="color: rgb(128,128,128);">RGB</span><span style="color: rgb(128,128,128);">格式的文件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceMgr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">fileData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// 2</span><span style="color: rgb(128,128,128);">、获取到文件的数据，存储成</span><span style="color: rgb(128,128,128);">ArrayBuffer</span></em>
      const <span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`buffer.bytelength:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// 3</span><span style="color: rgb(128,128,128);">、设置创建</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">的配置，</span><span style="color: rgb(128,128,128);">srcPixelFormat</span><span style="color: rgb(128,128,128);">是原数据的格式（即</span><span style="color: rgb(128,128,128);">RGB</span><span style="color: rgb(128,128,128);">文件的格式），</span><span style="color: rgb(128,128,128);">pixelFormat</span><span style="color: rgb(128,128,128);">是创建出来的</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">格式，</span><span style="color: rgb(128,128,128);">size</span><span style="color: rgb(128,128,128);">是分辨率</span></em>
      let <span style="color: rgb(0,0,255);">opts</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InitializationOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">editable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">srcPixelFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">pixelFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1080</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1920 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// 4</span><span style="color: rgb(128,128,128);">、创建</span><span style="color: rgb(128,128,128);">PixelMap</span></em>
      <span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">opts</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PixelMap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Succeeded in creating pixelmap.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to create pixelmap. code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to get RawFileContent,error code:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">示例文件仅作参考，实际开发请以本地文件为准</span></em>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">打开</span><span style="color: rgb(255,0,170);">RGB'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openRGB</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'imageData.rgb'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <em>      <span style="color: rgb(128,128,128);">// 5</span><span style="color: rgb(128,128,128);">、将</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">Image</span><span style="color: rgb(128,128,128);">组件显示出来</span></em>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Contain</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
 

#### 常见FAQ

Q：使用BGRA8888的格式创建PixelMap后，将其B和R颜色通道数据互换为RGBA8888格式后打印的像素格式应该为更换后的RGBA8888但仍为BGRA8888。
 
A：图像的像素数据储存在buffer中，创建PixelMap设置PixelMapFormat时就是指定以什么方式去解析读取像素数据。手动更改buffer里面的数据后没有改变PixelMap去解析buffer的方式，所以仍然是原本的格式，需要重新更改PixelMapFormat去读取数据。
