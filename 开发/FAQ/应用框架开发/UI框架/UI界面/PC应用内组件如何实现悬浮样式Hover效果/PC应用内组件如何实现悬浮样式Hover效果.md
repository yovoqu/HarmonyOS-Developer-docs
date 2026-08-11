# PC应用内组件如何实现悬浮样式Hover效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-754

#### 问题现象

PC应用如何实现鼠标悬停在组件上时，组件UI效果变更？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/hC5wTvM6T6CXMLIWueaSSA/zh-cn_image_0000002628395472.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005645Z&HW-CC-Expire=86400&HW-CC-Sign=8E26ECF54993EEEE11743C703CBB403CBA9D946D7BCADEBAEDFFA8425166EF6A)

 
 

#### 背景知识

- [@Styles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style)：@Styles装饰器可以将多条样式设置提炼成一个方法，直接在组件声明的位置调用。通过@Styles装饰器可以快速定义并复用自定义样式，仅仅应用于静态页面的样式复用。
- [stateStyles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles)：stateStyles可以依据组件的内部状态的不同，快速设置不同样式。stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下五种状态：focused、normal、pressed、disabled、selected。

 
 

#### 解决方案

例如按钮的默认状态、按下状态、禁用状态可以将@Styles与stateStyles组合使用来实现对应效果，悬浮状态还需要结合[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover)事件来实现。
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">定义在全局的</span><span style="color: rgb(128,128,128);">Button</span><span style="color: rgb(128,128,128);">样式</span></em>
<span style="color: rgb(181,106,1);">@Styles</span>
function <span style="color: rgb(0,0,255);">globalButtonStyle</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">160</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">80</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CustomerButton </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isHover</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">定义在组件内的</span><span style="color: rgb(128,128,128);">@Styles</span><span style="color: rgb(128,128,128);">封装的样式</span></em>
<em>  <span style="color: rgb(128,128,128);">// Disable</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">disabledStyle</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#A8B8F7'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <em><span style="color: rgb(128,128,128);">// normal</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">normalStyle</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#0A59F7'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// pressed</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">pressedStyle</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#0950DE'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <em><span style="color: rgb(128,128,128);">// hover</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">hoverStyle</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isHover </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(132,63,161);">'#0954EA' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#0A59F7'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Default'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">默认状态</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>false <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">globalButtonStyle</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateStyles</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">normal</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">normalStyle</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Pressed'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">按下状态</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>false <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">globalButtonStyle</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateStyles</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">normal</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">normalStyle</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">pressed</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pressedStyle</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Hover'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">悬浮状态</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>false <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">globalButtonStyle</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onHover</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">isHover</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">isHover</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isHover </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isHover</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateStyles</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">normal</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hoverStyle</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Disable'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">禁用状态</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>false <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">globalButtonStyle</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateStyles</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">disabled</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">disabledStyle</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
