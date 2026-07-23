# 怎么获取被@ObservedV2观察的数据对应的原始数据

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-918

#### 问题现象

@ObservedV2装饰的对象中，被@Trace装饰的成员变量名前会被加上"__ob_"的前缀，怎样获取到原始的对象？
 
 

#### 背景知识

状态管理V2装饰器会为装饰的变量生成getter和setter方法，同时为原有变量名添加"__ob_"的前缀。出于性能考虑，getTarget接口不会对V2装饰器生成的前缀进行处理，因此向[getTarget](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement#gettarget)接口传入[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰的类对象实例时，返回的对象依旧为对象本身，且被@Trace装饰的属性名仍有"__ob_"前缀。
 
 

#### 解决方案

可以用状态管理V2对象初始化一个同结构的[状态管理V1的@Observed装饰器和@ObjectLink装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)对象，然后用getTarget接口获取V1对象的原始数据，这样获取的数据结构和V2对象的原始结构相同。详细步骤如下：1. 定义结构相同的V1、V2对象：
```text
<span style="color: rgb(181,106,1);">@ObservedV2</span>
class <span style="color: rgb(0,0,255);">FormDataClassV2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Observed</span>
class <span style="color: rgb(0,0,255);">FormDataClassV1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FormDataClassV2</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 用V2对象初始化V1对象：
```text
let <span style="color: rgb(0,0,255);">dataV1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FormDataClassV1 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">FormDataClassV1</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataV2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">V2</span><span style="color: rgb(128,128,128);">对象初始化</span><span style="color: rgb(128,128,128);">V1</span><span style="color: rgb(128,128,128);">对象</span></em>
```

3. 用getTarget接口获取原始数据：
```text
let <span style="color: rgb(0,0,255);">rawV1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">UIUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTarget</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dataV1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">getTarget</span><span style="color: rgb(128,128,128);">接口获取原始对象</span></em>
```

 
 
完整示例参考如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@ObservedV2</span>
class <span style="color: rgb(0,0,255);">FormDataClassV2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Observed</span>
class <span style="color: rgb(0,0,255);">FormDataClassV1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FormDataClassV2</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">FormDataClassPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">dataV2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FormDataClassV2 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">FormDataClassV2</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'HelloWorld'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">dataV1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FormDataClassV1 </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">FormDataClassV1</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataV2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">V2</span><span style="color: rgb(128,128,128);">对象初始化</span><span style="color: rgb(128,128,128);">V1</span><span style="color: rgb(128,128,128);">对象</span></em>
          let <span style="color: rgb(0,0,255);">rawV1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">UIUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTarget</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dataV1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">getTarget</span><span style="color: rgb(128,128,128);">接口获取原始对象</span></em>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">rawV1</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此时打印的日志不带</span><span style="color: rgb(128,128,128);">__ob_</span><span style="color: rgb(128,128,128);">框架</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：getTarget接口的使用场景有哪些？
 
A：getTarget可以获取代理对象的原始对象，修改原始对象数据，不会触发UI刷新。使用场景如下：
 
- 类型比较或者序列化场景，需要获取原始对象。
- 三方库集成场景，需要传原始对象数据。
- 大量修改数据场景，如数据排序等，对原始对象操作避免代理层性能开销。
