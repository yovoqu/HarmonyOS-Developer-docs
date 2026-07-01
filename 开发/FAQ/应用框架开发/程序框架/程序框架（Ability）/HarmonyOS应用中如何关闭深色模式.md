# HarmonyOS应用中如何关闭深色模式

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-156

#### 问题现象

HarmonyOS深色模式支持关闭吗？是否可以在APP中不使用深色模式？
 
 

#### 背景知识

- [ApplicationContext.setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetcolormode11)方法可以自定义应用的颜色模式，官网案例参考：[深色模式适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dark-mode-adaptation)。该案例内有详细说明如何实现深浅色模式适配以及如何取消或跟随系统的深浅色切换。
- [setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)方法可以将[ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant#colormode)设置不同的枚举，开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

| 名称 | 值 | 说明 |

| --- | --- | --- |

| COLOR_MODE_NOT_SET | -1 | 表示未设置颜色模式。 |

| COLOR_MODE_DARK | 0 | 表示深色模式。 |

| COLOR_MODE_LIGHT | 1 | 表示浅色模式。 |

 
 

#### 解决方案
1. 应用主动设置深浅色模式的场景。如果应用调用[setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)接口主动设置了深浅色，则以接口效果优先。

  EntryAbility.ets文件示例参考如下：

  
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AbilityConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">UIAbility</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Want </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">window </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Want</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">launchParam</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AbilityConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LaunchParam</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">COLOR_MODE_NOT_SET</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to set colorMode. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);"> + </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">launchParam</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WindowStage</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// Main window is created, set main page for this ability</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Succeeded in loading the content.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(255,255,255);">applicationContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">applicationContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">COLOR_MODE_LIGHT</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span> <em>//</em><em><span style="color: rgb(128,128,128);">主动设置深浅色模式</span></em>
  <span style="color: rgb(181,106,1);">}</span>


  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onForeground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onBackground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">}</span>
```

2. 应用未主动设置深浅色模式的场景。
如果应用工程dark目录下有深色资源，则系统内置组件在深色模式下会自动切换成为深色。
3. 如果应用工程dark目录下没有任何深色资源，则系统内置组件在深色模式下仍会保持浅色体验。
 
 

#### 常见FAQ

Q：在没有调用[setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)接口的情况下，如何修改状态栏的颜色？
 
A：可以在EntryAbility.ets中修改状态栏的颜色。
 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">AbilityConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">UIAbility</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Want </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">window </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Want</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">launchParam</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AbilityConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">LaunchParam</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">COLOR_MODE_NOT_SET</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to set colorMode. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">want</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);"> + </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">launchParam</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  async <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WindowStage</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Main window is created, set main page for this ability</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Succeeded in loading the content.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,0,170);">(</span>await <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowSystemBarProperties</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置状态栏颜色为其他颜色</span></em>
      <span style="color: rgb(255,255,255);">statusBarColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ffa28d8f'</span><span style="color: rgb(181,106,1);">,</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置状态栏文本颜色为白色</span></em>
      <span style="color: rgb(255,255,255);">statusBarContentColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ffe30520'</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>


  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onForeground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onBackground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">}</span>
```
