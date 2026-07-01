# Grid如何实现根据屏幕宽度自适应列数

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1465

#### 问题现象

如何实现一个能够上拉加载更多的Grid列表，并且可以根据不同的屏幕大小适配不同展示列数？
 
 

#### 背景知识

- [栅格容器组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)(GridRow)仅可以和[栅格子组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)(GridCol)在栅格布局场景中使用。栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。
- 可通过GridCol的span属性设置占用列数，xs、sm、md、lg分别对应不同栅格大小设备上栅格容器组件的栅格列数。

 
 

#### 解决方案

- 可以通过栅格布局来实现Grid组件对不同屏幕大小的适配，具体实现方式及示例代码如下：1. 配置栅格容器组件(GridRow)的columns参数，即设定栅格布局的列数，默认API version 20之前为12列。

2. 配置栅格子组件(GridCol)的span参数，设定不同栅格大小设备对应的栅格列数，可根据屏幕越大对应显示的列数越多来设定xs、sm、md、lg的值。

3. 通过[onScrollStop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onscrollstop9)回调，触发加载更多数据。

  
```text
let <span style="color: rgb(0,0,255);">tmpData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">=</span>
  <span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">7</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">11</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">13</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">17</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">19</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">21</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">22</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">23</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">25</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">26</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">27</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">28</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">29</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">GridRowAdaptiveColumnCount </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">tmpData</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">GridRow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">columns</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">gutter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">GridCol</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">span</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">xs</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">sm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">md</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">lg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">80</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0D5AF5'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onBreakpointChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">breakpoint</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">breakpoint</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`onAreaChange, oldValue: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, newValue: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollSnap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">snapAlign</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ScrollSnapAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">START</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">snapPagination</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">enableSnapToStart</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">enableSnapToEnd</span><span style="color: rgb(181,106,1);">: </span>true
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollStop</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Scroll Stop'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">tmpData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">tmpData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">concat</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tmpData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 在三种不同屏幕下的运行效果图如下：
手机设备下对应span参数值为sm，可显示两列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/IvZ83Nd1R-uZmp6DX-xZvA/zh-cn_image_0000002658964565.png?HW-CC-KV=V1&HW-CC-Date=20260701T041241Z&HW-CC-Expire=86400&HW-CC-Sign=BA161E4B03170CB0A99B93FAEFDB3469E690A94A3D89D2E5D830621210065A5A)

- 折叠屏设备下对应span参数值为md，可显示四列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Gb9rm8NzSZyuVJIVkW2GVw/zh-cn_image_0000002628605356.png?HW-CC-KV=V1&HW-CC-Date=20260701T041241Z&HW-CC-Expire=86400&HW-CC-Sign=0ECEB64D48F7A58EF78EBBDACAF6D36501636FD1E722E93FA234FE11AF5583B7)

- 平板设备下对应span参数值为lg，可显示六列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mWxjnUeXQEuAsMGvsj_6jA/zh-cn_image_0000002658844613.png?HW-CC-KV=V1&HW-CC-Date=20260701T041241Z&HW-CC-Expire=86400&HW-CC-Sign=65CE71E4264F5E0A3E2B7487071DCEA237D0B360ABA412EE0AFF2347EE4FBAF3)
