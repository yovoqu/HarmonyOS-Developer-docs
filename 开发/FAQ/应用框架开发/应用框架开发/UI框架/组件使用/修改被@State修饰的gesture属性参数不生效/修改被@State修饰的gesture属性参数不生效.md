# 修改被@State修饰的gesture属性参数不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-640

#### 问题现象

对手势属性进行修改时，绑定手势gesture没有生效，如何解决该问题？
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PinchGesturePage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">lastScale</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isGesture</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#61CFBE'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(181,106,1);">: </span>null<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture </span>?
        <span style="color: rgb(0,0,255);">PinchGesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fingers</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionStart</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在手势开始时，记录当前的缩放比例</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastScale </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionUpdate</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例</span></em>
              let <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastScale </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(181,106,1);">;</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进行边界检查</span></em>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
              <em>// </em><em><span style="color: rgb(128,128,128);">更新缩放值</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">newScale</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手势结束时，不需要特殊处理</span></em>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">: </span>null
        <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`TWT-</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">onClick </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#5291FF'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/SRfFAAEARqO1_x-q9mr1KA/zh-cn_image_0000002628554400.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005800Z&HW-CC-Expire=86400&HW-CC-Sign=05EFA2C512096D0ADD3BB2F18205909E805690B2D69A307CE769279479B407B0)

 
 

#### 背景知识

[自定义手势判定](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge)为组件提供自定义手势判定能力。开发者可根据需要，在手势识别期间，决定是否响应手势。
 
 

#### 问题定位

问题代码中通过this.isGesture的值判断是否执行手势事件。但参考[绑定手势方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings)的说明部分，gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。
 
 

#### 分析结论

gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。但是可以通过[onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)来进行判断并决定是否识别手势。
 
 

#### 解决方案

使用手势拦截onGestureJudgeBegin来判断是否识别手势。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PinchGesturePage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">lastScale</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isGesture</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#61CFBE'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(181,106,1);">: </span>null<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onGestureJudgeBegin</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return <span style="color: rgb(0,0,255);">GestureJudgeResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTINUE</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            return <span style="color: rgb(0,0,255);">GestureJudgeResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">REJECT</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">PinchGesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fingers</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionStart</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在手势开始时，记录当前的缩放比例</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`The lastScale is </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastScale</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastScale </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionUpdate</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例</span></em>
              let <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastScale </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(181,106,1);">;</span>
            <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进行边界检查</span></em>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">newScale </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">更新缩放值</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">newScale</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`The newScale is </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scaleValue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手势结束时，不需要特殊处理</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'The action is end'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">        )</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`TWT-</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">onClick </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isGesture</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#5291FF'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
