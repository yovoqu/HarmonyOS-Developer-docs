# Interface (NativeMediaPlayerBridge)

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerbridge
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

[CreateNativeMediaPlayerCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-t#createnativemediaplayercallback12)回调函数的返回值类型。接管网页媒体的播放器和ArkWeb内核之间的一个接口类。
 
ArkWeb内核通过该接口类的实例对象来控制应用创建的用来接管网页媒体的播放器。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Interface首批接口从API version 12开始支持。 示例效果请以真机运行为准。

  

#### updateRect12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

updateRect(x: number, y: number, width: number, height: number): void
 
更新surface位置信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | surface相对于Web组件的x坐标信息。 单位：px。 |
| y | number | 是 | surface相对于Web组件的y坐标信息。 单位：px。 |
| width | number | 是 | surface的宽度。 单位：px。 |
| height | number | 是 | surface的高度。 单位：px。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### play12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

play(): void
 
播放媒体。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### pause12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pause(): void
 
暂停播放。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### seek12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(targetTime: number): void
 
跳转播放进度到指定时间点。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetTime | number | 是 | 播放跳转到的时间点。 单位：秒。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### setVolume12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVolume(volume: number): void
 
设置播放器音量值。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 播放器的音量。 取值范围：[0, 1.0]，其中0表示静音，1.0表示最大音量。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### setMuted12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setMuted(muted: boolean): void
 
设置静音状态。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muted | boolean | 是 | 是否静音。 true表示静音，false表示未静音。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### setPlaybackRate12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setPlaybackRate(playbackRate: number): void
 
设置播放速率。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| playbackRate | number | 是 | 播放速率。 取值范围：[0, 10.0]，其中1表示原速播放。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### release12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): void
 
销毁播放器。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### enterFullscreen12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

enterFullscreen(): void
 
播放器进入全屏。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### exitFullscreen12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

exitFullscreen(): void
 
播放器退出全屏。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### resumePlayer12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

resumePlayer?(): void
 
通知应用重建播放器，并恢复播放器的状态信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
 
  

#### suspendPlayer12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

suspendPlayer?(type: SuspendType): void
 
通知应用销毁播放器，并保存播放器的状态信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | SuspendType | 是 | 播放器挂起类型。 |
 
 
**示例：**
 
完整示例代码参考[onCreateNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#oncreatenativemediaplayer12)。
