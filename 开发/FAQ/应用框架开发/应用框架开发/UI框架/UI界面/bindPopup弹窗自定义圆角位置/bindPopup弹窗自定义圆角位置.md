# bindPopup弹窗自定义圆角位置

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1210

#### 问题现象

bindPopup弹窗如何自定义圆角位置？如只设置底部或者顶部圆角？
 
 

#### 背景知识

[bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)为组件绑定Popup气泡，入参[PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)的部分字段说明如下：
 
- radius：可以设置气泡圆角半径，但不支持自定义圆角位置。
- popupColor：设置气泡的背景颜色。

 
 

#### 解决方案

设置气泡的背景popupColor为透明色，再通过设置气泡内的最外层组件的圆角样式，以在视觉上实现气泡自定义圆角位置的效果。
 
> [!NOTE]
> 设置popupColor为透明色时一定要设置backgroundBlurStyle字段为BlurStyle.NONE。

 
只设置气泡弹窗的左上和右下圆角。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BindPopupDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义变量控制弹窗显示</span></em>

 <em> <span style="color: rgb(128,128,128);">// popup</span><span style="color: rgb(128,128,128);">构造器定义弹框内容</span></em>
  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Popup'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">topLeft</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottomRight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">Column</span><span style="color: rgb(128,128,128);">左上和右下圆角</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'click'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">builder</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mask</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">popupColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">气泡的背景色设为透明</span></em>
          <span style="color: rgb(0,0,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NONE</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">关闭气泡模糊背景</span></em>
          <span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置气泡的圆角</span></em>
          <span style="color: rgb(0,0,255);">shadow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
限制：由于是在气泡自定义内容函数中根组件设置圆角样式，所以不能在bindPopup入参中再设置箭头、阴影、背景颜色等样式，否则会和弹窗根组件设置的样式产生干扰。
