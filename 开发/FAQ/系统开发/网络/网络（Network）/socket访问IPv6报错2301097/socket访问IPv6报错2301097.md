# socket访问IPv6报错2301097

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-92

#### 问题现象

socket访问IPv6失败，会报错：{"code":2301097,"message":"Address family not supported by protocol"}。
 
 

#### 背景知识

socket模块支持通过[bind](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#bind-2)接口显式绑定IPv6地址和端口。
 
 

#### 问题定位

排查目标地址信息[NetAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#netaddress)中参数配置是否有误。
 
 

#### 分析结论

根据报错信息Address family not supported by protocol和代码示例可知，问题出在地址信息配置上面。由于NetAddress中family参数默认为IPv4，如果不重新配置family参数，使用的将会是IPv4网络。
 
 

#### 修改建议

将NetAddress中family参数设置为2，用以支持访问IPv6网络。
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">socket </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TlsSocketBind </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// tlsSocket</span><span style="color: rgb(128,128,128);">实例</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">tls</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TLSSocket </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constructTLSSocketInstance</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">绑定</span><span style="color: rgb(128,128,128);">tls</span></em>
  <span style="color: rgb(0,0,255);">bind</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">网络协议类型，可选类型：</span></em>
<em>    <span style="color: rgb(128,128,128);">// - 1</span><span style="color: rgb(128,128,128);">：</span><span style="color: rgb(128,128,128);">IPv4</span><span style="color: rgb(128,128,128);">。默认为</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">。</span></em>
<em>    <span style="color: rgb(128,128,128);">// - 2</span><span style="color: rgb(128,128,128);">：</span><span style="color: rgb(128,128,128);">IPv6</span><span style="color: rgb(128,128,128);">。地址为</span><span style="color: rgb(128,128,128);">IPV6</span><span style="color: rgb(128,128,128);">类型，该字段必须被显式指定为</span><span style="color: rgb(128,128,128);">2</span><span style="color: rgb(128,128,128);">。</span></em>
<em>    <span style="color: rgb(128,128,128);">// - 3</span><span style="color: rgb(128,128,128);">：</span><span style="color: rgb(128,128,128);">Domain</span><span style="color: rgb(128,128,128);">。地址为</span><span style="color: rgb(128,128,128);">Domain</span><span style="color: rgb(128,128,128);">类型，该字段必须被显式指定为</span><span style="color: rgb(128,128,128);">3</span><span style="color: rgb(128,128,128);">。</span></em>
    let <span style="color: rgb(0,0,255);">bindAddr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NetAddress </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'::1'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// address</span><span style="color: rgb(128,128,128);">需要根据实际地址进行填写</span></em>
      <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8080</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">family</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tls</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bind</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">bindAddr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">绑定失败</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">绑定成功</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">开始绑定</span><span style="color: rgb(255,0,170);">tls'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开始绑定</span><span style="color: rgb(128,128,128);">tls</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bind</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
