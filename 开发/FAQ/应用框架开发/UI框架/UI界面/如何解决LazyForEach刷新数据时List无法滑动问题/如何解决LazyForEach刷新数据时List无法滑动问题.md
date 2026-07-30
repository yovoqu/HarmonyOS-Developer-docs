# 如何解决LazyForEach刷新数据时List无法滑动问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-683

#### 问题现象

通过LazyForEach加载的List列表项，给数据数组重新赋值刷新数据之后，并通过onDataReloaded方法通知组件重新刷新时，List组件滑动一段距离之后无法继续滑动。
 
问题代码示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BaseDataSource </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./BaseDataSource'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">StringListModel </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./StringListModel'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MyComponent </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">dataSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BaseDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDataSource</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">aboutToDisappear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">刷新数据</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(132,63,161);">添加</span><span style="color: rgb(132,63,161);">hello'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadByKeyword</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'hello'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">3 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataSource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'appear:'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReachEnd</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadMore</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
BaseDataSource.ets：
 
```text
export class <span style="color: rgb(0,0,255);">BaseDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">存储实际数据的数组。</span></em>
  private <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">存储所有已注册的数据变更监听器。</span></em>
  private <span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataReloaded</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataReloaded</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">addCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">addOperation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataAddOperation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DataOperationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ADD</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">addCount</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">addOperation</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">delOperation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataDeleteOperation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DataOperationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DELETE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">delCount</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">delOperation</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">setDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReloaded</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">insertIndex </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">addCount </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">insertIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">addCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">delData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">delAllData</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">delCount </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">changeData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
DataLoader.ets：
 
```text
export class <span style="color: rgb(0,0,255);">DataLoader </span><span style="color: rgb(181,106,1);">{</span>
  static async <span style="color: rgb(0,0,255);">getByPage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">第</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">页</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">datas</span>
  <span style="color: rgb(181,106,1);">}</span>

  static async <span style="color: rgb(0,0,255);">getByKeyWord</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(132,63,161);">第</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">页</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">datas</span>
  <span style="color: rgb(181,106,1);">}</span>

  static async <span style="color: rgb(0,0,255);">getByFirstLetter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">letter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">letter</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(132,63,161);">第</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">page</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">页</span><span style="color: rgb(132,63,161);">-</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">datas</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
StringListModel.ets：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BaseDataSource </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./BaseDataSource'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">DataLoader </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./DataLoader'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">MIN_PAGE_SIZE </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">;</span>

export class <span style="color: rgb(0,0,255);">StringListModel </span><span style="color: rgb(181,106,1);">{</span>
  private static <span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">StringListModel </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">null</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BaseDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">BaseDataSource</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">MIN_PAGE_SIZE</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">hasMoreData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>

  private constructor<span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>

  static <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">StringListModel</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置每页加载的数量。</span></em>
  <span style="color: rgb(0,0,255);">setPageSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pageSize </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">MIN_PAGE_SIZE</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">getDataSource</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">加载第一页成语数据。</span></em>
  <span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过关键字来查找并加载第一页成语数据。</span></em>
  <span style="color: rgb(0,0,255);">loadByKeyword</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">!== </span>undefined <span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过拼音首字母来查找并加载第一页成语数据。</span></em>
  <span style="color: rgb(0,0,255);">loadByFirstLetter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">!== </span>undefined <span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">加载更多成语数据。</span></em>
  <span style="color: rgb(0,0,255);">loadMore</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">++;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  private <span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isFirstPage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">loadCallback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>

      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isFirstPage </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>

    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByKeyWord</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByFirstLetter</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByPage</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在页面销毁时调用。</span></em>
  <span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JRY4Be2JQ6el1aQn5OSkyQ/zh-cn_image_0000002658794111.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072500Z&HW-CC-Expire=86400&HW-CC-Sign=FA059D33EADC6A2EDDE198586849BB18EC5811D97DA40939548593A4524DC584)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/mcqgmOQpSV2Vyl1mAJlJjg/zh-cn_image_0000002628554746.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072500Z&HW-CC-Expire=86400&HW-CC-Sign=BA11EF4F1133D1CAAA6615AFADDF289128A4AA593447DB4094F527D50512BC6F)

 
 

#### 背景知识

