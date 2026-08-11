# 如何实现ListItem点击后居中显示的效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-576

#### 问题现象

如何利用List实现如下功能：
 1. 横向滚动导航栏支持点击切换。
2. 点击时自动滚动到目标位置。
3. 目标条目在容器中居中显示。
4. 动态高亮当前选中项。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/5QwFVpCoSKGRoj52qygFyw/zh-cn_image_0000002658911373.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005806Z&HW-CC-Expire=86400&HW-CC-Sign=5DD5C720C1FEFCD78F5BCCF719F7A35250D57458F6DE4AA26D7AA76B912F1B2F)

 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)是用于展示动态数据集合的核心组件，支持滚动、动态更新等特性。可以利用[listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)设置List组件排列方向。
- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)是一种可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [scrollToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolltoindex)：滑动到指定Index，支持设置滑动额外偏移量。

 
 

#### 解决方案
1. 定义一个CityList组件，包含一个Scroller和状态focusIndex。
2. 调用scrollToIndex()方法时，第三个参数传入[ScrollAlign.CENTER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollalign10枚举说明)，用来指定滚动对齐方式。
3. 每个标签项点击时会更新focusIndex并滚动到对应位置。
4. 根据focusIndex控制当前选中标签的背景色。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CityList </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listScroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">focusIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">allListString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'111'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'222'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'333'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'444'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'555'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'666'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'777'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'888'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'999'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">child</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tabName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">tabIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tabName</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">tabIndex</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listScroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollToIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tabIndex</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ScrollAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CENTER</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">tabIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">tabIndex </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">allListString</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">4 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tabIndex </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusIndex </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'#0088FF' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#F8F9F7'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listScroller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">allListString</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">child</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listDirection</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Axis</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Horizontal</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#FFF1F3'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignListItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ListItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
