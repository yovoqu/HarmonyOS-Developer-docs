# 如何检测设备SIM卡是否已变更

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-4

#### 问题现象

企业应用需要监听获取SIM卡标识，首次接入使用企业应用需要进行记录，以后认证使用企业应用都需要检测SIM卡是否做过变更，如何实现检测SIM卡是否已变更的功能？
 
 

#### 背景知识

- [SIM卡管理模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim#simgetsimoperatornumeric)提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。
- SIM卡管理模块中的[getSimOperatorNumeric](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim#simgetsimoperatornumeric)接口可以获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。

 
 

#### 解决方案

可以在首次接入使用应用时，将获取的PLMN信息存储在一个文件或系统设置中，后续再次使用应用时，则重新获取PLMN信息，与首次存储的PLMN信息进行匹配，进而判断SIM卡是否做过变更。
 
样例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">sim </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.TelephonyKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
<em> </em><em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">先获取首次存储</span>PLMN<span style="color: rgb(128,128,128);">号</span></em>
  <span style="color: rgb(0,0,255);">plmn</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'xxxxxxxxxxx'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">getSimOperatorNumeric</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">SIM</span><span style="color: rgb(128,128,128);">卡</span><span style="color: rgb(128,128,128);">PLMN</span><span style="color: rgb(128,128,128);">号</span></em>
    <span style="color: rgb(0,0,255);">sim</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSimOperatorNumeric</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`err: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> ,PLMN</span><span style="color: rgb(255,0,170);">号</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">plmn</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// SIM</span><span style="color: rgb(128,128,128);">卡未变更</span></em>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
       <em> </em><em><span style="color: rgb(128,128,128);">// SIM</span><span style="color: rgb(128,128,128);">卡已变更</span></em>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'getSimOperatorNumeric'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSimOperatorNumeric</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
