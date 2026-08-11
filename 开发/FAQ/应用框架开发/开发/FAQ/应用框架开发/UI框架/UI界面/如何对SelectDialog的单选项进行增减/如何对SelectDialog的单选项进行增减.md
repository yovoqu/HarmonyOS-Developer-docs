# 如何对SelectDialog的单选项进行增减

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1580

#### 问题现象

如图所示，[纯列表弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog#示例2纯列表弹出框)提供如下的示意图，如何自定义单选项的数量，使得弹窗属性title的内容是从string数组foreach遍历获取？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/xDuRdR7nSYSO52dOQrvIyQ/zh-cn_image_0000002658969515.png?HW-CC-KV=V1&HW-CC-Date=20260811T005710Z&HW-CC-Expire=86400&HW-CC-Sign=09C82D781B02838373D18F5BC87F05B66FEB0141A2F4D9B035989666E8D01BF4)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3Ejc15GRREKm7UL1o2Yk8A/zh-cn_image_0000002628610296.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005710Z&HW-CC-Expire=86400&HW-CC-Sign=AABF3C9A559988022AB3AE73ED2AA715B0274DC12703DB86209A9752852B970A)

 
 

#### 背景知识

[SelectDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog#selectdialog)：选择类弹出框，弹框中以列表或网格的形式提供可选的内容。
 
 

#### 解决方案

在aboutToAppear中使用for循环动态初始化SelectDialog的radioContent。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">SelectDialog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SelectDialogDemo </span><span style="color: rgb(181,106,1);">{</span>
 <em> <span style="color: rgb(128,128,128);">// title</span><span style="color: rgb(128,128,128);">数组</span></em>
  <span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// SelectDialog</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">radioContent</span><span style="color: rgb(128,128,128);">进行初始化</span></em>
  <span style="color: rgb(255,255,255);">radioContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">SheetInfo</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置默认选中</span><span style="color: rgb(128,128,128);">radio</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">index</span></em>
  <span style="color: rgb(255,255,255);">radioIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">dialogControllerList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SelectDialog</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本标题</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">selectedIndex</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">radioIndex</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">confirm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">取消</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将初始化后的</span><span style="color: rgb(128,128,128);">radioContent</span><span style="color: rgb(128,128,128);">赋值给</span><span style="color: rgb(128,128,128);">SelectDialog</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">radioContent</span><span style="color: rgb(128,128,128);">属性</span></em>
      <span style="color: rgb(255,255,255);">radioContent</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">radioContent</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">纯列表弹出框</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">96</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本文本文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本文本文本文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本文本文本文本文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">文本文本文本文本文本文本</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

          <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">赋值给</span><span style="color: rgb(128,128,128);">radioContent</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                let <span style="color: rgb(255,255,255);">sheetInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SheetInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,255,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">radioIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">                }</span><span style="color: rgb(181,106,1);">;</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">radioContent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">sheetInfo</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogControllerList</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">open</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">300 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImageSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'100%' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
