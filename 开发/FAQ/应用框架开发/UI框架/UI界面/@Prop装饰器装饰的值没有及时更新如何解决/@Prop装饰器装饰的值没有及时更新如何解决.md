# @Prop装饰器装饰的值没有及时更新如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1629

#### 问题现象

使用@Prop装饰器在父子组件间传递数据，当UI首次成功刷新时，子组件@Prop修饰的值并没有更新。
 
问题代码如下：
 
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Prop </span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child callback Prop'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">初始值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">parentFunc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">变更值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Parent State'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parentFunc</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
期待的效果：点击Button后，Button中、弹框提示和日志输出文本均为“变更值”。
 
问题表现如下：
 
当首次点击Button时，Button中文本“初始值”变更为“变更值”，UI刷新成功，但弹窗showToast和输出日志的“from Child callback Prop”的值仍为“初始值”，只有再次点击后，弹窗showToast和输出日志的“from Child callback Prop”的值才会变更为“变更值”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/pqouZ4BeSUeBCwd8aTIqkw/zh-cn_image_0000002628777478.png?HW-CC-KV=V1&HW-CC-Date=20260730T072439Z&HW-CC-Expire=86400&HW-CC-Sign=CA78730616C1C6E90171C474B2E4D28B454C47240DF188D37FC308FA44430BA3)

 
```text
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">41</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">50.041   13492</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">13492   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Parent State </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">41</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">50.042   13492</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">13492   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child callback Prop </span><span style="color: rgb(0,0,255);">初始值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">41</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">51.793   13492</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">13492   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Parent State </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">41</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">51.793   13492</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">13492   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child callback Prop </span><span style="color: rgb(0,0,255);">变更值</span>
```
 
 

#### 背景知识

- [@Prop装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop)装饰的变量可以和父组件建立单向的同步关系。
初始渲染时：

1. 执行父组件的build()函数将创建子组件的新实例，将数据源传递给子组件。
2. 初始化子组件@Prop装饰的变量。
 
- 更新：

1. 子组件@Prop更新时，更新仅停留在当前子组件，不会同步回父组件。
2. 当父组件的数据源更新时，子组件的@Prop装饰的变量将被来自父组件的数据源重置，所有@Prop装饰的本地的修改将被父组件的更新覆盖。
 - [@Watch装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)可以监听状态变量的更新并触发回调函数，回调的触发时机是根据状态变量真正变化的时间。
- [@Link](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link)装饰的变量与其父组件中的数据源共享相同的值。

 
 

#### 问题定位

UI可以正常刷新，说明@Prop的值已经被修改，但弹窗showToast和输出日志的“from Child callback Prop”的值没有变化，是因为@Prop装饰变量时会进行深拷贝，也就是说，@Prop更新变量不是即时的，需要一定时间。
 
参考[@Watch的触发时机](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch#watch的触发时机)，@Watch的回调函数会在其修饰值变更的同时触发，因此，通过@Watch的回调可以验证@Prop的刷新时机。
 
以下示例代码通过@Watch回调的触发时机来观察@Link和@Prop的刷新时机。
 
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Prop @Watch</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'onPropChange'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Link @Watch</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'onLinkChange'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">linkMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onPropChange</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child Prop'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onLinkChange</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child Link'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linkMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child callback Prop'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child callback Link'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linkMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linkMessage </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">初始值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">parentFunc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">变更值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Parent State'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">propMessage</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">linkMessage</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stateMessage</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parentFunc</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
第一次点击Button后，弹窗显示内容为“变更值”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/MoUpH1h8QOuZ1S_BLYdPQw/zh-cn_image_0000002658976793.png?HW-CC-KV=V1&HW-CC-Date=20260730T072439Z&HW-CC-Expire=86400&HW-CC-Sign=ED106E7150DAC002F48F93E07F9D0CBA24216EAECA396D16A681F000D77FB37E)

 
打印日志如下：
 
```text
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">47</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">04.556   20280</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">20280   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child Link </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">47</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">04.556   20280</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">20280   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Parent State </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">47</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">04.556   20280</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">20280   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child callback Prop </span><span style="color: rgb(0,0,255);">初始值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">47</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">04.556   20280</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">20280   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child callback Link </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">47</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">04.565   20280</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">20280   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child Prop </span><span style="color: rgb(0,0,255);">变更值</span>
```
 
查看上述日志的触发时间，发现在同一时间，子组件通过@Link接收父组件中传来的值时，这个值的变更与父组件中值的变更是同步的。而@Prop虽然也能感知父组件中值的变化并更新变量，但由于需要进行深拷贝，所以会略晚于@Link的同步更新。
 
 

#### 分析结论

@Prop装饰变量时会进行深拷贝，因此更新时间会略晚于父组件中值的更新。
 
 

#### 修改建议

如果希望父组件中msg的值更新时，子组件中msg也同步变更，有以下两种方法：
 
- 使用可以与父组件同步更新变量的@Link去同步数据。但需要注意的是，@Prop仅仅是接收数据，修改@Prop的值不会同步给父组件中的变量，而修改@Link的值会同步给父组件中的变量。
- 不依靠装饰器传值，使用代理类的替代方案：1. 定义一个controller类，在controller类中定义和子组件中类型相同的属性，在子组件中将实际封装的属性给到controller。

2. 父组件在使用时，new一个controller对象然后转入子类中，在父组件中调用controller对应的属性。

 
完整示例代码如下：
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">定义</span><span style="color: rgb(128,128,128);">controller</span><span style="color: rgb(128,128,128);">类</span></em>
class <span style="color: rgb(0,0,255);">ChildController </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span>private <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">初始值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ChildController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ChildController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Child '</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">childRef </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ChildController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">parentFunc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">childRef</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">变更值</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'from Parent State'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">childRef</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">updatePromise</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">childRef</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parentFunc </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
点击Button时，弹窗显示“变更值”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/bT8PNFCIQN2n5H54XT4kSg/zh-cn_image_0000002658856853.png?HW-CC-KV=V1&HW-CC-Date=20260730T072439Z&HW-CC-Expire=86400&HW-CC-Sign=4B278188B14408826F8B70AEF8A2D55DFA1753028FBAE70BFCA2BA7193DED644)

 
日志输出如下：
 
```text
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">52</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">19.572   21177</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">21177   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Parent State </span><span style="color: rgb(0,0,255);">变更值</span>
<span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">22 15</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">52</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">19.573   21177</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">21177   </span><span style="color: rgb(0,0,255);">A03d00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">JSAPP                    com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">examp</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(255,0,0);">42649434  </span><span style="color: rgb(0,0,255);">I     from Child  </span><span style="color: rgb(0,0,255);">变更值</span>
```
