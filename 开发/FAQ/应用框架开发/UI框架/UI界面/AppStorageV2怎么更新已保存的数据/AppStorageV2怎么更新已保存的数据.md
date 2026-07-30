# AppStorageV2怎么更新已保存的数据

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1336

#### 问题现象

AppStorageV2只有connect、remove、keys方法，没有update更新方法，如何更新已保存的数据？每次更新是否需要remove后再保存新的数据？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/L_jr2R-LTAKGBJEQw6flKA/zh-cn_image_0000002628600020.png?HW-CC-KV=V1&HW-CC-Date=20260730T072450Z&HW-CC-Expire=86400&HW-CC-Sign=342A0025AB474502AA4B1377A34F706FBB4CBEC8399862B5AF5984D068973BE4)

 
 

#### 背景知识

[AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement#appstoragev2)是在应用UI启动时会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorageV2将在应用运行过程保留其数据。数据通过唯一的键字符串值访问。
 
 

#### 解决方案

AppStorageV2当前并未提供更新接口，开发者可以先connect获取已保存的对象，然后直接给对象的属性赋值就可以实现数据更新，示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AppStorageV2 </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">Page </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">promptAction </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">AppStorageV2</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> new <span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">!;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'AppStorageV2 update'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">sample </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">AppStorageV2</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> new <span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">!;</span>
          <span style="color: rgb(0,0,255);">sample</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">p1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'AppStorageV2 get value'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">sample </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">AppStorageV2</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> new <span style="color: rgb(0,0,255);">Sample</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">!;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'p1 =' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">sample</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">p1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@ObservedV2</span>
export class <span style="color: rgb(0,0,255);">Sample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">p1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：AppStorageV2如何保存简单的string、number、boolean等变量？
 
A：AppStorageV2局限性详见[使用限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2#使用限制)。字符串等简单数据保存可参考以下方式：
 1. 参考“解决方案”，将数字（number）等基本类型封装为类。
2. 可以使用String、Number等构造类型：@Local prop: String = AppStorageV2.connect(String, () => new String('test'))!;
 
Q：若AppStorageV2与AppStorage使用相同的Key获取与储存数据是否会导致冲突？
 
A：AppStorageV2与AppStorage使用相同的Key并不会导致冲突。
 
Q：@Monitor如何监听AppStorageV2保存的数据的修改？
 
A：AppStorageV2的connect方法绑定状态变量后，状态变量的修改会同步到AppStorageV2内，可以通过监听该状态变量的修改实现AppStorageV2的修改监听。
