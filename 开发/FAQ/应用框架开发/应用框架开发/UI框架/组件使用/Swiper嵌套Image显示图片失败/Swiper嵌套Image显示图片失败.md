# Swiper嵌套Image显示图片失败

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-722

#### 问题现象

在Swiper组件中套用Image组件绑定onComplete事件，用图片实际绘制的宽度contentWidth、高度contentHeight作为图片的宽度和高度，Image组件不显示图片。
 
问题代码示例参考如下：
 
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SwiperImageDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">contentHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.img1'</span><span style="color: rgb(0,0,255);">)) </span><em>// </em><em><span style="color: rgb(128,128,128);">图片资源需自行配置</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onComplete</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'this.contentWidth'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'this.contentHeight'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'complete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'px'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'px'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)滑块视图容器，提供子组件滑动轮播显示的能力。
- Image加载图片的使用和注意事项请参考[存档图类型数据源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#存档图类型数据源)。
- [onComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#oncomplete)在图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸，其中包含以下数据：
width、height为图片实际宽高。
- componentWidth、componentHeight为Image组件宽高。
- contentWidth、contentHeight为图片实际绘制宽高。

 
 
 

#### 问题定位

程序运行的UI现象：Swiper未显示。
 
查看打印的数据信息：图片加载并解码后的数据。除图片实际宽高外，组件宽高和图片绘制宽高均为0。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/BrdtZeKYRrKOqQi0EJfbTA/zh-cn_image_0000002658794583.png?HW-CC-KV=V1&HW-CC-Date=20260811T005752Z&HW-CC-Expire=86400&HW-CC-Sign=4E6B47386A40A48E578314152FCBF39E3EACFBFADA097E9A36E569737789DAC5)

 
 

#### 分析结论

问题代码的组件结构为：Column->Swiper->Image。
 
由于初始未设置Swiper组件的宽高，则默认为0。且Image组件受限于父组件Swiper，绘制宽高为0，所以图片显示的大小为0。Swiper未设置宽高时自适应子组件大小，由于Image组件也未能撑开，所以在UI界面中，Swiper和Image均不显示。
 
 

#### 修改建议

在初始化时设置Swiper的宽高，保留Image组件绘制图片的空间，则组件宽高和图片实际绘制宽高不会为0，图片能正常显示。
 
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SwiperImageDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">contentHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.img1'</span><span style="color: rgb(0,0,255);">))</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">图片资源需自行配置</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onComplete</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'this.contentWidth'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">contentHeight</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'this.contentHeight'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'complete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentWidth </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'px'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentHeight </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'px'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">Swiper</span><span style="color: rgb(128,128,128);">设置宽高</span></em>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
查看打印的图片尺寸信息：组件宽高和图片实际绘制宽高大于0。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ZnFXejk_S6y75VgMigt6XA/zh-cn_image_0000002628555216.png?HW-CC-KV=V1&HW-CC-Date=20260811T005752Z&HW-CC-Expire=86400&HW-CC-Sign=5465A460346658B7DA6D0C37C603CD81D3A553C1E885C1992DC22979169D1A77)
