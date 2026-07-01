# @Consume和@ObjectLink的核心差异是什么

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-916

#### 问题现象

在HarmonyOS的ArkUI开发中，@Consume和@ObjectLink装饰器均可实现跨组件状态共享，它们的核心差异是什么？
 
 

#### 背景知识

- [@Provide和@Consume装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume)，应用于组件与其后代组件的双向数据同步。在祖先组件中通过@Provide装饰变量，以此给所有后代组件提供状态变量，后代组件中通过@Consume装饰的变量来接收这些状态变量，实现跨组件状态共享。
- 在实际应用开发中，应用会根据开发需要，封装自己的数据模型。对于数据模型多层嵌套的场景，[@Observed/@ObjectLink装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)配套使用可以弥补@Provide/@Consume装饰器仅能观察一层的能力限制。

 
 

#### 解决方案

- @Provide和@Consume作用于多层组件的参数传递，其中@Consume为数据消费方，可以通过绑定同样的key获取其最近父节点的@Provide的数据，@Provide和@Consume装饰数据类型需要一致。示例代码参考如下：
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SceneOneChild </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Consume </span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'child increase the day by 1'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setDate</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDate</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'child update the new date'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'2023-09-09'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">DatePicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">start</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1970-1-1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">end</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'2100-1-1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">selected</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SceneOneParent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Provide </span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Date </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'2021-08-08'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'parent increase the day by 1'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setDate</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDate</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'parent update the new date'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'2023-07-07'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">DatePicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">start</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1970-1-1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">end</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'2100-1-1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">selected</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedDate</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">SceneOneChild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- @Provide和@Consume只能观察到嵌套对象的第一层属性变化。而@Observed和@ObjectLink作用于父子组件间复杂对象的深层嵌套观察。示例代码参考如下：
```text
<span style="color: rgb(181,106,1);">@Observed</span>
class <span style="color: rgb(0,0,255);">Info </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SceneTwoChild </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@ObjectLink </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Info</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`num</span><span style="color: rgb(255,0,170);">的值</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">正确写法，可以更改</span><span style="color: rgb(128,128,128);">@ObjectLink</span><span style="color: rgb(128,128,128);">装饰变量的成员属性</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SceneTwoParent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Info </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`count</span><span style="color: rgb(255,0,170);">的值</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'click'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可以在父组件做整体替换</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">num </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">SceneTwoChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">num </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 总结
 
| 装饰器 | 用法差异 | 功能差异 |
| --- | --- | --- |
| @Consume/@Provide | 父子组件传参，通过key同步数据，无需使用子组件时手动传参。 | 适用于多层组件嵌套的场景，实现跨层数据双向同步，若数据为嵌套对象只能感知第一层属性变化，无法进行深层数据变化感知。 |
| @Observed/@ObjectLink | 父子组件传参，调用子组件时需要传入参数，并通过@ObjectLink接收。 | 适用于父子组件之间双向同步复杂对象/对象数组的场景，实现嵌套对象深层属性变化的感知，并刷新渲染UI。 |
