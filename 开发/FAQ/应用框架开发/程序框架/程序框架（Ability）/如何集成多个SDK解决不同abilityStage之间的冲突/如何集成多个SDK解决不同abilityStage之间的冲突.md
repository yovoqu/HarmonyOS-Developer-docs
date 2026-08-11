# 如何集成多个SDK解决不同abilityStage之间的冲突

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-161

#### 问题现象

应用集成多个SDK，不同的SDK均需要添加abilityStage工程文件。第一个SDK需要创建entry/src/main/ets/abilityStage/OneAbilityStage.ets，第二个SDK需要创建entry/src/main/ets/abilityStage/TwoAbilityStage.ets，而在模块的module.json5文件中添加srcEntry路径时，只能填入一个路径，如何解决该问题？
 
 

#### 背景知识

[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)是一个[Module级别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-overview#应用的多module设计机制)的组件管理器，用于进行Module级别的资源预加载、线程创建等初始化操作，以及维护Module下的应用状态。
 
 

#### 解决方案

由于AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。因此，无法在模块的module.json5文件中配置多个srcEntry，即指向abilityStage文件的地址。如果项目中集成多个SDK均需要配置abilityStage工程文件，可以将不同SDK的abilityStage工程文件合并成一个。如果在合并过程中存在命名冲突的问题，可以在导入函数时，通过重命名的方法来解决。示例代码如下：
 
模仿OneSDK提供的方法：
 
```text
export function <span style="color: rgb(0,0,255);">preInit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'strOne' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
模仿TwoSDK提供的方法：
 
```text
export function <span style="color: rgb(0,0,255);">preInit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'strTwo' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
使用方合并采用的方法：
 
```text
import <span style="color: rgb(0,0,255);">AbilityStage </span>from <span style="color: rgb(255,0,170);">'@ohos.app.ability.AbilityStage'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">preInit </span>as <span style="color: rgb(0,0,255);">preInitOne </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./OneAnalytics'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">preInit </span>as <span style="color: rgb(0,0,255);">preInitTwo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./TwoAnalytics'</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">MyAbilityStage </span>extends <span style="color: rgb(0,0,255);">AbilityStage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">preInitOne</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'One'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">preInitTwo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Two'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```
