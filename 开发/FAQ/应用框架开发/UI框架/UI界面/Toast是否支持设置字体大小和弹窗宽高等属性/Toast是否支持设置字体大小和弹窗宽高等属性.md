# Toast是否支持设置字体大小和弹窗宽高等属性

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1436

#### 问题现象

Toast是否支持自定义设置字体大小和弹窗背板的宽高等属性？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/_vhMeuFsRzaetoR_unRN4g/zh-cn_image_0000002628763654.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005651Z&HW-CC-Expire=86400&HW-CC-Sign=FA2E0BDA4BA54283FDD3E00A1911FF146B067D530C4120FBA614763757F3D735)

 
 

#### 背景知识

- [即时反馈（Toast）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-toast)是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。
- [不依赖UI组件的全局自定义弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)：在相对较复杂的应用场景中推荐使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口来实现自定义弹出框。

 
 

#### 解决方案

[this.getUIContext().getPromptAction().openToast](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#promptactionopentoast18)接口未提供设置字体大小和弹窗宽高等方法，可以使用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗来实现定制化样式。方案如下：
 
- 使用[this.getUIContext().getPromptAction().openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12)自定义弹窗，在相对较复杂的应用场景中推荐使用[全局自定义弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)的方式。
```text
let <span style="color: rgb(255,255,255);">customDialogId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">customDialogBuilder</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可自定义文字大小及颜色</span></em>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">自定义</span><span style="color: rgb(132,63,161);">Toast'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#fff'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index99 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">customDialogComponent</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">customDialogBuilder</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击弹出</span><span style="color: rgb(132,63,161);">Toast'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bold</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openCustomDialog</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customDialogComponent</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗背景色</span></em>
              <span style="color: rgb(255,255,255);">backgroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'rgba(0,0,0,0.8)'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NONE</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">cornerRadius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗宽度</span></em>
              <span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗高度</span></em>
              <span style="color: rgb(255,255,255);">isModal</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">dy</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100 </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">dialogId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">customDialogId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">dialogId</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">customDialogId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
