# Web组件如何加载HEIF、HEIC、SVGA、SVG文件

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-180

#### 问题现象

HEIF和HEIC、SVGA和SVG分别是什么，Web组件如何加载这些文件？
 
 

#### 背景知识

- HEIF图片（High Efficiency Image File Format），是一个用于单张图像或图像序列的文件格式。目前主流的HEIF图片均使用HEVC(H.265)编码。
- HEIC是符合HEIF标准、使用HEVC编码的具体图像文件。
- SVGA是一种轻量级的动画格式，相比GIF和APNG格式，它支持更多的动画特性，如透明度、缩放和旋转等。
- SVG（Scalable Vector Graphics）是可缩放矢量图形，它是一种基于XML（可扩展标记语言）的图形格式，用于描述二维图形和图像。具体可参考[SVG标签说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg)。

 
 

#### 解决方案

- HEIF、HEIC和SVG图片支持在HTML里直接通过img标签展示，以加载本地图片为例（需要先将HTML文件放到rawfile目录下，图片资源文件放到rawfile/img目录下）。完整样例代码如下：

  
```text
<em><!-- heif.html --></em>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>测试HEIF/HEIC/SVG图片</title>
    <style>
        p {
            font-size: 16px;
        }
        .flex-center {
            display: block;
            justify-content: center;
            align-items: center;
            min-height: 300px;
        }
        .responsive-img {
            width: 55%;
            height: auto;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
<div class="flex-center">
    <div>
        <p>HEIF图片</p>
       <em> <span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">!--</span><span style="color: rgb(128,128,128);">网络图片</span><span style="color: rgb(128,128,128);">src</span><span style="color: rgb(128,128,128);">直接换成对应的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">地址即可</span><span style="color: rgb(128,128,128);">--</span><span style="color: rgb(128,128,128);">></span></em>
        
![](img/test.heif)

    </div>
    <div>
        <p>HEIC图片</p>
       <em> <span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">!--</span><span style="color: rgb(128,128,128);">网络图片</span><span style="color: rgb(128,128,128);">src</span><span style="color: rgb(128,128,128);">直接换成对应的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">地址即可</span><span style="color: rgb(128,128,128);">--</span><span style="color: rgb(128,128,128);">></span></em>
        
![](img/test.heic)

    </div>
    <div>
        <p>SVG图片</p>
     <em>   <span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">!--</span><span style="color: rgb(128,128,128);">网络图片</span><span style="color: rgb(128,128,128);">src</span><span style="color: rgb(128,128,128);">直接换成对应的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">地址即可</span><span style="color: rgb(128,128,128);">--</span><span style="color: rgb(128,128,128);">></span></em>
        
![](img/test.svg)

    </div>
</div>
<script>
</script>
</body>
</html>
```
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">HEIFDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">Context</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'heif.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- SVGA动画不支持在HTML里直接通过img标签展示，可以通过使用SVGA-Web播放器([SVGAPlayer-Web](https://github.com/svga/SVGAPlayer-Web))在Web组件中加载SVGA动画，具体步骤如下：1. 在resources目录下新建一个resfile目录，并把HTML文件放到resfile目录下，图片资源文件放到resfile/img目录下，js文件放到resfile/js目录下。

2. 引入播放器库：在HTML的head标签中，引入SVGA播放器库。

  
```text
<script src="js/svga.min.js"></script>
```


3. 准备动画容器：在页面中创建一个div元素作为SVGA动画的舞台。

  
```text
<div id="svgaContainer"></div>
```


4. 加载并播放动画：编写JavaScript代码，初始化播放器并加载远程或本地的.svga文件。

  
```text
<span style="color: rgb(0,0,255);">document</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addEventListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'DOMContentLoaded'</span><span style="color: rgb(181,106,1);">, </span>function <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <em><span style="color: rgb(128,128,128);">// 1. </span><span style="color: rgb(128,128,128);">初始化播放器，绑定到容器</span></em>
  let <span style="color: rgb(0,0,255);">player </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SVGA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Player</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#svgaContainer'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// 2. </span><span style="color: rgb(128,128,128);">初始化解析器</span></em>
  let <span style="color: rgb(0,0,255);">parser </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SVGA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Parser</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <em><span style="color: rgb(128,128,128);">// 3. </span><span style="color: rgb(128,128,128);">加载并解析</span><span style="color: rgb(128,128,128);">SVGA</span><span style="color: rgb(128,128,128);">文件，此处</span><span style="color: rgb(128,128,128);">load</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">url</span><span style="color: rgb(128,128,128);">使用的是本地文件的地址，也可以使用在线的</span><span style="color: rgb(128,128,128);">svga</span><span style="color: rgb(128,128,128);">文件，例如：</span><span style="color: rgb(128,128,128);">xxx.com/xxx.svga</span></em>
  <span style="color: rgb(0,0,255);">parser</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">load</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"file:///data/storage/el1/bundle/entry/resources/resfile/img/test.svga"</span><span style="color: rgb(181,106,1);">,</span>
    function <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">videoItem</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// 4. </span><span style="color: rgb(128,128,128);">将解析好的视频项设置给播放器</span></em>
      <span style="color: rgb(0,0,255);">player</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setVideoItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">videoItem</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
     <em> <span style="color: rgb(128,128,128);">// 5. </span><span style="color: rgb(128,128,128);">开始播放动画</span></em>
      <span style="color: rgb(0,0,255);">player</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAnimation</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span>function <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'SVGA</span><span style="color: rgb(255,0,170);">文件加载失败</span><span style="color: rgb(255,0,170);">:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```


  完整的样例代码如下：

  
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SVGADemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">Context</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onControllerAttached</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setPathAllowingUniversalAccess</span><span style="color: rgb(0,0,255);">([</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">resourceDir</span>
            <span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'file://' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">resourceDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/svga.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
```text
<!DOCTYPE html>
<html>
<head>
    <title>加载SVGA</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .img-container {
            padding: 20px;
            margin: 10px;
        }
        .flex-center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #svgaContainer {
            width: 300px;
        }
    </style>
    <script src="js/svga.min.js"></script>
</head>
<body>
<div class="img-container flex-center">
    <div id="svgaContainer"></div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', function () {
       <em> // 1. 初始化播放器，绑定到容器</em>
        let player = new SVGA.Player('#svgaContainer');
       <em> // 2. 初始化解析器</em>
        let parser = new SVGA.Parser();
       <em> // 3. 加载并解析SVGA文件，此处load的url使用的是本地文件的地址，也可以使用在线的svga文件，例如：xxx.com/xxx.svga</em>
        parser.load("file:///data/storage/el1/bundle/entry/resources/resfile/img/test.svga",
            function (videoItem) {
              <em>  // 4. 将解析好的视频项设置给播放器</em>
                player.setVideoItem(videoItem);
             <em>   // 5. 开始播放动画</em>
                player.startAnimation();
            }, function (error) {
                console.error('SVGA文件加载失败:', error);
            });
    });
</script>
</body>
</html>
```
