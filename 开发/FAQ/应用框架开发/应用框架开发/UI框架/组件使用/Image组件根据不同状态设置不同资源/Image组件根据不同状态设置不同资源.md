# Image组件根据不同状态设置不同资源

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-756

#### 问题现象

如何根据三种不同状态设置不同的资源，如正常态，显示图片1，按压态显示图片2，不可用态显示图片3？
 
 

#### 背景知识

- 对于需要在应用中显示图片的场景，例如：按钮中的icon、网络图片、本地图片等。可以使用Image组件实现，Image支持多种图片格式，包括png、jpg、bmp、svg、gif和heif类型的图片格式，具体用法请参考[Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)。
- [stateStyles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles)可以依据组件的内部状态的不同，快速设置不同样式，目前提供了以下六种状态：
focused：获焦态。
- normal：正常态。
- pressed：按压态。
- disabled：不可用态。
- clicked：点击态。
- selected：选中态。

 - 触摸事件[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)可以识别手指在屏幕上的各种状态，如按压、抬起、移动等，更多状态请参考[TouchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#touchtype)。
- 长按手势[LongPressGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture#longpressgesture-1)在识别成功后会触发onAction事件回调，更多参考回调[事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture#事件)。

 
 

#### 解决方案

- **方案一**：通过stateStyles的normal、pressed、disabled实现，对三种状态设置不同的背景图。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">imageEnable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">正常态</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">normalStyle</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImage</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.normalStyle'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">按压态</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">pressedStyle</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImage</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.pressedStyle'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">不可用态</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">unableStyle</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImage</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.unableStyle'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">控制是否可用</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageEnable </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageEnable</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">30 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">按钮和图片之间的间距</span></em>

    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">stateStyles</span><span style="color: rgb(128,128,128);">控制不同状态的图片显示</span></em>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageEnable</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImageSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">200 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundImagePosition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateStyles</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">normal</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">normalStyle</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">disabled</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">unableStyle</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">pressed</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pressedStyle</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案二**：通过onTouch的TouchType.Up与TouchType.Down实现正常态和按压态图片的切换。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.normalStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">onTouch</span><span style="color: rgb(128,128,128);">控制不同状态的图片显示</span></em>
      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Up</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手指抬起后切换为常态图片</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.normalStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
          <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手指按下后切换为按压态图片</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.pressedStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案三**：通过LongPress手势识别成功回调修改展示的图片。在onAction中更改为按压态图片资源，在onActionEnd中改回正常态图片资源。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution3 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.normalStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
          <span style="color: rgb(0,0,255);">LongPressGesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">repeat</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAction</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.pressedStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.normalStyle'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">运行时替换为实际图片资源</span></em>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">        )</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
