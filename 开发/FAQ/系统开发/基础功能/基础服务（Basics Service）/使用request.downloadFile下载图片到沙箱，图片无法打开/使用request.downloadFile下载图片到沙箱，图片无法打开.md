# 使用request.downloadFile下载图片到沙箱，图片无法打开

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-65

#### 问题现象

使用request.downloadFile方法下载网络图片到沙箱，图片不能直接打开查看：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/sjnxaz-aSGOjkCJ2Qs9EZw/zh-cn_image_0000002628613956.png?HW-CC-KV=V1&HW-CC-Date=20260730T072604Z&HW-CC-Expire=86400&HW-CC-Sign=FB70593EA4066EFF5748361A2DF0A5D43BB9C260C65235BBEF74E0A0C098C094)

 
关键代码如下：
 
```text
<span style="color: rgb(0,0,255);">request</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">downloadFile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'http://www.example/fdb17952b79f46b3a20b9fc1d239177b_20250724145715AecsMOQ031.png'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">示例网址</span></em>
 <em> <span style="color: rgb(128,128,128);">// url:'https://copyright.bdstatic.com/vcg/creative/cc9c744cf9f7c864889c563cbdeddce6.jpg',</span></em>
  <span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">filesDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/test.png'</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
问题原因是什么，该如何解决？
 
 

#### 背景知识

- [request.downloadFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestdownloadfile9)：创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。
- [http.createHttp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#httpcreatehttp)：创建一个HTTP请求，里面包括发起请求、中断请求、订阅/取消订阅HTTP Response Header事件。
- [request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#request)：根据url地址，发起HTTP网络请求，使用callback方式作为异步方法。

 
 

#### 问题定位
1. 直接打开问题图片的链接是可以看到图片的；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jw-811-yTna-aErgIHglNA/zh-cn_image_0000002658973159.png?HW-CC-KV=V1&HW-CC-Date=20260730T072604Z&HW-CC-Expire=86400&HW-CC-Sign=792CD6A7FDC2CB5C9E446F2900935F48FA68537A075C0F75E55BE63760665D5A)


  使用request.downloadFile方法下载该图片到沙箱，然后导出到PC，再拖拽到浏览器，图片也不能查看了；

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/9NQn35w-TmC59ddnom9-RQ/zh-cn_image_0000002658853205.png?HW-CC-KV=V1&HW-CC-Date=20260730T072604Z&HW-CC-Expire=86400&HW-CC-Sign=F569441B5F5042EBB1F333634EC0C28D51665FCCB036ABB58E95C790B8020BA3)

2. 查看图片的二进制码，发现第二张图片和第一张图片的文件头有差异，多了以下高亮区域里的数据：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/aRyfjlmdT9CDbx0fAjVZKQ/zh-cn_image_0000002628773846.png?HW-CC-KV=V1&HW-CC-Date=20260730T072604Z&HW-CC-Expire=86400&HW-CC-Sign=6326A4A9741D37152E5AB3666E2A71ADD6D70707CAFAE7813F67472BD46646BA)

3. 读取前几个字节为1F 8B 08，其中1F 8B表明为gzip压缩，而08表示为deflate压缩。下载的是未解码的文件，所以图片无法显示。
 
 

#### 分析结论
1. request.downloadFile方法下载的是未解码的文件，所以图片无法显示。
2. 尝试使用http.createHttp().request(url: string, callback: AsyncCallback&lt;HttpResponse&gt;)方法请求图片资源，发现Image组件能够显示，所以考虑使用这种方式获取图片数据。
 
 

#### 修改建议

使用http.createHttp().request(url: string, callback: AsyncCallback)方法请求图片数据，然后把接收的数据写入沙箱，示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">http </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">fs </span>from <span style="color: rgb(255,0,170);">'@ohos.file.fs'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">下载图片</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPicture</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">http</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">request</span><span style="color: rgb(128,128,128);">方法从网络下载图片资源</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  async <span style="color: rgb(0,0,255);">getPicture</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处地址实际使用过程中替换为真实地址</span></em>
    <span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'xx.xx.xx'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpResponse</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">下载失败时弹窗提示检查网络，不执行后续逻辑</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请求失败</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`error.code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, error.message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>

      let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取沙箱路径（如：</span><span style="color: rgb(128,128,128);">filesDir</span><span style="color: rgb(128,128,128);">）</span></em>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">filePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filesDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/test.png'</span><span style="color: rgb(181,106,1);">;</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建文件并写入数据</span></em>
        let <span style="color: rgb(0,0,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CREATE </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_WRITE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        try <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">result </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>finally <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
