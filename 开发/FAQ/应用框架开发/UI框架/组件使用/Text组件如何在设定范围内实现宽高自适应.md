# Text组件如何在设定范围内实现宽高自适应

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1540

#### 问题现象

在Row布局中，左边是固定宽高组件，右边是Text组件的父组件，并且要求父组件占据Row组件剩余空间，但是当Text组件文字过多时会超出父组件设定范围，如何实现Text组件在父组件设定范围内的宽高自适应，避免超出父组件的设定范围？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Wz9_ZYQJRSetmP8ERJK4rA/zh-cn_image_0000002658848481.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041252Z&HW-CC-Expire=86400&HW-CC-Sign=784E152CF214A2EBAACFD7D85584865C6A018A4C9BCFDD967657C68600C6073A)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/VjDHKRI2TL-9PqGdHyGaCQ/zh-cn_image_0000002628609220.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041252Z&HW-CC-Expire=86400&HW-CC-Sign=4C7B0AE7026A58D605EB340C136236B9633D0E0D41A0A709E3351E9002F15410)

 
 

#### 背景知识

- [Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)组件是沿水平方向布局容器，Row组件在嵌套使用时，设置在外层的属性可能不会对内层子组件起到预期的效果，比如将constraintSize属性设置在外层Row时会导致内层Row中的子组件Text超出设定的范围。
- [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件能够使用[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes#constraintsize11)属性来设置约束尺寸，保证Text组件在设定好的范围内自由变动，并且其优先级高于[width](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#width)和[height](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#height)。

 
 

#### 解决方案

可以通过计算得出Text父组件在Row容器下的最大宽高，以此来设置属性constraintSize约束Text组件的最大尺寸，实现Text组件在设定范围内的宽高自适应。具体实现如下：1. 将constraintSize属性设置在Text组件下，约束Text组件的尺寸，并且通过计算，得出最大尺寸的具体值，Text的constraintSize属性的最大宽度是由：父组件的宽度maxWidth减去左边固定宽高组件的宽度stableWidth，再减去父组件左内边距margin.left，再减去父组件右内边距margin.right之后即可得到。在aboutToAppear生命周期方法中进行计算：
```text
<span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span>void <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">try </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">let screenW </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDefaultDisplaySync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取屏幕宽度，并转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
    <span style="color: rgb(255,255,255);">let stableW </span><span style="color: rgb(181,106,1);">=</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getNumber</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.float.page_text_font_size'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取页面字体大小，并转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
    <span style="color: rgb(255,255,255);">let marginR </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">removeCharacter</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginRight </span>as <span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">let marginL </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginLeft </span>as <span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">左边距直接转换为数字</span></em>
    <span style="color: rgb(255,255,255);">let marginT </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getNumber</span><span style="color: rgb(255,0,170);">((</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginTop </span>as <span style="color: rgb(181,106,1);">Resource</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">顶部边距直接转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
    <span style="color: rgb(255,255,255);">this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">screenW </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">stableW </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginR </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginL </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginT</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算最大宽度</span></em>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`this.maxWidth: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打印最大宽度</span></em>
  <span style="color: rgb(181,106,1);">} </span><span style="color: rgb(255,255,255);">catch </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 得出Text的在Row组件中的最大尺寸，并将其传入constraintSize属性，即可动态指定Text组件的尺寸，防止文字超出文本框。
```text
<span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">maxWidth</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
 
完整示例参考如下：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">display </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'123'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">maxWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">marginRight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Length </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'16vp'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">marginLeft</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Length </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">marginTop</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Length </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.float.page_text_font_size'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">removeCharacter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">result </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">replace</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">/[a-zA-Z]/g</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">screenW </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDefaultDisplaySync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取屏幕宽度，并转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
      let <span style="color: rgb(255,255,255);">stableW </span><span style="color: rgb(181,106,1);">=</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getNumber</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.float.page_text_font_size'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取页面字体大小，并转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
      let <span style="color: rgb(255,255,255);">marginR </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">removeCharacter</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginRight </span>as <span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">marginL </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginLeft </span>as <span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">左边距直接转换为数字</span></em>
      let <span style="color: rgb(255,255,255);">marginT </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getNumber</span><span style="color: rgb(255,0,170);">((</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">marginTop </span>as <span style="color: rgb(181,106,1);">Resource</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">顶部边距直接转换为</span><span style="color: rgb(128,128,128);">vp</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">screenW </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">stableW </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginR </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginL </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">marginT</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">计算最大宽度</span></em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`this.maxWidth: </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">打印最大宽度</span></em>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">    }</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ff18a2d0'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">maxWidth</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">maxWidth </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#fff2f5f5'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffeeeaea'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 
 

#### 常见FAQ

Q：在解决方案的aboutToAppear方法中，使用getNumber方法获取其中的数据，得到的数据单位都是px吗？
 
A：用getNumber方法获取数据的数据单位都是px。例如Integer对应的是原数值，float中的数不带单位时对应的是原数值，带"vp"，"fp"单位时对应的是px值。具体参考官网[资源管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)。
