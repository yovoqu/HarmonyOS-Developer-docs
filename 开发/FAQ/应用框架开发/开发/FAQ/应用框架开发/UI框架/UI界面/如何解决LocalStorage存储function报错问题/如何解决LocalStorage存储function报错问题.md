# 如何解决LocalStorage存储function报错问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1265

#### 问题现象

使用LocalStorage传递function报错：
 
```text
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">message</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">Component </span><span style="color: rgb(255,0,170);">'owning @Component UNKNOWN'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Illegal variable value error </span>with <span style="color: rgb(0,0,255);">decorated variable </span>undefined <span style="color: rgb(255,0,170);">'clickSend'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">failed </span><span style="color: rgb(181,106,1);">validation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'undefined, null, number, boolean, string, or Object but not function, not V2 @ObservedV2 / @Trace class, and makeObserved return value either, attempt to assign value type: '</span><span style="color: rgb(0,0,255);">function</span><span style="color: rgb(255,0,170);">', value: '</span>undefined'<span style="color: rgb(181,106,1);">!</span>
```
 
关键问题参考如下：
 
```text
function <span style="color: rgb(0,0,255);">openCommentsInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">hintMsg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LocalStorage </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">LocalStorage</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'title'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'hintMsg'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">hintMsg</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'clickSend'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">程序崩溃，报错</span></em>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)是页面级的UI状态存储，存储的类型有所限制。
 
 

#### 问题定位

查看以下报错日志的关键信息可知，clickSend是非法变量值，支持undefined、null、number、boolean、string、Object等类型，但不支持function函数类型变量。
 
```text
<span style="color: rgb(0,0,255);">Illegal variable value error </span>with <span style="color: rgb(0,0,255);">decorated variable </span>undefined <span style="color: rgb(255,0,170);">'clickSend'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">failed </span><span style="color: rgb(181,106,1);">validation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'undefined, null, number, boolean, string, or Object but not function ...'</span>
```
 
 

#### 分析结论

LocalStorage不支持存储function函数类型变量。
 
 

#### 修改建议

使用类class将函数function进行封装为Object对象，LocalStorage支持存储Object对象。
 
```text
let <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LocalStorage </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">LocalStorage</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">openCommentsInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">hintMsg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">object</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'title'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'hintMsg'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">hintMsg</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'clickSend'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">class</span><span style="color: rgb(128,128,128);">对</span><span style="color: rgb(128,128,128);">function</span><span style="color: rgb(128,128,128);">进行一层封装</span></em>
class <span style="color: rgb(0,0,255);">MyFunc </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">需要保存至</span><span style="color: rgb(128,128,128);">LocalStorage</span><span style="color: rgb(128,128,128);">的函数</span></em>
function <span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">storage</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">LocalStorageDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@LocalStorageLink</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'clickSend'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">myFunc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">object </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">LocalStorage</span><span style="color: rgb(128,128,128);">中存储的</span><span style="color: rgb(128,128,128);">clickSend</span><span style="color: rgb(128,128,128);">对象</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">向</span><span style="color: rgb(255,0,170);">storage</span><span style="color: rgb(255,0,170);">保存数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">myFunc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MyFunc </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MyFunc</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">myFunc</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clickSend </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将要保存的函数封装在</span><span style="color: rgb(128,128,128);">class</span><span style="color: rgb(128,128,128);">对象中</span></em>
          <span style="color: rgb(0,0,255);">openCommentsInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'title'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'hintMsg'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">myFunc</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">class</span><span style="color: rgb(128,128,128);">对象保存至</span><span style="color: rgb(128,128,128);">LocalStorage</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">读取</span><span style="color: rgb(255,0,170);">storage</span><span style="color: rgb(255,0,170);">的数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">tmp </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">myFunc </span>as <span style="color: rgb(0,0,255);">MyFunc</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">Object</span><span style="color: rgb(128,128,128);">对象转为</span><span style="color: rgb(128,128,128);">MyFunc</span><span style="color: rgb(128,128,128);">类</span></em>
          <span style="color: rgb(0,0,255);">tmp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clickSend</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">读取</span><span style="color: rgb(255,0,170);">storage</span><span style="color: rgb(255,0,170);">的数据成功</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">MyFunc</span><span style="color: rgb(128,128,128);">中的</span><span style="color: rgb(128,128,128);">clickSend</span><span style="color: rgb(128,128,128);">函数</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
运行截图如下：成功调用LocalStorage中存储的类对象的函数来打印数据。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Rnc9X2JTSiqZceAQrXHGoQ/zh-cn_image_0000002658835373.png?HW-CC-KV=V1&HW-CC-Date=20260811T005713Z&HW-CC-Expire=86400&HW-CC-Sign=8FD86F27B124CF0190ED576C201BA9D7A547DA38704202C4AA9AEF6BFF6651D7)
