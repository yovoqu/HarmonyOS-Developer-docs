# 使用PixelMap完成图像变换及常见问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-32

#### 问题现象

如何对图片进行裁剪、缩放、偏移、旋转、翻转、透明度修改等图像变换操作。
 
 

#### 背景知识

[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)是图像解码后的一种无压缩位图格式，图片解码是指将所支持格式的图片文件解码成统一的PixelMap格式，目前支持的图片格式有JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。PixelMap主要用于图像显示或进一步处理。这种格式可以有效地存储图像的原始数据，使其可以方便地进行[图像变换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation)，如裁剪、缩放、偏移、旋转、翻转、设置透明度等。
 
 

#### 解决方案

使用HarmonyOS的PixelMap进行图像变换主要涉及以下几个步骤：
 1. [图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)：首先，需要加载并解码图片文件，这将返回一个PixelMap对象，该对象用于后续的图像操作。
2. 获取图片信息：在进行变换之前，若需要获取图片的一些基本信息如宽度和高度，可以通过调用异步方法[getImageInfo()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#getimageinfo)或同步方法[getImageInfoSync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#getimageinfosync)来进行获取。
3. 执行图像变换：包括裁剪、缩放、旋转、翻转、透明度修改等操作，以图片缩放的具体示例代码如下：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">image </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">common </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">imagePixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PixelMap </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">scaleCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPixelMap</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">pixelMap</span></em>
  <span style="color: rgb(0,0,255);">getPixelMap</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">resourceManager</span><span style="color: rgb(128,128,128);">资源管理</span></em>
    const <span style="color: rgb(255,255,255);">resourceManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取图片数据</span></em>
    const <span style="color: rgb(255,255,255);">fileData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMediaContentSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em>// startIcon</em><em><span style="color: rgb(128,128,128);">为测试图片，开发者需要替换为实际图片</span></em>
    const <span style="color: rgb(255,255,255);">buffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fileData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">imageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">pixelMap </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createPixelMapSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">editable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">desiredDynamicRange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DecodingDynamicRange</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AUTO</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">对</span><span style="color: rgb(128,128,128);">pixelMap</span><span style="color: rgb(128,128,128);">进行缩放</span></em>
  <span style="color: rgb(0,0,255);">scalePixelMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PixelMap</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">scaleCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">scaleCount</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">scaleCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">pixelMap</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'80%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'60%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">None</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">缩小</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scaleCount </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scaleCount </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">0.1</span><span style="color: rgb(181,106,1);">;</span>
           <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取图片基本信息，如果宽高大于</span><span style="color: rgb(128,128,128);">300</span><span style="color: rgb(128,128,128);">，继续缩小</span></em>
              let <span style="color: rgb(255,255,255);">imageInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImageInfoSync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">imageInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">300 </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">imageInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">300</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scalePixelMap</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imagePixelMap</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scaleCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"100%"</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"100%"</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
更多[图像变换示例效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation#示例代码)。
 
 

#### 常见FAQ

Q：获取网络图片的PixelMap，如何进行居中剪裁（center crop）？
 
A：获取到PixelMap后，可调用[crop(region: Region)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9-1)方法，设置剪裁目标区域[region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#region8)参数为居中，对图片进行裁剪。
 
Q：HarmonyOS系统上，有时候竖屏图片加载时会显示成横屏。
 
A：有些设备会给图片加一个旋转属性，HarmonyOS相册组件是Image的API无法读取此属性，想要规避这个问题可以通过[getImageProperty()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource#getimageproperty11)获取旋转信息，判断图片是否要旋转，如果需要旋转可以通过[rotate(90)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#rotate)进行调整。
 
Q：图片缩放算法函数[scaleSync(x:number,y:number)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#scalesync)，x和y大概0.2左右（图片长宽尺寸缩小0.046），最终图片byte值为原始图的0.0558倍，这个结果不符合预期，预期也是0.046倍。
 
A：scaleSync影响的是PixelMap的比例大小，缩放后编码的数据会变小，但是不一定成比例。
 
Q：使用PixelMap.rotate旋转图片没有改变。
 
A：这个问题涉及PixelMap的深拷贝，可以参考[深拷贝demo](https://gitee.com/harmonyos_samples/image-depth-copy)。
 
Q：相同代码真机中无法正常旋转图片。
 
A：需要把图片解码设置选项[DecodingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#decodingoptions7)中设置editable：true。
 
Q：使用pixelMap.scale缩放图片没有效果。
 
A：[pixelMap.scale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#scale9-1)是异步函数，需要在执行成功后再进行别的操作，否则图片没有缩放效果，需要使用同步接口[pixelMap.scaleSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#scalesync12)，或者在接口pixelMap.scale前增加异步await。
 
Q：如何对拍照后获取的JPEG图像进行裁剪，再写回文件？
 
A：先将JPEG图像[解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)获取PixelMap对象，对PixelMap使用[crop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9)接口进行裁剪，再将裁剪后的PixelMap[编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding)成JPEG图像重新写入文件即可。
 
Q：为什么通过resourceManager.getMediaContent方法获取媒体文件内容后，通过createPixelMap方法转换失败？
 
A：[image.createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)方法的入参为图像像素数据，而resourceManager.[getMediaContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getmediacontent9)方法回调函数中返回的是媒体文件内容数据，媒体文件数据可以直接用于播放，但是不能作为image.createPixelMap方法的入参，需要通过解码转换为可用图片像素数据才可以用于图片处理或渲染。
