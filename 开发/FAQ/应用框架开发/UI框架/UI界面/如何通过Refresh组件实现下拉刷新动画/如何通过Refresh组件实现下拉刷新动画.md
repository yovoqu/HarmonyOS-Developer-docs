# 如何通过Refresh组件实现下拉刷新动画

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1504

#### 问题现象

如何使用Refresh组件实现下拉刷新动画？要求下拉刷新时页面内容不动，刷新动画始终位于页面顶部，并在刷新过程中展示。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/HBhgB_akSqu8wgwpeo101A/zh-cn_image_0000002628766428.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072435Z&HW-CC-Expire=86400&HW-CC-Sign=0F5BD21A96FD71C9BFA983A0370F5147D5C148F77E7A39A9D5C31D988890424A)

 
 

#### 背景知识

- [Refresh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh)组件是可以进行页面下拉操作并显示刷新动效的容器组件，它可以采用[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)显式动画来自定义动画效果。
- [Lottie](https://developer.huawei.com/consumer/cn/doc/quickApp-References/quickapp-component-lottie-0000001266273702)是一个适用于OpenHarmony的动画库，它可以解析json格式的动画，并在移动设备上进行本地渲染，以此来实现动画的播放、暂停等操作。

 
 

#### 解决方案

- **方案一：**使用Refresh组件的默认刷新样式，可以参考文档[Refresh实现下拉刷新动画示例一](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#示例1默认刷新样式)。
- **方案二：**使用Refresh组件结合Lottie实现自定义刷新动画。具体步骤如下：1. 引入必要的组件和配置：首先，确保项目中已经引入了Lottie动画库。在项目地址中打开终端，输入以下命令安装组件：
```text
ohpm install @ohos/lottie
```


2. 引入lottie.json自定义动画文件：json动画文件可以参考[工程示例中的json文件](https://gitcode.com/openharmony-tpc/lottieArkTS/tree/master/entry/src/main/ets/common/lottie)，在“resources/rawfile”文件夹下放入动画文件即可，例如在rawfile文件夹下创建“common/lottie/animation.json”动画文件。

3. 加载并配置Lottie动画：使用Lottie来配置下拉时的动画效果。
```json
<span style="color: rgb(0,0,255);">loadPullDownAnimation</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">lottie</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadAnimation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">container</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">渲染上下文</span></em>
    <span style="color: rgb(255,255,255);">renderer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'canvas'</span><span style="color: rgb(181,106,1);">, </span><em>// canvas</em><em><span style="color: rgb(128,128,128);">渲染模式</span></em>
    <span style="color: rgb(255,255,255);">loop</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">是否循环播放</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">默认</span><span style="color: rgb(128,128,128);">true</span></em>
    <span style="color: rgb(255,255,255);">autoplay</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否自动播放，默认</span><span style="color: rgb(128,128,128);">true</span></em>
    <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateName</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">contentMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Contain'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'common/lottie/animation.json'</span><span style="color: rgb(181,106,1);">, </span><em>// json</em><em><span style="color: rgb(128,128,128);">路径</span></em>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>
```


4. 在Refresh组件中使用[onStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onstatechange)和[onRefreshing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onrefreshing)等事件来配置下拉时不同状态下的动画效果。
```json
import <span style="color: rgb(255,255,255);">lottie</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AnimationItem </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/lottie'</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RefreshExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isRefreshing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">String</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'0'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'6'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'7'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'8'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'9'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'10'</span><span style="color: rgb(255,0,170);">]</span>
  private <span style="color: rgb(255,255,255);">mainCanvasRenderingContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(255,0,170);">()</span>
  private <span style="color: rgb(255,255,255);">animateItem</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimationItem </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">null </span><span style="color: rgb(181,106,1);">= </span>null
  private <span style="color: rgb(255,255,255);">animateName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'pullDownAnimate'</span>
  private <span style="color: rgb(255,255,255);">setting</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">setting</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">lottieName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'lottie_data'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">loadPullDownAnimation</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">lottie</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadAnimation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">container</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">渲染上下文</span></em>
      <span style="color: rgb(255,255,255);">renderer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'canvas'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// canvas</span><span style="color: rgb(128,128,128);">渲染模式</span></em>
      <span style="color: rgb(255,255,255);">loop</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否循环播放</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">默认</span><span style="color: rgb(128,128,128);">true</span></em>
      <span style="color: rgb(255,255,255);">autoplay</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否自动播放，默认</span><span style="color: rgb(128,128,128);">true</span></em>
      <span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateName</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">contentMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'Contain'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'common/lottie/animation.json'</span><span style="color: rgb(181,106,1);">, </span><em>// json</em><em><span style="color: rgb(128,128,128);">路径</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">customRefreshComponent</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#aabbcc'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDisAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">lottie</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lottieName</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// Canvas</span><span style="color: rgb(128,128,128);">销毁时顺带销毁</span><span style="color: rgb(128,128,128);">lottie</span><span style="color: rgb(128,128,128);">动画</span></em>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mainCanvasRenderingContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mainCanvasRenderingContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imageSmoothingEnabled </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mainCanvasRenderingContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">imageSmoothingQuality </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'medium'</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadPullDownAnimation</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'mainCanvasRenderingContext is not initialized'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置最小高度约束保证自定义组件高度随刷新区域高度变化时自定义组件高度不会低于</span><span style="color: rgb(128,128,128);">minHeight</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">constraintSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">minHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">32 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Refresh</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">refreshing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isRefreshing</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customRefreshComponent</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'70%'</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">80</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0xFFFFFF)</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollIndex</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">first</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">first</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignListItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ListItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Off</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0x89CFF0)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pullToRefresh</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">refreshOffset</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">64</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onStateChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">refreshStatus</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RefreshStatus</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Refresh onStatueChange state is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">refreshStatus</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">refreshStatus </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">未下拉</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(255,0,170);">()</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem </span><span style="color: rgb(181,106,1);">= </span>null
        <span style="color: rgb(181,106,1);">}</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">refreshStatus </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">下拉中</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadPullDownAnimation</span><span style="color: rgb(255,0,170);">()</span>
        <span style="color: rgb(181,106,1);">}</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">refreshStatus </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">刷新中</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">refreshStatus </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">刷新结束</span></em>
          <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(255,0,170);">()</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">animateItem </span><span style="color: rgb(181,106,1);">= </span>null
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">75</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onRefreshing</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isRefreshing </span><span style="color: rgb(181,106,1);">= </span>false
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`onRefreshing test`</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 

#### 常见FAQ

Q：在Tab栏中通过Refresh组件实现下拉刷新后，重复刷新同一项页面时，刷新效果不会重复显示。
 
A：可以给Refresh组件绑定一个参数用来控制刷新状态。
 
```text
<span style="color: rgb(0,0,255);">Refresh</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">refreshing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isRefreshing </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
每次重复刷新时，重置状态变量isRefreshing即可重复触发刷新效果。
 
Q：Refresh组件如何监听下拉高度变化？
 
A：可以通过[onOffsetChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onoffsetchange12)方法实时获取下拉高度，以此来控制下拉动画状态。
 
 

#### 总结

方案一、二都是通过Refresh组件实现下拉刷新动画，但实现方法略有不同，区别如下：
  
| 方案 | 特点 |
| --- | --- |
| 方案一 | 通过Refresh组件的通用属性来实现动画效果。 |
| 方案二 | 通过引入动画库来实现自定义动画效果。 |
 
 
常见场景如下：
 
- 工具类应用或功能型应用，如电话簿功能。
- 社交媒体应用或视频播放应用等。
