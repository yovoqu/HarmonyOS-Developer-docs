# ArkTS是否支持Partial类型

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-174

#### 问题现象

ArkTS是否支持Partial类型，如何使用？
 
 

#### 背景知识

Partial是TypeScript（简称TS）一个内置的泛型工具类型，作用是将目标类型的所有属性变为可选属性，即给每个属性添加?修饰符。
 
ArkTS是HarmonyOS应用的默认开发语言，在TS生态基础上做了扩展，是兼容TS/JavaScript（简称JS）生态的，因此也支持Partial。
 
HarmonyOS系统对TS/JS支持的详细情况见[兼容TS/JS的约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-migration-background#方舟运行时兼容tsjs)。
 
 

#### 解决方案

假设声明了一个表示用户信息的接口User：
 
```text
interface User <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">age</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">email</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
在默认情况下，User类型的变量必须包含name、age、email三个属性，缺一不可，否则编辑器就会出现"Property 'xxx' is missing in type..."的报错提示。而使用Partial后，得到的新类型中的所有属性都会变为可选，此时PartialUser类型的变量可以只包含部分属性，甚至为空：
 
```text
type PartialUser <span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">Partial</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">User</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(255,255,255);">pUser</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PartialUser </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Alice'</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 
完整示例参考如下：
 
```text
interface User <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">age</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">email</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>


<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PartialDemo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Partial</span><span style="color: rgb(132,63,161);">类型</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          type PartialUser <span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">Partial</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">User</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">pUser</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PartialUser </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Alice'</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
