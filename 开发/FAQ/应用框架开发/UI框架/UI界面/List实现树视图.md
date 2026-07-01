# List实现树视图

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-758

#### 问题现象

列表如何实现树视图折叠交互，并支持展开/折叠父项查看子项？示例图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/xCZdCvrgQy6jVjz_wAZIdg/zh-cn_image_0000002658795051.png?HW-CC-KV=V1&HW-CC-Date=20260701T041139Z&HW-CC-Expire=86400&HW-CC-Sign=72F9F0E093A03F405990EDEDDF92299315115D9C65F6268BAF97541A374AF39F)

 
 

#### 背景知识

[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)列表是一种容器组件，包含一系列相同宽度的列表项，[ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)是构成列表的基础单位，用来展示列表具体内容。
 
 

#### 解决方案

- **方案一**：1. 通过List与ListItem搭建标准化垂直列表架构，每个列表项均作为独立单元参与布局。

2. 借助[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)实现列表项内的纵向层级堆叠。

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ListTest </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">7</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isContentShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">selectItem</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">warn</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'no uiContext'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">initialIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isContentShow </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectItem </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">收起</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">展开</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
                      <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">,</span>
                      <span style="color: rgb(0,0,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'animation end'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">                    }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isContentShow </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isContentShow</span><span style="color: rgb(181,106,1);">;</span>
                      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectItem </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">;</span>
                    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceBetween</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

              if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isContentShow </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectItem </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这是内容区域</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0xFFFFFF)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0xF1F3F5)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/kNbgKl7WQb6x_aYvFla_Qg/zh-cn_image_0000002628555684.png?HW-CC-KV=V1&HW-CC-Date=20260701T041139Z&HW-CC-Expire=86400&HW-CC-Sign=959195F10814190B67EEAB7FDBA499329FC11AE0770CCFB7D4A877C591315D0C)

- **方案二**：

  参考[TreeView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeview)，作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">TreeController</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TreeView </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">treeController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TreeController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TreeController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">clickId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">treeController</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">secondaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'2'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">项目</span><span style="color: rgb(255,0,170);">1_1'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">项目</span><span style="color: rgb(255,0,170);">1_2'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">项目</span><span style="color: rgb(255,0,170);">2'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">3'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">secondaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'0'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">35</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">3-1'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">secondaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'0'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">33</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">4'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">secondaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'0'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">parentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">33</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">currentNodeId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">34</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isFolder</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">primaryTitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">项目</span><span style="color: rgb(255,0,170);">5'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buildDone</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">treeController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refreshNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">父节点</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">子节点</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">SideBarContainer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">SideBarContainerType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Embed</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">TreeView</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">treeController</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">treeController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sideBarWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showControlButton</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showSideBar</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/IGMME5YXQx2ICj_jtKGMVA/zh-cn_image_0000002658915007.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041139Z&HW-CC-Expire=86400&HW-CC-Sign=809F1F00FB36527AE3D7321704F39A3D546A9424EC27902B56E42B0729C22BA3)
