# 如何实现BLE蓝牙快速回连

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-12

#### 问题现象

如果应用已经与对端蓝牙设备建立过BLE蓝牙连接，那么如何不通过蓝牙扫描，就能够与之前已连接过的蓝牙设备快速建立连接？
 
 

#### 背景知识

- 在HarmonyOS中，若设备A与B没有建立配对，则它们的蓝牙虚拟MAC地址会随着开关机等操作发生改变。若设备A与设备B后建立了蓝牙配对，则它们的蓝牙虚拟MAC地址会被固化，即使设备开关机，蓝牙虚拟MAC地址也不会发生改变。
- API16及后续版本，HarmonyOS提供了无需配对就可将蓝牙虚拟MAC地址固化的API接口：[addPersistentDeviceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessaddpersistentdeviceid16)。由于应用通过蓝牙扫描获取到未配对或未固化的设备MAC地址是虚拟随机的，若想该虚拟随机地址不发生改变，可以调用addPersistentDeviceId接口持久化存储虚拟随机地址。
> [!NOTE]
> 使用蓝牙虚拟MAC地址固化API需要使用到 ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC 权限，且需要 ACL 权限申请通过后方可使用。 使用该接口时，开发者应明确该虚拟随机地址对应的对端蓝牙设备真实地址是不变的，若对端设备地址发生变化，持久化保存的地址信息也会失效，无法继续使用。


 
 

#### 解决方案

- 方案一：与对端设备第一次连接后，发起[蓝牙配对](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionpairdevice-1)，配对完成后，蓝牙虚拟MAC地址会被固化。后续无需重复建立蓝牙扫描，调用[getPairedDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetpaireddevices)接口就可以从已配对列表中获取对端蓝牙的虚拟MAC地址，向对端设备发起连接。
- 方案二：与对端设备第一次连接后，使用[addPersistentDeviceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessaddpersistentdeviceid16)接口固化对端设备虚拟MAC地址。后续同样无需重复建立蓝牙扫描，调用[getPersistentDeviceIds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessgetpersistentdeviceids16)接口就可以从已固化设备列表中获取对端蓝牙的虚拟MAC地址，向对端设备发起连接。

 
方案一、方案二完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">access</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">constant </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Reconnect </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GattClientDevice </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">方案一</span></em>
  <span style="color: rgb(0,0,255);">ReconnectOne</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">先查询已配对设备列表，判断需要连接的设备是否在已配对设备列表中存在。</span></em>
    let <span style="color: rgb(0,0,255);">devices </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPairedDevices</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRemoteDeviceName</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">需要连接的设备在已配对设备列表中存在，无需发起扫描，直接创建实例进行连接。</span></em>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'name'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">实例</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接前先创建连接状态回调监听</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChangeOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">需要连接的设备在已配对设备列表中不存在，开启常规</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙连接流程。</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">BLE</span><span style="color: rgb(128,128,128);">设备发现</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEDeviceFindOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">过滤参数可根据实际场景进行设置</span></em>
    let <span style="color: rgb(0,0,255);">scanFilter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanFilter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'name'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">扫描参数可根据实际场景配置</span></em>
    let <span style="color: rgb(0,0,255);">scanOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">interval</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">dutyMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanDuty</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SCAN_MODE_LOW_POWER</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">matchMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MatchMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MATCH_MODE_AGGRESSIVE</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startBLEScan</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">scanFilter</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">scanOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBLEDeviceFindOne</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'BLEDeviceFind'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanResult</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发现设备，创建实例进行连接</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接前先创建连接状态回调监听</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChangeOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接成功后，将已连接设备加入配对列表。</span></em>
<em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注意：加入配对列表时机并不固定，可根据实际场景来进行变更。</span></em>
      <span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pairDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pairDevice err'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBLEConnectionStateChangeOne</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'BLEConnectionStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BLEConnectionChangeState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">constant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ProfileConnectionState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STATE_DISCONNECTED</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果蓝牙意外断开了连接，可以在此处重新发起连接，以达到意外断连快速回连能力。</span></em>
