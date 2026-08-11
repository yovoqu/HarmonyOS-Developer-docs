# padding边距显示不准确

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-818

#### 问题现象

Row组件内包含Image和Text组件，当Text内容为多行时，Row组件设置的内边距显示不准确。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Frhk9B7oTmyOqzn35MD0IQ/zh-cn_image_0000002628398432.png?HW-CC-KV=V1&HW-CC-Date=20260811T005757Z&HW-CC-Expire=86400&HW-CC-Sign=06D05F50A32B9CA1080DADFBFEC0F520D294584DA7D66303A99E46FEBBC69AB7)

 
 

#### 背景知识

[Text组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)是显示一段文本的组件，可以设置属性[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes#constraintsize11)，在组件布局时，进行尺寸范围限制。
 
 

#### 解决方案

通过添加constraintSize属性来限制Text文本显示的最大长度，使内边距显示准确。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">constraintSizeExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">添加</span><span style="color: rgb(255,0,170);">constraintSize</span><span style="color: rgb(255,0,170);">属性下的状态，右</span><span style="color: rgb(255,0,170);">padding</span><span style="color: rgb(255,0,170);">样式添加正常</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">maxWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'90%' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">))   </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需自行替换图片</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rowStyle</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#77ceeb'</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">没有添加</span><span style="color: rgb(255,0,170);">constraintSize</span><span style="color: rgb(255,0,170);">属性下的状态，右</span><span style="color: rgb(255,0,170);">padding</span><span style="color: rgb(255,0,170);">添加未生效</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)) </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需自行替换图片</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rowStyle</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#f3f5f7'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Extend</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">)</span>
function <span style="color: rgb(0,0,255);">rowStyle</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceBetween</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：特定场景下constraintSize属性不生效？
 
A：在使用constraintSize属性来限制组件的尺寸时，当子组件设置了百分比宽度后，会导致组件被撑大，从而使constraintSize的设置失效。为了解决这个问题，可以在外层使用一个Scroll组件，并在该组件上设置constraintSize，以确保子组件即使占用了过多空间，也会显示滚动条。
 
Q：设置了constraintSize后，组件的宽高失效了。
 
A：constraintSize的优先级高于Width和Height。
 
Q：如何解决TextInput设置高度和padding后，输入内容底部被截断？
 
A：查看padding设置的top和bottom值，减少或设置为0。
