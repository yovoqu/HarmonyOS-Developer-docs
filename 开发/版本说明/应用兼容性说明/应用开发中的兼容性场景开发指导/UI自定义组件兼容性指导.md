# UI自定义组件兼容性指导

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-ui-component

在UI自定义组件中，状态管理装饰器需要通过自定义组件进行API版本隔离。
 
例如：在滚动列表滑动复用场景，@ReusableV2自定义组件复用新特性的API是在SDK版本5.1.0(18)提供，为了让应用兼容在基于API版本5.0.0(12)的老设备正常运行，开发者可以使用deviceInfo.sdkApiVersion进行兼容性判断。
 
（1）开发者需要提供基于API版本5.0.0(12)的自定义组件“V1Component” 及 5.1.0(18)的复用自定义组件“ReuseComponentV2”；
 
（2）在LazyForEach中使用 deviceInfo.sdkApiVersion进行兼容判断使用哪个自定义组件。
 
代码示例如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">deviceInfo </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">BasicDataSource </span>implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  public <span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listener </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">DataChangeListener</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listener </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BasicDataSource </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">BasicDataSource</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">deviceInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sdkApiVersion </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">18</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">ReuseComponentV2</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在</span><span style="color: rgb(128,128,128);">ROM</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">API</span><span style="color: rgb(128,128,128);">版本是</span><span style="color: rgb(128,128,128);">5.1.0(18)</span><span style="color: rgb(128,128,128);">及以上，使用</span><span style="color: rgb(128,128,128);">@ReusableV2</span><span style="color: rgb(128,128,128);">的复用组件</span>
          <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">V1Component</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)  </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在</span><span style="color: rgb(128,128,128);">ROM</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">API</span><span style="color: rgb(128,128,128);">版本是</span><span style="color: rgb(128,128,128);">5.1.0(18)</span><span style="color: rgb(128,128,128);">以下，使用</span><span style="color: rgb(128,128,128);">V1</span><span style="color: rgb(128,128,128);">的的普通组件</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">状态管理</span><span style="color: rgb(128,128,128);">V1</span><span style="color: rgb(128,128,128);">的自定义组件</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">V1Component </span><span style="color: rgb(181,106,1);">{   </span><span style="color: rgb(128,128,128);">// V1</span><span style="color: rgb(128,128,128);">的复用自定义组件</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`V1Component-- aboutToAppear`</span><span style="color: rgb(255,0,170);">)  </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果是</span><span style="color: rgb(128,128,128);">5.1.0(18)</span><span style="color: rgb(128,128,128);">以下的版本，</span><span style="color: rgb(128,128,128);">V1</span><span style="color: rgb(128,128,128);">的会创建</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">BaseCom</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(255,0,170);">)  </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">公共</span><span style="color: rgb(128,128,128);">UI</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">状态管理</span><span style="color: rgb(128,128,128);">V2</span><span style="color: rgb(128,128,128);">的自定义组件</span>
<span style="color: rgb(181,106,1);">@ReusableV2</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">ReuseComponentV2 </span><span style="color: rgb(181,106,1);">{  </span><span style="color: rgb(128,128,128);">// V2</span><span style="color: rgb(128,128,128);">的复用自定义组件</span>
  <span style="color: rgb(181,106,1);">@Param </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">aboutToReuse</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`ReuseComponentV2-- aboutToReusableV2`</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果是</span><span style="color: rgb(128,128,128);">5.1.0(18)</span><span style="color: rgb(128,128,128);">及以上的版本，</span><span style="color: rgb(128,128,128);">V2</span><span style="color: rgb(128,128,128);">复用组件生效</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">BaseCom</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">公共的</span><span style="color: rgb(128,128,128);">UI</span>
<span style="color: rgb(181,106,1);">@Builder </span>function <span style="color: rgb(0,0,255);">BaseCom</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{  </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">@Builder</span><span style="color: rgb(128,128,128);">抽取公共</span><span style="color: rgb(128,128,128);">UI</span><span style="color: rgb(128,128,128);">组件</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'ReuseComponentChild num:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
在上述示例中，通过deviceInfo.sdkApiVersion来判断API版本：
 
（1）当识别当前设备ROM的API版本是5.1.0(18)及以上版本的设备，V2的复用组件会生效，往下滑动页面，会打印"ReuseComponentV2-- aboutToReusableV2"日志，即“ReuseComponentV2”的组件在滑动过程被复用；
 
（2）如果是5.1.0(18)以下的版本，会创建V1组件，会打印"V1Component-- aboutToAppear"的日志，即“V1Component”的组件在滑动过程被创建。
