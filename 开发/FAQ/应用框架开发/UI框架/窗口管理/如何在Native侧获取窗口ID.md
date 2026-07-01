# 如何在Native侧获取窗口ID

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1373

#### 问题现象

在进行系统级功能开发、输入事件拦截、无障碍服务、屏幕录制、窗口管理时，如何在Native侧需要获取窗口的ID，以便后续的功能开发。
 
 

#### 背景知识

HarmonyOS的窗口模块将窗口界面分为系统窗口、应用窗口两种基本类型。
 
- 系统窗口：系统窗口指完成系统特定功能的窗口。如音量条、壁纸、通知栏、状态栏、导航栏等。
- 应用窗口：应用窗口区别于系统窗口，指与应用显示相关的窗口。根据显示内容的不同，应用窗口又分为应用主窗口、应用子窗口两种类型。应用窗口开发可以参考[管理应用窗口（Stage模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage)。
应用主窗口：应用主窗口用于显示应用界面，会在"任务管理界面"显示。设置方式参考[设置应用主窗口](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-application-window#设置应用主窗口)。
- 应用子窗口：应用子窗口用于显示应用的弹窗、悬浮窗等辅助窗口，不会在"任务管理界面"显示。应用子窗口的生命周期跟随应用主窗口。设置方式参考[设置应用子窗口](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-application-window#设置应用子窗口)。

 
 
ArkTS与Native跨语言交互开发详见[使用Node-API实现跨语言交互开发流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process)。
 
 

#### 解决方案

实现Native侧获取窗口ID可参考如下步骤：
 1. 由于在Native侧无法直接获取window实例，需要在ArkTS侧EntryAbility的onWindowStageCreate生命周期中获取。
```json
<span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span>void <span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// Main window is created,set main page for this ability</span></em>
  <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">'Ability onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// 1.</span><span style="color: rgb(128,128,128);">获取应用主窗口。</span></em>
  <span style="color: rgb(0,0,255);">let windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Window </span><span style="color: rgb(181,106,1);">| </span>null <span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">let errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">if </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to obtain the main window. CCode:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">windowClass</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">getWindowProperties</span><span style="color: rgb(128,128,128);">方法获取</span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(128,128,128);">信息</span></em>
    <span style="color: rgb(0,0,255);">this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getWindowProperties</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'windowID'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Succeeded in obtaining the main window. Result:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 获取到windowID后，调用Native方法将windowID传入Native侧。
```text
import <span style="color: rgb(0,0,255);">testNapi </span>from <span style="color: rgb(255,0,170);">'libentry.so'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@StorageLink</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'windowID'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'setWindowID'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 在Native侧接收到windowID后，将windowID进行固化用于后续使用。
```text
<span style="color: rgb(0,0,255);">int32_t g_WindowID</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">size_t argc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_value args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_typedarray_type type_napi</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">argc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">napi_get_value_int32</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">g_WindowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">OH_LOG_Print</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">LOG_INFO</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"setWindowID"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"get windowID %{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">g_WindowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
完整示例参考如下：
 
entry>src>main>ets>entryability>EntryAbility.ets：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">COLOR_MODE_NOT_SET</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Main window is created,set main page for this ability</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>// 1.</em><em><span style="color: rgb(128,128,128);">获取应用主窗口。</span></em>
    let <span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMainWindow</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">errCode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to obtain the main window. CCode:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">windowClass</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">getWindowProperties</span><span style="color: rgb(128,128,128);">方法获取</span><span style="color: rgb(128,128,128);">id</span><span style="color: rgb(128,128,128);">信息</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getWindowProperties</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'windowID'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Succeeded in obtaining the main window. Result:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageDestroy'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onForeground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onBackground'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 
entry>src>main>ets>pages>Index.ets：
 
```text
import <span style="color: rgb(0,0,255);">testNapi </span>from <span style="color: rgb(255,0,170);">'libentry.so'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@StorageLink</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'windowID'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'setWindowID'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
entry>src>main>cpp>types>libentry>index.d.ts：
 
```text
export const <span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">;</span>
```
 
entry>src>main>cpp>napi_init.cpp：
 
```text
<em>/*</em>
<em><span style="color: rgb(128,128,128);"> * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>
<span style="color: rgb(181,106,1);">#</span><span style="color: rgb(0,0,255);">include </span><span style="color: rgb(255,0,170);">"napi/native_api.h"</span>
<span style="color: rgb(181,106,1);">#</span><span style="color: rgb(0,0,255);">include </span><span style="color: rgb(255,0,170);">"hilog/log.h"</span>
<span style="color: rgb(0,0,255);">int32_t g_WindowID</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">size_t argc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_value args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_typedarray_type type_napi</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">argc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">napi_get_value_int32</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">g_WindowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">OH_LOG_Print</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">LOG_INFO</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">0x0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"setWindowID"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"get windowID %{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">g_WindowID</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">EXTERN_C_START</span>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">Init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_value exports</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">napi_property_descriptor desc</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  { </span><span style="color: rgb(255,0,170);">"setWindowID"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">setWindowID</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">napi_define_properties</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">desc</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">desc</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">desc</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
return <span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">EXTERN_C_END</span>

<span style="color: rgb(0,0,255);">static napi_module demoModule </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nm_version </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">nm_flags </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">nm_filename </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">nm_register_func </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Init</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">nm_modname </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">"entry"</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">nm_priv </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">((</span>void<span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">  .</span><span style="color: rgb(0,0,255);">reserved </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(0,0,255);">extern </span><span style="color: rgb(255,0,170);">"C" </span><span style="color: rgb(0,0,255);">__attribute__</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">constructor</span><span style="color: rgb(0,0,255);">)) </span>void <span style="color: rgb(0,0,255);">RegisterEntryModule</span><span style="color: rgb(0,0,255);">(</span>void<span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">napi_module_register</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">demoModule</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：Native侧有办法对窗口进行管理和控制么？
 
A：可以通过[WindowManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager)模块的C API对窗口进行控制，由于其接口均需要windowID作为入参，需要在调用前获取到windowID。
 
Q：如何传入多个windowID？
 
A：如果需要传入多个windowID可以通过构建Int32Array进行填充，在Native侧创建数组接收。
