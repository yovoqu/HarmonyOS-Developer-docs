# 组件设置maskShape不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1285

#### 问题现象

设置组件的maskShape属性后，组件遮罩未生效且组件本身消失，注释该属性后组件恢复正常显示。
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">maskSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">180</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Circle</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0D5AF5'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskShape</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">CircleShape</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskSize</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskSize </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#00000000'</span><span style="color: rgb(0,0,255);">))</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
注释maskShape属性前后效果图对比：
 
注释前：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/S0ApbEAcQB2w24vd1X7YKg/zh-cn_image_0000002658957193.png?HW-CC-KV=V1&HW-CC-Date=20260701T041328Z&HW-CC-Expire=86400&HW-CC-Sign=82BE86265D71B9B2848CE630EF74340CEDE83F6C164E67049AC0F109D6014FEB)

 
注释后：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/KEIj9aCrTyexiVeTPLPTOw/zh-cn_image_0000002658837241.png?HW-CC-KV=V1&HW-CC-Date=20260701T041328Z&HW-CC-Expire=86400&HW-CC-Sign=BB59AF258D23CE845616CF9958D15EE27B2BC012A1FFE28AC9BB7E9302DE158F)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/LBO4B4mIRzC0Fbr4prR_UQ/zh-cn_image_0000002628597976.png?HW-CC-KV=V1&HW-CC-Date=20260701T041328Z&HW-CC-Expire=86400&HW-CC-Sign=6E52DD33638895AA95886BC35B9D740FD5012A2593F33FD4DC5CA50BDC348397)

 
 

#### 背景知识

- 通用属性[maskShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#maskshape12)是用于为组件添加指定形状的遮罩，遮罩后，组件显示为遮罩的形状（即若指定圆形遮罩，则组件最终显示为圆形），遮罩形状从组件的左上角开始绘制。
- 在指定遮罩形状时可以通过[fill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-circle#fill)属性填充形状颜色，使遮罩后的组件呈现不同的透明度；当填充的颜色为黑色（Color.Black或000000）、透明（Color.Transparent）或透明度为00（16进制颜色00XXXXXX）的颜色时，会将组件完全遮罩，组件不显示。

 
 

#### 问题定位
1. 排查maskShape是否设置了黑色、透明色或透明度为00的颜色；
2. 确认组件在遮罩后的位置有可显示的内容。
 
 

#### 分析结论

问题代码中，组件Circle设置的遮罩层形状CircleShape填充了颜色#00000000，即透明度为00的黑色，导致组件被完全遮罩，不显示。
 
 

#### 修改建议

调整maskShape形状的填充颜色，不设置为黑色、透明色或透明度为00的颜色。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">CircleShape </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">maskSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">180</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Circle</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0D5AF5'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskShape</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">CircleShape</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskSize</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maskSize</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0000FF'</span><span style="color: rgb(0,0,255);">))</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
