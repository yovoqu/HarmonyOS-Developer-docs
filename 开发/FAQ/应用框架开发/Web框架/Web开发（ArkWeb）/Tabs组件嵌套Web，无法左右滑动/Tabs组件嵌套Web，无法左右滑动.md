# Tabs组件嵌套Web，无法左右滑动

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-152

#### 问题现象

使用Tabs组件嵌套Web组件的布局，当左右滑动时，Tabs组件不能切换。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vp-xoMhVRDKxLFsmYIm4oQ/zh-cn_image_0000002629059056.png?HW-CC-KV=V1&HW-CC-Date=20260723T013343Z&HW-CC-Expire=86400&HW-CC-Sign=697DEB1B8AF315312CED788C7D74F0BF75EA4BF10D570E245AF4D5E11A69246F)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/xvJYbdUaQsebW0J9jzdCMg/zh-cn_image_0000002659258359.png?HW-CC-KV=V1&HW-CC-Date=20260723T013343Z&HW-CC-Expire=86400&HW-CC-Sign=9DB8925C9D66F450571B3B6D0D3060EBAEC6A1CD5D09CE31186817C9BB0E7C75)

 
 

#### 背景知识

- [runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)：在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用，并且回调也将在用户界面（UI）线程上调用。
- [nestedScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#nestedscroll11)：调用以设置嵌套滚动选项。
- touch-action：用于指定某个给定的区域是否允许用户操作，以及如何响应用户操作（比如浏览器自带的划动、缩放等）。

 
 

#### 问题定位

- 检查在线网址是否能左右滑动，排查是网址问题导致还是Web组件属性设置问题。
- 查看nestedScroll属性是否正确设置，若设置为SELF_ONLY，则只自身滚动，不与父组件联动。
- 用浏览器查看该网址是否只设置了touch-action:pan-y属性，该属性只能支持垂直滑动。

 
 

#### 分析结论

网页中CSS样式只设置了touch-action:pan-y，网页只能垂直滑动，导致不能响应Tabs切换操作。
 
 

#### 修改建议

可以使用[runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)的方法向H5中注入touch-action:pan-x pan-y样式来覆盖之前的touch-action设置。
 
端侧示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">selectedIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">tabController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TabsController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TabsController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">controller1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">controller2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#182431'</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">selectedFontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#0a59f7'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedFontColor </span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">500 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">22</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">7</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">7 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Divider</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0a59f7'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">opacity</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">barPosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BarPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">CommonWeb</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller1</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">网页</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">CommonWeb</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller2</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">网页</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">vertical</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barMode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Fixed</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">56</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animationDuration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CommonWeb </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">customStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'* {touch-action: pan-x pan-y!important; }'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'fit_content.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zoomAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onlineImageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">scrollForward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">scrollBackward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPageEnd</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">runJavaScript</span><span style="color: rgb(128,128,128);">注入样式</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">runJavaScript</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span>
<span style="color: rgb(255,0,170);">                    const head = document.head;</span>
<span style="color: rgb(255,0,170);">                    console.info(head);</span>
<span style="color: rgb(255,0,170);">                    const style = document.createElement('style');</span>
<span style="color: rgb(255,0,170);">                    style.appendChild(document.createTextNode("</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customStyle</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">"));</span>
<span style="color: rgb(255,0,170);">                    head.appendChild(style)</span>
<span style="color: rgb(255,0,170);">                `</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
fit_content.html示例代码如下：
 
```text
<em><!DOCTYPE html></em>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
    <title>Fit-Content</title>
</head>
<style>
    * {
       touch-action: pan-y;
    }
</style>
<body>
<div>
    <div><h2 id="使用场景">使用场景</h2>
        <p>ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。常见使用场景包括：</p>
        <ul>
            <li><p>
                应用集成Web页面：应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。</p>
            </li>
            <li><p>
                浏览器网页浏览场景：浏览器类应用可以使用Web组件，打开三方网页，使用无痕模式浏览Web页面，设置广告拦截等。</p>
            </li>
            <li><p>小程序：小程序类宿主应用可以使用Web组件，渲染小程序的页面。</p></li>
        </ul>
    </div>
    <div><h2 id="能力范围">能力范围</h2>
        <p>Web组件为开发者提供了丰富的控制Web页面能力。包括：</p>
        <ul>
            <li><p>Web页面加载：声明式加载Web页面和离屏加载Web页面等。</p></li>
            <li><p>生命周期管理：组件生命周期状态变化，通知Web页面的加载状态变化等。</p></li>
            <li><p>常用属性与事件：UserAgent管理、Cookie与存储管理、字体与深色模式管理、权限管理等。</p>
            </li>
            <li><p>
                与应用界面交互：自定义文本选择菜单、上下文菜单、文件上传界面等与应用界面交互能力。</p>
            </li>
            <li><p>App通过JavaScriptProxy，与Web页面进行JavaScript交互。</p></li>
            <li><p>安全与隐私：无痕浏览模式、广告拦截、坚盾守护模式等。</p></li>
            <li><p>维测能力：DevTools工具调试能力，使用crashpad收集Web组件崩溃信息。
            </p></li>
        </ul>
    </div>
    <div><h2 id="约束与限制">约束与限制</h2>
        <ul>
            <li>Web内核版本：ArkWeb基于谷歌Chromium内核开发，使用的Chromium版本为M114。</li>
        </ul>
    </div>
</div>
</body>
</html>
```
