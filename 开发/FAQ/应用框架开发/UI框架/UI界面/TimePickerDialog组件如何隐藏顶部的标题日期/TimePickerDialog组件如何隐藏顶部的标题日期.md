# TimePickerDialog组件如何隐藏顶部的标题日期

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1226

#### 问题现象

TimePickerDialog组件标题的日期如何才能隐藏？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/5LEizWLuT2uJusBqFmkRUA/zh-cn_image_0000002658953237.gif?HW-CC-KV=V1&HW-CC-Date=20260723T013123Z&HW-CC-Expire=86400&HW-CC-Sign=381FABC949CC7359A17ACCE6EE01455D1271A608C6B95C4E3EEBF969D45001B4)

 
 

#### 背景知识

- 开发者可根据24小时的时间区间，创建时间滑动选择器弹窗[TimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-fixes-style-dialog#时间滑动选择器弹窗-timepickerdialog)，将时间信息清晰地展示在弹出的窗口上。组件顶部标题默认是当日日期，可以通过selected属性来更改日期。
- [CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)通过CustomDialogController类显示自定义弹窗。
- [TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker)为时间选择组件，可以根据指定参数创建选择器，支持选择小时及分钟。TimePicker除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持设置[useMilitaryTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#usemilitarytime)、[disappearTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#disappeartextstyle10)、[textStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#textstyle10)等属性。

 
 

#### 解决方案

TimePickerDialog属于固定样式弹出框，采用固定的布局格式，暂不支持直接隐藏标题的日期，可在自定义弹窗CustomDialog中加入TimePicker来实现。
 
```json
<span style="color: rgb(181,106,1);">@CustomDialog</span>
struct <span style="color: rgb(0,0,255);">CustomDialogExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">CustomDialogController</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">cancel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TimePicker</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TimePickerResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hour </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'select current date is: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">disappearTextStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">font</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Lighter </span><span style="color: rgb(181,106,1);">} }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">font</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal </span><span style="color: rgb(181,106,1);">} }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedTextStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">font</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bolder </span><span style="color: rgb(181,106,1);">} }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TestPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">null </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CustomDialogExample</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">cancel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onCancel</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAccept</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">cancel</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">existApp</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">onWillDismiss</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DismissDialogAction</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'reason:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,255,255);">DismissReason</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PRESS_BACK</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dismiss</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,255,255);">DismissReason</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">TOUCH_OUTSIDE</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dismiss</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">customStyle</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">cornerRadius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在自定义组件即将析构销毁时将</span><span style="color: rgb(128,128,128);">dialogController</span><span style="color: rgb(128,128,128);">置空</span></em>
  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogController </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">dialogController</span><span style="color: rgb(128,128,128);">置空</span></em>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onCancel</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Callback when the first button is clicked'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onAccept</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Callback when the second button is clicked'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">existApp</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Click the callback in the blank area'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'click me'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogController </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">open</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0x317aff)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：TimePickerDialog时间滑动选择器弹窗如何显示24小时制？
 
A：TimePickerDialog默认为12小时制，可通过将useMilitaryTime属性设置为true，将展示时间显示为24小时制。
