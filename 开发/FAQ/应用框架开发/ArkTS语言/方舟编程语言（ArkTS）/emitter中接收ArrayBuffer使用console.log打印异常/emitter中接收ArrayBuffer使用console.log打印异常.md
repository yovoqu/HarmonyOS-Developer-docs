# emitter中接收ArrayBuffer使用console.log打印异常

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-161

#### 问题现象

emitter中接收传过来的ArrayBuffer，使用console.log方式打印ArrayBuffer，结果是{}。
 
 

#### 背景知识

- [emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter)：提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。
- [Base64Helper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#base64helper9)：Base64Helper类提供Base64编解码和Base64URL编解码功能。
- [TextDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textdecoder)：TextDecoder用于将字节数组解码为字符串，支持utf-8、utf-16le/be、iso-8859和windows-1251等不同的编码格式。

 
 

#### 问题定位

使用debug调试发现，ArrayBuffer数据正常发送，且正常接收到，使用console.log(${JSON.stringify(arrayBuffer)})二进制流时，显示异常。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ntUbGTUtTUKiDF4vd4IVyg/zh-cn_image_0000002628899070.png?HW-CC-KV=V1&HW-CC-Date=20260723T012431Z&HW-CC-Expire=86400&HW-CC-Sign=BE046AFF997B72BBEFE5B3A0DD2873D7942D0B0BA25291D7AAAA0E04B7CC2301)

 
 

#### 分析结论

ArrayBuffer是原始字节流格式的数据，JSON.stringify会调用ArrayBuffer对象的toJSON()方法，默认没有实现这个方法，所以打印结果为空对象{}。
 
 

#### 修改建议

由以上分析结论可知，要打印ArrayBuffer需要解码成对应格式才能打印：
 
可以使用[TextDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textdecoder)工具类将ArrayBuffer解码成字符串之后打印。
 
示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">emitter </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">EmitterParam </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">arrayBuffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello ArrayBuffer!'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InnerEvent </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">eventId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义回调方法</span></em>
  private <span style="color: rgb(0,0,255);">callback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EventData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">arrayBuffer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">eventData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'buffer'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">textDecoder </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextDecoder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">textDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeToString</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">arrayBuffer</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">收到数据：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用分段打印到控制台</span></em>
    <span style="color: rgb(0,0,255);">printInChunks</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">bufView </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">strLen </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">strLen</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">bufView</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charCodeAt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bufView</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开启监听</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">发送数据</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EventData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arrayBuffer</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">emitter</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">emit</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">eventData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>


<em>/*</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">分段打印日志</span></em>
<em><span style="color: rgb(128,128,128);"> * */</span></em>
function <span style="color: rgb(0,0,255);">printInChunks</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">chunkSize </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">chunkSize</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">chunkSize</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：为什么打印较长字符串hilog会截断？
 
A：console.log打印日志单次打印有长度限制，超出会被截断，可以使用分段打印。
