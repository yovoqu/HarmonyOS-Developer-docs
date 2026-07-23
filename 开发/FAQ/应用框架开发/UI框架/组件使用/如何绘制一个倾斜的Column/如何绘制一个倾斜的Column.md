# 如何绘制一个倾斜的Column

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1185

#### 问题现象

UI开发中，如何绘制一个倾斜指定角度的Column？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/n9u7Cm1LRJ-vaQq10RJOFA/zh-cn_image_0000002628752850.png?HW-CC-KV=V1&HW-CC-Date=20260723T012710Z&HW-CC-Expire=86400&HW-CC-Sign=9E53336A0E7B654BDFED823D1B285732379F326934043A03447C711908692A3F)

 
 

#### 背景知识

[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)：可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform3d20)接口。参数可设置当前组件的变换矩阵。object当前仅支持[Matrix4Transit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4#matrix4transit)矩阵对象类型。[matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4)：提供矩阵变换功能，支持对图形进行平移、旋转和缩放等。
 
 

#### 解决方案

通过给对应的[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)添加transform属性，根据倾斜的角度计算出弧度，使用matrix4.[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4#matrix4init)创建一个四阶矩阵，将创建的四阶矩阵对象作为transform的参数传入，即可得到一个倾斜指定角度的Column。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">matrix4 </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">matrix1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">matrix4</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Matrix4Transit </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将角度转换为弧度（</span><span style="color: rgb(128,128,128);">Math.tan</span><span style="color: rgb(128,128,128);">需要弧度制）</span></em>
    const <span style="color: rgb(0,0,255);">angleRad </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">14 </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PI </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">180</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算倾斜角度对应的</span><span style="color: rgb(128,128,128);">tan</span><span style="color: rgb(128,128,128);">值</span></em>
    const <span style="color: rgb(0,0,255);">tanValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tan</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">angleRad</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">matrix4.init</span><span style="color: rgb(128,128,128);">创建一个</span><span style="color: rgb(128,128,128);">4x4</span><span style="color: rgb(128,128,128);">的变换矩阵</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">matrix1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">matrix4</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">([</span>
      <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">tanValue</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">第一行：</span><span style="color: rgb(128,128,128);">x</span><span style="color: rgb(128,128,128);">方向倾斜</span></em>
      <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">第二行：保持</span><span style="color: rgb(128,128,128);">y</span><span style="color: rgb(128,128,128);">不变</span></em>
      <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">第三行：</span><span style="color: rgb(128,128,128);">z</span><span style="color: rgb(128,128,128);">不变</span></em>
      <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><em> // </em><em><span style="color: rgb(128,128,128);">第四行：齐次坐标</span></em>
    <span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Column</span><span style="color: rgb(255,0,170);">倾斜</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">transform</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">matrix1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
