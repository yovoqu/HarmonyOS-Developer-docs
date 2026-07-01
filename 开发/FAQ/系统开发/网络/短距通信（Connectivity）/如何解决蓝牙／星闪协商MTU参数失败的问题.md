# 如何解决蓝牙/星闪协商MTU参数失败的问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-24

#### 问题现象

在蓝牙/星闪功能开发过程中，协商MTU时，有时会出现[2900099](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager#section2900099)/[1009700099](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code#section15998194717498)错误的问题，该如何解决？
 
 

#### 背景知识

- BLE蓝牙提供了[setBLEMtuSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#setblemtusize)接口用于client端同server端协商MTU（最大传输单元，取值范围23~517）大小。
- 星闪提供了[requestMtuSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#section171901711153612)接口用于client端同server端协商MTU（最大传输单元，取值范围22~512）大小。
- 蓝牙/星闪同server端协商MTU前，需要保证client端同server端处于连接的状态。

 
 

#### 问题定位

- 排查在协商MTU前，蓝牙/星闪client端同server端是否断开了连接。
- 检查协商的MTU参数范围是否合理。

 
 

#### 分析结论

- 结论一：setBLEMtuSize/requestMtuSize接口调用时机不对，需要在蓝牙/星闪client端和server端连接成功后，才能调用setBLEMtuSize/requestMtuSize接口协商MTU参数。
- 结论二：协商的MTU参数设置不在取值范围内。

 
 

#### 修改建议

协商MTU前，需保证client端同server端处于连接的状态，且协商的MTU参数需要设置在取值范围内。
 
- 蓝牙/星闪端：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">constant </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ssap </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.NearLinkKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BleAndSsapSetMtu </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">GattClientDevice </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">ssapClient</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ssap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Client </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">端</span><span style="color: rgb(128,128,128);">mtu</span></em>
  <span style="color: rgb(0,0,255);">setBleMtu</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">端实例，</span><span style="color: rgb(128,128,128);">bleMac</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端虚拟</span><span style="color: rgb(128,128,128);">mac</span><span style="color: rgb(128,128,128);">地址，需要提前获取</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'bleMac'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙连接状态监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">协商结果监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BLEMtuChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onBLEConnectionStateChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'BLEConnectionStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BLEConnectionChangeState</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <em>    <span style="color: rgb(128,128,128);">// state.state</span><span style="color: rgb(128,128,128);">返回结果为</span><span style="color: rgb(128,128,128);">2</span><span style="color: rgb(128,128,128);">时，表示</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">端同</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端成功建立了连接。</span></em>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">constant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ProfileConnectionState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">STATE_CONNECTED</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">setBLEMtuSize</span><span style="color: rgb(128,128,128);">接口，同</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端协商</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">，参数取值范围</span><span style="color: rgb(128,128,128);">23~517</span><span style="color: rgb(128,128,128);">。</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setBLEMtuSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">128</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">BLEMtuChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'BLEMtuChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// MTU</span><span style="color: rgb(128,128,128);">协商结果监听回调，回调触发，表示协商成功。</span></em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`BLEMtuChange, mtu: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置星闪端</span><span style="color: rgb(128,128,128);">mtu</span></em>
  <span style="color: rgb(0,0,255);">setSsapMtu</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">端实例，</span><span style="color: rgb(128,128,128);">ssapMac</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端虚拟</span><span style="color: rgb(128,128,128);">mac</span><span style="color: rgb(128,128,128);">地址，需要提前获取</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ssapClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">ssap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createClient</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'ssapMac'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙连接状态监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onConnectionStateChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">协商结果监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ssapMtuChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ssapClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onConnectionStateChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ssapClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'connectionStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ssap</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ConnectionChangeState</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// state.state</span><span style="color: rgb(128,128,128);">返回结果为</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">时，表示</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">端同</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端成功建立了连接。</span></em>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">requestMtuSize</span><span style="color: rgb(128,128,128);">接口，同</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端协商</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">，参数取值范围</span><span style="color: rgb(128,128,128);">22~512</span><span style="color: rgb(128,128,128);">，默认值为</span><span style="color: rgb(128,128,128);">256</span><span style="color: rgb(128,128,128);">字节。</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ssapClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">requestMtuSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">128</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">ssapMtuChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ssapClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'mtuChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <em>    <span style="color: rgb(128,128,128);">// MTU</span><span style="color: rgb(128,128,128);">协商结果监听回调，回调触发，表示协商成功。</span></em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`mtuChange, mtu:  </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">连接</span><span style="color: rgb(132,63,161);">ble</span><span style="color: rgb(132,63,161);">蓝牙，并协商</span><span style="color: rgb(132,63,161);">MTU'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙，并协商</span><span style="color: rgb(128,128,128);">MTU</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setBleMtu</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">连接星闪，并协商</span><span style="color: rgb(132,63,161);">MTU'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接星闪，并协商</span><span style="color: rgb(128,128,128);">MTU</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setSsapMtu</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SpaceAround</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 

#### 常见FAQ

Q：在BLE蓝牙开发流程中，setBLEMtuSize()接口在什么时候调用最合适？
 
A：setBLEMtuSize()方法只能在调用[connect()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#connect)接口成功连接上蓝牙之后调用。建议在调用[getServices()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservices)接口获取server端支持的所有服务能力之前调用。
