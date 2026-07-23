# HID蓝牙配对后如何实现自动连接

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-8

#### 问题现象

在与HID设备完成配对后，如何实现自动连接？如果在系统蓝牙界面手动点击连接之后，后续断开是否会稳定回连？
 
 

#### 背景知识

- 从API16版本开始，@ohos.bluetooth.connection模块提供了[connectAllowedProfiles](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionconnectallowedprofiles16-1)接口，支持对HFP、HID、A2DP设备主动发起连接。
- 从API12版本开始，@ohos.bluetooth.connection模块提供了[getRemoteProfileUuids](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetremoteprofileuuids12)接口，可用于查询对端蓝牙设备的profile协议能力，建议仅对已配对的设备调用该方法。

 
 

#### 解决方案

- 当与HID设备完成配对，调用connectAllowedProfiles接口成功建立连接后，后续每次重新打开蓝牙开关，系统都可以自动与HID设备建立连接。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">connection </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ConnectivityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">connectAllowedProfiles </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">connectAllowedProfiles</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发起蓝牙配对请求，此处的</span><span style="color: rgb(128,128,128);">mac</span><span style="color: rgb(128,128,128);">需要提前获取</span></em>
    <span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pairDevice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'xx.xx.xx.xx'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`pairDevice, device name err:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">订阅蓝牙配对状态变化事件</span></em>
    <span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'bondStateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BondStateParam</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">蓝牙已配对</span></em>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">state </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BondState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOND_STATE_BONDED</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">getRemoteProfileUuids</span><span style="color: rgb(128,128,128);">接口获取对端蓝牙支持的</span><span style="color: rgb(128,128,128);">Profile</span><span style="color: rgb(128,128,128);">类型</span></em>
        <span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRemoteProfileUuids</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ProfileUuids</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getRemoteProfileUuids errCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, errMessage: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, dataArray: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当</span><span style="color: rgb(128,128,128);">dataArray</span><span style="color: rgb(128,128,128);">中支持类型包含</span><span style="color: rgb(128,128,128);">A2DP</span><span style="color: rgb(128,128,128);">、</span><span style="color: rgb(128,128,128);">HFP</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">HID</span><span style="color: rgb(128,128,128);">其中的一种，可调用</span><span style="color: rgb(128,128,128);">connectAllowedProfiles</span><span style="color: rgb(128,128,128);">接口发起连接</span></em>
            <span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connectAllowedProfiles</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deviceId</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`connectAllowedProfiles errCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, errMessage: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                return<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'connectAllowedProfiles'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'connect Allowed Profiles'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建蓝牙配对状态变化监听，发起蓝牙配对，连接蓝牙</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connectAllowedProfiles</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 如果在系统蓝牙界面使用手动点击的方式与HID设备建立连接，需要在已配对的设备配置信息中打开‘输入设备’开关，才能实现稳定回连。

 
 

#### 常见FAQ

Q：在HarmonyOS中，connection.connectAllowedProfiles接口用于连接支持特定配置文件的蓝牙设备。请问该接口支持哪些profile类型？
 
A：connection.connectAllowedProfiles接口支持的profile类型理论上只包括A2DP、HFP和HID这三种，但是有个特殊的profile类型HOGP。HOGP实际上为HID Over GATT Protocol的缩写，HID以前是只有BR设备有的，后来HID profile为了适配BLE设备才有了HOGP profile这个类型，属于HID profile的一种。
