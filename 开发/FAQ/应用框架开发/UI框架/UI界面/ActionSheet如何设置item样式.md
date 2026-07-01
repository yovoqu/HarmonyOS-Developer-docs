# ActionSheet如何设置item样式

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1002

#### 问题现象

ActionSheet默认的item样式间距过小，不便于交互，如何设置item样式？
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ShowActionSheetExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'showActionSheet'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showActionSheet</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'ActionSheet title'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">cornerRadius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">borderStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BorderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Solid</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">asymmetric</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OPACITY</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Sharp </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">combine</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1.5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1.5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Sharp </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OPACITY</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Smooth </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">combine</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0.5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Smooth </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)))</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Confirm button'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Get Alert Dialog handled'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">sheets</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'apples'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'apples'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'bananas'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'bananas'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'pears'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pears'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span>
            <span style="color: rgb(0,0,255);">]</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9EIIahzkREC1mOkXjSEBDg/zh-cn_image_0000002658804039.png?HW-CC-KV=V1&HW-CC-Date=20260701T041137Z&HW-CC-Expire=86400&HW-CC-Sign=E56CF7621187DAD69E6BFCB2D6C406B92BF738AD1F641482604A1AFAF6820D5B)

 
 

#### 背景知识

- [列表选择器弹窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-action-sheet)适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时适用这种方案。
- 列表选择器弹窗通过UIContext中的[showActionSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showactionsheet)接口实现，可以通过修改配置width、height、transition等接口来自定义弹窗样式及弹出效果。

 
 

#### 解决方案

ActionSheet的item之间的间距过小，可以给ActionSheet每个item的title添加换行符来实现，具体可参考如下代码：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ShowActionSheetExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'showActionSheet'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showActionSheet</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">水果列表</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">以下为有货的水果</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">cornerRadius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">确认</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Get Alert Dialog handled'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">sheets</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">apples</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'apples'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">bananas</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'bananas'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">pears</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pears'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span>
            <span style="color: rgb(0,0,255);">]</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
