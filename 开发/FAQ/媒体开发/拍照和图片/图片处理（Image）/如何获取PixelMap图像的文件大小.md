# 如何获取PixelMap图像的文件大小

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-48

#### 问题现象

在编辑PixelMap时，由于PixelMap在动态的修改，有什么方法可以获取到PixelMap图像的大小。
 
 

#### 背景知识

- [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)：是一种用于管理和操作像素数据的数据结构。它通常用于图像处理和渲染，能够动态地存储和修改像素信息，主要特点：
动态修改：PixelMap，可以实时更新和修改像素数据，支持高效的像素操作。
- 像素访问：可以通过索引直接访问和修改单个像素值。
- 图像渲染：可以将PixelMap转换为图像文件或直接在屏幕上进行渲染。

 - [ImagePacker](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding)：图片编码指将PixelMap编码成不同格式的图片文件，当前支持编码为JPEG、WebP、PNG和HEIF格式，用于后续处理，如保存、传输等。
- [getPixelBytesNumber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#getpixelbytesnumber7)：获取图像像素的总字节数。
- [packToData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13)：图片编码获取到的文件流，写入文件保存即可得到一张图片。
- [packToFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofile11)：图片编码进文件，通过传入对应的文件路径，编码后的PixelMap数据将直接写入文件。

 
 

#### 解决方案

获取PixelMap的文件大小可以通过以下两种方案：
- 使用[getPixelBytesNumber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#getpixelbytesnumber7)方法获取图像像素的总字节数，需要注意的是该方法得到的是位图占的字节数。在对PixelMap进行处理前，需要使用createImageSource获取图片的ArrayBuffer，并创建新的PixelMap实例。
- 可使用ImagePacker的[packToData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13)方法，将PixelMap图片进行编码，从而获取到图片文件的大小。使用方式和效果图如下：

 
 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">image </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Page </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PixelMap </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">saveToData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">packOpts</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PackingOption </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">format</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'image/png'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">quality</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">imagePackerApi</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ImagePacker </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImagePacker</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">imagePackerApi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">packToData</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">packOpts</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`packToData</span><span style="color: rgb(255,0,170);">后的文件大小：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">CreatePixelMap</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMediaContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">提取图片数据的缓冲区</span>
      let <span style="color: rgb(0,0,255);">arrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteOffset</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteOffset</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">ImageSource</span><span style="color: rgb(128,128,128);">对象</span>
      let <span style="color: rgb(0,0,255);">imageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">arrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置初始化选项</span>
      let <span style="color: rgb(0,0,255);">opts</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InitializationOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">editable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">pixelFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6 </span><span style="color: rgb(255,0,170);">} }</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">PixelMap</span>
      <span style="color: rgb(0,0,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">opts</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to create pixelmap. code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CreatePixelMap</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">PixelMap</span><span style="color: rgb(128,128,128);">的像素字节数</span>
          let <span style="color: rgb(0,0,255);">pixelBytesNumber</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pixelMap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelBytesNumber</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`PixelMap</span><span style="color: rgb(255,0,170);">像素的总字节数：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pixelBytesNumber</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">saveToData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/4eQqQw0yTJiR59U46Tg0Jg/zh-cn_image_0000002658911821.png?HW-CC-KV=V1&HW-CC-Date=20260701T041038Z&HW-CC-Expire=86400&HW-CC-Sign=2CE93DCC77B1975D32EBA0995015023E3D1A995B97F8C2D2ED4F3B228AFFAB14)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Bz9enBOQQrOTsMF3EG2Slw/zh-cn_image_0000002628392612.png?HW-CC-KV=V1&HW-CC-Date=20260701T041038Z&HW-CC-Expire=86400&HW-CC-Sign=084F21B7898FABA5254CE26130EFA557324B4A72984D2065423691FF1401A9C0)

 
 

#### 常见FAQ

Q：通过getPixelBytesNumber方法获取到的图片大小和实际图片大小相差较大。
 
A：图片解码内存占用是宽 * 高 * 像素字节数，默认是rgba格式即一个像素占用四字节，所以通过getPixelBytesNumber方法获取到的图片大小为宽 * 高 * 4。
 
Q：ImageInfo中的stride表示什么含义？getPixelBytesNumber获取到的字节数和通过height乘以stride得到的数值为什么不同？
 
A：[ImageInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#imageinfo)中的stride表示图片跨距，内存中每行像素所占的空间。stride通常满足：stride≥图像宽度×每像素字节数。[getPixelBytesNumber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#getpixelbytesnumber7)是获取图像像素的总字节数。图像像素总字节数=图像高度x图像宽度x每像素字节数。所以图像像素总字节数小于等于height*stride。
 
Q：packToData方法执行时提示未定义。
 
A：[packToData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13)方法在API13以上才提供，需要系统升级到对应版本以上才能使用该方法。
 
Q：[packToFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofile11-1)方法执行时提示[62980115](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image#section62980115-图片无效参数)。
 
A：packToFile接口使用Promise形式时，无返回结果，需按接口规范使用。
