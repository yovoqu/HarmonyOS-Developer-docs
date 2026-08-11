# 如何实现TcpSocket断开重连

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-125

#### 问题现象

TcpSocket异常断开连接后，如何实现循环重连？
 
 

#### 背景知识

建立TcpSocket连接前，需要通过[constructTCPSocketInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#socketconstructtcpsocketinstance)创建tcp实例，然后才能调用[connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#connect)接口连接指定tcp服务。若是TcpSocket异常断开，需调用[close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#close-2)接口销毁之前的实例，然后重新创建TcpSocket实例，调用connect接口尝试重连。
 
 

#### 解决方案

TcpSocket不具备自动回连机制，开发者需要通过业务逻辑实现循环重连，具体实现可参考如下代码：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">socket </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TcpSocketReconnect </span><span style="color: rgb(255,0,170);">{</span>
  <em><span style="color: rgb(128,128,128);">// 1.tcpSocket</span><span style="color: rgb(128,128,128);">实例</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TCPSocket </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// 2.</span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">socket</span><span style="color: rgb(128,128,128);">实例</span></em>
  <span style="color: rgb(0,0,255);">createSocket</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constructTCPSocketInstance</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerEvents</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// 3.</span><span style="color: rgb(128,128,128);">注册事件监听</span></em>
  <span style="color: rgb(0,0,255);">registerEvents</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'close'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Connection closed'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>// </em><em><span style="color: rgb(128,128,128);">获取当前</span><span style="color: rgb(128,128,128);">tcpSocket</span><span style="color: rgb(128,128,128);">连接状态</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getState</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SocketStateBase</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'getState fail'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'getState success:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果</span><span style="color: rgb(128,128,128);">tcpSocket</span><span style="color: rgb(128,128,128);">未关闭连接，释放旧连接，然后开始重连</span></em>
<em>        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果</span><span style="color: rgb(128,128,128);">tcpSocket</span><span style="color: rgb(128,128,128);">已关闭连接，说明用户需要主动断开，无需重连</span></em>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isConnected</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">close</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Close error:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          <em>// </em><em><span style="color: rgb(128,128,128);">触发重连。注：此处应根据开发者业务所需，判断是否需要触发重连</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reconnect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'error'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Error occurred:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reconnect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">错误时触发重连</span></em>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// 4.</span><span style="color: rgb(128,128,128);">实现重连逻辑</span></em>
  <span style="color: rgb(0,0,255);">reconnect</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Reconnecting...'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建新连接</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSocket</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connectToServer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">// 5.</span><span style="color: rgb(128,128,128);">建立连接</span></em>
  <span style="color: rgb(0,0,255);">connectToServer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NetAddress </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'36.137.xxx.xxx'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8080</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5000 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Connect failed:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Connect success'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">初始化实例</span><span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">创建回连机制</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>// </em><em><span style="color: rgb(128,128,128);">初始化实例</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">创建回连机制</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSocket</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">建立连接</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">建立连接</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connectToServer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
