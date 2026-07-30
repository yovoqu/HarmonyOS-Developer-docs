# 解决Slider精度问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1280

#### 问题现象

Slider组件，step设置为0.1时，滑动时显示的value不是正常的35.1、35.2、35.3，而是35.70000076293945、36.400001525878906这类数值，如何解决？
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Question </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">textTimerController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextTimerController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextTimerController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">35</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">34.5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">43.1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OutSet</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">step</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.1</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showTips</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/dKgBOfWTSn6WUObdpDPC1w/zh-cn_image_0000002628757874.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072349Z&HW-CC-Expire=86400&HW-CC-Sign=F1B670D26D5CD6DA584654EA4EA3516E2E6C600E532C10319CF30EF9D3210D95)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6fpeuVJyR2OQYhZeITk6Sg/zh-cn_image_0000002658957189.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072349Z&HW-CC-Expire=86400&HW-CC-Sign=CF976F392087D466FF6D834F2D238EB91652A005755F6DDBFCBBCC28D383FF7D)

 
 

#### 背景知识

[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-slider)：滑动条组件，用来快速调节设置值，如音量、亮度等。
 
 

#### 解决方案

浮点数在计算机中是通过二进制形式存储的，某些十进制浮点数在二进制中无法精确表示，导致了运算结果的精度问题。
 1. 使用toFixed(3)将数值转换为十进制定点模式表示的字符串，并保留小数点后3位。
2. 使用slice(0, -1)截取字符串。
3. 使用parseFloat返回一个新的浮点数，并展示。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextTimerExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">textTimerController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextTimerController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextTimerController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">35</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">34.5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">43.1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OutSet</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">step</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.1</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parseFloat</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toFixed</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showTips</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tempLatrue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
