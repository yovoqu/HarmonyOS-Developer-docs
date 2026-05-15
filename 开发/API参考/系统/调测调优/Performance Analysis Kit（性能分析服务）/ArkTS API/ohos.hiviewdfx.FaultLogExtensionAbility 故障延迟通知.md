# @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本模块实现故障的延迟通知功能。

[HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)订阅崩溃、应用冻屏事件时，只有当应用下次启动后才能接收上一次的事件。如果应用无法启动或长时间未打开，则存在故障无法及时上报的局限性。

本模块作为该场景的补充。在应用实现FaultLogExtensionAbility后，当应用发生崩溃或冻屏时，系统服务预计会在30分钟后拉起FaultLogExtensionAbility。

开发者可在[onFaultReportReady](#onfaultreportready)中订阅并处理故障事件。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';
```


## FaultLogExtensionAbility
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

应用接入故障延迟通知需要通过FaultLogExtensionAbility实现，开发者可以在[onFaultReportReady](#onfaultreportready)中订阅并处理故障事件。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/gjxxE8yYQja7qLfl682Jmg/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084743Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0E12A2BFA045E57EA0A2EA398E00D37881BFFCDBD39DD09257507654FFC3AB7)

- FaultLogExtensionAbility被拉起后只有很短的时间完成故障处理，建议处理时间不要超过10秒。超时没有处理完成可以在[onDisconnect](#ondisconnect)中保存状态。
- 从开机或上次拉起FaultLogExtensionAbility后，应用首次触发崩溃或冻屏开始计时。在拉起FaultLogExtensionAbility前反复触发崩溃或冻屏事件均不会重新计时。
- FaultLogExtensionAbility自身崩溃时，不会再次被系统服务拉起。


### 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FaultLogExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext) | 否 | 否 | FaultLogExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。 |


### onConnect
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onConnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成连接时调用此接口，用于执行初始化操作，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**


```ts
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
  onConnect() {
    console.info('onConnect');
  }
}
```


### onDisconnect
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onDisconnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成断开连接时调用此接口，用于释放资源清理运行状态，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**


```ts
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
  onDisconnect() {
    console.info('onDisconnect');
  }
}
```


### onFaultReportReady
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onFaultReportReady(): void

FaultLogExtensionAbility回调。系统服务通知FaultLogExtensionAbility可以进行故障处理时，回调此接口，可以在该方法中订阅故障事件进行处理。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**


```ts
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
  onFaultReportReady() {
    hiAppEvent.addWatcher({
      name: 'watcher',
      appEventFilters: [
        {
          domain: hiAppEvent.domain.OS,
          names: [hiAppEvent.event.APP_CRASH, hiAppEvent.event.APP_FREEZE],
        },
      ],
      onReceive: (
        domain: string,
        appEventGroups: Array<hiAppEvent.AppEventGroup>,
      ) => {
        // 进行故障事件处理
      },
    });
  }
}
```


## 附录
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本模块不允许调用的API名单如下。


| Kit名称 | 模块名称 |
| --- | --- |
| AVSessionKit | [@ohos.multimedia.avsession (媒体会话管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession) |
| AbilityKit | [@ohos.UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) |
| ArkUI | [@ohos.window (窗口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window) |
| AudioKit | [@ohos.multimedia.audio (音频管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (后台任务管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-backgroundtaskmanager) |
| BackgroundTasksKit | [@ohos.reminderAgent (后台代理提醒)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagent) |
| BackgroundTasksKit | [@ohos.reminderAgentManager (后台代理提醒)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager) |
| BackgroundTasksKit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager) |
| BasicServicesKit | [@ohos.power (系统电源管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-power) |
| BasicServicesKit | [@ohos.wallpaper (壁纸)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper) |
| CameraKit | [@ohos.multimedia.camera (相机管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera) |
| CameraKit | [@ohos.multimedia.cameraPicker (相机选择器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camerapicker) |
| ConnectivityKit | [@ohos.wifiManager (WLAN)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager) |
| ConnectivityKit | [@ohos.wifiManagerExt (WLAN扩展接口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext) |
| ConnectivityKit | [@ohos.wifiext (WLAN扩展接口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiext) |
| IMEKit | [@ohos.inputMethod (输入法框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod) |
| MediaLibraryKit | [@ohos.multimedia.movingphotoview (动态照片)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview) |
| NotificationKit | [@ohos.notification (Notification模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification) |
| NotificationKit | [@ohos.notificationManager (NotificationManager模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager) |
| SensorServiceKit | [@ohos.vibrator (振动)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator) |
| TelephonyKit | [@ohos.telephony.call (拨打电话)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call) |
| TelephonyKit | [@ohos.telephony.sim (SIM卡管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim) |
| TelephonyKit | [@ohos.telephony.sms (短信服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sms) |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (用户认证)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth) |
