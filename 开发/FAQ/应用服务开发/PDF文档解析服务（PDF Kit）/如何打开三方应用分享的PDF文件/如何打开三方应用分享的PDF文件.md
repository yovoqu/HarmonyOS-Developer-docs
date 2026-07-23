# 如何打开三方应用分享的PDF文件

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-6

#### 问题现象

分享PDF文件时，分享面板没有自己开发的应用，如何打开三方应用分享的PDF文件。
 
 

#### 背景知识

- [分享服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-introduction)为应用提供文本、图片、视频等内容跨应用、跨端分享能力。
- [标准化数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list)（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。
- [应用沙箱](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。
- [预览PDF文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-component)PDF Kit提供了丰富的PDF文档预览能力，比如：页面跳转、页面缩放、单双页显示、页面适配、滚动视图方式预览。

 
 

#### 解决方案
1. 目标应用注册支持分享内容的能力。在应用配置文件添加skills。
```ArkTS
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": [
      "phone"
    ],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          },
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">添加</span><span style="color: rgb(128,128,128);">skill</span><span style="color: rgb(128,128,128);">配置</span></em>
          {
            "actions": [
              <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">必需，声明数据处理能力</span></em>
              "ohos.want.action.viewData",
              "ohos.want.action.sendData"
            ],
            "uris": [
              {
                "scheme": "file",
                <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">目标应用在配置支持接收的数据类型时，需穷举支持的</span><span style="color: rgb(128,128,128);">UTD</span></em>
                "utd": "com.adobe.pdf",
               <em> <span style="color: rgb(128,128,128);">// maxFileSupported</span><span style="color: rgb(128,128,128);">对于归属指定类型的文件，标识一次支持接收的最大数量。默认为</span><span style="color: rgb(128,128,128);">0</span><span style="color: rgb(128,128,128);">，代表不支持此类文件的分享</span></em>
                "maxFileSupported": <span style="color: rgb(0,0,255);">1</span>
              },
              {
                "scheme": "file",
                "utd": "general.object",
                "maxFileSupported": <span style="color: rgb(0,0,255);">1</span>
              }
            ]
          }
        ]
      }
    ]
  }
}
```

2. 获取三方应用分享的内容。由于存在应用沙箱隔离，被分享的目标应用无法直接操作宿主应用沙箱中的文件，需拷贝文件至本应用沙箱。
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIAbility</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">window </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">systemShare </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ShareKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fileIo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">0x0000</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">handleSharedData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onNewWant</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">handleSharedData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WindowStage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Ability onWindowStageCreate'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in loading the content.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">handleSharedData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">systemShare</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSharedData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">systemShare</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SharedData</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getRecords</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">record</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">systemShare</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SharedRecord</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">record</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uri</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

          try <span style="color: rgb(255,0,170);">{</span>
            <em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">uri</span><span style="color: rgb(128,128,128);">，缓存至应用沙箱</span></em>
            const <span style="color: rgb(0,0,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">record</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uri</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_ONLY</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            const <span style="color: rgb(0,0,255);">destPath </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cacheDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'/' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
            const <span style="color: rgb(0,0,255);">outFile </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">destPath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_WRITE </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CREATE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            const <span style="color: rgb(0,0,255);">shareFilePath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">outFile</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">copyFileSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">outFile</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">outFile</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'SHARE_FILE_PATH'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">shareFilePath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to parse share data. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to getSharedData. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```

3. 使用PdfView预览PDF文件。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">pdfService</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">PdfView</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">pdfViewManager </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PDFKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">!;</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">pdfViewManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PdfController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">pdfViewManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PdfController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">预览</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          const <span style="color: rgb(0,0,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'SHARE_FILE_PATH'</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">pdfDocument</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">pdfService</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PdfDocument </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">pdfService</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PdfDocument</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">pdfDocument</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadDocument</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">path</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadDocument</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">path</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">PdfView</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">pageFit</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">pdfService</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">FIT_WIDTH</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">showScroll</span><span style="color: rgb(181,106,1);">: </span>true
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pdfview_app_view'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
 

#### 常见FAQ

Q：为什么WPS移动版分享PDF文件看不到目标应用？
 
A：宿主应用在发起文件分享时，填写的UTD可能有差异，目标应用需穷举支持的UTD类型“general.object”。
