# TextPicker组件如何禁止响应事件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-734

#### 问题现象

TextPicker组件如何禁止所有响应事件，或者禁止指定响应事件？
 
 

#### 背景知识

- [enabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable#enabled)：用于控制事件交互，值为true表示组件可交互，值为false表示组件不可交互。
- [onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)：用于自定义手势判定。

 
 

#### 解决方案
1. 禁止组件的全部响应事件，可以配置enabled属性值为false使TextPicker组件不可交互，不响应事件。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextPickerExample1 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">select</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'AAAAA'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'BBBBBBBBBBBBB'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'CCCC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'DDDDDDDD'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'EEE'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">range</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">selected</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(0,0,255);">[</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">]</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">核心代码：交互能力（</span><span style="color: rgb(128,128,128);">false</span><span style="color: rgb(128,128,128);">）</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/J9yH8ZgURXK_hwdbLJmQpQ/zh-cn_image_0000002658794593.png?HW-CC-KV=V1&HW-CC-Date=20260730T072327Z&HW-CC-Expire=86400&HW-CC-Sign=0C6E2BD5CFB2AC4564E35737E7A0B5762F468A5700BD43EFA0A2D21EB4ABCA04)

2. 禁止组件指定的响应事件，可以通过onGestureJudgeBegin自定义手势判定函数，自主决定是否响应。如下相关代码实现了当前TextPicker的选中项点击事件被禁止，而不影响对其他手势事件的响应。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextPickerExample2 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">select</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'AAAAA'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'BBBBBBBBBBBBB'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'CCCC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'DDDDDDDD'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'EEE'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">range</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">selected</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fruits</span><span style="color: rgb(0,0,255);">[</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">]</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">核心代码：判断是否为点击事件，使用长按做对比</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
          <span style="color: rgb(0,0,255);">LongPressGesture</span><span style="color: rgb(0,0,255);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'longPress1'</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置长按手势标志</span></em>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAction</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">长按</span><span style="color: rgb(255,0,170);">longPress'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">        )</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
          <span style="color: rgb(0,0,255);">TapGesture</span><span style="color: rgb(0,0,255);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'tap1'</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置点击手势标志</span></em>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAction</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">tap1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">        )</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onGestureJudgeBegin</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">gestureInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BaseGestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">gestureInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">GestureControl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GestureType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TAP_GESTURE</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">返回</span><span style="color: rgb(128,128,128);">REJECT</span><span style="color: rgb(128,128,128);">会使点击手势失败</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`REJECT </span><span style="color: rgb(255,0,170);">点击已禁用</span><span style="color: rgb(255,0,170);">  event: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            return <span style="color: rgb(0,0,255);">GestureJudgeResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">REJECT</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">返回</span><span style="color: rgb(128,128,128);">CONTINUE</span><span style="color: rgb(128,128,128);">将保持系统判定。</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`CONTINUE </span><span style="color: rgb(255,0,170);">保持系统判定</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            return <span style="color: rgb(0,0,255);">GestureJudgeResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTINUE</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/kaYeAGqgSA6oT0E67IfBhw/zh-cn_image_0000002628555226.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072327Z&HW-CC-Expire=86400&HW-CC-Sign=5D1679D5360977EB11652B35C2BAFADC071730D110A448DC2D57E8DFAD8D96F5)


  以长按手势为例，区分是否禁用对应的手势。代码中设置点击手势标志：“点击tap1”无打印，长按手势标志打印：“长按longPress”。

  日志如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/FIITL8SZTjGzuUADcSZJeg/zh-cn_image_0000002658914549.png?HW-CC-KV=V1&HW-CC-Date=20260730T072327Z&HW-CC-Expire=86400&HW-CC-Sign=75B1779D1A2F695B5E0EC5374F3C23C0F45A937ED4ECFF2BE48298C131C2AC53)

 
 

#### 总结

若需全局禁用组件交互行为，建议优先使用enabled属性，该属性可直接禁用所有事件响应。对于需要选择性禁用特定交互事件的场景，可通过onGestureJudgeBegin方法进行自定义是否响应特定事件。
