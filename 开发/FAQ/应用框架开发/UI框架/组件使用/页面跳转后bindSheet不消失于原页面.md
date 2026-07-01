# 页面跳转后bindSheet不消失于原页面

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-583

#### 问题现象

在A页面打开bindSheet后跳转其他页面，希望返回A页面时bindSheet仍是打开状态。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/exZm3qYCQmyKccojDZJrMQ/zh-cn_image_0000002658791767.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041333Z&HW-CC-Expire=86400&HW-CC-Sign=40A74CBA96A2BBBA7F41304197E46B36403EB4D098017DFD57F73AC13CAED614)

 
 

#### 背景知识

- [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)为组件绑定半模态页面。
- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)用于页面间的路由导航组件，作为页面的根容器使用，[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)作为Navigation目的页面的根节点。
- [pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname11)用于跳转指定的NavDestination页面，同时可以使用onPop回调函数来处理新页面返回的结果。
- onPop的返回类型为[PopInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#popinfo11)，包含一个由开发者定义的对象result，[pop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pop11)方法可以触发onPop回调并传入页面处理结果。

 
 

#### 解决方案
1. 定义状态变量isShow控制bindSheet显隐。
2. 利用onPop回调函数的返回值PopInfo中的result的值决定isShow。在如下代码中，若传回的result的值为1，则令isShow=true。
3. 在子页面中使用pop方法传入result的值。
 
完整示例参考如下：
 
页面一：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义状态变量</span><span style="color: rgb(128,128,128);">isShow</span><span style="color: rgb(128,128,128);">控制</span><span style="color: rgb(128,128,128);">bindSheet</span><span style="color: rgb(128,128,128);">显隐</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">pageInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">myBuilder</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'ToSecondPage'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'SecondPage'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">onPop</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">onPop</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">result </span>as <span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageInfo</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'bindSheet'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindSheet</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isShow</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">myBuilder</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">SheetSize</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MEDIUM</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">blurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Thick</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">showClose</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'title'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">subtitle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'subtitle' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">preferType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">SheetType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CENTER</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
页面二：
 
```text
<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">SecondPageBulider</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">SecondPage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">SecondPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">pageInfo </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onBackPress</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'ToSecondPage'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">navctx</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pageInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">navctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
在“src/main”目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router_map"，并在“src/main/resources/base/profile”目录下新增router_map.json。
 
router_map.json：
 
```ArkTS
{
  <span style="color: rgb(132,63,161);">"routerMap"</span><span style="color: rgb(181,106,1);">: </span>[
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"SecondPage"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"pageSourceFile"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"src/main/ets/pages/PageTwo.ets"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"buildFunction"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"SecondPageBulider"</span>
    }
  ]
}
```
