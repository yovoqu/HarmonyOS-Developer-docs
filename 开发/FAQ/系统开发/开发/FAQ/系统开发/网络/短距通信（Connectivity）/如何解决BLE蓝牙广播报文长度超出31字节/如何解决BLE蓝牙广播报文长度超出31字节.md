# 如何解决BLE蓝牙广播报文长度超出31字节

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-26

#### 问题现象

BLE蓝牙广播，如果设置携带设备名就发不了13条serviceUuids数据，应该怎么在携带设备名称和发送13条serviceUuids数据之间做取舍？
 
问题代码示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ble </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'BleAdvertisingManager'</span><span style="color: rgb(181,106,1);">;</span>

export class <span style="color: rgb(0,0,255);">BleAdvertisingManager </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">advHandle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">0xFF</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// 1.</span><span style="color: rgb(128,128,128);">定义广播状态上报事件</span></em>
  <span style="color: rgb(255,255,255);">onReceiveEvent </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AdvertisingStateChangeInfo</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'advertiserState'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">state</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// 2.</span><span style="color: rgb(128,128,128);">首次启动广播</span></em>
  public async <span style="color: rgb(0,0,255);">startAdvertising</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <em><span style="color: rgb(128,128,128);">// 2.1</span><span style="color: rgb(128,128,128);">设置广播发送的参数</span></em>
    let <span style="color: rgb(255,255,255);">setting</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AdvertiseSetting </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">interval</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">160</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">txPower</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">connectable</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// 2.2</span><span style="color: rgb(128,128,128);">构造广播数据</span></em>
    let <span style="color: rgb(255,255,255);">manufactureValueBuffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">manufactureValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">manufactureValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">manufactureValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">manufactureValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">;</span>


    let <span style="color: rgb(255,255,255);">serviceValueBuffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">6</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">7</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">manufactureDataUnit</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ManufactureData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">manufactureId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">4567</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">manufactureValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">manufactureValueBuffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">serviceDataUnit1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ServiceData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">serviceUuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"0000181A-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">serviceValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">serviceDataUnit2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ServiceData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">serviceUuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"19991999-0000-1000-8000-00805f9b34fb"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">serviceValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">serviceValueBuffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">advData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AdvertiseData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">serviceUuids</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span>
        <span style="color: rgb(132,63,161);">"000008F0-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00000810-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00009D13-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"0000950E-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00004E2D-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"000041F0-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00001DE1-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00007EB9-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"0000F59C-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00002D98-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"0000343D-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00002B0B-0000-1000-8000-00805F9B34FB"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"00002D89-0000-1000-8000-00805F9B34FB"</span>
      <span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">manufactureData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">serviceData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

   <em> <span style="color: rgb(128,128,128);">// 2.3</span><span style="color: rgb(128,128,128);">构造广播启动完整参数</span><span style="color: rgb(128,128,128);">AdvertisingParams</span></em>
    let <span style="color: rgb(255,255,255);">advertisingParams</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AdvertisingParams </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">advertisingSettings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">setting</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">advertisingData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">advData</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">注意</span><span style="color: rgb(128,128,128);">:</span><span style="color: rgb(128,128,128);">广播报文长度不能超过</span><span style="color: rgb(128,128,128);">31</span><span style="color: rgb(128,128,128);">个字节</span></em>
      <span style="color: rgb(255,255,255);">advertisingResponse</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">advData</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">注意</span><span style="color: rgb(128,128,128);">:</span><span style="color: rgb(128,128,128);">广播报文长度不能超过</span><span style="color: rgb(128,128,128);">31</span><span style="color: rgb(128,128,128);">个字节</span></em>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0 </span><em>// </em><em><span style="color: rgb(128,128,128);">可选参数，若参数大于</span><span style="color: rgb(128,128,128);">0</span><span style="color: rgb(128,128,128);">，则广播发送一段时间后会停止，但分配的广播资源还在，可重新启动发送</span></em>
    <span style="color: rgb(181,106,1);">}</span>

   <em> <span style="color: rgb(128,128,128);">// 2.4</span><span style="color: rgb(128,128,128);">首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播标识</span><span style="color: rgb(128,128,128);">ID</span></em>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'advertisingStateChange'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">onReceiveEvent</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">advHandle </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">ble</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAdvertising</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">advertisingParams</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'err'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
```
 
 

#### 背景知识

- 启动发送BLE广播报文[ble.startAdvertising](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blestartadvertising11)方法中，[AdvertisingParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#advertisingparams11)参数中的[AdvertiseData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#advertisedata)是描述BLE广播报文数据内容，也可以用作回复扫描请求的广播报文数据内容。当前只支持传统广播，因此报文最大长度为31个字节。若超出最大长度（31个字节）限制，会导致启动广播失败。若携带了所有参数，尤其是携带了蓝牙设备名称，需要注意广播报文长度。
- UUID类型有16字节、4字节、2字节三种：0000xxxx-0000-1000-8000-00805f9b34fb：2字节。

  xxxxxxxx-0000-1000-8000-00805f9b34fb：4字节。

  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx：16字节。

 
 

#### 问题定位

根据问题代码中的serviceUuids可以发现，1条serviceUuid是2字节，13条就是26字节。如果广播要携带设备名，占用的字节数取决于设置界面的蓝牙名称的总长度，问题中的设备名"XXXX XXPro"占用10个字节，因此会超出最大长度（31个字节）限制，会导致启动广播失败。
 
 

#### 分析结论

启动广播失败是因为超出了报文最大长度，serviceUuid可以在连接之后服务发现的时候获取，不一定要在广播的时候全都带上。
 
服务发现流程：[getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservices-1)，client获取server端支持的所有服务能力。获取返回的结构体[GattService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#gattservice)中会有所有的serviceUuid。
 
 

#### 修改建议

如果一定要在广播时设置携带设备名，建议减少serviceUuid的条数，后续在服务发现流程获取serviceUuid。
