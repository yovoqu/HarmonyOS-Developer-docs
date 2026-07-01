# LazyForEach嵌套递归使用

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1015

#### 问题现象

树形结构列表如何高效渲染？
 
1. 数据量规模较大（4000+），如何保证页面渲染速度？
2. 结构多层嵌套，且层级深度不确定，如何遍历数据并绘制界面？
 

#### 背景知识

- [LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件，可以保证数据加载以及绘制的流畅度，提升使用体验。
- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。它适合用于高效地显示结构化、可滚动的信息。

 
 

#### 解决方案

通过递归的形式，按层级实现每一个子树，最后组合为完整的树形结构列表。
 
- 单个层级实现：使用LazyForEach组件按需加载当前层级的数据，避免一次性渲染所有数据，提升性能。
- 多层级实现：
通过递归的方式遍历数据，动态生成子层级的树形结构。
- 每个层级的LazyForEach组件需嵌套在List容器中，且List容器需设置固定高度或使用constraintSize属性限制高度，以确保懒加载机制生效。

 - 性能优化：
当数据量较大时，使用cachedCount属性控制懒加载的缓冲区大小，提升渲染效率。
- 使用constraintSize属性限制层级高度，避免无限拉伸影响用户体验。

 
 
示例代码如下：
 1. 主逻辑代码：
- 使用aboutToAppear生命周期钩子生成模拟数据。

2. 使用自定义递归函数Node遍历数据，每次递归使用LazyForEach组件渲染当前层级的数据项。

3. 通过点击事件控制子层级的展开与折叠。

4. 数据类型生成：
自定义数据数组类型：
```text
<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义数据数组类型</span>
<span style="color: rgb(181,106,1);">@Observed</span>
export class <span style="color: rgb(0,0,255);">ObservedArray</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> extends <span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">args </span>instanceof <span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      super<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      super<span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```


5. LazyForEach基础数据继承类：
```text
<span style="color: rgb(128,128,128);">// LazyForEach</span><span style="color: rgb(128,128,128);">基础数据继承类</span>
export class <span style="color: rgb(0,0,255);">BasicDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">T </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">warn</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Cannot read </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, please override getDate`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return undefined<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataReloaded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


6. LazyForEach数据源类：
```text
<span style="color: rgb(128,128,128);">//  LazyForEach</span><span style="color: rgb(128,128,128);">数据源类</span>
export class <span style="color: rgb(0,0,255);">LazyDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> extends <span style="color: rgb(0,0,255);">BasicDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">T </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">pushData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">pushArrayData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ObservedArray</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">newData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">pushDataPositionArray</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ObservedArray</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, ...</span><span style="color: rgb(0,0,255);">newData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">appendArrayData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ObservedArray</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">deleteData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getDataList</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ObservedArray</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">clear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">isEmpty</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


7. 数据对象：
```text
<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">数据对象</span>
export class <span style="color: rgb(0,0,255);">TreeData </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">parentId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">level</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">childList</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">LazyDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">TreeData</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">parentId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">level</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">childList</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">LazyDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">TreeData</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parentId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parentId</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">level </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">level</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">childList </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">childList</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 总结
1. LazyForEach需要关注[使用限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach#使用限制)。
2. 相关UI界面限制，使用通用constraintSize配置，防止数据组件过多，降低交互性。
