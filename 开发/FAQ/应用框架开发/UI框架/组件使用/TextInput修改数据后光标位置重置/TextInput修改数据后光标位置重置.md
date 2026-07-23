# TextInput修改数据后光标位置重置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-933

#### 问题现象

在使用TextInput组件银行卡号格式化（每四位数字后自动添加一个空格）或电话号码格式化时，用户在任意位置进行删除或新增操作，光标应保留在操作位置。但实际使用中存在两个问题：一是空格可以被删除，二是执行删除或插入操作时，光标会重置到输入框末尾。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/-_7ynMj4Rn2jhgrIpKNU0Q/zh-cn_image_0000002658919559.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012635Z&HW-CC-Expire=86400&HW-CC-Sign=C2C73AD86274EC0476A736C290C4B1F99E5F9AAA0164333C38459E6ACB65A856)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/FtMZhx3sRTGXp0I4GQEjvw/zh-cn_image_0000002628400356.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012635Z&HW-CC-Expire=86400&HW-CC-Sign=EE4A557A33C198C526E1F2352EBEB9205F93AF714F7EF4146AB1E9456C8E2256)

 
 

#### 背景知识

[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)组件为单行输入框组件，通常用于响应用户的输入操作。当输入框中输入的内容发生变化时，会自动触发[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)回调，该组件还可通过[caretPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#caretposition10)函数设置光标位置。
 
 

#### 问题定位

onChange函数的规格为value值变化后执行，所以删除空格、删除数字或者添加数字等编辑操作改变value值，导致数据需要重新格式化，也就是重新赋值，此时光标会位于输入值的末尾。
 
 

#### 分析结论

为了达到预期效果，在value值变化前就将展示结果和光标位置获取到，之后再进行赋值以及光标位置定位。
 
 

#### 修改建议

参考[电话号码格式化](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#示例6电话号码格式化)中示例，做出以下修改：
 1. 在onTextSelectionChange回调函数中记录当前光标的位置；
2. 实现calcCaretPosition计算光标位置的函数；
3. 在onWillInsert和onWillDelete方法中，自定义处理增删空格逻辑。
 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">caretPositionExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">nextCaret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用于记录下次光标设置的位置</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">actualCh</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用于记录光标在第</span><span style="color: rgb(128,128,128);">i</span><span style="color: rgb(128,128,128);">个数字后插入或者第</span><span style="color: rgb(128,128,128);">i</span><span style="color: rgb(128,128,128);">个数字前删除</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">lastCaretPosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">lastCaretPositionEnd</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">isEmpty</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">str </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'undefined' </span><span style="color: rgb(181,106,1);">|| !</span><span style="color: rgb(0,0,255);">str </span><span style="color: rgb(181,106,1);">|| !</span>new <span style="color: rgb(0,0,255);">RegExp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[^</span>\\<span style="color: rgb(255,0,170);">s]'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">removeSpace</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isEmpty</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
      return <span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return <span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">replace</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">RegExp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[</span>\\<span style="color: rgb(255,0,170);">s]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'g'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">setCaret</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret </span><span style="color: rgb(181,106,1);">!== -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'to keep caret position right, change caret to'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">caretPosition</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">calcCaretPosition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">befNumberNoSpace</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">removeSpace</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">befNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">插入场景</span></em>
      for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">+= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">befNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
      for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">-= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
            break<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    } </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">befNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">删除场景</span></em>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Caret at last, no need to change'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPositionEnd</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">按键盘上回退键一个一个删的情况</span></em>
        for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
        for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">--</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);">-= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actualCh </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">;</span>
              break<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      } </span>else <span style="color: rgb(255,0,170);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">剪切</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">手柄选择一次删多个字符</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextCaret </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">保持光标位置</span></em>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'48vp'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">removeSpace</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">nextText </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">nextText </span><span style="color: rgb(181,106,1);">+= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
                if <span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">% </span><span style="color: rgb(255,0,0);">4 </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">!== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bankNumberNoSpace</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">nextText </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span>
<span style="color: rgb(255,0,170);">            }</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">nextText </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">nextText </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此时说明数字已经格式化完成了，在这个时候改变光标位置不会被重置掉</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setCaret</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">calcCaretPosition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nextText</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTextSelectionChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">selectionStart</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">selectionEnd</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">记录光标位置</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'selection change: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">selectionStart</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">selectionEnd</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPosition </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">selectionStart</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastCaretPositionEnd </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">selectionEnd</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">onWillInsert</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">onWillDelete</span><span style="color: rgb(128,128,128);">判断是否为空格，是空格就不给添加和删除，如果需要用户删除空格的时候不删除空格而是直接后退一位</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillInsert</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">InsertValue</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">insertValue</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              return false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              return true<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillDelete</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DeleteValue</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">deleteValue</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              return false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              return true<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

TextInput组件通过onChange自定义处理输入值时，重新赋值后光标位置会默认位于末尾，故需要记录光标位置，进行赋值。
