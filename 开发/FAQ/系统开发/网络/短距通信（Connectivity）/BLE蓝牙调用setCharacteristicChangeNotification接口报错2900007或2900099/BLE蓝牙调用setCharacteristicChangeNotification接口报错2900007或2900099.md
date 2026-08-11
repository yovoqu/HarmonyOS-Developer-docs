# BLE蓝牙调用setCharacteristicChangeNotification接口报错2900007或2900099

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-11

#### 问题现象

在BLE蓝牙应用开发过程中，调用setCharacteristicChangeNotification接口时出现2900007或2900099报错，该如何排查解决？
 
 

#### 背景知识

- [2900007](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager#section2900007)表示接口调用超时。当client端向server端发起了请求，在一定时间内（约10s）client端没有收到server端的应答，client端就会返回此错误码。
- [2900099](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager#section2900099)表示接口调用操作失败。一般接口调用阻塞，会返回此错误码。
- [setCharacteristicChangeNotification](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#setcharacteristicchangenotification)接口提供了client端启用或者禁用接收server端特征值内容变更通知的能力，使用前需仔细阅读接口下方说明。
- 调用setCharacteristicChangeNotification接口后，底层会默认通过描述符的形式向server端写入一次数据请求，server端可通过[descriptorWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#ondescriptorwrite)接收请求，然后调用[sendResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#sendresponse)接口向client返回数据，client成功接收到数据后，即一个完整的setCharacteristicChangeNotification接口请求流程才算完毕。

 
 

#### 问题定位

- 排查server端（server端以HarmonyOS NEXT设备为例）是否创建了[on('descriptorWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#ondescriptorwrite)监听。若server端没有创建此监听，将无法接收到client端发来的描述符请求，client端setCharacteristicChangeNotification接口将会处于持续请求的阻塞状态。
- 排查server端接收到client端发来的描述符请求后，是否及时应答（检查日志是否返回OnSetNotifyCharacteristic关键字）。若server端在接收到client端发来的描述符请求后没有及时调用sendResponse接口应答，client端setCharacteristicChangeNotification接口同样会处于持续请求的阻塞状态。参考错误日志如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/K3Y3QJHiSUqQI5AuIYLq1w/zh-cn_image_0000002628772390.png?HW-CC-KV=V1&HW-CC-Date=20260811T005931Z&HW-CC-Expire=86400&HW-CC-Sign=C14BCAE82336EF9024A6AE31EA26F2AFFF783600381862E7029C3BFDDCA55E2A)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/vIQh6MQQR-O7Zb2D4QkzaQ/zh-cn_image_0000002658971711.png?HW-CC-KV=V1&HW-CC-Date=20260811T005931Z&HW-CC-Expire=86400&HW-CC-Sign=583B737D71F8CAF8E424728DC441DABBBA10DCD2DC27E580772C678F0D14BB46)

- 检查client端调用setCharacteristicChangeNotification接口时，是否有其它异步接口调用未完成，导致setCharacteristicChangeNotification接口调用被阻塞。排查方式如下：
通过在接口回调中设置日志打印，查看接口调用的完整顺序流程。从创建对象实例到数据传输，BLE蓝牙client端接口调用顺序参考如下：1. 调用[createGattClientDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blecreategattclientdevice)接口创建client实例。

2. 创建BLE蓝牙连接状态监听、MTU变化监听、特征值变化监听等接口。

3. 调用[connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#connect)接口连接BLE蓝牙。

4. 调用[setBLEMtuSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#setblemtusize)接口协商MTU。

5. 调用[getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservices-1)接口获取server端支持的所有服务能力。

6. 调用setCharacteristicChangeNotification接口设置server端特征值内容变更通知的能力。

7. 调用[writeCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#writecharacteristicvalue)接口向server端写入特征值数据。
- 排查系统日志输出。可在问题复现后[生成hilog日志](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog#hilog日志生成)，查看日志中各接口调用开始/完成时，系统日志输出的时间点，从而判断是否出现了接口调用阻塞情况。如：setCharacteristicChangeNotification接口调用开始时，系统日志中会打印出关键字setCharacteristicChangeNotification。接口调用完成时，可通过setCharacteristicChangeNotification接口Callback回调中自定义的日志进行判断。参考问题日志如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/EUkUgx6mQc6-u9WSH-OMUQ/zh-cn_image_0000002628612500.png?HW-CC-KV=V1&HW-CC-Date=20260811T005931Z&HW-CC-Expire=86400&HW-CC-Sign=E362111953A112DD5FDB3FFA50A07789A2499804739DFAD1A342BFBBFE204986)


 
 
 

#### 分析结论

- server端没有创建on('descriptorWrite')监听，或接收到client端发来的描述符请求后，没有及时应答。
- 在调用setCharacteristicChangeNotification接口前一般会先调用setBLEMtuSize异步接口，与server端协商MTU数据传输大小。然后再调用getServices接口，获取server端的特征值服务列表。因此，需要在setBLEMtuSize和getServices接口依次调用成功后，才可以调用setCharacteristicChangeNotification接口，设置接收server端特征值内容变更通知的能力。

 
 

#### 修改建议

- client端调用setCharacteristicChangeNotification接口前，需开启server端订阅client的描述符写请求事件监听，同时在接收到描述符请求后，及时做出消息回复。
- 可对setBLEMtuSize、getServices和setCharacteristicChangeNotification接口调用顺序进行修改，并添加MTU变更事件监听，同时通过一一赋值的方式创建characteristic对象。

 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">constant </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">PermissionRequestResult </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">setCharacteristicChangeNotification </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">GattClientDevice </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AtManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAtManager</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestPermissionsFromUser</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'ohos.permission.ACCESS_BLUETOOTH'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PermissionRequestResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`requestPermissionsFromUser fail, err-</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`data:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">client</span><span style="color: rgb(128,128,128);">端实例，</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端虚拟</span><span style="color: rgb(128,128,128);">mac</span><span style="color: rgb(128,128,128);">地址</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">使用时</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">需要根据实际进行修改</span></em>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createGattClientDevice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'deviceMAC'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`createGattClientDevice error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙连接状态监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBLEConnectionStateChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">监听事件</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BLEMtuChange</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">端</span><span style="color: rgb(128,128,128);">ble</span><span style="color: rgb(128,128,128);">蓝牙</span></em>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`connect error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">onBLEConnectionStateChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'BLEConnectionStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BLEConnectionChangeState</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">constant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ProfileConnectionState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">STATE_CONNECTED</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接成功，先与</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">协商</span><span style="color: rgb(128,128,128);">MTU</span><span style="color: rgb(128,128,128);">，参数范围</span><span style="color: rgb(128,128,128);">23~517</span></em>
          try <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setBLEMtuSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">128</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`on BLEConnectionStateChange error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">BLEMtuChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'BLEMtuChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// MTU</span><span style="color: rgb(128,128,128);">协商成功</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">getServices</span><span style="color: rgb(128,128,128);">接口获取</span><span style="color: rgb(128,128,128);">server</span><span style="color: rgb(128,128,128);">服务。</span></em>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">协商成功</span><span style="color: rgb(132,63,161);">,mtu</span><span style="color: rgb(132,63,161);">参数为</span><span style="color: rgb(132,63,161);">:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">mtu</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getServices</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`on BLEMtuChange error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">getServices</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getServices</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">GattService</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">筛选出指定特征值服务，并设置通知变更能力。</span></em>
<em>        <span style="color: rgb(128,128,128);">// server</span><span style="color: rgb(128,128,128);">端指定服务</span><span style="color: rgb(128,128,128);">uuid,</span><span style="color: rgb(128,128,128);">使用时</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">需要根据实际进行修改</span></em>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">serviceUuid </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'uuid'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          let <span style="color: rgb(255,255,255);">descriptors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BLEDescriptor</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">arrayBuffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">descV </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">arrayBuffer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">descV</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">11</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">arrayBufferC </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
     <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过一一赋值的方式创建</span><span style="color: rgb(128,128,128);">characteristic</span><span style="color: rgb(128,128,128);">对象</span></em>
          let <span style="color: rgb(255,255,255);">characteristic</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BLECharacteristic </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">serviceUuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">serviceUuid</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">characteristicUuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">characteristics</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">characteristicUuid</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">characteristicValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">arrayBufferC</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">descriptors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">descriptors</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">gattClient</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">setCharacteristicChangeNotification</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">characteristic</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'notifyCharacteristicChanged callback failed'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'notifyCharacteristicChanged callback successful'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`getServices error:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">连接</span><span style="color: rgb(132,63,161);">BLE</span><span style="color: rgb(132,63,161);">蓝牙，并发起请求</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">连接</span><span style="color: rgb(128,128,128);">BLE</span><span style="color: rgb(128,128,128);">蓝牙，并发起</span><span style="color: rgb(128,128,128);">setCharacteristicChangeNotification</span></em><em>请求</em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SpaceAround</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
> [!NOTE]
> 使用蓝牙能力时，需要在module.json5中添加ohos.permission.ACCESS_BLUETOOTH权限。

 
 

#### 常见FAQ

Q：BLE蓝牙writeCharacteristicValue接口写入数据时，2900099报错是什么原因？
 
A：关于BLE写入数据报错2900099，有如下原因：
- 当上一个非监听类BLE蓝牙接口（setBLEMtuSize、getServices和setCharacteristicChangeNotification）回调还未返回时写入数据，会出现2900099报错提示，导致写入数据失败。因此，需要保证在其它非监听类BLE接口回调触发完成后，再调用writeCharacteristicValue接口写入数据。
- 每次重连GATT设备时都会重新创建新的gattClient对象，建立一路新的GATT连接。若每次连接关闭后不及时调用[close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#close-1)接口销毁gattClient对象实例，则会导致每次重连时重复多次调用setCharacteristicChangeNotification和getService，出现busy现象，进而导致报错2900099。因此，每次连接关闭后，需及时销毁gattClient对象。
- 参数错误，系统日志会同时打印Invalid parameters，需要排查是否按GATT规范传入了正确的[BLECharacteristic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blecharacteristic)。

 
 
Q：一个setCharacteristicChangeNotification接口能否同时设置多个特征值服务？
 
A：一个setCharacteristicChangeNotification只能设置一个特征值服务变更通知，如果需要对多个特征值服务进行设置，需要多次调用setCharacteristicChangeNotification接口。
 
Q：早期存量设备没有描述值不能提供descriptors字段，怎么调用setCharacteristicChangeNotification接口呢？
 
A：descriptor可以传入[]空列表调用setCharacteristicChangeNotification接口。
