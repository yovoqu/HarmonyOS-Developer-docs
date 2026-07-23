# http请求通过MultiFormData分片上传报错

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-85

#### 问题现象

通过http.MultiFormData[]上传失败，错误信息：
 
```text
{<span style="color: rgb(132,63,161);">"timestamp"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">1747124996117</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"status"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">400</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"error"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">"Bad Request"</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"exception"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">"org.springframework.web.multipart.support.MissingServletRequestPartException"</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"message"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">"Required request part 'chunk' is not present"</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"path"</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">"/upload/clip"</span>}
```
 
 

#### 背景知识

httpRequest实现分片上传需要服务器那边配合定义好协议传参，在[MultiFormData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#multiformdata11)里添加相关参数。
 
 

#### 问题定位

这是传参错误导致,错误示例如下:
 
```text
<span style="color: rgb(0,0,255);">uploadFile1</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">httpRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MultiFormData</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">formData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MultiFormData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx.mp4'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">contentType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'video/mp4'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">remoteFileName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx.mp4'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(132,63,161);">'vid'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">'fseq'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">'cmd5'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">'chunk'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">''</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">formData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(255,0,170);">(</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uploadUrl</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">method</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RequestMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">POST</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">header</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(132,63,161);">'Content-Type'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'multipart/form-data'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'APPID'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'TOKEN'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">'VERSION'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">multiFormDataList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HttpResponse</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to uploadFile. Code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Succeeded to uploadFile:  </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
应把data数据放到requestMultipart中。
 
 

#### 分析结论

数据结构不对导致服务器无法捕获引起错误，修改传参可解决处理。
 
 

#### 修改建议

通过对象requestMultipart上传时需要把data数据拎出来单独push到requestMultipart对象里面才能收到。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">http </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">uploadUrl</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'http://127.0.0.1:9588/'</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">替换为实际服务器</span><span style="color: rgb(128,128,128);">URL</span><span style="color: rgb(128,128,128);">。</span></em>



  <span style="color: rgb(0,0,255);">uploadFile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">httpRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MultiFormData</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">formData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MultiFormData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'share.txt'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">数据名称。</span></em>
      <span style="color: rgb(255,255,255);">contentType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'text/plain'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">数据类型，自</span><span style="color: rgb(128,128,128);">API 11</span><span style="color: rgb(128,128,128);">开始支持该属性。</span></em>
      <span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><em>//</em><em><span style="color: rgb(128,128,128);">替换为实际文件路径。</span></em>
      <span style="color: rgb(255,255,255);">remoteFileName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'share.txt'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">上传到服务器保存为文件的名称。</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">formData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,255,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(255,0,170);">(</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uploadUrl</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">method</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RequestMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">POST</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">header</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(132,63,161);">'Content-Type'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'multipart/form-data'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">multiFormDataList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">requestMultipart</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HttpResponse</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to uploadFile. Code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Succeeded to uploadFile:  </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MultiFormData</span><span style="color: rgb(132,63,161);">分片上传</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        let <span style="color: rgb(255,255,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        let <span style="color: rgb(255,255,255);">filePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filesDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'/' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'share.txt'</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">文件沙箱路径，使用时替换实际文件路径。</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uploadFile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filePath</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：使用requestInStream设置multiFormDataList上传文件，当remoteFileName的名字过长时会提示500，换成其他短文件名则不会出现问题。
 
A：使用multiFormDataList设置remoteFileName时，当文件名包含中文、空格、特殊符号或长度超过255字符，可能触发服务器端异常，需通过URL编码处理。
 
Q：multiFormDataList上传文件的filePath字段能使用fd吗？
 
A：filePath中需要传入一个文件路径，而fd://int的语法是以fd标识一个媒体资源，非文件路径。
