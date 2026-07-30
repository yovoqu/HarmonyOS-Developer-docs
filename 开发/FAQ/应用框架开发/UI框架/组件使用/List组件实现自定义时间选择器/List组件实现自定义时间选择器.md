# List组件实现自定义时间选择器

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1415

#### 问题现象

目前HarmonyOS官方提供的TextPicker组件没有横向滑动的能力，怎样实现横向滑动的时间选择器？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4EU6zWyDTXawMr-uLawZLw/zh-cn_image_0000002628763170.png?HW-CC-KV=V1&HW-CC-Date=20260730T072359Z&HW-CC-Expire=86400&HW-CC-Sign=E23FB56ECAC230FAC53E78AE55561074D9FA6856963D0F6D4481A7E25707F569)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/KwCOIg0sTcih3C14YNqXkA/zh-cn_image_0000002658962483.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072359Z&HW-CC-Expire=86400&HW-CC-Sign=EE4B4FC99A98DA4DA94AA16F1C0F734448169F8FB9082F9E2AA3AB186B16625B)

 
 

#### 背景知识

- [TextPicker组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)：滑动选择文本内容的组件，但是没有横向滑动的能力，目前只支持竖向滑动。
- [List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：是官方提供的常用的滚动组件之一，其接口[listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)可设置List组件排列方向，其Axis参数如下：

  
| 序号 | 名称 | 说明 |
| --- | --- | --- |
| 1 | Vertical | 方向为纵向。 |
| 2 | Horizontal | 方向为横向。 |
 
 
 

#### 解决方案

由于TextPicker组件没有横向滑动的能力，因此可以采用List滑动组件，实现横向滚动的时间选择器，采用[scrollSnapAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#scrollsnapalign10)属性使List中间项对齐，同时将中间的Item差异化处理来进行突出显示。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ListCustomTimePicker </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'10'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'15'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'20'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'25'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'30'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'35'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'40'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'45'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'50'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'55'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'60'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">centerIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
              <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断语句</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">当索引位置在显示的中间时，对该时间放大处理</span></em>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerIndex </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerIndex </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'20%'</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">单行显示</span><span style="color: rgb(128,128,128);">5</span><span style="color: rgb(128,128,128);">个</span><span style="color: rgb(128,128,128);">item</span></em>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollSnapAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ScrollSnapAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CENTER</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">中间项对齐</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listDirection</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Axis</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Horizontal</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// List</span><span style="color: rgb(128,128,128);">组件设置横向滚动</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollIndex</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">firstIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">lastIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">centerIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取屏幕中间</span><span style="color: rgb(128,128,128);">item</span><span style="color: rgb(128,128,128);">的索引值</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">centerIndex</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`firstIndex</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">firstIndex</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,lastIndex</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">lastIndex</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0xDCDCDC)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
