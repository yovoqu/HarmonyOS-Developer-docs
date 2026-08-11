# socket.sppReadAsync循环读取异常

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-33

#### 问题现象

蓝牙spp连接成功后，调用socket.sppReadAsync，循环读取设备数据，只会成功读取一次，而后出现异常。问题代码如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">socket </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">clientNumber </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">入参</span><span style="color: rgb(128,128,128);">clientNumber</span><span style="color: rgb(128,128,128);">由</span><span style="color: rgb(128,128,128);">sppAccept</span><span style="color: rgb(128,128,128);">或</span><span style="color: rgb(128,128,128);">sppConnect</span><span style="color: rgb(128,128,128);">接口获取。</span>
let <span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1024</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">flag </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
while <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">flag</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  try <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sppReadAsync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">clientNumber</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">outBuffer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">outBuffer</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`sppRead success, data = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'sppRead error, data is null'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">flag </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`startSppRead errCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, errMessage: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

- [socket.sppReadAsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppreadasync18)通过socket读取对端所发送数据的异步接口，该接口支持断开连接时spp操作异常错误返回。
- 异步函数同时访问同一个变量时，执行顺序不可预测，数据竞争不一致导致访问冲突；
- [errorManager.on('unhandledRejection')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager#errormanageronunhandledrejection12)注册被拒绝promise监听器。注册后可以捕获到当前线程中未被捕获到的promise rejection。

 
 

#### 问题定位

返回错误码401表示参数错误，删除while循环，就不会报错401，由此可得是多次调用导致的入参错误问题。socket.sppReadAsync是异步函数，在未等待执行结果后同时调用异步函数，并将同一个变量作为入参，导致数据资源存在竞争，导致入参异常。
 
 

#### 分析结论

在执行异步函数时，应避免同时使用同一变量作为入参，否则可能存在资源访问异常情况，应该在异步函数执行完成后使用同一变量。
 
 

#### 修改建议

socket.sppReadAsync该接口为异步接口，需要等异步回调结果返回后才能进行下一次调用。具体代码参考官方接口[socket.sppReadAsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppreadasync18)示例代码。
 
 

#### 常见FAQ

Q：在经典蓝牙中，应用该如何感知蓝牙是否已经断连？
 
A：调用sppReadAsync方法来监听spp蓝牙是否断开连接，如果spp蓝牙断开的话，接口会返回2901054错误。
 
 

#### 总结

在异步函数调用中，应该充分考虑入参是否存在资源竞争关系，是否存在明显的执行逻辑顺序。
