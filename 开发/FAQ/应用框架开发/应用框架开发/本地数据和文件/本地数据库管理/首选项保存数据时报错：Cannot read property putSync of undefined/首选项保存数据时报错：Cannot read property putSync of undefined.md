# 首选项保存数据时报错：Cannot read property putSync of undefined

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-58

#### 问题现象

运行问题代码后闪退，日志如下：
 
```text
<span style="color: rgb(255,255,255);">Pid</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">8619</span>
<span style="color: rgb(255,255,255);">Uid</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">20020045</span>
<span style="color: rgb(255,255,255);">Reason</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">TypeError</span>
<span style="color: rgb(255,255,255);">Error name</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">TypeError</span>
<span style="color: rgb(255,255,255);">Error message</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">Cannot read property putSync of </span>undefined
<span style="color: rgb(255,255,255);">Stacktrace</span><span style="color: rgb(181,106,1);">:</span>
  <span style="color: rgb(255,255,255);">at </span><span style="color: rgb(0,0,255);">saveData </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">entry</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">main</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">ets</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">pages</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">Index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ets</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">71</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,255,255);">  at </span><span style="color: rgb(0,0,255);">anonymous </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">entry</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">main</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">ets</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">pages</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,255,255);">Index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ets</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">41</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">11</span><span style="color: rgb(255,0,170);">)</span>
```
 
 
问题代码示例参考如下：
 
```ArkTS
<em>// index.ets</em>

import <span style="color: rgb(0,0,255);">Prompt </span>from <span style="color: rgb(255,0,170);">'@system.prompt'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">preferences </span>from <span style="color: rgb(255,0,170);">'@ohos.data.preferences'</span><span style="color: rgb(181,106,1);">;</span>


let <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Preferences</span>
class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Options </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'myStore' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">dataPreferences </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPreferencesSync</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">savedText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这里将显示保存的内容</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>


  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输入框</span></em>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入要保存的内容</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <em>// </em><em><span style="color: rgb(128,128,128);">保存按钮</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">保存数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">saveData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">显示保存内容的按钮</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">显示保存内容</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">显示保存内容的文本区域</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">savedText</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保存数据到</span><span style="color: rgb(128,128,128);">Preferences</span></em>
  private <span style="color: rgb(0,0,255);">saveData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if<span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText </span><span style="color: rgb(181,106,1);">== </span>null<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Prompt</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">内容为空请重试</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      return
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">putSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'my'</span><span style="color: rgb(181,106,1);">,</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flush</span><span style="color: rgb(0,0,255);">()</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从</span><span style="color: rgb(128,128,128);">Preferences</span><span style="color: rgb(128,128,128);">加载数据</span></em>
  private <span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">get_text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'my'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">'6666'</span><span style="color: rgb(0,0,255);">)</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">savedText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">get_text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 

#### 背景知识

- [通过用户首选项实现数据持久化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences)：用户首选项(Preferences)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。
- 首选项实例可见[demo](https://gitee.com/harmonyos_samples/preferences)。

 
 

#### 问题定位
1. 根据报错信息‘Cannot read property putSync of undefined’和报错代码行‘at saveData (entry/src/main/ets/pages/Index.ets:71:5)’，可定位至saveData()方法中的putSync属性未找到。
2. putSync是dataPreferences的方法，dataPreferences的实例化是在class文件entryAbility进行调用的。检查代码后发现主程序没有关于entryAbility的调用链，即dataPreferences未实例化。
 
 

#### 分析结论

dataPreferences未实例化导致报错。
 
 

#### 修改建议

在主程序中添加异步方法aboutToAppear()方法，并在里面进行Preferences实例化：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">promptAction </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">preferences </span>from <span style="color: rgb(255,0,170);">'@ohos.data.preferences'</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Preferences</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">savedText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这里将显示保存的内容</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">Context</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Options </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'myStore' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">dataPreferences </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">preferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPreferencesSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输入框</span></em>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入要保存的内容</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

 <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保存按钮</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">保存数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">saveData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">显示保存内容的按钮</span></em>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">显示保存内容</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">显示保存内容的文本区域</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">savedText</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保存数据到</span><span style="color: rgb(128,128,128);">Preferences</span></em>
  private <span style="color: rgb(0,0,255);">saveData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText </span><span style="color: rgb(181,106,1);">== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">内容为空请重试</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">putSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'my'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flush</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从</span><span style="color: rgb(128,128,128);">Preferences</span><span style="color: rgb(128,128,128);">加载数据</span></em>
  private <span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">get_text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">dataPreferences</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'my'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'6666'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">savedText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">get_text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：dataPreferences存储后的文件路径在哪里？
 
A：dataPreferences实际上是一个xml文件，位置放在data/app/el2/100/base/&lt;包名&gt;/haps/entry/preferences目录下。可以在IDE右下角，点击Device File Browser，找到文件路径。
