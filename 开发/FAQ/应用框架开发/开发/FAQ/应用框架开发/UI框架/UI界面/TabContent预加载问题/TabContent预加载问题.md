# TabContent预加载问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1137

#### 问题现象

在aboutToAppear回调中使用preloadItems方法来实现TabContent组件的预加载，结果未生效，为什么？如何解决？
 
 

#### 背景知识

- [aboutToAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行，早于[Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)组件的渲染。
- [preloadItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#preloaditems12)是控制器[TabsController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)的一个方法，能够控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，预加载到不存在的索引时就会报错。
- Router路由与导航Navigation各自的生命周期不同，具体情况如下图：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kBuBkw9bTdCm6ziTs8Iq1A/zh-cn_image_0000002658928745.png?HW-CC-KV=V1&HW-CC-Date=20260811T005648Z&HW-CC-Expire=86400&HW-CC-Sign=D5878B1CE26594F749D745EF2E1B0400C45BC577CEA6F008ADED40CD9A4B7733)
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Zs-NAF35T5aKPqgNKn5y2A/zh-cn_image_0000002658808797.png?HW-CC-KV=V1&HW-CC-Date=20260811T005648Z&HW-CC-Expire=86400&HW-CC-Sign=40DF94AE505492E70004E73789F9DC810C8894F88D807CC94F9FC6EA64EA52DC)


 
 

#### 问题定位

在Tabs组件中，将预加载方法preloadItems在aboutToAppear方法中直接调用，由于aboutToAppear会在Tabs组件完成渲染前就被调用，Tabs组件的索引也就获取不到，因此导致preloadItems方法预加载了不存在的索引，从而预加载失败并且产生报错。
 
 

#### 分析结论

预加载方法preloadItems在aboutToAppear回调中被直接调用，导致预加载了不存在的索引，从而致使预加载失败。
 
 

#### 修改建议

aboutToAppear被调用的时候Tabs组件尚未完成渲染，导致Tabs的预加载方法加载不存在的索引，从而预加载失败，使用执行时间相对靠后的**生命周期**执行预加载方法即可预防问题，方案如下：
 
- **场景一**：使用Router页面生命周期函数[onPageShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow)。

  onPageShow回调在Router页面每次显示时都会触发一次，可以在该生命周期中调用预加载方法preloadItems，通过打印日志的方法来判断TabContent预加载是否成功，调用onPageShow的示例代码如下：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RouterPageShowSolution </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">tabsController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TabsController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TabsController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">tabsData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onPageShow</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">preloadItems</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'onPageShow preloadItems success.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to publish notification, error</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **场景二**：使用组件挂载事件[onAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide#onappear)。onAppear回调在组件挂载显示后触发，可以在该生命周期中调用预加载方法preloadItems，通过打印日志的方法来判断TabContent预加载是否成功，调用onAppear的示例代码如下：

  
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NavAppearSolution </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">tabsController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TabsController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TabsController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">tabsData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabsController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">preloadItems</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">])</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'onAppear preloadItems success.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to publish notification, error</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 常见FAQ

Q：Tabs组件预加载生效之后会调用aboutToAppear方法吗？
 
A：被预加载的TabContent中的对应控件的aboutToAppear方法会被调用，可以添加日志来验证。
 
Q：有没有办法能够在aboutToAppear回调里进行预加载？
 
A：确认TabContent创建完成后再进行Tabs组件的预加载，可以通过同步获取数据再进行预加载。
 
Q：为什么页面组件在TabContent加载的时候只调用aboutToAppear，不调用onPageShow？
 
A：onPageShow是页面级的生命周期，Tabs切换触发的应该是子组件组件级的生命周期aboutToAppear。
 
 

#### 总结

由于aboutToAppear回调会在执行其build()函数之前执行，此时preloadItems方法让未完成渲染的Tabs组件去预加载子组件会失败，本文主要提供了两种方案，onPageShow回调和onAppear回调都能够在Tabs渲染完成之后调用。
