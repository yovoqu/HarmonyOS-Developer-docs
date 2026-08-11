# 如何通过SVG字符串加载图片

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-51

#### 问题现象

通过其他三方库生成的SVG字符串，需要使用Image组件进行加载，如何实现？
 
 

#### 背景知识

- [Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)可显示矢量图（SVG格式的图片），SVG标签文档请参考[SVG标签说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg)。如果SVG图片没有原始大小，需要给Image组件设置宽高，否则不显示。SVG图片不支持通过image标签引用svg格式和gif格式的本地其他图片。
- 加载SVG图片目前可行的方法有很多，例如下载为SVG文件，然后通过文件读取；或者解析为Uint8Array，然后转为[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)进行加载，目前转为PixelMap方式可行性更高。

 
 

#### 解决方案

需要显示的SVG图片样例效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/oxRpaxLaRuWZNRIH_gJOIg/zh-cn_image_0000002658911825.png?HW-CC-KV=V1&HW-CC-Date=20260811T005542Z&HW-CC-Expire=86400&HW-CC-Sign=1737D3733D1A32AAE44D743D03B5E45E92DDFF2186596505195F4E2EEAD1C881)

 
首先可以使用[TextEncoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textencoder)类的[encodeInto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#encodeinto9)方法，将SVG字符串转化为Uint8Array类型，然后使用[createImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreateimagesource9-2)通过buffer创建ImageSource实例，最后使用[createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource#createpixelmap7)返回结果。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">image </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">util </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PixelMap </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将以下内容替换成从三方库得到的</span><span style="color: rgb(128,128,128);">SVG</span><span style="color: rgb(128,128,128);">字符串</span></em>
  <span style="color: rgb(255,255,255);">svgContent </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">uint8ArrayToPixelMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">svg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PixelMap</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">encoder </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextEncoder</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">encoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeInto</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">svg</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">iconArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">source </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">iconArray</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">source</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMap</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">source</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击根据字符串加载</span><span style="color: rgb(132,63,161);">SVG</span><span style="color: rgb(132,63,161);">图片</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uint8ArrayToPixelMap</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">svgContent</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PixelMap</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
