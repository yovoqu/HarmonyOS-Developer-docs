# SegmentButton如何设置点击回调事件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1142

#### 问题现象

SegmentButton如何设置点击回调事件来监听当前点击的Tab？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ydMMVG19SyuxCeX8HIRK1g/zh-cn_image_0000002628409706.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012703Z&HW-CC-Expire=86400&HW-CC-Sign=4D42842BDA179D1D82661AE7240DAE226347EC0A4003FF03678840D0D0A140FE)

 
 

#### 背景知识

- [SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)为分段按钮组件，包含页签类分段按钮、单选类分段按钮、多选类分段按钮。
- [@Watch装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)应用于对状态变量的监听。如果开发者需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。@Watch提供了状态变量的监听能力，@Watch仅能监听到可以观察到的变化。

 
 

#### 解决方案

使用@Watch装饰器设置onSegmentButtonChange回调函数，用于监听当前点击的Tab。
 
```text
import <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">ItemRestriction</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">SegmentButton</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">SegmentButtonOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">SegmentButtonTextItem</span>
<span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos.arkui.advanced.SegmentButton'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SegmentButtonClickCallback </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">tabOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SegmentButtonOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">SegmentButtonOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tab</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">buttons</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">页签按钮</span><span style="color: rgb(132,63,161);">1' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">页签按钮</span><span style="color: rgb(132,63,161);">2' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">页签按钮</span><span style="color: rgb(132,63,161);">3'</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">] </span>as <span style="color: rgb(181,106,1);">ItemRestriction</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">SegmentButtonTextItem</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BACKGROUND_THICK</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">tf</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State @Watch</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'onSegmentButtonChange'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">tabSelectedIndexes</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onSegmentButtonChange</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tf </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tf</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">选中按钮索引</span><span style="color: rgb(132,63,161);"> -- </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabSelectedIndexes</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">25 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">SegmentButton</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabOptions</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">selectedIndexes</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">$tabSelectedIndexes</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabSelectedIndexes</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">` </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tf</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
