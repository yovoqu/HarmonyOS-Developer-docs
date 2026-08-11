# Span组件响应组件外点击事件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1337

#### 问题现象

由于Span组件不支持宽高属性设置，因此在其文字内容外部无法触发点击事件。目前有一组包含联系人的数据，需要点击每个联系人能够跳转到对应的联系人详情信息页面（联系人所在行也都能响应点击事件），Span组件如何实现该功能？
 
 

#### 背景知识

[Span组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)目前仅支持继承的属性包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontfamily、textShadow，但不支持通用属性，因此即使设置了通用属性，如：width、height，但并不会生效。
 
 

#### 解决方案

[点击事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click)可以获取点击位置相对于被点击元素原始区域左上角的Y坐标，可以通过给出的Y坐标和对象显示区域计算出对应Span组件。
 
以下为具体步骤：
 1. 通过点击事件获取组件高度、当前点击的Y坐标值。
2. 基于Span组件总数，计算出单个Span高度值。
3. 使用点击的Y坐标值对Span高度值整除，计算出被点击的对应Span组件区域。
```text
import <span style="color: rgb(0,0,255);">hilog </span>from <span style="color: rgb(255,0,170);">'@ohos.hilog'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">张三</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">李四</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">王五</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">赵六</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onClicked</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">area</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span>as <span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">组件总高度</span></em>
    const <span style="color: rgb(0,0,255);">avgHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">分配到每个</span><span style="color: rgb(128,128,128);">Span</span><span style="color: rgb(128,128,128);">的平均高度</span></em>

    let <span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">floor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">y </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">avgHeight</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">计算点击位置所在编号，取整，忽略小数部分</span></em>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">联系人信息</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Show dialog error.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contacts</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontFamily</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'HarmonyOS Sans'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClicked</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
