# 调用call.makeCall发生编译告警：The API is not supported on all devices

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-3

#### 问题现象

调用Telephony Kit（蜂窝通信服务）的[call.makeCall](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call#callmakecall7)方法会有编译告警：
 
```text
<span style="color: rgb(0,0,255);">The API is not supported on all devices</span><span style="color: rgb(181,106,1);">. </span><span style="color: rgb(0,0,255);">Use the canIUse condition to determine whether the API is supported</span><span style="color: rgb(181,106,1);">. </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">ArkTSCheck</span><span style="color: rgb(181,106,1);">></span>
```
 
 

#### 背景知识

- SysCap，全称SystemCapability，即系统能力，指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。每个系统能力对应多个API，随着目标设备是否支持该系统能力共同存在或消失。
- [call.makeCall](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call#callmakecall7)使用的系统能力是：SystemCapability.Applications.Contacts。

 
 

#### 解决方案

当设备不支持具体的系统能力时就会提示The API is not supported on all devices，该提示不会影响在具备系统能力的设备上运行结果。针对该提示，有两种处理方案：
 
- **方案一**：调用系统API之前可以先判断是否具备系统能力，可以防止运行时报错。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">call </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.TelephonyKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CallPhoneTest </span><span style="color: rgb(255,0,170);">{</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Call Phone'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">call</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hasVoiceCapability</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">call</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">makeCall</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'135****1234'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案二**：在module.json5可以移除未使用的设备类型。由于DevEco Studio默认创建的项目会包含phone，tablet，2in1三种设备类型。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Zl-OxdNuR5uAqvvMjsKl0A/zh-cn_image_0000002628773306.png?HW-CC-KV=V1&HW-CC-Date=20260811T005941Z&HW-CC-Expire=86400&HW-CC-Sign=0046D45D13220CC9ABC9E4758D506F4AB8648DB0A52A0C57D2512D0117D7217B)


  tablet和2in1不具备SystemCapability.Applications.Contacts能力。

  所以默认没有修改设备类型时，会提示编译告警。移除下例代码中tablet，2in1后则不会再出现告警：

  
```json
"deviceTypes": [
  "phone",
  "tablet",
  "2in1",
  "car",
  "wearable",
  "tv"
],
```


 
 

#### 常见FAQ

Q：为什么平板没有SIM卡槽，使用canIUse("SystemCapability.Telephony.CallManager")判断系统能力返回为true?
 
A：由于分布式通信特性，通信相关部件需要在平板上保留，应用开发不能保证都会使用canIUse，为了避免应用因为不调用canIUse，直接使用API导致应用crash，设备需要预置所有的部件，所以当前对于平板设备，不建议使用canIUse机制。
 
Q：如何实现拉起拨号盘，直接拨打号码和发送短信？
 
A：目前可以参照[Telephony Kit（蜂窝通信服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/telephony-kit)实现拨打电话和发送短信。
