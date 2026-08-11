# 自定义UI组件无类型、无id，UI测试该如何操作

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-21

#### 问题现象

组件测试，UI测试，自定义UI组件无法通过类型找到，也无id属性，应该怎么操作？
 
 

#### 背景知识

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。
 
On提供的API能力具有以下几个特点:
 1. 支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。
2. 控件属性支持多种匹配模式。
3. 支持控件绝对定位，相对定位，可通过ON.isBefore和ON.isAfter等API限定邻近控件特征进行辅助定位。
 
On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。
 
UiTest API文档：[UI Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#on9)。
 
 

#### 解决方案

如果不能通过类型或id找到，可以尝试通过text、描述、组件的位置关系等进行定位。
 
```text
async function <span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">driver</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Driver </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Driver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">on</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">On </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'456'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isBefore</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'123'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">查找</span><span style="color: rgb(128,128,128);">text</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">123</span><span style="color: rgb(128,128,128);">之前的第一个</span><span style="color: rgb(128,128,128);">text</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">456</span><span style="color: rgb(128,128,128);">的组件</span></em>
  let <span style="color: rgb(0,0,255);">button</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Component </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">driver</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">findComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  await <span style="color: rgb(0,0,255);">button</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>
```
