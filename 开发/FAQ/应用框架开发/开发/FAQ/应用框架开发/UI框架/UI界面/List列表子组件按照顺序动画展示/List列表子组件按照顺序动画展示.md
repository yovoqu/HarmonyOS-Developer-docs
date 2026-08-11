# List列表子组件按照顺序动画展示

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-651

#### 问题现象

列表（List）通常会一次性全部展示出来，那么如何实现列表中的子组件能够依照链式先后顺序动画进行展示？
 
 

#### 背景知识

组件的某些通用属性变化时，可以通过[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)属性动画实现渐变过渡效果。
 
 

#### 解决方案
1. 根据数据源this.data创建List。
```text
if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">CardItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 创建List的每个子组件CardItem,该组件可以根据其在列表中的索引（index）来计算出一个适当的延迟时间，从而实现一种链式的动画效果，即前一个动画结束之后，下一个动画随即开始。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EaseOut</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
```

3. 当CardItem组件首次出现在视图中（即onAppear事件被触发时），将启动该组件的入场动画。
```text
.onAppear(() => {
  <span style="color: rgb(132,63,161);">this.isAppear = </span><span style="color: rgb(181,106,1);">true</span>;
})
.onDisAppear(() => {
  <span style="color: rgb(132,63,161);">this.isAppear = </span><span style="color: rgb(181,106,1);">false</span>;
})
```

4. 完整示例参考如下：
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CardItem </span><span style="color: rgb(181,106,1);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">List</span><span style="color: rgb(128,128,128);">的每个子组件</span><span style="color: rgb(128,128,128);">CardItem</span></em>
  <span style="color: rgb(181,106,1);">@Prop </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isAppear</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">24</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Green</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">60</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">opacity</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isAppear </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">translate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isAppear </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(255,0,170);">)</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">增加动画效果</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">120</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">EaseOut</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件出现启动组件的入场动画</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isAppear </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDisAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isAppear </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ChainList </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否展示</span><span style="color: rgb(128,128,128);">List</span></em>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'show list'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据数据源</span><span style="color: rgb(128,128,128);">this.data</span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">List</span></em>
      if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">CardItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
 

#### 总结

属性动画（animation）能够与诸如列表(List)之类的组件相配合，通过调整这些组件的特定属性，如width、height、backgroundColor等，实现一系列动态视觉效果。
