# 如何实现自定义UI单选功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-677

#### 问题现象

实现一个单选组件，要求：①绘制指示图标，②选中项需显示高亮状态。
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pgh2B1e6QyCCgQFDE8Q0oQ/zh-cn_image_0000002658914057.png?HW-CC-KV=V1&HW-CC-Date=20260730T072324Z&HW-CC-Expire=86400&HW-CC-Sign=5A0DA3FD1136E4212AE4C0410E28C4AC3C4B6C60C0132D220A2008B84AE60DAB)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/lNYZA2K7T2OyTwCcCkcLxg/zh-cn_image_0000002658794107.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072324Z&HW-CC-Expire=86400&HW-CC-Sign=054BD33DC0AD436F2B5673A6CEB0A867B1C31258457DB4A6B3107FF0066893BA)

 
 

#### 背景知识

- [Polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon)：多边形绘制组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

采用Stack容器实现层叠布局，通过@State变量控制Polygon绘制的三角形指示图标显示与隐藏状态，结合条件渲染，实现选中时的高亮切换效果。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RadioPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">select</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'SELECT_OPTION_1'</span><span style="color: rgb(181,106,1);">; </span><em>// SELECT_OPTION_1</em><em><span style="color: rgb(128,128,128);">为选项一，</span><span style="color: rgb(128,128,128);">SELECT_OPTION_2</span><span style="color: rgb(128,128,128);">为选项二</span></em>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">commonUI</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">selectValue</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">imageUrl</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">imageUrl</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">150</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">select </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">selectValue </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(132,63,161);">'#ff5892de' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ffc4cac7' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">根据</span><span style="color: rgb(128,128,128);">select</span><span style="color: rgb(128,128,128);">变量判断选中的</span><span style="color: rgb(128,128,128);">border</span><span style="color: rgb(128,128,128);">颜色</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">select </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">selectValue</span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(132,63,161);">'#ff5892de' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ffc4cac7'</span><span style="color: rgb(255,0,170);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">根据</span><span style="color: rgb(128,128,128);">select</span><span style="color: rgb(128,128,128);">变量判断选中的</span><span style="color: rgb(128,128,128);">backgroundColor</span><span style="color: rgb(128,128,128);">颜色</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>

      if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">select </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">selectValue</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">三角形指示图标</span></em>
        <span style="color: rgb(0,0,255);">Polygon</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">points</span><span style="color: rgb(255,0,170);">([[</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">]])</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ff5892de'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">select </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">selectValue</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SpaceBetween </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">选项一</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">commonUI</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'SELECT_OPTION_1'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">选项一</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">选项二</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">commonUI</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'SELECT_OPTION_2'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">选项二</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
