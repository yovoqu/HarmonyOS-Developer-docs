# Image动态设置圆角大小

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-842

#### 问题现象

使用Slider组件希望实现滑动时控制Image组件圆角的变化，但滑动Slider时圆角没有改变。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/tIbyrHAPQyuMhQET4FLDwg/zh-cn_image_0000002628558546.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012622Z&HW-CC-Expire=86400&HW-CC-Sign=56B8C8588EAE05F097AE646AFF4B13E0907650C4474D3ACC69E461CBC085A71D)

 
 

#### 背景知识

- [clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)：用于对组件进行裁剪、遮罩处理。
- [borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)：设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。
- [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
- [$$语法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)：内置组件双向同步。

 
 

#### 解决方案

针对滑动Slider时圆角没有改变的问题，需要注意以下事项：
 
- 想通过Slider组件值改变来同步改变Image组件的圆角，需要将.borderRadius()属性值和Slider组件的value值双向绑定。
- 实现圆角变化效果后如果需要图片跟随圆角值发生变化，需要给Image组件添加.clip(true)属性。

 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ImageChange </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>

      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.background'</span><span style="color: rgb(0,0,255);">))</span> <em>// </em><em><span style="color: rgb(128,128,128);">可根据具体场景替换为可用资源</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">裁剪超出</span><span style="color: rgb(128,128,128);">Image</span><span style="color: rgb(128,128,128);">组件的图片</span></em>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radius </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'PX'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#007AFF'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">60</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OutSet</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radius </span><em>// </em><em><span style="color: rgb(128,128,128);">双向绑定</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">blockSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">trackColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#E5E5EA'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#007AFF'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">trackThickness</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">6</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">7</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">13</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
