# ArkTS通过TCP检测多域名连通性并自动选择备用地址

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-102

#### 问题现象

在HarmonyOS应用中，App启动阶段需要判断网络是否可用。当前网络连接逻辑要求如下：
 
- 首先检测主地址https://app.xxx.cn:8443是否可连接。
- 若主地址连接失败，则依次尝试备用地址https://app1.xxx.cn:8443和https://app2.xxx.cn:8443。
- 每个地址的判断超时时长为2秒。
- 若有可连通地址，则将该地址设置为全局使用的Constants.DOMAIN，供后续网络请求使用。

 
该机制可保证在弱网或网络切换场景下，App能快速切换至可用地址，保障功能可用性。
 
 

#### 背景知识

在ArkTS开发中，[NetworkKit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-kit)提供了基于TCP的[socket](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/socket-connection)接口，可用于检测目标地址是否连通，而不依赖于上层[HTTP请求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request)。
 
相比传统的方式，TCP连接判断具有更低的延迟和更明确的网络连通性判定结果，适合用于冷启动时的网络环境选择。
 
此外，[BusinessError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)接口定义了连接失败的错误信息结构，可以通过错误码或错误信息进行异常判断与处理。
 
 

#### 解决方案

该方案通过以下三步实现目标地址的连通性检测和优选逻辑：
 1. 定义一个包含主地址和两个备用地址的优先级列表，每个地址包括host和port：
```text
<em>// </em><em><span style="color: rgb(128,128,128);">仅供展示，请根据需要替换真实地址</span></em>
const <span style="color: rgb(0,0,255);">PRIORITY_TARGETS</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CheckTarget</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">主地址</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">备用地址</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app1.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">备用地址</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app2.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
```

2. 基于TCP实现网络连通性检测。使用socket.constructTCPSocketInstance()创建TCP套接字，并设置连接目标和超时时间（默认2000ms）。连接成功即视为网络连通，失败则记录错误信息。
```text
private async <span style="color: rgb(0,0,255);">checkNetworkConnectivity</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">NetWorkResult</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  return new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">tcpSocket </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constructTCPSocketInstance</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">connectOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ConnectOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">port</span>
      <span style="color: rgb(255,0,170);">} </span>as <span style="color: rgb(0,0,255);">NetAddress</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">connectOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">close</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(181,106,1);">: </span>true <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">errorCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">`ERROR_</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">errorMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 按照优先级依次检测并选用第一个可用地址。通过遍历PRIORITY_TARGETS列表，逐一调用上一步的检测函数。若某个地址连通，则将其设置为全局使用的Constants.DOMAIN并立即返回成功；若均不可达则返回失败。
```text
private async <span style="color: rgb(0,0,255);">checkWithPriority</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(0,0,255);">(</span>const <span style="color: rgb(0,0,255);">target </span>of <span style="color: rgb(0,0,255);">PRIORITY_TARGETS</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">正在检测 </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> (</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">)...`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">result </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">checkNetworkConnectivity</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">✅ </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">连通！</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Constants</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">❌ </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">不可达</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">errorMessage</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
通过以上实现，预期效果如下：
 
- 在2秒内完成主地址的连通性判断。
- 若主地址不可用，将自动判断备用地址，整个判断过程控制在合理的总耗时内（最多6秒）。
- Constants.DOMAIN被设置为首个可用地址，后续网络请求均基于该地址执行。

 
此方案可广泛应用于HarmonyOS Next版本App的冷启动初始化阶段，提高App网络初始化成功率和稳定性。运行本示例需要在工程的module.json5文件中添加网络权限ohos.permission.INTERNET。
 
完整示例代码如下：
 
- Index.ets代码：

 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">socket </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">Constants </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'../constants/Constants'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">NetWorkResult</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ConnectOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NetAddress</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">CheckTarget </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'../model/DataModel'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">TAG </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'NetworkTest'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">仅供展示，请根据需要替换真实地址</span></em>
const <span style="color: rgb(0,0,255);">PRIORITY_TARGETS</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CheckTarget</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">主地址</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">备用地址</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app1.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">备用地址</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'app2.xxx.cn'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8443 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isChecking</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  private async <span style="color: rgb(0,0,255);">checkWithPriority</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>const <span style="color: rgb(0,0,255);">target </span>of <span style="color: rgb(0,0,255);">PRIORITY_TARGETS</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">正在检测 </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> (</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">)...`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(0,0,255);">result </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">checkNetworkConnectivity</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">✅ </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">连通！</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Constants</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
        break<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">❌ </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">不可达</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">errorMessage</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  private async <span style="color: rgb(0,0,255);">checkNetworkConnectivity</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">NetWorkResult</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">tcpSocket </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">socket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constructTCPSocketInstance</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(0,0,255);">connectOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ConnectOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">port</span>
        <span style="color: rgb(255,0,170);">} </span>as <span style="color: rgb(0,0,255);">NetAddress</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">connectOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">tcpSocket</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">close</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(181,106,1);">: </span>true <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">errorCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">`ERROR_</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">errorMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">网络连通性检测</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">检测中</span><span style="color: rgb(255,0,170);">...' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">开始检测</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isChecking</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">checkWithPriority</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
- DataModel.ets代码：

 
```text
export interface <span style="color: rgb(0,0,255);">CheckTarget </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">网络地址类型</span></em>
export interface <span style="color: rgb(0,0,255);">NetAddress </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

export interface <span style="color: rgb(0,0,255);">ConnectOptions </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">address</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NetAddress</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

export interface <span style="color: rgb(0,0,255);">NetWorkResult </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">isReachable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">errorCode</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">errorMessage</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
- Constants.ets代码：

 
```text
export class <span style="color: rgb(0,0,255);">Constants </span><span style="color: rgb(255,0,170);">{</span>
  static <span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
