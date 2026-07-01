# rawfile目录下文件夹如何复制到沙箱目录并读写

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-55

#### 问题现象

如何实现rawfile目录下文件夹复制到沙箱目录，并支持读写功能？
 
 

#### 背景知识

应用资源文件目录分为在base目录、限定词目录、rawfile目录、resfile目录。而rawfile目录、resfile目录通常存放其他类型文件（例如txt文件、db文件等等），原始文件形式保存。rawfile目录和resfile目录同在[资源目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#资源目录)下，目录中的资源文件会被直接打包进应用，不经过编译，也不会分配资源ID。二者的主要不同之处在于访问方式：
 
- resfile目录：应用安装后，resfile资源会被解压到应用沙箱路径，通过Context属性resourceDir获取到resfile资源目录后，可通过文件路径以只读权限访问。
- rawfile目录：通过文件路径和文件名进行访问（"\$rawfile('filename')"）；或者通过Context获取[resourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)后，调用资源管理接口访问。

 
应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“[沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)”。通常rawfile/resfile目录下文件/文件夹无法直接在应用中读写，需要复制到应用沙箱下才可以读写。
 
 

#### 解决方案

假设rawfile目录下存在apps文件夹（路径：rawfile/apps），需将其复制到沙箱目录。由于rawfile目录下的文件夹无法跟随应用安装解压到沙箱目录，若需要将整个文件夹拷贝到沙箱目录，需要进行递归遍历文件夹等操作，不推荐。因此目前有以下两种推荐方案：
 
- **方案一：rawfile目录下的文件夹直接复制到resfile目录下（resfile/apps），然后再复制到沙箱。**由于resfile下文件夹随应用安装解压到应用沙箱目录，但是仅能以只读方式访问，所以也需要将其文件复制到沙箱目录下进行读写。1. 通过context.resourceDir获取resfile目录，context.filesDir获取沙箱目录。

2. 使用[fs.copyDirSync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fscopydirsync10)把resfile/apps直接复制到沙箱目录。
- **方案二：把需要复制的目录压缩成zip，复制zip并解压到沙箱目录。**1. 通过[getRawFd()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getrawfd9)获取rawfile/apps.zip所在hap包的descriptor信息（示例代码中的参数data）。

2. 使用buffer将rawfile/apps.zip文件内容复制到沙箱临时文件路径（示例代码中的参数filepath）。

3. 使用[zlib.decompressFile()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib#zlibdecompressfile9)解压zip文件至沙箱通用文件路径（示例代码中的参数sandboxPath）。

 
完整示例参考如下：
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fileIo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">zlib </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import type <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import type <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RawfileToSandbox </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <em>// </em><em><span style="color: rgb(128,128,128);">方案一：</span><span style="color: rgb(128,128,128);">rawfile</span><span style="color: rgb(128,128,128);">目录下的文件夹直接复制到</span><span style="color: rgb(128,128,128);">resfile</span><span style="color: rgb(128,128,128);">目录下（</span><span style="color: rgb(128,128,128);">resfile/apps</span><span style="color: rgb(128,128,128);">），然后再复制到沙箱。</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">复制</span><span style="color: rgb(255,0,170);">resFile</span><span style="color: rgb(255,0,170);">目录下文件夹到沙箱目录</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">srcPath </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/apps/'</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">destPath </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filesDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/apps/'</span><span style="color: rgb(181,106,1);">;</span>
            <em>// </em><em><span style="color: rgb(128,128,128);">判断文件夹是否存在</span></em>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">accessSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">destPath</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mkdirSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">destPath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">copyDirSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">srcPath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">destPath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`copy directory failed with error message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">方案二：把需要复制的目录压缩成</span><span style="color: rgb(128,128,128);">zip</span><span style="color: rgb(128,128,128);">，复制</span><span style="color: rgb(128,128,128);">zip</span><span style="color: rgb(128,128,128);">并解压到沙箱目录。</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">复制</span><span style="color: rgb(255,0,170);">zip</span><span style="color: rgb(255,0,170);">到沙箱，并解压</span><span style="color: rgb(255,0,170);">zip'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
 <em>         <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">fd</span><span style="color: rgb(128,128,128);">来进行拷贝，避免文件过大的内存占用问题</span></em>
<em>          <span style="color: rgb(128,128,128);">// data.fd</span><span style="color: rgb(128,128,128);">是</span><span style="color: rgb(128,128,128);">hap</span><span style="color: rgb(128,128,128);">包的</span><span style="color: rgb(128,128,128);">fd</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">data.offset</span><span style="color: rgb(128,128,128);">表示目标文件在</span><span style="color: rgb(128,128,128);">hap</span><span style="color: rgb(128,128,128);">包中的偏移，</span><span style="color: rgb(128,128,128);">data.length</span><span style="color: rgb(128,128,128);">表示目标文件的长度</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'apps.zip'</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            try <span style="color: rgb(255,0,170);">{</span>
              let <span style="color: rgb(0,0,255);">sandboxPath </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filesDir</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">沙箱路径：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">sandboxPath</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">filePath </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/bfapps.zip'</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">压缩文件路径：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">dest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CREATE </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_WRITE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">bufsize </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">4096</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">buf </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">bufsize</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">off </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">readLen </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

<em>              <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">把</span><span style="color: rgb(128,128,128);">rawfile</span><span style="color: rgb(128,128,128);">压缩包文件内容复制到沙箱路径</span></em>
              let <span style="color: rgb(0,0,255);">len </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">bufsize </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              while <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">len </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(0,0,255);">readLen </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(181,106,1);">;</span>
                if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">readLen </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  break<span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
                <span style="color: rgb(0,0,255);">off </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(181,106,1);">;</span>
                if <span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">readLen</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">bufsize</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">bufsize </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">readLen</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
                <span style="color: rgb(0,0,255);">len </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">bufsize </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">对沙箱路径下的压缩文件进行解压</span></em>
              await <span style="color: rgb(0,0,255);">zlib</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decompressFile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sandboxPath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeRawFd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'apps.zip'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed, error = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 
 

#### 常见FAQ

Q：zlib.decompressFile()的参数inFile和outFile可以取到项目内的路径吗？
 
A：inFile和outFile文件路径必须为沙箱路径。
 
Q：为什么context.getApplicationContext().resourceDir返回值是空字符串？
 
A：通过ApplicationContext获取的是应用级别的应用文件路径，这其中不包括resourceDir，详情参考[获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)。
 
 

#### 总结
 
|    | 方案一 | 方案二 |
| --- | --- | --- |
| 关键接口 | fs.mkdirSync、 fs.copyDirSync | resourceManager.getRawFd、 fs.openSync、fs.readSync、fs.writeSync、zlib.decompressFile |
| 使用场景 | 适用于文件夹下嵌套层级少，子目录、子文件小的情况，因为copyDirSync直接拷贝文件夹会造成应用开销大，占用运行内存 | 适用于文件夹下嵌套层级多，子目录、子文件大的情况，该方案利用了压缩、解压，buffer循环读取可以减少应用开销、占用内存较少 |
 
 
综上所述，需要读写rawfile文件夹需要先复制到应用沙箱，两种方案需要根据开发者具体场景进行选择。
