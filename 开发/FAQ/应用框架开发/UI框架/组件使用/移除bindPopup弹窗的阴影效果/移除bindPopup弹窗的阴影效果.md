# 移除bindPopup弹窗的阴影效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1216

#### 问题现象

如何移除bindPopup弹窗的阴影效果？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/GYAkKrglSB-QG4guufHuEg/zh-cn_image_0000002628753486.png?HW-CC-KV=V1&HW-CC-Date=20260723T012715Z&HW-CC-Expire=86400&HW-CC-Sign=C17A548F7171FD83FDABC4F0966DE92A2279EB7D405F2BAB2DF38DF5CFFF9212)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/J_AaYqGZT26F9YrxUV2Njg/zh-cn_image_0000002658952799.png?HW-CC-KV=V1&HW-CC-Date=20260723T012715Z&HW-CC-Expire=86400&HW-CC-Sign=ABCF69A8743B9A4AD18CFE106F8E0B2B28009B9FE56E202BB3A1132D76C0AD36)

 
 

#### 背景知识

- [ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明)：阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。
- [阴影效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect)：阴影接口shadow可以为当前组件添加阴影效果。

 
 

#### 解决方案

通过配置ShadowOptions实现阴影效果的灵活控制。在ShadowOptions模式中，当满足radius设置为0时，即可实现无阴影效果。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PopupExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'popup'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'this is a popup'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">arrowHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">arrowWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">shadow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
