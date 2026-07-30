# 活体检测完成返回指定Navigation路由页面功能实现

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-8

#### 问题现象

[startLivenessDetection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection)接口的参数[InteractiveLivenessConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#interactivelivenessconfig)中可以设置successfulRouteUrl和failedRouteUrl分别作为人脸活体检测成功/失败后跳转的页面路径。页面路由只支持Router方式，不支持Navigation方式。
 
如何实现检测结束后自动跳转到Navigation路由的指定页面？
 
 

#### 背景知识

- 人脸活体检测具有两个同名startLivenessDetection接口：[startLivenessDetection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection)跳转到人脸活体检测页面的入口，使用Promise异步回调；[startLivenessDetection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection)跳转到人脸活体检测页面的入口，使用Promise异步回调获取跳转结果，使用callback回调获取检测结果。
- [Navigation路由操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation#路由操作)支持：页面跳转、页面替换、参数获取等多种。

 
 

#### 解决方案

实现思路：在[startLivenessDetection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection)接口的callback回调函数中获取检测结果，再根据检测结果调用NavPathStack.pushPath()（或NavPathStack.replacePath()）方法跳转到成功/失败页面。
 
具体步骤：
 
- 定义检测结果对象，可根据业务需求自定义实现，简单示例：
```text
<span style="color: rgb(128,128,128);">/**</span>
<span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">人脸识别结果对象</span>
<span style="color: rgb(128,128,128);"> */</span>
export class <span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义</span><span style="color: rgb(128,128,128);">code</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">message</span>
  <span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">|</span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
- [startLivenessDetection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection)接口的callback回调函数中获取检测结果：
```text
<span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startLivenessDetection</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">routerOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InteractiveLivenessResult </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当路由跳转错误时，获取结果失败，</span><span style="color: rgb(128,128,128);">result</span><span style="color: rgb(128,128,128);">返回</span><span style="color: rgb(128,128,128);">undefined</span>
  let <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  if<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);"> !</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在发生错误如路由跳转失败</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">参数错误</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">权限被拒绝时，会抛出错误码，详见</span><span style="color: rgb(128,128,128);">ArkTS API</span><span style="color: rgb(128,128,128);">错误码</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`LivenessCollectionIndex failed to detect. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">，</span><span style="color: rgb(255,0,170);">message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Error'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'StartLivenessDetectionFailed'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`LivenessCollectionIndex Succeeded in detecting result: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">mPixelMap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Success'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'StartLivenessDetectionSuccess'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Failed'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Detection'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 检测结果目标页面接收路由参数。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getParamByIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is succeed.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```


 
完整示例如下：
 
- 权限声明与路由配置（src/main/module.json5）：
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
    "routerMap": "$profile:route_map", <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">路由配置</span>
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
          }
        ]
      }
    ],
    "extensionAbilities": [
      {
        "name": "EntryBackupAbility",
        "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
        "type": "backup",
        "exported": false,
        "metadata": [
          {
            "name": "ohos.extension.backup",
            "resource": "$profile:backup_config"
          }
        ],
      }
    ],
    "requestPermissions": [ <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">权限声明</span>
      {
        "name": "ohos.permission.CAMERA",
        "reason": "$string:reason_of_camera",
        "usedScene": {
          "when": "always"
        }
      }
    ]
  }
}
```

- 权限原因配置（src/main/resources/base/element/string.json）：
```json
{
  "string": [
    {
      "name": "module_desc",
      "value": "module description"
    },
    {
      "name": "EntryAbility_desc",
      "value": "description"
    },
    {
      "name": "EntryAbility_label",
      "value": "label"
    },
    {
      "name": "reason_of_camera",
      "value": "活体检测"
    }
  ]
}
```

- 路由配置文件（src/main/resources/base/profile/route_map.json）：
```ArkTS
{
  "routerMap": [
    {
      "name": "Detection",
      "pageSourceFile": "src/main/ets/pages/Detection.ets",
      "buildFunction": "DetectionBuilder",
      "data": {
        "description" : "this is Detection"
      }
    },
    {
      "name": "StartLivenessDetectionSuccess",
      "pageSourceFile": "src/main/ets/pages/StartLivenessDetectionSuccess.ets",
      "buildFunction": "StartLivenessDetectionSuccessBuilder",
      "data": {
        "description" : "this is StartLivenessDetectionSuccessBuilder"
      }
    },
    {
      "name": "StartLivenessDetectionFailed",
      "pageSourceFile": "src/main/ets/pages/StartLivenessDetectionFailed.ets",
      "buildFunction": "StartLivenessDetectionFailedBuilder",
      "data": {
        "description" : "this is StartLivenessDetectionFailedBuilder"
      }
    }
  ]
}
```

- 首页（src/main/ets/pages/Index.ets）:
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">param </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRouter</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getParams</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'StartLivenessDetectionSuccess'</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">去检测</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pageInfos</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Detection' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">name</span><span style="color: rgb(128,128,128);">指定的</span><span style="color: rgb(128,128,128);">NavDestination</span><span style="color: rgb(128,128,128);">页面信息入栈</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">NavigationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Auto</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">首页</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 检测页面（src/main/ets/pages/Detection.ets）：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Permissions </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">interactiveLiveness </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.VisionKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(128,128,128);">/**</span>
<span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">人脸识别结果对象</span>
<span style="color: rgb(128,128,128);"> */</span>
export class <span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义</span><span style="color: rgb(128,128,128);">code</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">message</span>
  <span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">|</span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">DetectionBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Detection</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">Detection </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">failResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1008302000</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">array</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Permissions</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'ohos.permission.CAMERA'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">actionsNum</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">isSilentMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DetectionMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">INTERACTIVE_MODE </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DetectionMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">INTERACTIVE_MODE</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Top</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">动作数量：</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actionsNum</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">80 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>

        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">开始检测</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Normal</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">192</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0x317aff)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">56</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startDetection</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">检测页面</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">detectionResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">param </span>as <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">failResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">跳转到人脸活体检测控件</span>
  private <span style="color: rgb(0,0,255);">routerLibrary</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">routerOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InteractiveLivenessConfig </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">isSilentMode</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isSilentMode</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">routeMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">RouteRedirectionMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BACK_MODE</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">actionsNum</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actionsNum</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">canIUse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'SystemCapability.AI.Component.LivenessDetect'</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startLivenessDetection</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">routerOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactiveLiveness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InteractiveLivenessResult </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当路由跳转错误时，获取结果失败，</span><span style="color: rgb(128,128,128);">result</span><span style="color: rgb(128,128,128);">返回</span><span style="color: rgb(128,128,128);">undefined</span>
        let <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        if<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);"> !</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在发生错误如路由跳转失败</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">参数错误</span><span style="color: rgb(128,128,128);">/</span><span style="color: rgb(128,128,128);">权限被拒绝时，会抛出错误码，详见</span><span style="color: rgb(128,128,128);">ArkTS API</span><span style="color: rgb(128,128,128);">错误码</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`LivenessCollectionIndex failed to detect. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">，</span><span style="color: rgb(255,0,170);">message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Error'</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'StartLivenessDetectionFailed'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>

        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`LivenessCollectionIndex Succeeded in detecting result: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">mPixelMap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Success'</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'StartLivenessDetectionSuccess'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finalResult </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(255,0,170);">'code'</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Failed'</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'Detection'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'LivenessCollectionIndex this api is not supported on this device'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">校验</span><span style="color: rgb(128,128,128);">CAMERA</span><span style="color: rgb(128,128,128);">权限</span>
  private <span style="color: rgb(0,0,255);">startDetection</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAtManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestPermissionsFromUser</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">array</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">res</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">res</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">permissions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">res</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">permissions</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'ohos.permission.CAMERA' </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">res</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">authResults</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">routerLibrary</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to request permissions from user. Code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 检测成功页面（src/main/ets/pages/StartLivenessDetectionSuccess.ets）：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./Detection'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">StartLivenessDetectionSuccessBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">StartLivenessDetectionSuccess</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">StartLivenessDetectionSuccess </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Top</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Success'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Green</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">260 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getParamByIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is succeed.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 检测失败页面（src/main/ets/pages/StartLivenessDetectionFailed.ets）：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./Detection'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">StartLivenessDetectionFailedBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">StartLivenessDetectionFailed</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">StartLivenessDetectionFailed </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Top</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Failed'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Red</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bolder</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">260 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      }</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NavDestinationContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DetectionResult </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getParamByIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">DetectionResult</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">detectionResult</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">finalResult</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'message'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Detection result is failed.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 常见FAQ

Q：调用startLivenessDetection接口，没有像期望结果那样跳转到指定页面，而是跳转到默认页面，原因是什么？
 
A：使用callback回调获取检测结果的startLivenessDetection接口，当前只适用于RouteRedirectionMode.BACK_MODE跳转模式。检查入参InteractiveLivenessConfig对象的routeMode属性值是否为RouteRedirectionMode.BACK_MODE。
 
 

#### 总结

通过自行判断检测结果跳转指定页面，可以突破路由方式的限制，更灵活的实现业务需求。
