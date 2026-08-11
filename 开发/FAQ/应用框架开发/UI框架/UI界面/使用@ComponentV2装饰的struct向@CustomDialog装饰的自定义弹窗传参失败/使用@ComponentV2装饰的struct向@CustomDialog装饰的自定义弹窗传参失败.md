# 使用@ComponentV2装饰的struct向@CustomDialog装饰的自定义弹窗传参失败

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-771

#### 问题现象

在@ComponentV2组件中无法直接将数据传递给@CustomDialog组件。
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@ComponentV2</span>
export struct <span style="color: rgb(0,0,255);">Page </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">dialogController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CustomDialogController </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">AccountSafeDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
 <em> <span style="color: rgb(128,128,128);">// ...</span></em>
<span style="color: rgb(255,0,170);">}</span>
```
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">定义弹窗</span></em>
<span style="color: rgb(181,106,1);">@CustomDialog</span>
export struct <span style="color: rgb(0,0,255);">AccountSafeDialog </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Link </span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// ...</span></em>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

- [@ComponentV2装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)为搭配V2状态变量使用的自定义组件装饰器。[@Link装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link)装饰的变量与其父组件中的数据源共享相同的值，[自定义弹窗CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)通过CustomDialogController类显示自定义弹窗，二者均仅在状态管理V1中使用。
- 可以通过使用NavDestination的[Dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationmode枚举说明11)模式实现弹窗。此时整个NavDestination无组件占位部分默认透明显示。

 
 

#### 问题定位

运行代码报错：
 
```text
<span style="color: rgb(0,0,255);">error </span><span style="color: rgb(181,106,1);">message</span><span style="color: rgb(181,106,1);">:</span>undefined <span style="color: rgb(255,0,170);">'selectIndex'</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">21</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">Component </span><span style="color: rgb(255,0,170);">'AccountSafeDialog'</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">375</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">:</span>
<span style="color: rgb(181,106,1);">constructor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">source variable </span>in <span style="color: rgb(0,0,255);">parent</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">ancestor </span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">Component must be defined</span><span style="color: rgb(181,106,1);">. </span><span style="color: rgb(0,0,255);">Application error</span><span style="color: rgb(181,106,1);">!</span>
```
 
报错信息显示无法找到变量selectIndex，代码中使用@Local修饰了selectIndex，说明该变量为父组件传递，检查父组件发现为@ComponentV2修饰组件，与子组件的@CustomDialog装饰器存在不同的状态管理版本。
 
 

#### 分析结论

@ComponentV2装饰器的组件与使用@CustomDialog装饰器的自定义弹窗组件之间存在状态管理版本不兼容，导致数据无法正确传递给使用@CustomDialog装饰器的自定义弹窗组件。
 
 

#### 修改建议

可使用@ComponentV2的Page替换@CustomDialog，使用Navigation的Dialog模式实现弹窗。
 1. Index.ets，通过[pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname11)方法将指定的NavDestination页面信息入栈。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">NavigationExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pushPath'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPathByName</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pageOne'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">, </span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">name</span><span style="color: rgb(128,128,128);">指定的</span><span style="color: rgb(128,128,128);">NavDestination</span><span style="color: rgb(128,128,128);">页面信息入栈</span></em>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'NavIndex'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 创建PageOne.ets，作为弹窗页面，并设置NavDestination的mode为DIALOG模式。
```text
<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">PageOneBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">PageOne</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@ComponentV2</span>
export struct <span style="color: rgb(0,0,255);">PageOne </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectIndex</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">param </span>as <span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">200 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Pink</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">NavDestinationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DIALOG</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideBackButton</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下：
```ArkTS
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```