- [onDataReloaded](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach#ondatareloaded)能够通知组件重新加载所有数据，键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件，重新加载数据完成后调用。
- [onDatasetChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach#ondatasetchange12)进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件，与其它操作数据的接口不能混用。

 
 

#### 问题定位

由问题代码可知，自定义方法notifyDataReloaded调用了onDataReloaded通知数据的重新加载，而调用onDataReloaded时，键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件，而单纯的调用onDataReloaded刷新数据并不会更新键值，因此在问题图中，当LazyForEach刷新数据之后，由于没有继续重建子组件，而是复用了原先的子组件，导致List列表项下滑到一定程度就无法继续下滑。
 
 

#### 分析结论

在刷新数据时需要进行数据添加操作，使子组件得以重建而非复用。
 
 

#### 修改建议

- **方案一**：在自定义方法notifyDataReloaded中使用onDatasetChange方法代替onDataReloaded进行组件重新加载数据，onDatasetChange能够进行批量的数据处理，包括数据添加、重载所有数据等操作，可以避免复用原先的子组件。也可以对调用notifyDataReloaded方法的setDatas方法添加数据添加功能，修改后的BaseDataSource：
```text
export class <span style="color: rgb(0,0,255);">BaseDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">T</span><span style="color: rgb(181,106,1);">></span> implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataReloaded</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">reloadOperation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataReloadOperation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DataOperationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RELOAD</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">reloadOperation</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">addCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">addOperation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataAddOperation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DataOperationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ADD</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">addCount</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">addOperation</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">delOperation</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataDeleteOperation </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DataOperationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DELETE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">delCount</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">delOperation</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  private <span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">listener </span>of this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>


  <span style="color: rgb(0,0,255);">setDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">insertIndex </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">addCount </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">insertIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">addCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">insertIndex </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">addCount </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">insertIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">addCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">delData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">delAllData</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">delCount </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">changeData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">T</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listeners </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

- **方案二**：将setDatas方法替换为先删除后再添加的方法，修改后StringListModel：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BaseDataSource </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./BaseDataSource'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">DataLoader </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./DataLoader'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">MIN_PAGE_SIZE </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">;</span>

export class <span style="color: rgb(0,0,255);">StringListModel </span><span style="color: rgb(181,106,1);">{</span>
  private static <span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">StringListModel </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">null</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BaseDataSource</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">BaseDataSource</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">MIN_PAGE_SIZE</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">hasMoreData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>

  private constructor<span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>

  static <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">StringListModel</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">设置每页加载的数量</span></em>
<em><span style="color: rgb(128,128,128);">   * @param pageSize </span><span style="color: rgb(128,128,128);">每页加载数量不能小于最小加载数量</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">setPageSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pageSize </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">MIN_PAGE_SIZE</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">getDataSource</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">加载第一页成语数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

<em>  <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">通过关键字来查找并加载第一页成语数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @param keyword</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">loadByKeyword</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">!== </span>undefined <span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">通过拼音首字母来查找并加载第一页成语数据</span></em>
<em><span style="color: rgb(128,128,128);">   * @param firstLetter</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">loadByFirstLetter</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">!== </span>undefined <span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <em><span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">加载更多成语数据</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">loadMore</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">++;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  private <span style="color: rgb(0,0,255);">loadData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isFirstPage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">loadCallback </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">datas </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>

      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">hasMoreData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(181,106,1);">;</span>

      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isFirstPage </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">delAllData</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addDatas</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">datas</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByKeyWord</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">keyword</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByFirstLetter</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">firstLetter</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">DataLoader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getByPage</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">curPage</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageSize</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">loadCallback</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">释放。可在页面销毁时调用，如</span><span style="color: rgb(128,128,128);">page</span><span style="color: rgb(128,128,128);">页中的</span><span style="color: rgb(128,128,128);">aboutToDisappear</span><span style="color: rgb(128,128,128);">方法中</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stringDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">StringListModel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sInstance </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 

#### 常见FAQ

Q：为什么onDatasetChange方法不能与其它操作数据的接口混用？
 
A：onDatasetChange方法用于通知LazyForEach组件进行批量的数据处理。该方法接受一个包含多个数据操作的数组作为参数。这些操作可以包括数据的添加、删除、移动等。当在onDatasetChange中传入包含删除操作的数据集时，系统会认为这是一个不兼容的操作，从而导致崩溃。因此onDatasetChange方法不能与其他操作数据的接口混用。
 
Q：使用onDatasetChange方法有哪些注意点？
 
A：调用一次onDatasetChange时，每个index对应的数据只能被操作一次。如果多次操作同一个index，LazyForEach仅生效第一次操作。并且onDatasetChange不能与其他DataChangeListener的更新接口混用。如在同一个LazyForEach中，调用过onDataAdd接口后，不能再调用onDatasetChange接口；反之，调用过onDatasetChange接口后，也不能调用onDataAdd等其他更新接口。页面中不同LazyForEach之间互不影响。具体可参考官网指南LazyForEach中的[数据更新](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach#数据更新)、onDatasetChange。
