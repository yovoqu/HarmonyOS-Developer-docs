# ArkTS中as类型断言常见场景以及注意事项

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-182

#### 问题现象

- **场景一：** 使用as类型断言不能转换JSON.parse()方法解析的JSON字符串中成员属性的数据类型。举例说明：
```json
<em>// </em><em><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">ItemModel</span><span style="color: rgb(128,128,128);">类接收</span><span style="color: rgb(128,128,128);">responseData</span><span style="color: rgb(128,128,128);">中</span><span style="color: rgb(128,128,128);">JSON</span><span style="color: rgb(128,128,128);">字符串的内容</span></em>
let <span style="color: rgb(0,0,255);">responseData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`{"id":123,"name":"Example","price":200}` </span><em>// </em><em><span style="color: rgb(128,128,128);">在</span><span style="color: rgb(128,128,128);">responseData</span><span style="color: rgb(128,128,128);">中的</span><span style="color: rgb(128,128,128);">price</span><span style="color: rgb(128,128,128);">值为</span><span style="color: rgb(128,128,128);">number</span><span style="color: rgb(128,128,128);">类型的</span><span style="color: rgb(128,128,128);">200</span></em>

class <span style="color: rgb(0,0,255);">ItemModel </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">作为接收类的</span><span style="color: rgb(128,128,128);">ItemModel</span><span style="color: rgb(128,128,128);">中</span><span style="color: rgb(128,128,128);">price</span><span style="color: rgb(128,128,128);">类型为</span><span style="color: rgb(128,128,128);">string</span></em>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">JSON.parse()</span><span style="color: rgb(128,128,128);">解析</span><span style="color: rgb(128,128,128);">JSON</span><span style="color: rgb(128,128,128);">字符串，并用</span><span style="color: rgb(128,128,128);">as</span><span style="color: rgb(128,128,128);">得到</span><span style="color: rgb(128,128,128);">ItemModel</span><span style="color: rgb(128,128,128);">类型实例</span></em>
let <span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">responseData</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">ItemModel</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">此时得到</span><span style="color: rgb(128,128,128);">item.price</span><span style="color: rgb(128,128,128);">类型为</span><span style="color: rgb(128,128,128);">number</span><span style="color: rgb(128,128,128);">而非定义的</span><span style="color: rgb(128,128,128);">string</span></em>
<span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`typeofprice: </span><span style="color: rgb(255,0,170);">${</span>typeof <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出为</span><span style="color: rgb(128,128,128);">typeofprice:number</span></em>
```

- **场景二：** 使用params为options赋值，但是as number未生效，options接收到的依旧是带引号的string类型。
```text
<span style="color: rgb(0,0,255);">private </span><span style="color: rgb(181,106,1);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">mapCommon</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MapOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">zoom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(255,0,170);">'latitude'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'39.9'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">'longitude'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'116.4'</span>
<span style="color: rgb(255,0,170);">}</span>

this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">latitude </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">lat</span><span style="color: rgb(181,106,1);">;</span>
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">longitude </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">lon</span><span style="color: rgb(181,106,1);">;</span>
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/pt7CoDK6SHipRttT98n8MA/zh-cn_image_0000002629058992.png?HW-CC-KV=V1&HW-CC-Date=20260701T041130Z&HW-CC-Expire=86400&HW-CC-Sign=50543E9EA657930482440D1F901AEB5D0285397BF725D9D4149EA8B28024AD52)

- **场景三：** 对对象类型使用类型断言，DevEco Studio静态检查报错Object literal must correspond to some explicitly declared class or interface (arkts-no-untyped-obj-literals) &lt;ArkTSCheck&gt;：
```text
interface <span style="color: rgb(0,0,255);">Test </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">a</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">b</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

const <span style="color: rgb(0,0,255);">a </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">a</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'aa'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">b</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'bb'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">c</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'cc'</span>
<span style="color: rgb(255,0,170);">} </span>as <span style="color: rgb(0,0,255);">Test</span>
```


 
 

#### 背景知识

