# 如何自定义bindPopup的交互式关闭功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1312

#### 问题现象

- 场景一：如何设置bindPopup的参数实现点击弹窗外部关闭弹窗？
- 场景二：bindPopup如何拦截系统返回事件，自定义返回逻辑？

 
 

#### 背景知识

- [onWillDismiss](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#basedialogoptions11)：交互式关闭回调函数。
- [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)：为组件绑定Popup气泡，API介绍请参考：[Popup控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup)。
- bindPopup方法的传参[PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)中，autoCancel可以控制气泡是否关闭，默认值为true。该参数表示：页面有操作时，是否自动关闭气泡。
- [气泡提示（Popup）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-popup)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

 
 

#### 解决方案

- **场景一**：将组件bindPopup方法的传参[PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)中的autoCancel设置为true，即可实现点击外部自动关闭气泡。
- **场景二**：可以使用onWillDismiss事件拦截气泡返回关闭，自定义返回事件逻辑。
```json
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SFI20250721204737765691 </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">handlePopup1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">handlePopup2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">使用</span><span style="color: rgb(132,63,161);">onWillDismiss</span><span style="color: rgb(132,63,161);">事件拦截气泡返回关闭</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Button1'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup1 </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">使用</span><span style="color: rgb(132,63,161);">onWillDismiss</span><span style="color: rgb(132,63,161);">事件拦截气泡返回关闭</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">messageOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">textColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">font</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'20vp'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FontStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">placement</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Placement</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">enableArrow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">targetSpace</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'15vp'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            let <span style="color: rgb(255,255,255);">timer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup1 </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">10000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isVisible</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup1 </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">clearTimeout</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">timer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">onWillDismiss</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span>
<span style="color: rgb(255,0,170);">            (</span><span style="color: rgb(255,255,255);">dismissPopupAction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DismissPopupAction</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'dismissReason:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissPopupAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
              if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissPopupAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">DismissReason</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PRESS_BACK</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
           <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义返回事件逻辑</span></em>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">str </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">自定义返回事件，执行成功。</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span>
              if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">dismissPopupAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">reason </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">DismissReason</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">TOUCH_OUTSIDE</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">dismissPopupAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dismiss</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span>
          <span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Button2'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup2 </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">未拦截气泡返回关闭</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">messageOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">textColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">font</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'20vp'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">FontStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">placement</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Placement</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">enableArrow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">targetSpace</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'15vp'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            let <span style="color: rgb(255,255,255);">timer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup2 </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">10000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isVisible</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">handlePopup2 </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">clearTimeout</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">timer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 

#### 常见FAQ

Q：如何拦截气泡的退出事件？
 
A：通过配置onWillDismiss的boolean类型为false时，[拦截气泡的退出事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#示例6为气泡拦截退出事件)。
