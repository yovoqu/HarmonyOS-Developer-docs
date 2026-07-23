# 如何解决Scroll组件设置高度限制后，无法顶部对齐的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-725

#### 问题现象

在实现滚动列表效果时，由于加载的数据数量不确定，比如购物车场景时。需要实现在数据较多时列表能正常滚动，数据较少时，数据能从顶部开始排布。但是当Scroll组件设置layoutWeight属性时，如果数据较少，Scroll居中排布，无法实现顶部对齐效果。不设置layoutWeight属性时数据少可以实现顶部对齐，但是数据过多时会导致数据展示不全。即：Scroll组件设置高度与不设置高度会产生不同的排布效果。项目结构如下：
 
```text
<span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">()</span>
  <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/OpqOi6hLTJupYx4UAL70eg/zh-cn_image_0000002658794587.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012605Z&HW-CC-Expire=86400&HW-CC-Sign=3D02DD3A2367E6F002A5AE794C63052B5275E309D493578BE87D5CA1087E383E)

 
 

#### 背景知识

- [Scroll组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：该组件是可滚动的容器组件，当子组件的布局尺寸超过Scroll组件的尺寸时，内容可以滚动。同时，若子组件的布局尺寸小于Scroll组件的尺寸时，则Scroll组件不可滚动，且默认居中排布。
- [align](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#align)：该属性是组件的通用位置设置属性，可以设置组件内子组件的排布方式，其参数枚举详见：[Alignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#alignment)。
- [layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)：该属性为组件的通用属性，用于设置组件的布局权重，使用该属性的组件在父容器（Row/Column/Flex）的主轴方向按照各子组件的layoutWeight属性参数大小的比值分配父组件剩余尺寸。

 
 

#### 问题定位

针对Scroll组件设置高度与不设置高度会产生不同的排布效果的分析如下（Scroll组件为深灰色）：
 
- Scroll未设置layoutWeight时：若此时没有设置Scroll组件的其它高度限制，比如.height属性，则Scroll组件会自适应内部子组件的总高度（最高为屏幕显示高度，也就是0~100%的高度）。此时若是Scroll的父组件为[Column组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)，由于Column组件默认自上而下排布，所以Scroll组件会从Column的顶部开始布局。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/umSgjkZRQFOc5bigWjbn1w/zh-cn_image_0000002628555220.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012605Z&HW-CC-Expire=86400&HW-CC-Sign=72945979A4A6FA85CF77F2006D5171940F20D900DE93F559AABE416A38244C36)


  由图片现象可知，Scroll组件没有高度限制时，高度随子组件高度变化。当Scroll背景颜色与页面背景颜色一致时，布局满足列表从顶部开始排列。但是数据过多时，由于Scroll组件高度会被子组件撑到屏幕高度的100%，若Scroll组件上方有其它兄弟组件，会导致Scroll展示不全，底部被挤出显示区。滚动列表展示不全的相关问题可参考行业常见问题：[List展示不全](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1126)。

  
> [!NOTE]
> Scroll未设置高度限制时，顶部对齐效果是Scroll组件从父组件Column组件顶部开始布局，并不是Scroll子组件从Scroll顶部开始布局。


 
- Scroll设置layoutWeight时：此时相当于给了Scroll组件的高度限制，其高度为父组件除去其它子组件后的剩余高度。Scroll子组件的布局尺寸小于Scroll组件的尺寸时，其子组件默认居中排布，问题复现如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/_pjcAcQIT4e_Nsay93R-ww/zh-cn_image_0000002658914541.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012605Z&HW-CC-Expire=86400&HW-CC-Sign=401E91C10176BA3AE7E73E81FBF17BDB7D06C678A44E121A1B2BCF496F64DB8F)


  由图片现象可知，Scroll组件设置高度限制后，当其内数据较少时，默认居中排布。

 
 

#### 分析结论

Scroll组件需要设置高度限制，否则若Scroll背景颜色与页面背景颜色不一致时，会有显示问题，且若Scroll上方存在兄弟组件，Scroll组件过高时会展示不全。当设置Scroll组件高度后，可以通过设置.align(Alignment.Top)属性实现Scroll子组件顶部排布效果。
 
 

#### 修改建议

通过以下方式可实现列表数据较少时顶部对齐，数据较多时可滚动的效果：
 
- **方案一**：Scroll组件设置高度限制，同时增加.align(Alignment.Top)属性。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">SceneOne </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'6'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'7'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'8'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'9'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'10'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'11'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'12'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'13'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">我是标题，点击我更新数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">点击刷新数据</span></em>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2 </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2 </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">数据</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Top</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// Scroll</span><span style="color: rgb(128,128,128);">组件内部子组件按照顶部开始排列</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// Scroll</span><span style="color: rgb(128,128,128);">组件自动占满父组件剩余部分</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案二**：可以采用List组件实现。

  [List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)在限制过高度后，当其子组件高度小于List组件高度时，默认从顶部开始排布。参考方案一，核心修改代码如下：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">SceneTwo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'6'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'7'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'8'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'9'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'10'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'11'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'12'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'13'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">我是标题，点击我更新数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>// </em><em><span style="color: rgb(128,128,128);">点击刷新数据</span></em>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2 </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2 </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">数据</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(255,0,170);">}</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">6</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'95%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// List</span><span style="color: rgb(128,128,128);">组件自动占满父组件剩余部分</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 总结
1. Scroll组件在未设置高度时，其高度跟随子组件高度自适应。可以实现数据量少时，数据从顶部开始排列，但是数据较多时，Scroll组件会默认撑开到屏幕的100%高度，当Scroll上方有其它兄弟组件时，会出现Scroll显示不全的问题。
2. 当Scroll组件设置高度限制后，若子组件高度小于Scroll组件高度，则默认居中排布，可以采用.align(Alignment.Top)通用属性使其从顶部开始排布。
3. 由于List组件在设置高度限制后，若子组件高度小于List组件高度时是默认从顶部开始排布，所以也可以用List组件替代Scroll组件。
