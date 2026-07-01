# http请求requestInStream接口如何使用

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-81

#### 问题现象

http请求requestInStream接口如何获取响应数据？
 
 

#### 背景知识

[requestInStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#requestinstream10)可以根据URL地址，发起http网络请求并返回流式响应。
 
 

#### 解决方案

使用[requestInStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#requestinstream10)接口需要注意，callback回调返回的是number类型的数据，也就是响应码，不会返回具体的数据，可通过[on("dataReceive")](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#ondatareceive10)接收响应数据，当订阅成功时，error为undefined，data为接收到的http流式数据，类型为ArrayBuffer；否则为错误对象。
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">http </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Header </span><span style="color: rgb(255,0,170);">{</span>
  public <span style="color: rgb(0,0,255);">contentType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">contentType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentType </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">contentType</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">createAndRequest</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">httpRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpRequestOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">method</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">RequestMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">POST</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认为</span><span style="color: rgb(128,128,128);">http.RequestMethod.GET</span><span style="color: rgb(128,128,128);">。</span></em>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当使用</span><span style="color: rgb(128,128,128);">POST</span><span style="color: rgb(128,128,128);">请求时此字段用于传递请求体内容，具体格式与服务端协商确定。</span></em>
    <span style="color: rgb(0,0,255);">extraData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'data to send'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">expectDataType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpDataType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STRING</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，指定返回数据的类型。</span></em>
    <span style="color: rgb(0,0,255);">usingCache</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认为</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">。</span></em>
    <span style="color: rgb(0,0,255);">priority</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认为</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">。</span></em>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者根据自身业务需要添加</span><span style="color: rgb(128,128,128);">header</span><span style="color: rgb(128,128,128);">字段。</span></em>
    <span style="color: rgb(0,0,255);">header</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Header</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'application/json'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">readTimeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">60000</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认为</span><span style="color: rgb(128,128,128);">60000ms</span><span style="color: rgb(128,128,128);">。</span></em>
    <span style="color: rgb(0,0,255);">connectTimeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">60000</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认为</span><span style="color: rgb(128,128,128);">60000ms</span><span style="color: rgb(128,128,128);">。</span></em>
    <span style="color: rgb(0,0,255);">usingProtocol</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HttpProtocol</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HTTP1_1</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，协议类型默认值由系统自动指定。</span></em>
    <span style="color: rgb(0,0,255);">usingProxy</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选，默认不使用网络代理，自</span><span style="color: rgb(128,128,128);">API 10</span><span style="color: rgb(128,128,128);">开始支持该属性。</span></em>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestInStream</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'EXAMPLE_URL'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestInStream OK! ResponseCode is ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestInStream ERROR : err = ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'dataReceive'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'dataReceive length: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'dataEnd'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Receive dataEnd !'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'click'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'HelloWorld'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">createAndRequest</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 
当所有数据接收完毕后，on('dataEnd', () => {})方法会被调用，标志着数据接收完成。在使用完http请求对象后，调用destroy()方法来主动销毁这个对象，避免资源泄露。
 
 

#### 总结

requestInStream接口是用于处理http请求返回的流式数据的方法。在HarmonyOS中，当http请求的响应数据量较大时，比如超过5M、100M，使用requestInStream可以有效地处理这些数据，避免内存溢出等问题。
 
 

#### 常见FAQ

Q：http发起的requestInStream流式请求，dataReceiveProgress无回调。
 
A：服务端需返回Content-Length字段，不然没有数据长度，dataReceiveProgress也就不会被触发。
