# 常见数据格式与ArrayBuffer的互相转换

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-175

#### 问题现象

ArrayBuffer是HarmonyOS开发中经常用到的数据类型，很多接口的入参都要求是ArrayBuffer，如何将一些常见的数据类型转换为ArrayBuffer类型？
 
 

#### 背景知识

- [Base64Helper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#base64helper9)：Base64Helper类提供Base64编解码和Base64URL编解码功能。
- [TextEncoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textencoder)：TextEncoder将字符串编码为字节数组，支持多种编码格式。

 
 

#### 解决方案

**Base64与ArrayBuffer互相转换**
 
Base64转ArrayBuffer：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">Base64</span><span style="color: rgb(128,128,128);">格式字符串转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">类型</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src Base64</span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">base64ToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  let <span style="color: rgb(0,0,255);">base64Helper </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Base64Helper</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">base64Helper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
ArrayBuffer转Base64：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">转换为</span><span style="color: rgb(128,128,128);">Base64</span><span style="color: rgb(128,128,128);">格式</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">数据</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns Base64</span><span style="color: rgb(128,128,128);">格式字符串</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">arrayBufferToBase64</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">转成</span><span style="color: rgb(128,128,128);">string</span><span style="color: rgb(128,128,128);">，再编码成</span><span style="color: rgb(128,128,128);">base64</span></em>
  let <span style="color: rgb(0,0,255);">textDecoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'utf-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">textDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeToString</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
**string与ArrayBuffer的互相转换**
 
string转ArrayBuffer：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将字符串转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src </span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">stringToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  let <span style="color: rgb(0,0,255);">textEncoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextEncoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UTF-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">textEncoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeInto</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
ArrayBuffer转string：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式转换为字符串</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns </span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">arrayBufferToString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">textDecoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UTF-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">textDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeToString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
**collections.ArrayBuffer与ArrayBuffer的互相转换**
 
collections.ArrayBuffer转ArrayBuffer：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">CollectionsArrayBufferToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  let <span style="color: rgb(0,0,255);">collectionsUint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
ArrayBuffer转collections.ArrayBuffer：
 
```text
<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据转换为</span><span style="color: rgb(128,128,128);">collections.ArrayBuffer</span></em>
<em><span style="color: rgb(128,128,128);"> * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> * @returns collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(0,0,255);">public static </span><span style="color: rgb(0,0,255);">ArrayBufferToCollectionsArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  let <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
完整代码及测试样例如下：
 
pages/Index.ets：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">StringUtil</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Base64Util</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">CollectionsArrayBufferUtil </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'../utils/ArrayBufferUtil'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">collections </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Base64</span><span style="color: rgb(255,0,170);">与</span><span style="color: rgb(255,0,170);">Arraybuffer</span><span style="color: rgb(255,0,170);">互相转换</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">base64 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'SGVsbG8gSGFybW9ueU9TLCBIZWxsbyBXb3JsZC4='</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Base64Util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">base64ToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">base64</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">base64 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Base64Util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arrayBufferToBase64</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">base64</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'string</span><span style="color: rgb(255,0,170);">和</span><span style="color: rgb(255,0,170);">ArrayBuffer</span><span style="color: rgb(255,0,170);">互相转换</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">str </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello HarmonyOS, Hello World.'</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">StringUtil</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">str </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">StringUtil</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arrayBufferToString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'collections.ArrayBuffer</span><span style="color: rgb(255,0,170);">与</span><span style="color: rgb(255,0,170);">ArrayBuffer</span><span style="color: rgb(255,0,170);">互相转换</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">array </span><span style="color: rgb(181,106,1);">=</span>
            <span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">101</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">108</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">108</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">111</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">97</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">114</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">109</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">111</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">110</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">121</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">79</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">83</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">44</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">101</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">108</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">108</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">111</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,0);">87</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">111</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">114</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">108</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">46</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">collectionsArrayBuffer </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CollectionsArrayBufferUtil</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CollectionsArrayBufferToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">collectionsArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">collectionsArrayBuffer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CollectionsArrayBufferUtil</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBufferToCollectionsArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ret</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`collectionsArrayBuffer.byteLength: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">collectionsArrayBuffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
utils/ArrayBufferUtil.ets：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">提供</span><span style="color: rgb(128,128,128);">Base64</span><span style="color: rgb(128,128,128);">格式数据与</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">的互相转换能力</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
export class <span style="color: rgb(0,0,255);">Base64Util </span><span style="color: rgb(255,0,170);">{</span>
  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">Base64</span><span style="color: rgb(128,128,128);">格式字符串转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">类型</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src Base64</span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">base64ToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">base64Helper </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Base64Helper</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">base64Helper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>


  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">转换为</span><span style="color: rgb(128,128,128);">Base64</span><span style="color: rgb(128,128,128);">格式</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns Base64</span><span style="color: rgb(128,128,128);">格式字符串</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">arrayBufferToBase64</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return <span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">转成</span><span style="color: rgb(128,128,128);">string</span><span style="color: rgb(128,128,128);">，再编码成</span><span style="color: rgb(128,128,128);">base64</span></em>
    let <span style="color: rgb(0,0,255);">textDecoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'utf-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">textDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeToString</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">;</span>

<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">提供</span><span style="color: rgb(128,128,128);">string</span><span style="color: rgb(128,128,128);">格式数据与</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">的互相转换能力</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
export class <span style="color: rgb(0,0,255);">StringUtil </span><span style="color: rgb(255,0,170);">{</span>
  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将字符串转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src </span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">stringToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">textEncoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextEncoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UTF-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">textEncoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeInto</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>


 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式转换为字符串</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns </span><span style="color: rgb(128,128,128);">字符串</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">arrayBufferToString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">textDecoder </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UTF-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">textDecoder</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeToString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(255,0,170);">}</span>

<em>/**</em>
<em><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">提供</span><span style="color: rgb(128,128,128);">collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据与</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">的互相转换能力</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
export class <span style="color: rgb(0,0,255);">CollectionsArrayBufferUtil </span><span style="color: rgb(255,0,170);">{</span>
<em>  <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据转换为</span><span style="color: rgb(128,128,128);">ArrayBuffer</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">CollectionsArrayBufferToArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">collectionsUint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>


  <em><span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据转换为</span><span style="color: rgb(128,128,128);">collections.ArrayBuffer</span></em>
<em><span style="color: rgb(128,128,128);">   * @param src ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns collections.ArrayBuffer</span><span style="color: rgb(128,128,128);">格式数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  public static <span style="color: rgb(0,0,255);">ArrayBufferToCollectionsArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">byteLength </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uint8Array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">collectionsUint8Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer </span>as <span style="color: rgb(0,0,255);">collections</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(255,0,170);">}</span>
```
