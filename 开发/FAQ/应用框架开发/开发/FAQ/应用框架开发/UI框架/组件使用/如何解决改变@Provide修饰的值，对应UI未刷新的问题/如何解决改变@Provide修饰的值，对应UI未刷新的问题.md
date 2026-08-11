# 如何解决改变@Provide修饰的值，对应UI未刷新的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-566

#### 问题现象

采用@Provide装饰器声明了一个状态变量，通过其它类提供的方法实现数据修改，但是没有触发UI刷新，页面上的数据没有改变。
 
- 首页Index.ets代码如下：
```text
import <span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./PlayInfo'</span>
import <span style="color: rgb(0,0,255);">player </span>from <span style="color: rgb(255,0,170);">'./AVPlayer'</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageStack'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">pageStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'playInfo'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">currentPlayInfo</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">正在播放</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">没有播放</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Change PlayInfo'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">player</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideTitleBar</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 封装PlayInfo类，并导出全局实例对象给到Index.ets页面。

  PlayInfo.ets代码如下：
```text
export class <span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false
  <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span>
<span style="color: rgb(255,0,170);">}</span>

let <span style="color: rgb(0,0,255);">currentPlayInfo </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(0,0,255);">currentPlayInfo </span>as <span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(181,106,1);">;</span>
```

- 封装AVPlayer方法类，修改播放的数据。

  AVPlayer.ets代码如下：
```text
import <span style="color: rgb(0,0,255);">currentPlayInfo </span>from <span style="color: rgb(255,0,170);">'./PlayInfo'</span>

class <span style="color: rgb(0,0,255);">AVPlayer </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">play</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying </span><span style="color: rgb(181,106,1);">= !</span><span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第 </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">首</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>

let <span style="color: rgb(0,0,255);">player </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AVPlayer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(0,0,255);">player </span>as <span style="color: rgb(0,0,255);">AVPlayer</span><span style="color: rgb(181,106,1);">;</span>
```


 
点击“Change PlayInfo”文本时，希望文本“没有播放”更新为“正在播放第XX首”，问题现象如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/nD8PrSHrSDWg9xkZMkJLhw/zh-cn_image_0000002628392140.png?HW-CC-KV=V1&HW-CC-Date=20260811T005819Z&HW-CC-Expire=86400&HW-CC-Sign=5F5E6BF3F2C0850A6FFD3FC80C1BE6E1385BF2F7D61940F08CDDAF9764920B2F)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/dBvoOhz-T1mBhUY4b03sJQ/zh-cn_image_0000002658791421.png?HW-CC-KV=V1&HW-CC-Date=20260811T005819Z&HW-CC-Expire=86400&HW-CC-Sign=B54BEC69745DADE327DAF5B4E2A750B5A1EC2C3C037C170E2B3F14A47BFE1EC6)

 
 

#### 背景知识

- [状态管理概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview)：在声明式UI编程框架中，UI是程序状态的运行结果，用户构建了一个UI模型，其中应用的运行时的状态是参数。当参数改变时，UI作为返回结果，也将进行对应的改变。这些运行时的状态变化所带来的UI的重新渲染，在ArkUI中统称为状态管理机制。自定义组件拥有变量，变量必须被装饰器装饰才可以成为状态变量，状态变量的改变会引起UI的渲染刷新。如果不使用状态变量，UI只能在初始化时渲染，后续将不会再刷新。下图展示了State和View(UI)之间的关系。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/efqm_WZgTIWma6ua2dJLAA/zh-cn_image_0000002628552036.png?HW-CC-KV=V1&HW-CC-Date=20260811T005819Z&HW-CC-Expire=86400&HW-CC-Sign=FC462819930266BD2BEF21DF580E1DA70AB974B5CFA91F1CF701A7BDEDE019B0)

View(UI)：UI渲染，是指把build方法内的UI描述和@Builder装饰的方法内的UI描述映射到界面。
- State：状态，指驱动UI更新的数据。用户通过触发组件的事件方法，改变状态数据。状态数据的改变，将引起UI的重新渲染。
- 状态变量：被状态装饰器装饰的变量，状态变量值的改变会引起UI的渲染更新。示例：@State num: number = 1，其中@State是状态装饰器，num是状态变量。
- 常规变量：没有被状态装饰器装饰的变量，通常应用于辅助计算。它的改变不会引起UI的刷新。

 
 - [@Provide/@Consume装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume)：该装饰器为状态管理装饰器的一种，可以实现组件与后代组件数据的共享与双向同步，修改时可实现同步刷新UI。

 
 

#### 问题定位
1. ArkUI编程框架中，页面刷新需要通过状态装饰器装饰的状态变量的修改刷新UI界面。
2. 对于@Provide装饰器而言，装饰的状态变量会被代理为一个Proxy对象。在问题代码示例中，该代理对象为playInfo，而非currentPlayInfo。因此，AVPlayer类中play()函数虽然修改了对象currentPlayInfo，但是currentPlayInfo对象是普通变量，所以无法刷新UI界面。
 
 

#### 分析结论

play()函数修改的是普通变量currentPlayInfo，而不是状态变量playInfo，所以不会触发UI刷新。play()函数需要修改的是状态变量playInfo，才会刷新UI界面。
 
 

#### 修改建议

应将AVPlayer类中play()函数修改的普通变量currentPlayInfo替换为状态变量playInfo。由于状态变量playInfo并不是全局实例对象，无法通过引用导入的方式修改，所以通过重写play()方法，在调用时传入状态变量playInfo并修改。修改如下：
 1. 定义PlayInfo类。
```text
export class <span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

let <span style="color: rgb(0,0,255);">currentPlayInfo </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(0,0,255);">currentPlayInfo </span>as <span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(181,106,1);">;</span>
```

2. 重写play()方法为需要传参的函数。

  AVPlayer.ets代码如下：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./PlayInfo'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">AVPlayer </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">playNew</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying </span><span style="color: rgb(181,106,1);">= !</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">第 </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">} </span><span style="color: rgb(255,0,170);">首</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>

let <span style="color: rgb(0,0,255);">player </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AVPlayer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(0,0,255);">player </span>as <span style="color: rgb(0,0,255);">AVPlayer</span><span style="color: rgb(181,106,1);">;</span>
```

3. 将状态变量playInfo传入，实现点击修改，并刷新UI界面。首页Index.ets代码如下：

  
```text
import <span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./PlayInfo'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">player </span>from <span style="color: rgb(255,0,170);">'./AVPlayer'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageStack'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">pageStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'playInfo'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PlayInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">currentPlayInfo</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isPlaying</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">正在播放</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">没有播放</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Change PlayInfo'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">需要修改的是状态变量，以实现驱动</span><span style="color: rgb(128,128,128);">UI</span><span style="color: rgb(128,128,128);">更新的效果</span></em>
            <span style="color: rgb(0,0,255);">player</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playNew</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">playInfo </span>as <span style="color: rgb(0,0,255);">PlayInfo</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideTitleBar</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
 

#### 总结

- ArkUI是基于MVVM模式的声明式UI的编程框架，通过状态变量的变化驱动UI的更新，因此在需要更新UI时，需要修改对应的状态变量。
- 对于未被装饰器装饰的变量或者对象等，主要是用于类型声明、初始化、计算等，修改这类普通变量无法直接引起UI数据的刷新。
