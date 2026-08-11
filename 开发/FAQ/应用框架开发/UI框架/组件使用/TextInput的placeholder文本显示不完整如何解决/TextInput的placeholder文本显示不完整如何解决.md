# TextInput的placeholder文本显示不完整如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-821

#### 问题现象

当TextInput组件的placeholder文本过长时，会导致显示不完整，影响用户体验，该如何优化这一问题？
 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)为单行文本输入框组件，placeholder为设置无输入时的提示文本，可通过[placeholderFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#placeholderfont)和[placeholderColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#placeholdercolor)设置placeholder文本样式和文本颜色，包括字体大小，字体粗细，字体族，字体风格等。
- [TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)为多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。
- [promptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction)可创建并显示文本提示框、对话框和操作菜单。

 
 

#### 解决方案

TextInput组件的placeholder文本较长时，默认会使用省略号来截断过长的文本。可通过以下四种方案让placeholder文本显示完整。
 
- **方案一**：使用promptAction创建文本提示框来展示整个placeholder文本。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'input your word'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Grey</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">400 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'[0-9]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">placeholder </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/MqH0Gp9uS-uSbeHj2Mw0ug/zh-cn_image_0000002658917661.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=CB51FD95C66A7B127AE2512D5630A10E2513E7C607A56ED50EB17CB2CAD9074B)

- **方案二**：使用TextArea组件，组件不设置高度时，会自适应内容高度，从而实现placeholder多行显示。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample2 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextAreaController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextAreaController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextArea</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'input your word'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Grey</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">400 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'[0-9]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/DlFATeRMRq6Iefch7ekpLA/zh-cn_image_0000002628398434.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=BBFB124C07B73D869F2C25DCCD3D8EFBBBEA879677F683651965C1E0C221EF58)

- **方案三**：placeholder文本大小默认为16fp，可通过placeholderFont将placeholder文本大小设置小一点，如10fp。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample3 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'input your word'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Grey</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">400 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'[0-9]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/uy1i3LaORd6dPMAbv_YcBA/zh-cn_image_0000002658797717.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=F9B3608B9AEA0F455F3AD523E7BFD8C24BA58A3718A52B3D8F7B4D8C6E481475)

- **方案四**：可设置TextInput的[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#style9)为Inline，文本选中底板高度与输入框高度相同，在输入时可显示全部placeholder文本。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample4 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'input your word'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Grey</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">placeholderFont</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">weight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">400 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">style</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextInputStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Inline</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">wordBreak</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">WordBreak</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">BREAK_WORD</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'[0-9]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/4e-VJS15Qc-jhYAHbRLYhg/zh-cn_image_0000002628558352.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=65371E750073E434EFE8921020B1345DCA6A524F5F3277D71D3B140596F3178F)


 
 

#### 总结

四种方案的特点如下表：
  
| 方案 | 特点 |
| --- | --- |
| 使用promptAction创建文本提示框 | 通过弹窗显示placeholder文本，不会破坏原有的页面布局。 |
| 使用TextArea组件替代TextInput组件 | 若页面布局时高度足够显示多行，可以使用TextArea组件，但不支持设置type为密码类型。 |
| 通过placeholderFont修改placeholder文本大小 | 适用于placeholder文本相对较短的场景，但字体设置太小会影响开发者的阅读体验。 |
| 设置TextInput组件的style为Inline | 在输入时输入框高度会变化，会导致布局变化，可根据具体需要选择。 |
