# 如何实现组件RTL方向排列与滑动效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-671

#### 问题现象

List组件横向排列，要求RTL方向排列与滑动并且内容靠右显示，该如何实现？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/UOiFOD9ERFC6jZFZjJNGlg/zh-cn_image_0000002628554564.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041308Z&HW-CC-Expire=86400&HW-CC-Sign=64F57D485007453CCC1DD449DE488A0531D8DF89F246DA73C26CF40E39C2E26B)

 
 

#### 背景知识

- RTL：[布局](https://developer.huawei.com/consumer/cn/doc/design-guides/design-globalization-0000001748539688#section18548122665310)中的RTL（Right to Left，从右到左）语言的普遍特征有：事件发展顺序从右到左进行。
- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
- [listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)：设置List组件排列方向。
- initialIndex：[ListOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listoptions18对象说明)中的initialIndex用于设置当前List初次加载时显示区域起始位置的item索引值。
- [scrollSnapAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#scrollsnapalign10)：设置列表项滚动结束对齐效果。

 
 

#### 解决方案

设置List组件listDirection属性使之横向排列，使用reverse()方法将数据源反向排列，设置initialIndex参数使数据从最后一位开始显示可使组件RTL方向排列与滑动，最后通过设置scrollSnapAlign属性即可实现使组件靠右显示效果。
 
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ListExample </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">scrollerForList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">页面加载时初始化数据</span></em>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">25</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>

     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始显示的列表项索引（从后往前显示）</span></em>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">initialIndex</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scrollerForList </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使数据源反向排列</span></em>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reverse</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#d5d5d5'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBarWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">chainAnimation</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Spring</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listDirection</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Axis</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Horizontal</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置组件横向排列</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">55</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollSnapAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ScrollSnapAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">END</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">视图中的最后一项将在列表末尾对齐。</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lanes</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
> [!NOTE]
> 在上述方案的基础上将初始显示的列表项索引去掉，给List组件设置 stackFromEnd 属性值为true也可实现以上效果。该属性从API version 19开始支持。

 
 

#### 常见FAQ

Q：当initialIndex设置为滚动列表最后一页的索引时，无法跳转过去，如何处理？
 
A：initialIndex属性用于设置List组件初次加载时视口起始位置显示的item的索引值。当List的元素是通过异步函数动态加载的时候，这个属性会失效，这是因为initialIndex只在List组件初次创建时考虑，一旦List的内容发生变化（如通过异步加载数据），initialIndex的设置就不会生效。
 
为了解决这个问题，可以在加载完所有数据后，使用[scrollToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolltoindex)方法手动滚动到期望的位置。这样，即使在List的内容动态变化后，也可以确保视图滚动到正确的位置。
 
Q：stackFromEnd是否是V2的属性？
 
A：[stackFromEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#stackfromend19)并非状态管理V1/V2中的属性，而是一个与布局相关的属性，用于列表组件控制布局方向。
 
 

#### 总结

实现此效果的关键在于将数据源反向排列，设置初始显示位置为最后一项数据。
