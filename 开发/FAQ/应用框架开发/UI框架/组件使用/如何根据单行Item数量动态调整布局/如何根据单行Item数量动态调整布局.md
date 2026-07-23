# 如何根据单行Item数量动态调整布局

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-674

#### 问题现象

如何使用Grid组件实现布局只有一行，宽度固定，横向排列，当Item数量小于5时，Item宽度按照数量均分，当Item数量大于5时指定宽度且横向可以滚动的效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/I4wuIlR5Ss6BzPr1j81tcw/zh-cn_image_0000002658913891.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012555Z&HW-CC-Expire=86400&HW-CC-Sign=72F596CA0A31ABBE397223EDD57A84B9CC1621E6EC2F6AABDD4D2A74F26B4FD4)

 
 

#### 背景知识

- [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
- [rowsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#rowstemplate)：设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。
- [columnsGap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#columnsgap)：设置列与列的间距。设置为小于0的值时，按默认值显示。
- [display.getDefaultDisplaySync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)：获取当前默认的[display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)对象。
- [px2vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12)：将px单位的数值转换为以vp为单位的数值。

 
 

#### 解决方案

获取当前屏幕的宽度，当Item数量大于5时，Item宽度指定为100vp，当Item数量小于5时，动态设置Item宽度。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">display </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">HorizontalIndex </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">screenWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">6</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">7</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">display.getDefaultDisplaySync()</span><span style="color: rgb(128,128,128);">方法获取当前屏幕宽度</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">screenWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDefaultDisplaySync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getItemWidth</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当</span><span style="color: rgb(128,128,128);">Item</span><span style="color: rgb(128,128,128);">数量大于</span><span style="color: rgb(128,128,128);">5</span><span style="color: rgb(128,128,128);">时，宽度指定为</span><span style="color: rgb(128,128,128);">100</span></em>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return <span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当</span><span style="color: rgb(128,128,128);">Item</span><span style="color: rgb(128,128,128);">数量小于</span><span style="color: rgb(128,128,128);">5</span><span style="color: rgb(128,128,128);">时，</span><span style="color: rgb(128,128,128);">Item</span><span style="color: rgb(128,128,128);">宽度按照数量均分</span></em>
      return <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">screenWidth </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Grid</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">GridItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getItemWidth</span><span style="color: rgb(255,0,170);">())</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置当前网格布局行的数量为</span><span style="color: rgb(128,128,128);">1</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rowsTemplate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'1fr'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置列与列的间距为</span><span style="color: rgb(128,128,128);">10</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">columnsGap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#fafafa'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">数量改变</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
