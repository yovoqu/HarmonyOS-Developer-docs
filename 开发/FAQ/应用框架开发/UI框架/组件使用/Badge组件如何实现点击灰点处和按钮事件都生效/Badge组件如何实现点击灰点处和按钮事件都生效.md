# Badge组件如何实现点击灰点处和按钮事件都生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1577

#### 问题现象

点击按钮蓝色部分才会响应点击事件，被灰点遮挡的部分点击无响应，如何实现点击灰点处和按钮事件都生效？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/e1Uvipy3RLuOLBkS635P0g/zh-cn_image_0000002658969083.png?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=052A62EB17C80159A3376B0E11180D5EFF5AF1E1043A3FB81725369DB2692FDD)

 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BadgeClickTest </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">badgeCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">80</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Badge</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">badgeCount</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">maxCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">99</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'20vp'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">badgeColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#ddd'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">badgeSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">+1'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">170</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">25 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">badgeCount </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0D5AF5'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bBuW0JoUSvuy4X3-OuBs3Q/zh-cn_image_0000002658849135.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=30C1C9500833C713E7837F46E58F4A6E8968507E7FF7CD6835BCF9F44134FE01)

 
 

#### 背景知识

- [Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)：信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

将按钮点击事件迁移至Badge组件，可以实现点击灰点处和按钮事件都生效。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BadgeClickTest </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">badgeCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">80</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Badge</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">badgeCount</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">maxCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">99</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'20vp'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">badgeColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#ddd'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">badgeSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">+1'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">170</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">25 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>// </em><em><span style="color: rgb(128,128,128);">将按钮点击事件迁移至</span><span style="color: rgb(128,128,128);">Badge</span><span style="color: rgb(128,128,128);">组件</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">badgeCount </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
