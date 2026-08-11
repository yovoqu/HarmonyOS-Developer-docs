# Text绑定自定义菜单

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-772

#### 问题现象

Text组件绑定自定义菜单如何实现以下效果：
 
- bindSelectionMenu展示的菜单在用户触碰屏幕时自动消失。
- 长按出现自定义菜单，双击手势不出现默认菜单。

 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/VycHdmELR7S69-C6mIMM5g/zh-cn_image_0000002658795071.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=BB2DDFFBB17144BFC2F8CDB227B59DA67408F3D2BC7F5DA916EF47E734C5E7B0)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/UHS5Z8rQQmCU0mIpMR0CSw/zh-cn_image_0000002628555700.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=B3E6779DEFF22A0CCCB7168136911F3BF540A2290DDFADAF9F83F8997EFDFDED)

 
 

#### 背景知识

- [绑定手势方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings)为组件绑定不同类型的手势事件，并设置事件的响应方法。
- [bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)方法能设置Text自定义选择菜单，使用方法可参考[文本绑定自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例8文本绑定自定义菜单)。

 
 

#### 解决方案

- 在页面最外层组件添加点击事件，关闭菜单，实现触摸屏幕菜单消失的效果。
- 双击手势出现默认菜单是系统默认规格，可以为Text组件绑定双击事件覆盖默认行为。

 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BindMenuPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>undefined<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Hello World'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">ImageSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">图片资源需自行替换</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100px'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100px'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parallelGesture</span><span style="color: rgb(255,0,170);">(</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">重写双击手势事件，关闭菜单</span></em>
        <span style="color: rgb(0,0,255);">TapGesture</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAction</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSelectionMenu</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">GestureMask</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">copyOption</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">CopyOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">InApp</span><span style="color: rgb(255,0,170);">)</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">TextResponseType.LONG_PRESS</span><span style="color: rgb(128,128,128);">，可以通过长按方式弹出自定义菜单</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindSelectionMenu</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextSpanType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DEFAULT</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LongPressImageCustomMenu</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TextResponseType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LONG_PRESS</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在页面根节点设置点击事件，关闭菜单</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSelectionMenu</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">关闭菜单</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">LongPressImageCustomMenu</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Menu</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">MenuItemGroup</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
     <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">图片资源需自行替换</span></em>
          <span style="color: rgb(0,0,255);">MenuItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">startIcon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Long Press Image Menu 1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">labelInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">MenuItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">startIcon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Long Press Image Menu 2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">labelInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">MenuItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">startIcon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Long Press Image Menu 3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">labelInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#F0F0F0'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
