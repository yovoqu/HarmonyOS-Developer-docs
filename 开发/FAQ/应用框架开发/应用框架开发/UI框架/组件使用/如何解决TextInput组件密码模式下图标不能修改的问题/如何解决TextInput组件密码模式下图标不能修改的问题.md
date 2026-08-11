# 如何解决TextInput组件密码模式下图标不能修改的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1014

#### 问题现象

TextInput密码输入模式（Password）下系统控制密码显隐的PasswordIcon图标的位置、大小、颜色无法更改，而应用某些定制化场景下需要更改PasswordIcon位置、大小、颜色等。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/nsRFbOwTSDqcBXwDCsrkEA/zh-cn_image_0000002658923997.png?HW-CC-KV=V1&HW-CC-Date=20260811T005818Z&HW-CC-Expire=86400&HW-CC-Sign=CEDD158DA2CB17E21AD818B161E326883E027C075E36A0E9D130668CE8FD1E6B)

 
 

#### 背景知识

[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)为单行文本输入框组件。可以通过[InputType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#inputtype枚举说明)设置输入框类型，常见的类型有：Normal、Password、Email、Number、PhoneNumber等。在TextInput输入类型为Password时，输入的字符会表现为点（·），在[showPasswordIcon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpasswordicon9)设置为true时，行尾会有一个小眼睛图标，点击可控制密码的显隐。
 
 

#### 解决方案

当前的规格不支持更改icon图标的大小及位置，许多APP均是使用的此规格，由于并不阻塞功能的开发，此场景可以通过实现一个自定义组件，来完成行尾密码图标位置、大小、颜色的修改。自定义组件由TextInput和Image组成，使用Stack容器作为父容器。需要注意的是需要将TextInput自带的PasswordIcon设置为不显示，然后将需要替换的图标放入到Image组件中即可，此时即可随意更改位置、大小、颜色。具体代码细节如下：
 
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIconExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// TextInput</span><span style="color: rgb(128,128,128);">行尾图标宽度</span>
  <span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// TextInput</span><span style="color: rgb(128,128,128);">行尾图标宽度</span>
  <span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// TextInput</span><span style="color: rgb(128,128,128);">组件高度</span>
  <span style="color: rgb(0,0,255);">textInputHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">56</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// TextInput</span><span style="color: rgb(128,128,128);">输入内容</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">密码是否可见</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">passwordState</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// TextInput</span><span style="color: rgb(128,128,128);">行尾图标图片</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">icon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.ic_public_password_visible'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// TextInputController</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Row </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">InputType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Password</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showPasswordIcon</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处需将自带的行尾小眼睛图标设置成不显示</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showPassword</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">passwordState</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textInputHeight</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#E8E7E7'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">Image</span><span style="color: rgb(128,128,128);">组件自定义实现行尾图标</span>
          <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">icon</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">290</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">点击行尾图标改变状态和</span><span style="color: rgb(128,128,128);">icon</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">passwordState </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">passwordState</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">icon </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">passwordState </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'app.media.ic_public_password_visible' </span><span style="color: rgb(181,106,1);">:</span>
                <span style="color: rgb(255,0,170);">'app.media.ic_public_password_invisible'</span>
              <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIcon </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(128,128,128);">// icon</span><span style="color: rgb(128,128,128);">宽高</span><span style="color: rgb(128,128,128);">20vp</span>
      <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIconExample</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50vp'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Blank</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// icon</span><span style="color: rgb(128,128,128);">宽高</span><span style="color: rgb(128,128,128);">30vp</span>
      <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIconExample</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50vp'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Blank</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// icon</span><span style="color: rgb(128,128,128);">宽高</span><span style="color: rgb(128,128,128);">40vp</span>
      <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIconExample</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">40 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50vp'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Blank</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(128,128,128);">// icon</span><span style="color: rgb(128,128,128);">宽高</span><span style="color: rgb(128,128,128);">50vp</span>
      <span style="color: rgb(0,0,255);">ModifyTextInputPasswordModeIconExample</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">iconWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50vp'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：TextInput模式为Password的情况下，输入框右边的小眼睛如何设置能不显示？
 
A：设置[showPasswordIcon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpasswordicon9)为false。
 
Q：TextInput右侧默认的icon如何设置自定义图片？
 
A：使用[PasswordIcon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#passwordicon10)属性即可。
 
 

#### 总结

对于TextInput其他输入类型，均可采用此方法来实现自定义组件，以满足更多的定制化要求，此处不再一一举例，参考上述代码实现即可。甚至如果想定制一个TextInput的输入类型，也可以参考此方法去实现。
