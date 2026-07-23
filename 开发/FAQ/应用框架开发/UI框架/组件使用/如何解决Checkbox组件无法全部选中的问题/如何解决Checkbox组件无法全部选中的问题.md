# 如何解决Checkbox组件无法全部选中的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1371

#### 问题现象

List中有Checkbox组件，全选只能选中屏幕中的选项，超出屏幕的选项不能被选中。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/v7wRW_ntRJa6_y6Db4YPIA/zh-cn_image_0000002658961253.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012741Z&HW-CC-Expire=86400&HW-CC-Sign=1E065910D318C7DDFEE8510043EE95A1B5FA1CF3248AA0ABF42F7E23BE66AE06)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/vOjdVTJ0To-DmK9JK9G5XQ/zh-cn_image_0000002658841305.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012741Z&HW-CC-Expire=86400&HW-CC-Sign=618AFB0C43E338DB7736E209B8D509AF97EFCF72F287F194724292E8CBA772CF)

 
 

#### 背景知识

- [Checkbox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox)是一种常见且实用的交互元素，它允许用户从一系列选项中选择多个项。无论是电子商务网站上的商品筛选，还是在线表单的数据收集，Checkbox都发挥着重要作用。
- [List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list)只加载和渲染当前屏幕可视区域内的列表项，这被称为按需加载。当用户滚动列表时，List组件会动态加载和卸载列表项，以确保只渲染当前可见的项，从而提高性能。

 
 

#### 解决方案

List组件按需加载的特性使得每次只有当前可见项被渲染，导致全选时无法选中所有组件，可以在List组件外再套一层Scroll组件，确保所有组件可以被渲染。
 
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SelectAllCheckBoxSample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">alignItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">CheckboxGroup</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">group</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'checkboxGroup' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">checkboxShape</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">CheckBoxShape</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ROUNDED_SQUARE</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'FF0858F8'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">itemName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CheckboxGroupResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`checkbox group content </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">itemName</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">} </span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mark</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">strokeColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">unselectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Select All'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">40 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>

        <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在外面套一层</span><span style="color: rgb(128,128,128);">scroll</span></em>
          <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Start</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">alignItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                    <span style="color: rgb(0,0,255);">Checkbox</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'checkbox' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">group</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'checkboxGroup' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'FF0858F8'</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">shape</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">CheckBoxShape</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ROUNDED_SQUARE</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Checkbox</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">change is</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mark</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
                        <span style="color: rgb(255,255,255);">strokeColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(181,106,1);">,</span>
                        <span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">,</span>
                        <span style="color: rgb(255,255,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
                      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">unselectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
                      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
                    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Checkbox</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(181,106,1);">}</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">160</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">}</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignListItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ListItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>

        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'16PX' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>

  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
