# PersistentStorage持久化数据无法删除

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-752

#### 问题现象

当用户登录时，会使用PersistentStorage进行部分数据的存储，当用户退出登录或切换账号时需要清除该数据，如何正确的删除数据？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/SNj4Fj5AQjK7ceRJBoI-9w/zh-cn_image_0000002658794737.png?HW-CC-KV=V1&HW-CC-Date=20260723T012609Z&HW-CC-Expire=86400&HW-CC-Sign=B156231FC3F921F1171E66965C16FC134ACCCCE1DF6B85CABA99969DF912F903)

 
 

#### 背景知识

- [PersistentStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage)用于实现持久化数据存储的模块。它提供了在设备本地持久化存储和读取数据的功能，适用于需要保存用户数据、应用状态、配置信息等场景。
- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)：PersistentStorage提供状态变量持久化的能力，但是其持久化和读回UI的能力都需要依赖AppStorage。

 
 

#### 解决方案
1. 可以使用[deleteProp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management#deleteprop10)将key对应的属性从PersistentStorage中删除，需要注意的是这样删除的是持久化中的用户数据，应用中的数据依旧存在，需要用户退出应用重新进入才能看出删除的效果。如果在应用不退出的前提删除数据。
```text
<span style="color: rgb(255,255,255);">PersistentStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">persistProp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'P'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'123'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TestCase6 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">PersistentStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deleteProp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'P'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">delete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'P'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">已删除持久化中的数据</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除持久化数据</span><span style="color: rgb(132,63,161);">P'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">查看</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          let <span style="color: rgb(255,255,255);">appData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'P'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">输出：</span><span style="color: rgb(132,63,161);">appData'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">appData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 如果当前有页面使用@StorageLink的属性，AppStorage.delete就无法删除。可以改成AppStorage.link的形式，删除应用数据前可以取消订阅。
```text
<span style="color: rgb(255,255,255);">PersistentStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">persistProp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'123456'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Test </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">linkToId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SubscribedAbstractProperty</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">link</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">uid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">linkToId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">应用中当前</span><span style="color: rgb(132,63,161);">id</span><span style="color: rgb(132,63,161);">的值：</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uid</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除本地持久化的数据</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">删除持久化的数据后，应用中的数据还存在，需要退出应用才能看到效果</span></em>
          <span style="color: rgb(255,255,255);">PersistentStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deleteProp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">已删除持久化中的数据</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">取消</span><span style="color: rgb(132,63,161);">linkToId'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">linkToId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aboutToBeDeleted</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除应用中的状态变量</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果没有订阅者，则删除成功</span></em>
          let <span style="color: rgb(255,255,255);">flag </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">delete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'id'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">flag</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除应用状态变量成功</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">删除应用状态变量失败</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
