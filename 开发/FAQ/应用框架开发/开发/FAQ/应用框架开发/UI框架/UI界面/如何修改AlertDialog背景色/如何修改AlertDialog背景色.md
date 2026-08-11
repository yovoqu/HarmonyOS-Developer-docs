# 如何修改AlertDialog背景色

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1535

#### 问题现象

AlertDialog设置了backgroundColor，但是背景色仅可以看见很浅的颜色。
 
问题代码如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        const <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showAlertDialog</span><span style="color: rgb(0,0,255);">(</span>
          <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'title'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'text11'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Green</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">gridCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rgba(10,89,247,0.4)'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'button'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Button-clicking callback'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Closed callbacks'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
        <span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/k6MiS8zyQdGSVuQ2O08jgg/zh-cn_image_0000002658846259.png?HW-CC-KV=V1&HW-CC-Date=20260811T005700Z&HW-CC-Expire=86400&HW-CC-Sign=AA3807E11643269314063B2788752548F07DA6AC7DA161ABE2D0FBA5BAE15F90)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/TQkhSwscQe6nXLBBNyEKug/zh-cn_image_0000002628766896.png?HW-CC-KV=V1&HW-CC-Date=20260811T005700Z&HW-CC-Expire=86400&HW-CC-Sign=5EF516DC9E07D01ABCA300E94F8F0F56EC8FBD7AFC184F8E3DFA06B5EED60D02)

 
 

#### 背景知识

[警告弹窗(AlertDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box)是一种对话框组件，用来在应用中弹出提示、确认、输入等交互式对话框。[AlertDialogParam对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box#alertdialogparam对象说明)中的属性backgroundColor与backgroundBlurStyle分别控制弹窗背板颜色与弹窗背板模糊材质。
 
 

#### 解决方案

backgroundColor会与弹窗默认的模糊属性backgroundBlurStyle叠加产生效果，出现背景色被其它颜色覆盖从而导致的仅可以看见很浅的颜色，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊，示例代码如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">AlertDialogBackgroundColor </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          const <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showAlertDialog</span><span style="color: rgb(0,0,255);">(</span>
            <span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗标题</span></em>
              <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'title'</span><span style="color: rgb(181,106,1);">,</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗内容</span></em>
              <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">弹窗内容</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置偏移量</span></em>
              <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">gridCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">,</span>
            <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置背景色</span></em>
              <span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rgba(10,89,247,0.4)'</span><span style="color: rgb(181,106,1);">,</span>
           <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭背景虚化，</span><span style="color: rgb(128,128,128);">backgroundBlurStyle</span><span style="color: rgb(128,128,128);">为非</span><span style="color: rgb(128,128,128);">NONE</span><span style="color: rgb(128,128,128);">值时，则不要设置</span><span style="color: rgb(128,128,128);">backgroundColor</span><span style="color: rgb(128,128,128);">，否则颜色显示将不符合预期效果。</span></em>
              <span style="color: rgb(0,0,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NONE</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'button'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Button-clicking callback'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Closed callbacks'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span>
          <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
