# Tabs如何根据TabBar数量更改页签栏排布

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1536

#### 问题现象

应用中有的Tabs页面的数量是通过服务端返回的结果动态显示的，TabBar的数量较多时保持均分显示，但是数量较少时希望能够靠拢显示，避免有大量的留白间距影响视觉体验。
 
 

#### 背景知识

[Tabs组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
 
- [barGridAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#bargridalign10)：以栅格化方式设置TabBar的可见区域。
- 可以通过改变入参[BarGridColumnOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#bargridcolumnoptions10对象说明)动态调整TabBar的显示效果。

 
 

#### 解决方案

设置Tabs的barGridAlign属性，通过调整BarGridColumnOptions的sm和margin属性，以达到TabBar靠拢或者均分的效果。
 
用户在输入框输入小于等于10的数字后，以4为阈值：TabBar数量小于4时，页签靠拢显示；TabBar数量大于等于4时，页签均分显示。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">promptAction </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TabsView </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">tabList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">tabsController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TabsController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TabsController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">tabsNum</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextInputController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextInputController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">generateCharacterList</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">n</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">n</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    return <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabsNum</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'input your tab number'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffd9dbd9'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">InputType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Number</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            let <span style="color: rgb(255,255,255);">tabNum </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">tabNum </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'tab number must be little then 10'</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,255,255);">showMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ToastShowMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DEFAULT</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">80</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              return<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabList </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateCharacterList</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabsController </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabList</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barGridAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">sm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">margin</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">tabList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">4 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(80,160,79);">80 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 总结

要实现Tabs组件中的TabBar根据数量均分或者靠拢显示，通过设置Tabs组件的barGridAlign属性调整。
