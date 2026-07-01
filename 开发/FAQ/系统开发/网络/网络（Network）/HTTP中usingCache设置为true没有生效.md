# HTTP中usingCache设置为true没有生效

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-121

#### 问题现象

使用http请求，设置usingCache：true同时调用flush方法，但是还是获取不到缓存。
 
问题代码示例参考如下：
 
```json
let <span style="color: rgb(255,255,255);">option</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HttpRequestOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">usingCache</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">header</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(132,63,161);">'Cache-Control'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'max-age=315360000'</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
let <span style="color: rgb(255,255,255);">httpRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttp</span><span style="color: rgb(255,0,170);">()</span>
let <span style="color: rgb(255,255,255);">httpResponseCache </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createHttpResponseCache</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,255,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'https://xxxxxx'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">option</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">res</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">http</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HttpResponse</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">httpResponseCache</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flush</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'HttpCache flush fail'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      const <span style="color: rgb(255,255,255);">newsResponse </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">res</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">()) </span>as <span style="color: rgb(181,106,1);">NewsResponse</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">newsList </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">newsResponse</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span>
<span style="color: rgb(255,255,255);">      console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'HttpCache flush success'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`HttpCache error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当该请求使用完毕时，开发者务必调用</span><span style="color: rgb(128,128,128);">destroy</span><span style="color: rgb(128,128,128);">方法主动销毁该</span><span style="color: rgb(128,128,128);">JavaScript Object</span><span style="color: rgb(128,128,128);">。</span></em>
    <span style="color: rgb(255,255,255);">httpRequest</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
```
 
 

#### 背景知识

- [flush](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#flush9)：将缓存中的数据写入文件系统，以便在下一个http请求中访问所有缓存数据，使用callback方式作为异步方法。缓存数据包括：响应头(header)、响应体(result)、cookies、请求时间(requestTime)和响应时间(responseTime)。
- Cache-Control：用于指定缓存策略，如no-cache, no-store, max-age, public, private等。

 
 

#### 问题定位

检查服务端是否设置了Cache-Control字段。
 
 

#### 分析结论

Cache-Control为通用报头，通常是在服务器端设置的，如果在HttpRequestOptions中header里设置'Cache-Control': 'max-age=xxxx'，缓存不会生效。
 
 

#### 修改建议

在服务器端中设置http请求头为Cache-Control：max-age=xxxx即可。
 
 

#### 常见FAQ

Q：IP地址响应头也设置的Cache-Control：max-age=60，但依然还是缓存失败，这是为什么？
 
A：可能因为之前其他缓存影响，导致此IP地址缓存失败，重新清空浏览器缓存或者重新卸载安装APP。
