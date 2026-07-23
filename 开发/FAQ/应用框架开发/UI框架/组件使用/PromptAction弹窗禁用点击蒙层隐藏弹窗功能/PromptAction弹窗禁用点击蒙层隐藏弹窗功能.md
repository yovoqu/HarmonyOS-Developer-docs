# PromptAction弹窗禁用点击蒙层隐藏弹窗功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-718

#### 问题现象

PromptAction自定义弹窗如何实现在点击弹窗外围的蒙层时，弹窗不关闭？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/WY2et_8HSXCqJuwLTarrkA/zh-cn_image_0000002628395300.png?HW-CC-KV=V1&HW-CC-Date=20260723T012603Z&HW-CC-Expire=86400&HW-CC-Sign=96A7B9C2539596BE11D13508FB2467862474B434AF1C2196A307A442029F1AA8)

 
 

#### 背景知识

- [PromptAction弹窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)：为官网提供的一种弹窗方式，由于上下文不明确，在API18以后部分接口废弃。废弃的接口建议通过[this.getUIContext().getPromptAction()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getpromptaction)获取弹窗实例后调用。
- [onWillDismiss](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#basedialogoptions11)：PromptAction弹窗的关闭事件可以在通过onWillDismiss方法指定是否关闭弹窗。方法内指定对应的[DismissDialogAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#dismissdialogaction12)信息控制是否关闭弹窗，关闭调用dismiss()函数，不关闭则不调用即可。控制关闭事件参考[DismissReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#dismissreason12枚举说明)。

 
 

#### 解决方案

实现PromptAction弹窗禁用点击蒙层隐藏弹窗功能时，只需要在onWillDismiss内控制关闭信息：在dismissDialogAction.reason !== DismissReason.TOUCH_OUTSIDE条件下调用dismiss()关闭函数即可，在该条件下除了点击蒙层不关闭弹窗外，其他关闭条件都不影响。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">PromptAction </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">promptAction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PromptAction </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">customDialogComponentId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">customDialogComponent</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">弹窗</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">确认</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">customDialogComponentId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">取消</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">customDialogComponentId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SpaceBetween</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'click me'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openCustomDialog</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customDialogComponent</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">onWillDismiss</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DismissDialogAction</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,255,255);">DismissReason</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">TOUCH_OUTSIDE</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">dismissDialogAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dismiss</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">              }</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">dialogId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">customDialogComponentId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">dialogId</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 总结

本方案通过onWillDismiss内回调实现点击蒙层不关闭弹窗的功能。同时也可以采用isModal设置为false，取消弹窗蒙层，实现类似点击弹窗外不关闭的功能，但是该功能还会导致点击穿透。
