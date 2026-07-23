# 如何使两个TextInput组件有序输入内容

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1167

#### 问题现象

有两个TextInput组件A和B，在B组件输入的时候，需先判断A组件是否有输入内容，如果A组件没有输入内容，B组件不允许输入并提示：请先输入A组件。只有当A组件有输入内容时，B组件才可以正常输入内容并展示。请问该场景如何实现？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/YCdoLFM8RjiusOfM3McVXw/zh-cn_image_0000002658809139.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012707Z&HW-CC-Expire=86400&HW-CC-Sign=9F53EB089AFFEF356D7E04F41E00BC0C96866E1740C663F65728C405BD0FEE6A)

 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)：单行文本输入框组件。
- [@ohos.promptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)：创建并显示文本提示框、对话框和操作菜单。
- [focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)：设置当前组件是否可以获焦。

 
 

#### 解决方案
1. 设置一个状态变量isShow控制B组件是否可以获取焦点。
2. 在onChange事件中使用if/else条件判断。
3. 当A组件有输入内容时，赋值isShow为true，此时B组件获取焦点能够输入。当A组件没有输入内容时，赋值isShow值为false，此时B组件获取不了焦点也不能够输入内容。
 
完整示例参考如下：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">OrderIndex </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'A' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">val</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">val</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">val </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'B'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(255,0,170);">)</span> <em>// </em><em><span style="color: rgb(128,128,128);">是否可以获焦</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">请先输入</span><span style="color: rgb(132,63,161);">A</span><span style="color: rgb(132,63,161);">组件</span><span style="color: rgb(132,63,161);">'</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
