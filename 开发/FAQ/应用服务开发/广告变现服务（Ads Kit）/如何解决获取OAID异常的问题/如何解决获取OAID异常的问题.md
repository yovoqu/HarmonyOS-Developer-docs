# 如何解决获取OAID异常的问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ads-3

#### 问题现象

获取OAID会遇到以下常见的问题，应该如何解决？
 
- 调用identifier.getOAID获取到的OAID值是00000000-0000-0000-0000-000000000000，且没有授权弹窗。
- 调用identifier.getOAID接口报错。

 
 

#### 背景知识

[OAID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/oaid-service#获取oaid信息)是一种非永久性设备标识符，基于开放匿名设备标识符，可在保护用户个人数据隐私安全的前提下，向用户提供个性化广告，同时三方监测平台也可以向广告主提供转化归因分析。OAID的获取方式参考[identifier.getOAID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid#identifiergetoaid)。
 
 

#### 问题定位
1. 应用是否正确的配置了ohos.permission.APP_TRACKING_CONSENT权限。
2. 应用是否开启“跨应用关联访问权限”。
3. 应用授权弹窗是否点击确认。
 
 

#### 分析结论

针对identifier.getOAID获取异常的问题，主要有以下几种可能的原因：
 1. 应用未在当前模块的module.json5文件中配置ohos.permission.APP_TRACKING_CONSENT权限。
2. 应用配置了ohos.permission.APP_TRACKING_CONSENT权限，但是“跨应用关联访问权限”设置为“禁止”。
3. 应用配置了ohos.permission.APP_TRACKING_CONSENT权限，但在弹窗提示用户授权时，用户未选择手动授权。
 
 

#### 修改建议
1. 配置相关权限：在应用的module.json5文件中添加ohos.permission.APP_TRACKING_CONSENT权限配置。确保该权限被正确声明，以便应用能够请求获取OAID的权限。该权限为user_grant权限，当申请的权限为user_grant权限时，reason，abilities标签必填，具体申请方式请参见[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。
2. 跨应用关联访问权限：可以通过在应用内提供明确的指引或说明，引导用户前往设置-隐私安全-跨应用关联，手动开启允许“跨应用关联访问权限”，告知用户开启该权限的必要性和用途，以提高用户的授权意愿。比如通过代码跳转设置-隐私二级页面。
3. 用户手动授权：调用requestPermissionsFromUser接口弹窗，提示并引导用户允许对应权限。

  
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Want </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">identifier </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AdsKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">oaid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">jumpToSetting</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'com.huawei.hmos.settings'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'com.huawei.hmos.settings.MainAbility'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">uri</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'privacy_settings'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">parameters</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
<em>        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传对应应用的包名</span></em>
        <span style="color: rgb(255,255,255);">pushParams</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'com.example.myapplication'</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">requestOAIDTrackingConsentPermissions</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Context</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进入页面时，向用户请求授权广告跨应用关联访问权限</span></em>
    const <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AtManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAtManager</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestPermissionsFromUser</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'ohos.permission.APP_TRACKING_CONSENT'</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">authResults</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'succeeded in requesting permission'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">identifier</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getOAID</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`get oaid failed, error: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">oaid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`succeeded in getting oaid by callback , oaid: </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">oaid</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'user rejected'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`request permission failed, error: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`catch err-</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">跳转设置</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">jumpToSetting</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">获取</span><span style="color: rgb(132,63,161);">oaid'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestOAIDTrackingConsentPermissions</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">oaid</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
 

#### 常见FAQ

Q：如何分辨接口异常是权限问题导致的？
 
A：一些常见的Kit（比如推送服务、地图服务等）需要在AppGallery Connect网站上先开通服务并完成[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)，或者在项目中需要配置相应的权限（可参考[申请应用权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-app-permissions)），因此需要先确认集成的Kit是否需要配置这些权限，在开发之前应该做好相应的开发准备，确保不会因为权限问题阻塞开发。
