# 如何实现点击GridItem获取选中内容

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1235

#### 问题现象

使用Grid组件，如何实现点击item后高亮，再次点击则需要取消高亮，最后还要收集已选选项。
 
 

#### 背景知识

- [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
- [GridItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem)：网格容器中单项内容容器。

 
 

#### 解决方案
1. 实现功能时将GridItem内容抽取为独立组件，为item内容设置点击事件，通过点击时状态变量的变化控制item背景色变化。
2. 想要获取选中的item，则需要通过item的点击事件将点击时获取到的index插入到数组中，并通过indexOf判断点击内容是否已存在数组中，当不存在时，将选中内容插入数组；当存在时，则不做插入操作。
 
完整示例参考如下：
```json
class <span style="color: rgb(0,0,255);">ProductInfo </span><span style="color: rgb(181,106,1);">{</span>
  public <span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  public <span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">productName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">GridHighLight </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">services</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ProductInfo</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span>
    new <span style="color: rgb(0,0,255);">ProductInfo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'HUAWEI nova 12'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">ProductInfo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'HUAWEI nova 11'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">ProductInfo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'HUAWEI nova 13'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">ProductInfo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'24'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'HUAWEI nova 14'</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,0,170);">  ]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">clickThings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Provide </span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Grid</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">services</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ProductInfo</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">GridItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">父组件中传递数据</span></em>
            <span style="color: rgb(0,0,255);">ToDoItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ProductInfo</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">columnsTemplate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'1fr 1fr 1fr'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">columnsGap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rowsGap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">选中的</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">GridItem</span><span style="color: rgb(128,128,128);">内容抽取为独立组件</span></em>
<span style="color: rgb(181,106,1);">@Component</span>
export default struct <span style="color: rgb(0,0,255);">ToDoItem </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isComplete</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">selectIndex</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Consume </span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isComplete </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(132,63,161);">'#0D5AF5' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">60</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过状态变量控制背景色变化</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isComplete </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isComplete</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndex</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isComplete</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndex</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">利用</span><span style="color: rgb(128,128,128);">indexOf</span><span style="color: rgb(128,128,128);">判断是否存在</span><span style="color: rgb(128,128,128);">selectIndexList</span><span style="color: rgb(128,128,128);">中</span></em>
            let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndex</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">!== -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">selectIndexList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
