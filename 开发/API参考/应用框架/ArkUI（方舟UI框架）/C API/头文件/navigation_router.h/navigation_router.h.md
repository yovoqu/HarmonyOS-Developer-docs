# navigation_router.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-navigation-router-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义Navigation和Router组件的相关枚举。
 
**引用文件：** <arkui/node_attributes/navigation_router.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [NDKNavigation](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKNavigation)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_NavDestinationState | ArkUI_NavDestinationState | 定义NavDestination组件的状态。 |
| ArkUI_RouterPageState | ArkUI_RouterPageState | 定义Router（路由页面）的状态。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_NavDestinationState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_NavDestinationState
```
 
**描述**
 
定义NavDestination组件的状态。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NAV_DESTINATION_STATE_ON_SHOW = 0 | NavDestination组件显示。 |
| ARKUI_NAV_DESTINATION_STATE_ON_HIDE = 1 | NavDestination组件隐藏。 |
| ARKUI_NAV_DESTINATION_STATE_ON_APPEAR = 2 | NavDestination从组件树上挂载。 |
| ARKUI_NAV_DESTINATION_STATE_ON_DISAPPEAR = 3 | NavDestination从组件树上卸载。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_SHOW = 4 | NavDestination组件显示之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_HIDE = 5 | NavDestination组件隐藏之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_APPEAR = 6 | NavDestination挂载到组件树之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_WILL_DISAPPEAR = 7 | NavDestination从组件树上卸载之前。 |
| ARKUI_NAV_DESTINATION_STATE_ON_BACK_PRESS = 100 | NavDestination从组件返回。 |
 
 
  

#### ArkUI_RouterPageState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_RouterPageState
```
 
**描述**
 
定义[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)（路由页面）的状态。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ROUTER_PAGE_STATE_ABOUT_TO_APPEAR = 0 | Router Page即将创建。 |
| ARKUI_ROUTER_PAGE_STATE_ABOUT_TO_DISAPPEAR = 1 | Router Page即将销毁。 |
| ARKUI_ROUTER_PAGE_STATE_ON_SHOW = 2 | Router Page显示。 |
| ARKUI_ROUTER_PAGE_STATE_ON_HIDE = 3 | Router Page隐藏。 |
| ARKUI_ROUTER_PAGE_STATE_ON_BACK_PRESS = 4 | Router Page返回时。 |
