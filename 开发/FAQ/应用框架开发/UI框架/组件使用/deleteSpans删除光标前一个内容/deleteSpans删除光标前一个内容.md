# deleteSpans删除光标前一个内容

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1230

#### 问题现象

使用deleteSpans方法，如何实现仅删除富文本光标前的一个内容？
 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)是支持图文混排和文本交互式编辑的组件，其包含getCaretOffset方法用于获取光标位置。
 
 

#### 解决方案

通过[getCaretOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getcaretoffset10)方法获取光标位置，计算前一个内容的起始位置，并将其传入[deleteSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#deletespans)方法。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RichEditorDeleteDemo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTextSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击</span><span style="color: rgb(132,63,161);">delete</span><span style="color: rgb(132,63,161);">，一次只删除一个内容</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'delete'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        let <span style="color: rgb(255,255,255);">offset </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCaretOffset</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deleteSpans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">offset </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">end</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">offset </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
