# 解决RichEditor输入换行符后监听异常的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1398

#### 问题现象

正常输入文字如'1，2，3'等，inputStr都能准确获取，如果先输入一个换行符，再输入文字,如'1，2，3'，'1'这个文字就获取不到，再次输入'2'，'3'能监听到，如何解决该问题？
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">StackExample </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(255,0,170);">()</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输入框</span></em>
      <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enterKeyType</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EnterKeyType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NEW_LINE</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">maxHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">minHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">35</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">defaultFocus</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onSubmit</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">enterKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">EnterKeyType</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SubmitEvent</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keepEditableState</span><span style="color: rgb(255,0,170);">() </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保持输入状态</span></em>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onIMEInputComplete</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorTextSpanResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听文字输入</span></em>
          const <span style="color: rgb(255,255,255);">start </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetInSpan</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span>
          const <span style="color: rgb(255,255,255);">end </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetInSpan</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取输入的字符串</span></em>
          const <span style="color: rgb(255,255,255);">inputStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">end</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/bjIl7yT1RWGd8CGk9Y6EfQ/zh-cn_image_0000002628763130.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012745Z&HW-CC-Expire=86400&HW-CC-Sign=B2F4126132E074612EDCC66BF13DB73AD8BC6B71701B7F9AE8ED61565C42F38C)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nBDxk65oQguHx2oT_S2X5A/zh-cn_image_0000002658962443.png?HW-CC-KV=V1&HW-CC-Date=20260723T012745Z&HW-CC-Expire=86400&HW-CC-Sign=EB773FFD7C6BF5C304C3741CCF1F8F1C057B09356B9D1F89AD9BAAFA158D4A97)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/22B3MPGGTiSXb3pPpylDNA/zh-cn_image_0000002628603234.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012745Z&HW-CC-Expire=86400&HW-CC-Sign=D5DE7026D076DBDF14F08434AE287E72C04613738CD737CBA5F5B66193E0BC89)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JIQwt60CQcScmzsMmLKbUg/zh-cn_image_0000002658842497.png?HW-CC-KV=V1&HW-CC-Date=20260723T012745Z&HW-CC-Expire=86400&HW-CC-Sign=2088AB211E75D7B36882BA9C52E26D25C3F8775B744B68CA3AE65ADB184AE9B3)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)支持图文混排和文本交互式编辑的组件。
 
- [onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onsubmit12)按下软键盘输入法回车键触发该回调。
- [onDidIMEInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#ondidimeinput12)输入法完成输入时，触发回调。
- [getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)获取span信息。
- [onIMEInputComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onimeinputcomplete)：输入法完成输入后，触发回调。

 
 

#### 解决方案

onIMEInputComplete接口仅支持返回一个文本span的信息，存在\n会触发span分裂，所以换行后监听异常。
 1. 使用onDidIMEInput代替onIMEInputComplete，获取当前输入内容的范围。
2. 使用getSpans获取当前输入的内容并打印，实现监听。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">StackExample </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输入框</span></em>
      <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enterKeyType</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EnterKeyType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NEW_LINE</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">maxHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">minHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">35</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">defaultFocus</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onSubmit</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">enterKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">EnterKeyType</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SubmitEvent</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keepEditableState</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保持输入状态</span></em>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDidIMEInput</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextRange</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          const <span style="color: rgb(255,255,255);">start </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(255,255,255);">end </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">end</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(255,255,255);">curSpans </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSpans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">end</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">end</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,255,255);">curSpans</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span>typeof <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item </span>as <span style="color: rgb(181,106,1);">RichEditorTextSpanResult</span><span style="color: rgb(255,0,170);">)) </span><span style="color: rgb(181,106,1);">{</span>
              const <span style="color: rgb(255,255,255);">cur </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">item </span>as <span style="color: rgb(181,106,1);">RichEditorTextSpanResult</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(132,63,161);">输入的字符</span><span style="color: rgb(132,63,161);">: " </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">cur</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">cur</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetInSpan</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">cur</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetInSpan</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]))</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