- 在ArkTS中，as关键字是类型断言的一种语法，它不会在运行时改变值的类型，只是在编译阶段告知编译器以特定类型来处理这个值；
- 参考官方文档[JSON.parse()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json#jsonparse)的用法和[构造函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts#构造函数)的使用。

 
 

#### 解决方案

- **场景一：**
方案一：可以为ItemModel类定义构造函数，在构造函数中实现类型转换。示例代码如下：
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">JSON </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">solution1Builder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">solution1</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>
class <span style="color: rgb(0,0,255);">ItemModel </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">这里定义构造函数，将输入的</span><span style="color: rgb(128,128,128);">price</span><span style="color: rgb(128,128,128);">转为</span><span style="color: rgb(128,128,128);">string</span><span style="color: rgb(128,128,128);">类型</span></em>
  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">JSON</span><span style="color: rgb(128,128,128);">字符串数据</span></em>
let <span style="color: rgb(0,0,255);">responseData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`{"id":123,"name":"Example","price":200}`</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">responseData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">solution1 </span><span style="color: rgb(255,0,170);">{</span>
  public <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Click to test'</span><span style="color: rgb(181,106,1);">;</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">new</span><span style="color: rgb(128,128,128);">调用构造函数，构造新的</span><span style="color: rgb(128,128,128);">ItemModel</span></em>
  public <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemModel </span><span style="color: rgb(181,106,1);">=</span>
    new <span style="color: rgb(0,0,255);">ItemModel</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'id'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'name'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'price'</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Click to test'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用模型数据</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item ID:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item ID:123</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item Name:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item Name:Example</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item Price:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item Price:200</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`typeof Price:</span><span style="color: rgb(255,0,170);">${</span>typeof this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">验证输出</span><span style="color: rgb(128,128,128);">typeof Price:string</span></em>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
- 方案二：利用JSON.parse的reviver参数，手动转换key为price时value的类型。示例代码如下：
```text
<em>// </em><em><span style="color: rgb(128,128,128);">新建</span><span style="color: rgb(128,128,128);">ts</span><span style="color: rgb(128,128,128);">文件，写入类型转换逻辑</span></em>
<em><span style="color: rgb(128,128,128);">// entry/src/main/ets/pages/test.ts</span></em>
export function <span style="color: rgb(0,0,255);">reviverFunc</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">key </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">"price"</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">num_price </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">String</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">)</span>
    return <span style="color: rgb(0,0,255);">num_price</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  return <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">JSON </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">reviverFunc </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./test'</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">导入</span><span style="color: rgb(128,128,128);">reviverFunc</span></em>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">solution2Builder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">solution2</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

class <span style="color: rgb(0,0,255);">ItemModel </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">price</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">JSON</span><span style="color: rgb(128,128,128);">字符串数据</span></em>
let <span style="color: rgb(0,0,255);">responseData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`{"id":123,"name":"Example","price":200}`</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">solution2 </span><span style="color: rgb(255,0,170);">{</span>
  public <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Click to test'</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用</span><span style="color: rgb(128,128,128);">JSON.parse</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">reviverFunc</span><span style="color: rgb(128,128,128);">参数，创建</span><span style="color: rgb(128,128,128);">item</span><span style="color: rgb(128,128,128);">实例</span></em>
  public <span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">responseData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reviverFunc</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">ItemModel</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Click to test'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用模型数据</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item ID:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item ID:123</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item Name:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item Name:Example</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Item Price:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出</span><span style="color: rgb(128,128,128);">:Item Price:200</span></em>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`typeof Price:</span><span style="color: rgb(255,0,170);">${</span>typeof this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">price</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">验证输出</span><span style="color: rgb(128,128,128);">typeof Price:string</span></em>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 
- **场景二：**将params类型改为Record<string, number>或者将value值去掉引号（''），在ArkTS中，as关键字是类型断言的一种语法，它不会在运行时改变值的类型，只是在编译阶段告知编译器以特定类型来处理这个值。
- **场景三：**断言类型Test与被断言对象的类型不完全一致，阅读示例代码发现类型Test缺少了一个名为c的属性，在类型Test中增加该属性的声明即可。
