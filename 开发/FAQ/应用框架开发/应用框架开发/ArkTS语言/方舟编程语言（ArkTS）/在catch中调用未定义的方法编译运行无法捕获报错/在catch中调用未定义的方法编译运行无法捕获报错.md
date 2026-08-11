# 在catch中调用未定义的方法编译运行无法捕获报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-181

#### 问题现象

定义了一个异步函数，使用try-catch来捕获可能出现的异常，如果在catch中调用未定义的方法，代码能正常编译，运行时也没有任何错误提示，但是catch之后的代码不会执行。问题代码示例参考如下：
 
```text
export async function <span style="color: rgb(0,0,255);">getLocalImgOrientation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">oriFilePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">orientation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  try <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">Logger</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'try called'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">oriFilePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_ONLY</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ImageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">orientation </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImageProperty</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PropertyKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ORIENTATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">Logger</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'catch called'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// sayHello()</span><span style="color: rgb(128,128,128);">是一个没有声明和定义的不存在的函数，但是编译不会报错</span></em>
    <span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sayHello</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处日志不会被打印</span></em>
  <span style="color: rgb(255,255,255);">Logger</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'tag one'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">rotate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">orientation</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">rotate </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">90</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  return <span style="color: rgb(255,255,255);">rotate</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
调用代码示例参考如下：
 
```text
<span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">异步任务中调用不存在函数</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传入一个错误参数，模拟发生异常</span></em>
    let <span style="color: rgb(255,255,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'empty'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">getLocalImgOrientation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">Logger</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`r is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
```
 
 

#### 背景知识

[async/await](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/async-concurrency-overview#asyncawait)：基于Promise的语法糖，async函数本身并不会直接定义微任务，但它内部的异步操作（尤其是await后面的代码）会以微任务的形式执行。
 
 

#### 解决方案

异常发生时，catch的参数e类型为any，此时调用了未定义的函数编译器无法报错属于正常现象。async函数内部的异步任务是以微任务的形态执行的，执行失败不会导致整个进程crash，也不会导致运行报错。可以通过在调用的外层函数处增加catch来捕获报错。
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">传入一个错误参数，模拟发生异常</span></em>
let <span style="color: rgb(255,255,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'empty'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">getLocalImgOrientation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`r is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
运行后控制台会打印错误日志“code: undefined, undefined is not callable”。
 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,255,255);">fs </span>from <span style="color: rgb(132,63,161);">'@ohos.file.fs'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">image </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ImageKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">异步任务中调用不存在函数</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传入一个错误参数，模拟发生异常</span></em>
          let <span style="color: rgb(255,255,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'empty'</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">getLocalImgOrientation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`r is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">r</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

async function <span style="color: rgb(0,0,255);">getLocalImgOrientation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">oriFilePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">orientation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  try <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'try called'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">oriFilePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fs</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_ONLY</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ImageSource </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createImageSource</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">orientation </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">imageSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImageProperty</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">image</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PropertyKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ORIENTATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'try called'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// sayHello()</span><span style="color: rgb(128,128,128);">是一个没有声明和定义的不存在的函数，但是编译不会报错</span></em>
    <span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sayHello</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处日志不会被打印</span></em>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'tag'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">rotate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">orientation</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">rotate </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">90</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  return <span style="color: rgb(255,255,255);">rotate</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
