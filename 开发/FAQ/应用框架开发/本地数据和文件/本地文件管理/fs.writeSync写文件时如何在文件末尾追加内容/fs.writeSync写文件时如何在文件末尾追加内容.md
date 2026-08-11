# fs.writeSync写文件时如何在文件末尾追加内容

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-64

#### 问题现象

如何使用fs.writeSync实现在文件末尾追加内容？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/QVAQBVHZSim9Tov_Q3-jnA/zh-cn_image_0000002629059024.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005849Z&HW-CC-Expire=86400&HW-CC-Sign=6AFAE63C7A0FA788AB30E593D5F04B228A68FF92C4ECC91D4B909E49115CD728)

 
 

#### 解决方案

[fs.writeSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fswritesync)写文件时需要先使用[fs.openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)打开文件，打开文件时可设置模式为“OpenMode.APPEND”，以追加方式打开。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">systemDateTime </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">fileIo </span>as <span style="color: rgb(255,255,255);">fs </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">当前</span><span style="color: rgb(132,63,161);">test.txt</span><span style="color: rgb(132,63,161);">为文件的内容是：</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">展示文件内容</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">追加文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          let <span style="color: rgb(255,255,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">Context</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">filePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cacheDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'/test.txt'</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取文件路径</span></em>
          let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">=</span>
            <span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_WRITE </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">APPEND </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CREATE</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置以追加方式打开文件</span></em>
          let <span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">systemDateTime</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTime</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">','</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取当前时间作为写入文件的内容</span></em>
          let <span style="color: rgb(255,255,255);">writeLen </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">向文件内写入内容，返回值为写入内容的长度</span></em>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`writeLen</span><span style="color: rgb(132,63,161);">：</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">writeLen</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭文件</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readTextSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">读取文件内容</span></em>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
