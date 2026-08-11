# TextInput限制输入

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-883

#### 问题现象

TextInput如何限制输入的内容格式以及限制输入的内容长度？
 
 

#### 背景知识

[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)是单行文本输入框组件，常用于响应用户的输入操作，比如手机号输入，表单的输入等。针对输入的内容格式以及长度、行数，一些场景下需要进行限制，常见的场景如下：
 1. 限制输入的格式：
限制只能输入手机号或者邮箱。
2. 首位不允许出现空格。
3. 限制输入中文、英文、数字或者emoji表情包。
4. 限制输入两位小数。
5. 限制输入数字范围。
6. 限制输入的长度：
限制文本的内容长度，比如不超过20个字符。
7. 限制文本的字节数量，比如不超过32个字节。
 
 

#### 解决方案
1. 限制输入的格式：
限制只能输入手机号或者邮箱。TextInput的[InputType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#inputtype枚举说明)属性支持设置不同的输入框类型，利用InputType.PhoneNumber、InputType.Email可拉起数字键盘，即可限制类型为手机号码、邮箱：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">TextInputExample1 </span><span style="color: rgb(255,0,170);">{</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入手机号码</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">InputType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhoneNumber</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLength</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">11</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 如果对type的过滤效果不满意，可以使用inputFilter覆盖。
2. 限制只能输入身份证号。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">PromptAction </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PromptAction </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入身份证号</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[0-9Xx]'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLength</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">EditableTextChangeValue</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">checkIncludeWord</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">非最后一位为</span><span style="color: rgb(128,128,128);">X</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">X</span><span style="color: rgb(128,128,128);">输入无效</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">replace</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">/[xX]/</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">输入不符合身份证号规则，仅最后一位可以为</span><span style="color: rgb(255,0,170);">x</span><span style="color: rgb(255,0,170);">或</span><span style="color: rgb(255,0,170);">X' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            return true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPaste</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">身份证号长度不超过</span><span style="color: rgb(255,0,170);">18</span><span style="color: rgb(255,0,170);">位</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">checkIncludeWord</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">输入不符合身份证号规则，除最后一位可为数字或大小写</span><span style="color: rgb(255,0,170);">X</span><span style="color: rgb(255,0,170);">外，其余应为数字</span><span style="color: rgb(255,0,170);">'</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">checkIncludeWord</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">检测粘贴内容包含英文字母且非最后一位为</span><span style="color: rgb(128,128,128);">x</span><span style="color: rgb(128,128,128);">的情况</span>
  let <span style="color: rgb(0,0,255);">groups </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[a-zA-Z]'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">groups </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">groups</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">groups</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">endsWith</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'x'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">endsWith</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'X'</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return true<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  return false<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 首位不允许出现空格。利用[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)事件监听将要输入的字符，如果字符以空格开头则阻止输入：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample3 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在将要输入时调用的回调。在返回</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">时，表示正常插入，返回</span><span style="color: rgb(128,128,128);">false</span><span style="color: rgb(128,128,128);">时，表示不插入。</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startsWith</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            return true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 限制输入中文、英文、数字或者emoji表情包。TextInput的[inputFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#inputfilter8)属性支持输入正则表达式，以下使用正则表达式限制中文字符输入：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample4 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[^</span>\u<span style="color: rgb(255,0,170);">4e00-</span>\u<span style="color: rgb(255,0,170);">9fa5]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">限制输入中文内容 ：</span><span style="color: rgb(255,0,170);"> '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 使用TextInput的[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)属性限制emoji表情包输入：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample5 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">EditableTextChangeValue</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">表情不包括数字</span>
          let <span style="color: rgb(0,0,255);">regx1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">/\p{Emoji}(?</span><span style="color: rgb(255,0,170);"><</span><span style="color: rgb(255,0,170);">!\p{N})/gu</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">数字表情</span>
          let <span style="color: rgb(0,0,255);">regx2 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">/[\d#*]\uFE0F?\u20E3/gu</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">圆圈数字表情</span>
          let <span style="color: rgb(0,0,255);">regx3 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">/[\u2460-\u24FF\u3250-\u32FF]/g</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">regx1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">regx2</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">regx3</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            return true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

5. 限制输入两位小数。利用inputFilter限制输入格式，并在[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)方法内使用parseFloat和toFixed方法组合使其保留两位小数，最后限制输入的小数不超过两位：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample6 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">insertValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">输入的值</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">insertValue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">InputType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NUMBER_DECIMAL</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">input </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseFloat</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">input</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">toFixed</span><span style="color: rgb(128,128,128);">方法将浮点数格式化为保留两位小数的字符串</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">insertValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toFixed</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">insertValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">((</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">insertValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'.'</span><span style="color: rgb(0,0,255);">)[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          return true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'^-?</span>\\<span style="color: rgb(255,0,170);">d*</span>\\<span style="color: rgb(255,0,170);">.?</span>\\<span style="color: rgb(255,0,170);">d{0,2}$'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">限制输入两位小数 ：</span><span style="color: rgb(255,0,170);"> '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

6. 限制输入数字范围。使用TextInput的inputFilter属性限制只能输入负号和数字，并通过[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)事件处理输入内容以满足要求。以下为限制输入数字范围-50~150：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample7 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入</span><span style="color: rgb(255,0,170);">-50~150'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[</span>\-<span style="color: rgb(255,0,170);">0-9]'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInputExample </span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);"> ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'-'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          let <span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isNaN</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'0'</span><span style="color: rgb(181,106,1);">;</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">num </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'-50'</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">num </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">150</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'150'</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```

7. 限制输入的长度。
限制文本的内容长度，比如不超过20个字符。

  TextInput的[maxLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#maxlength)属性可以限制文本的最大输入字符数：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample8 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLength</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

8. 限制文本的字节数量，比如不超过32个字节。

  TextInput的onWillChange事件在输入内容发生变化前触发，获取到输入的字符串后循环遍历内容，利用charCodeAt方法获取该字符的UniCode码，若UniCode码>255则为中文，可以判断为2个字符。代码实现如下：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample9 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">lastText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">getByteLength</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">charCode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charCodeAt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">charCode </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">0xff) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    return <span style="color: rgb(0,0,255);">byteLength</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'input your word...'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'70%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'58'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">input </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">num </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByteLength</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">input</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">num </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">32</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">' '</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastText</span><span style="color: rgb(181,106,1);">;</span>
            return false<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lastText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">input</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">input</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          return true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


  
> [!NOTE]
> 限制TextInput组件输入的文本长度，当输入超过限制长度时，输入框会闪烁一下，然后显示限制长度内的文本内容。


  解决方案：使用onWillChange回调，在输入前对输入内容做判断，限制显示内容的长度。
 
 

#### 常见FAQ

Q：TextInput和TextArea如何禁止输入？
 
A：可以设置输入框组件enabled属性为false来禁用文本输入。
 
Q：常见的用正则表达式过滤的场景有哪些？
 
A：较为常见的有英文和数字的过滤、中文的过滤以及手机号、邮箱、身份证号、银行卡号等表单验证场景。
 
Q：TextInput组件使用inputFilter字符串匹配无效，怎么处理？
 
A：TextInput组件的inputFilter仅支持单个字符匹配，粘贴时，inputFilter可以多字符匹配。可通过onWillChange事件处理文本内容。
 
Q：以上方法在其他组件适用吗？
 
A：TextInput、TextArea、Search都是输入框组件，以上方法在TextArea上也适用。
 
Q：如何只禁用空格键？
 
A：可以通过TextInput的inputFilter属性设置支持输入的正则表达式。参考示例如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextInputExample10 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">禁止空格输入</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputFilter</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'^[^</span>\\<span style="color: rgb(255,0,170);">s]*$'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TextInputExample </span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);"> '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">val</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
Q：inputFilter( '^\\d*$' )过滤，会让键盘输入不能是负数，为什么还会导致通过手动设置的方式也无法设置负数？
 
A：通过软键盘输入、粘贴板粘贴、TextInput的text属性直接赋值、addText的方式都可以触发inputFilter过滤，是规格如此，所以即使通过粘贴板粘贴、addText的方式都无法输入负数。
 
Q：TextInput如何实现多行显示？
 
A：给TextInput的[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#style9)设置为[TextInputStyle.Inline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textinputstyle9枚举说明)内联输入风格后，再设置maxLines可实现多行显示。
 
 

#### 总结

TextInput限制输入主要在内容格式以及长度方面。设置type、inputFilter以及maxLength属性即可快速达到所需限制效果，如果需要自定义实现限制策略，则可以使用onWillChange事件获取到用户输入的内容，然后针对字符串进行限制处理。
