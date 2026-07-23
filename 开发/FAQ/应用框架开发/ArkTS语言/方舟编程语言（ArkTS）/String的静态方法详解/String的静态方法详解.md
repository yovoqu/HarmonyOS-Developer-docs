# String的静态方法详解

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-180

#### 问题现象

在开发HarmonyOS应用时，开发者需根据字符编码生成字符串，或处理包含转义字符的模板字符串。若不了解String.fromCharCode()、String.fromCodePoint()和String.raw()三个静态方法的使用场景与差异，容易导致字符生成错误或模板字符串处理异常。
 
 

#### 背景知识

在JavaScript中，String是一个内置对象，提供一系列静态方法用于处理字符与字符串。在HarmonyOS应用开发中，基于JS语言的ArkTS（ArkUI TypeScript）同样支持这些方法。
 
- String.fromCharCode()：将一组Unicode码点（0–65535）转换为对应的字符串。仅支持16位的BMP（基本多文种平面）字符。
- String.fromCodePoint()：支持更广范围的Unicode码点（包括代理对），能正确处理超出BMP的字符（如Emoji表情、古文字等）。
- String.raw()：用于创建“原始模板字符串”（raw template string），其中转义字符（如\n、\t）不会被解析，而是作为字面量保留。

 
 

#### 解决方案
1. 使用String.fromCharCode()生成基础字符。当需要根据Unicode码点（0–65535）生成字符串时，使用String.fromCharCode()。

  
```text
<em>// </em><em><span style="color: rgb(128,128,128);">生成字母</span><span style="color: rgb(128,128,128);">'A'</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">'Z'</span></em>
const <span style="color: rgb(0,0,255);">charA </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">65</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">charZ </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">charA</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">charZ</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">生成数字</span><span style="color: rgb(128,128,128);">'0'</span><span style="color: rgb(128,128,128);">到</span><span style="color: rgb(128,128,128);">'9'</span></em>
const <span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">48</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">57</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">join</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
```
 
> [!NOTE]
> 适用场景：处理ASCII或基本拉丁字符，不涉及Emoji或特殊符号。

2. 使用String.fromCodePoint()支持完整Unicode。当需要处理超出16位范围的Unicode字符（如：、、）时，必须使用String.fromCodePoint()。

  
```text
<em>// </em><em><span style="color: rgb(128,128,128);">生成地球</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span></em>
const <span style="color: rgb(0,0,255);">earth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F30D)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">earth</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">生成程序员</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span></em>
const <span style="color: rgb(0,0,255);">programmer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F469</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F4BB)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">programmer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">生成家庭</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span></em>
const <span style="color: rgb(0,0,255);">family </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F468</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F469</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F467</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F466)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">family</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
> [!NOTE]
> String.fromCharCode()对于代理对（如0xD83D和0xDCCD）会返回错误字符，而fromCodePoint()可正确处理。

3. 使用String.raw()获取原始模板字符串。当需要在模板字符串中保留原始的转义字符（如\n、\t、\\）时，应使用String.raw()。

  
```text
<em>// </em><em><span style="color: rgb(128,128,128);">普通模板字符串：转义字符会被解析</span></em>
const <span style="color: rgb(0,0,255);">normalStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第一行</span><span style="color: rgb(255,0,170);">\n</span><span style="color: rgb(255,0,170);">第二行</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">normalStr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">String.raw()</span><span style="color: rgb(128,128,128);">：转义字符作为字面量保留</span></em>
const <span style="color: rgb(0,0,255);">rawStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">raw</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第一行</span><span style="color: rgb(255,0,170);">\n</span><span style="color: rgb(255,0,170);">第二行</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">rawStr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">处理路径字符串（避免反斜杠被转义）</span></em>
const <span style="color: rgb(0,0,255);">filePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">raw</span><span style="color: rgb(255,0,170);">`C:\Users\John\Documents`</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
> [!NOTE]
> 适用场景：构建正则表达式、路径字符串、日志格式、多行文本模板等需要保留转义字符的场景。

 
完整示例参考如下：
 
```text
import <span style="color: rgb(0,0,255);">hilog </span>from <span style="color: rgb(255,0,170);">'@ohos.hilog'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">StringStaticMethod </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'fromCharCode'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">生成字母</span><span style="color: rgb(128,128,128);">'A'</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">'Z'</span></em>
          const <span style="color: rgb(0,0,255);">charA </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">65</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">charZ </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">charA</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">charZ</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">生成数字</span><span style="color: rgb(128,128,128);">'0'</span><span style="color: rgb(128,128,128);">到</span><span style="color: rgb(128,128,128);">'9'</span></em>
          const <span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
          for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">48</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">57</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCharCode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">digits</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">join</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'fromCodePoint'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>// </em><em><span style="color: rgb(128,128,128);">生成地球</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span></em>
          const <span style="color: rgb(0,0,255);">earth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F30D)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">earth</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">生成程序员</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span></em>
          const <span style="color: rgb(0,0,255);">programmer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F469</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F4BB)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">programmer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">生成家庭</span><span style="color: rgb(128,128,128);">Emoji</span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span><span style="color: rgb(128,128,128);"></span></em>
          const <span style="color: rgb(0,0,255);">family </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromCodePoint</span><span style="color: rgb(0,0,255);">(0x1F468</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F469</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F467</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x200D</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x1F466)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">family</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'String.raw'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">普通模板字符串：转义字符会被解析</span></em>
          const <span style="color: rgb(0,0,255);">normalStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第一行</span><span style="color: rgb(255,0,170);">\n</span><span style="color: rgb(255,0,170);">第二行</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">normalStr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">String.raw()</span><span style="color: rgb(128,128,128);">：转义字符作为字面量保留</span></em>
          const <span style="color: rgb(0,0,255);">rawStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">raw</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第一行</span><span style="color: rgb(255,0,170);">\n</span><span style="color: rgb(255,0,170);">第二行</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">rawStr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">处理路径字符串（避免反斜杠被转义）</span></em>
          const <span style="color: rgb(0,0,255);">filePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">raw</span><span style="color: rgb(255,0,170);">`C:\Users\John\Documents`</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：String.fromCharCode()和String.fromCodePoint()有什么区别？
 
A：String.fromCharCode()仅支持16位码点（0–65535），不支持代理对；而String.fromCodePoint()支持完整的Unicode码点（包括Emoji和生僻字），能正确处理超出BMP的字符。
 
Q：为什么在处理Emoji时推荐使用String.fromCodePoint()？
 
A：Emoji通常由多个码点组成（如0x1F469+0x200D+0x1F4BB），这些码点可能包含代理对。String.fromCodePoint()能正确解析并组合这些码点，而fromCharCode()会失败或产生乱码。
 
Q：String.raw()与模板字符串中的raw属性有何关系？
 
A：String.raw()是一个静态方法，用于创建“原始模板字符串”。它实际上等价于调用模板字符串的raw属性，例如：String.raw等价于templateString.raw。
 
 

#### 总结

掌握String.fromCharCode()、String.fromCodePoint()和String.raw()三个静态方法，是编写高质量、跨平台兼容的HarmonyOS应用开发中不可或缺的能力。
 
- 使用fromCharCode()处理常见ASCII字符。
- 使用fromCodePoint()处理Emoji、多语言字符。
- 使用raw()保留模板字符串中的转义字符。

 
> [!NOTE]
> 举一反三：在处理国际化文本、日志输出、配置文件生成等场景时，可灵活结合这三个方法，提升代码可读性与健壮性。
