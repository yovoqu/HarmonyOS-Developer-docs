# 如何解决AttributeModifier封装scale动画问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1523

#### 问题现象

- **问题一**：使用AttributeModifier封装组件的弹出和消失动画，在实际使用过程中无动画效果。
```text
class <span style="color: rgb(0,0,255);">FrameWorkAnimation </span>implements <span style="color: rgb(0,0,255);">AttributeModifier</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">CommonAttribute</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">弹窗退出时的动画</span></em>
  <span style="color: rgb(0,0,255);">exitShowDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1.0</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗展示时的帧动画</span></em>
    <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keyframeAnimateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">onFinish</span><span style="color: rgb(0,0,255);">()</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开始展示弹窗</span></em>
  <span style="color: rgb(0,0,255);">startShowDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span>
    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <em>// </em><em><span style="color: rgb(128,128,128);">弹窗展示时的帧动画</span></em>
      <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keyframeAnimateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
      <span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">applyNormalAttribute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CommonAttribute</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">centerX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">centerY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **问题二**：为什么CommonModifier重写的onAppear和onDisAppear没有被调用，如何使其跟随绑定组件的生命周期调用？
```text
export class <span style="color: rgb(0,0,255);">FrameWorkAnimation </span>extends <span style="color: rgb(0,0,255);">CommonModifier </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span>
  private <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">UIContext</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    super<span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">uiContext</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CommonAttribute </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'FrameWorkAnimation onAppear'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span>
    return super<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onDisAppear</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CommonAttribute </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'FrameWorkAnimation onDisAppear'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span>
    return super<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDisAppear</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/saGXa9f8SqSqLjOd3Hp2cg/zh-cn_image_0000002628606986.png?HW-CC-KV=V1&HW-CC-Date=20260730T072447Z&HW-CC-Expire=86400&HW-CC-Sign=C2B829946DF078DD33E5BB8F0AEB69805A5BA4B054071252818402212F1E1C76)

 
 

#### 背景知识

[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifiert)支持自定义class实现动态设置组件的属性，但不支持封装[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)属性。组件的布局类属性（如scale、rotate等）变化时的动画效果，无法用AttributeModifier封装。
 
 

#### 问题定位

- 问题一分析：调用FrameWorkAnimation的startShowDialog、exitShowDialog方法后会改变scaleDialog值，再通过scale属性控制组件的缩放实现动画效果，但是scale属于animation一类属性，AttributeModifier不支持封装。
- 问题二分析：FrameWorkAnimation重写了onAppear、onDisAppear方法，希望组件在创建和消失时调用。组件的生命周期是在运行时由开发框架在特定的时间进行调用。而AttributeModifier是一种属性修饰器，用于动态修改组件属性，在组件中使用AttributeModifier时，其onAppear等事件并不会跟随组件生命周期，而是作用于AttributeModifier本身。

 
 

#### 分析结论
1. AttributeModifier不支持封装组件的scale属性，所以无法实现动画效果。
2. AttributeModifier的onAppear、onDisAppear只作用于自身，不会跟随被绑定的组件生命周期。
 
 

#### 修改建议

不用AttributeModifier封装，直接使用class封装startShowDialog、exitShowDialog方法，在组件尾部直接调用scale方法，在startShowDialog中修改scaleDialog后，变化同步至scale，实现动画效果。通过export关键字可将封装的class导出，即可在别的文件中调用。
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">动画封装类</span></em>
export class <span style="color: rgb(0,0,255);">AnimateTest </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">缩小按钮的帧动画</span></em>
  <span style="color: rgb(0,0,255);">startAnimate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keyframeAnimateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
    <span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">AttributeModifierAnimateDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Button'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">animate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">AnimateTest </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AnimateTest</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">70</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听动画类中</span><span style="color: rgb(128,128,128);">scaleDialog</span><span style="color: rgb(128,128,128);">变化来缩放</span></em>
          <span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleDialog</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">centerX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">centerY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Button2'</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开始动画</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAnimate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
