# Column宽高自适应背景图片大小

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1275

#### 问题现象

给Column设置一张背景图片，如何做到Column宽高自适应背景图片大小？即图片有多大，Column就有多大。
 
 

#### 背景知识

- [Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)是一种线性布局组件，容器内子元素按照垂直方向排列。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)是层叠布局组件，提供元素可以重叠的布局。
- Image的[fitOriginalSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fitoriginalsize)属性用于设置图片的显示尺寸是否跟随图源尺寸。

 
 

#### 解决方案
1. 在需要设置背景图片的Column中使用层叠布局组件Stack。
2. 在Stack中使用Image作为背景图片，并将Image的fitOriginalSize属性设置为true。
 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ColumnLayout </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fitOriginalSize</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
在IDE中查看ArkUI Inspector预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/YL4_iqcJQ320MoD9IVB1jw/zh-cn_image_0000002658835381.png?HW-CC-KV=V1&HW-CC-Date=20260701T041240Z&HW-CC-Expire=86400&HW-CC-Sign=5AE4364C77663D188674CFF35DEE615D6DC7D17ADD7F00004E540B7A3C0D0558)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/wA7mN5mUSiqhv9abH1YAHQ/zh-cn_image_0000002628756018.png?HW-CC-KV=V1&HW-CC-Date=20260701T041240Z&HW-CC-Expire=86400&HW-CC-Sign=157B31423ADC67C11E601697EF0702872C78552C4683E6F4960761E42F3747AB)
