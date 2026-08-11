# Wi-Fi始终连接，如何感知Wi-Fi本身从无网络到有网络的状态

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-97

#### 问题现象

手机连接到未认证的Wi-Fi，认证后无法感知到认证成功，即网络连接成功。
 
 

#### 背景知识

- 设备从无网络到有网络会触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件。
- 设备从有网络到无网络状态会触发netLost事件。
- 设备从Wi-Fi到蜂窝会触发netLost事件（Wi-Fi丢失）之后触发netAvailable事件（蜂窝可用）。

 
 

#### 解决方案

- 实测该场景不会发送[netAvailable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetavailable)或[netLost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetlost)事件。
- 需要监听[netCapabilitiesChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetcapabilitieschange)事件，判断connection.NetCapabilityInfo中的[NetCap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netcap)类型。若包含NET_CAPABILITY_PORTAL=17（还没有认证时会返回），则表示还没有进行认证，当前网络不可用。

 
先在module.json5文件中配置网络权限[ohos.permission.INTERNET](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissioninternet)和允许应用获取数据网络信息[ohos.permission.GET_NETWORK_INFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionget_network_info)。
 
完整示例参考如下：
 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">connection </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(255,255,255);">netCon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NetConnection </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createNetConnection</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Connection </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">先使用</span><span style="color: rgb(128,128,128);">register</span><span style="color: rgb(128,128,128);">接口注册订阅事件</span></em>
    <span style="color: rgb(255,255,255);">netCon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">register</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始检测网络状态</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅网络丢失事件</span></em>
          <span style="color: rgb(255,255,255);">netCon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'netLost'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NetHandle</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">网络丢失</span><span style="color: rgb(132,63,161);">: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">netId</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅网络能力变化事件</span></em>
          <span style="color: rgb(255,255,255);">netCon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'netCapabilitiesChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NetCapabilityInfo</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">订阅网络能力变化</span><span style="color: rgb(132,63,161);">: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">netCap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">bearerTypes</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅网络可用事件</span></em>
          <span style="color: rgb(255,255,255);">netCon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'netAvailable'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NetHandle</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">网络可用</span><span style="color: rgb(132,63,161);">: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">netId</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：开发预下载的功能，需要判断当前app的网络请求为闲时进行下载，是否有相关API可以进行判断？
 
A：可以使用connection模块的[on('netBlockStatusChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetblockstatuschange)监听事件判断当前网络的阻塞状态。