<em>        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">不过需要保证此时</span><span style="color: rgb(128,128,128);">this.gattClient</span><span style="color: rgb(128,128,128);">实例没有被销毁。</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">方案二</span></em>
  <span style="color: rgb(0,0,255);">ReconnectTwo</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">先查询已固化设备列表，判断需要连接的设备是否在已固化设备列表中存在。</span></em>
    let <span style="color: rgb(0,0,255);">devices </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">access</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPersistentDeviceIds</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRemoteDeviceName</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(0,0,255);">isValid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">access</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isValidRandomDeviceId</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      <em>// </em><em><span style="color: rgb(128,128,128);">需要连接的设备在已固化设备列表中存在，同时该地址有效，无需发起扫描，直接创建实例进行连接。</span></em>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isValid </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'name'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">实例</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">devices</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
        <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接前先创建连接状态回调监听</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChangeTwo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">需要连接的设备在已固化设备列表中不存在，开启常规</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙连接流程。</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">BLE</span><span style="color: rgb(128,128,128);">设备发现</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEDeviceFindTwo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">过滤参数可根据实际场景进行设置</span></em>
    let <span style="color: rgb(0,0,255);">scanFilter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanFilter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'name'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">扫描参数可根据实际场景配置</span></em>
    let <span style="color: rgb(0,0,255);">scanOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">interval</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">dutyMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanDuty</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SCAN_MODE_LOW_POWER</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">matchMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MatchMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MATCH_MODE_AGGRESSIVE</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startBLEScan</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">scanFilter</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">scanOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBLEDeviceFindTwo</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'BLEDeviceFind'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ScanResult</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发现设备，创建实例进行连接。</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接前先创建连接状态回调监听</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChangeTwo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接成功后，将已连接设备加入固化列表。</span></em>
<em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注意：加入固化列表时机并不固定，可根据实际场景来进行变更。</span></em>
      <span style="color: rgb(0,0,255);">access</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addPersistentDeviceId</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBLEConnectionStateChangeTwo</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'BLEConnectionStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BLEConnectionChangeState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">constant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ProfileConnectionState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STATE_DISCONNECTED</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果蓝牙意外断开了连接，可以在此处重新发起连接，以达到意外断连快速回连能力。</span></em>
<em>        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">不过需要保证此时</span><span style="color: rgb(128,128,128);">this.gattClient</span><span style="color: rgb(128,128,128);">实例没有被销毁。</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ble</span><span style="color: rgb(255,0,170);">蓝牙连接</span><span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">支持快速回连</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,0,170);">方案</span><span style="color: rgb(255,0,170);">1)'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发起连接</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReconnectOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ble</span><span style="color: rgb(255,0,170);">蓝牙连接</span><span style="color: rgb(255,0,170);">/</span><span style="color: rgb(255,0,170);">支持快速回连</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,0,170);">方案</span><span style="color: rgb(255,0,170);">2)'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发起连接</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReconnectTwo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
> [!NOTE]
> 由于方案二需要使用受限开放的ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC权限，一般推荐使用方案一。若业务中不能包含配对场景，且可以成功申请ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC权限，就可以采取方案二。

 
 

#### 常见FAQ

Q：由于担心蓝牙虚拟MAC地址变化，需要在重新连接前一直扫描，会造成资源消耗，应该如何解决？
 
A：可以使用[addPersistentDeviceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessaddpersistentdeviceid16)持久化蓝牙地址，就不需要在重连前一直扫描。
 
Q：使用addPersistentDeviceId持久化后，是否即使蓝牙设备关机重启，只要蓝牙物理MAC地址不变，被持久化的虚拟MAC地址也不会发生改变？
 
A：是的，只要对端蓝牙设备真实地址保持不变，那么被addPersistentDeviceId接口持久化的虚拟MAC地址就不会发生改变。
