# gameBuddyService（游戏伴随服务）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-gamebuddyservice
**支持设备：** Phone | Tablet | TV

本模块提供游戏伴随服务能力。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  

#### 导入模块

**支持设备：** Phone | Tablet | TV

```text
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
```
 
  

#### GameApplicationStatus

**支持设备：** Phone | Tablet | TV

此枚举描述游戏应用状态。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOREGROUND | 1 | 游戏应用处于前台。 |
| BACKGROUND | 2 | 游戏应用处于后台。 |
| TERMINATED | 3 | 游戏应用已终止。 |
| BUDDY_TERMINATED | 4 | 游戏伴随服务已终止。 |
 
 
  

#### MessageType

**支持设备：** Phone | Tablet | TV

此枚举描述消息类型，用于客户端应用发送状态消息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| INFORMATION | 1 | 信息类型。 |
| WARNING | 2 | 警告类型。 |
| ERROR | 3 | 错误类型。 |
 
 
  

#### AudioInfo

**支持设备：** Phone | Tablet | TV

音频信息结构体，描述在游戏伴随服务和客户端应用之间传输的音频数据属性。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioType | string | 否 | 否 | 音频数据类型。当前支持的音频数据类型为PCM。 |
| sampleRate | number | 否 | 否 | 音频数据采样率。 当前支持的音频数据采样率为16000Hz。 |
| sampleBit | number | 否 | 否 | 音频数据采样位数。当前支持的音频数据采样位数为16位。 |
| channel | number | 否 | 否 | 音频通道。当前支持的音频通道数为1。 |
| audioData | ArrayBuffer | 否 | 否 | 音频数据。 |
 
 
  

#### QueryMessage

**支持设备：** Phone | Tablet | TV

查询信息结构体，描述发送给客户端应用进行用户查询的数据属性。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioInfo | AudioInfo | 否 | 是 | 音频信息。 |
 
 
  

#### AppStateMessage

**支持设备：** Phone | Tablet | TV

应用状态信息结构体，描述客户端应用可发送的状态的数据属性。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | MessageType | 否 | 否 | 消息类型。 |
| message | string | 否 | 否 | 消息内容。 |
 
 
  

#### setFloatWindowAvatar

**支持设备：** Phone | Tablet | TV

setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise&lt;void&gt;
 
设置悬浮窗的头像和头像描述。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| avatar | image.PixelMap | 是 | 头像。支持设置的头像图片分辨率为30x30至200x200像素。 |
| avatarDescription | string | 否 | 头像描述。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |
| 1009503004 | Invalid avatar resolution. Please set the image resolution between 30x30 and 200x200 pixels. |
 
 
**示例**：
 
```text
import { image } from '@kit.ImageKit';
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 3,
    size: { height: 100, width: 100 }
};
let pixelMap = image.createPixelMapSync(opts);
gameBuddyService.setFloatWindowAvatar(pixelMap, 'avatar description').then(() => {
  hilog.info(0x0000, 'gameBuddyService', `Set avatar success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService', `Set avatar failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});
```
 
  

#### sendAppStateMessage

**支持设备：** Phone | Tablet | TV

sendAppStateMessage(message: AppStateMessage): Promise&lt;void&gt;
 
客户端应用发送状态消息给游戏伴随服务。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | AppStateMessage | 是 | 发送的状态消息。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |
 
 
**示例**：
 
```text
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const message:gameBuddyService.AppStateMessage = {
    type: gameBuddyService.MessageType.INFORMATION,
    message: 'App is running normally'
};

gameBuddyService.sendAppStateMessage(message).then(() => {
  hilog.info(0x0000, 'gameBuddyService', `send appState message success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService', `send appState message failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});
```
 
  

#### onGameApplicationStatus

**支持设备：** Phone | Tablet | TV

onGameApplicationStatus(callback: Callback&lt;GameApplicationStatus&gt;): void
 
注册游戏应用状态变化的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;GameApplicationStatus&gt; | 是 | 回调函数，返回GameApplicationStatus对象。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |
 
 
**示例**：
 
```text
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数注册
try {
  gameBuddyService.onGameApplicationStatus((status) => {
    hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${status}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册
let statusCallback = (status: gameBuddyService.GameApplicationStatus) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${status}`);
};
try {
  gameBuddyService.onGameApplicationStatus(statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
 
  

#### offGameApplicationStatus

**支持设备：** Phone | Tablet | TV

offGameApplicationStatus(callback?: Callback&lt;GameApplicationStatus&gt;): void
 
取消游戏应用状态变化的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;GameApplicationStatus&gt; | 否 | 回调函数，返回GameApplicationStatus对象。需与注册时传入的回调函数是同一个。若不设置该参数，则取消注册所有的回调函数监听事件。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
 
 
**示例**：
 
```text
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数或无回调调用，取消该事件所有监听
// 无回调
try {
  gameBuddyService.offGameApplicationStatus();
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 匿名函数
try {
  gameBuddyService.offGameApplicationStatus((status) => {
    hilog.info(0x0000, 'gameBuddyService', `Game application status: ${status}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册，则仅取消该特定函数的监听
let statusCallback = (status:gameBuddyService.GameApplicationStatus) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${status}`);
};
try {
  gameBuddyService.offGameApplicationStatus( statusCallback );
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
 
  

#### onQueryMessage

**支持设备：** Phone | Tablet | TV

onQueryMessage(callback: Callback&lt;QueryMessage&gt;): void
 
注册用户查询消息的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;QueryMessage&gt; | 是 | 回调函数，返回QueryMessage对象。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |
| 1009503003 | The game buddy service fails to start audio capture. Please perform audio capture directly or try again later. |
 
 
**示例**：
 
```json
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数注册
try {
  gameBuddyService.onQueryMessage((message) => {
    hilog.info(0x0000, 'gameBuddyService', `Query message received: ${JSON.stringify(message)}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册
let messageCallback = (message: gameBuddyService.QueryMessage) => {
  hilog.info(0x0000, 'gameBuddyService', `Query message received: ${JSON.stringify(message)}`);
};
try {
  gameBuddyService.onQueryMessage(messageCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
 
  

#### offQueryMessage

**支持设备：** Phone | Tablet | TV

offQueryMessage(callback?: Callback&lt;QueryMessage&gt;): void
 
取消用户查询消息的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;QueryMessage&gt; | 否 | 回调函数，返回QueryMessage对象。需与注册时传入的回调函数是同一个。若不设置该参数，则取消注册所有的回调函数监听事件。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
 
 
**示例**：
 
```json
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数或无回调调用，取消该事件所有监听
// 无回调
try {
  gameBuddyService.offQueryMessage();
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 匿名函数
try {
  gameBuddyService.offQueryMessage((message) => {
    hilog.info(0x0000, 'gameBuddyService', `Query message received: ${JSON.stringify(message)}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册，则仅取消该特定函数的监听
let messageCallback = (message:gameBuddyService.QueryMessage) => {
  hilog.info(0x0000, 'gameBuddyService', `Query message received: ${JSON.stringify(message)}`);
};
try {
  gameBuddyService.offQueryMessage( messageCallback );
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
 
  

#### onGameSnapshot

**支持设备：** Phone | Tablet | TV

onGameSnapshot(callback: Callback&lt;number&gt;): void
 
注册游戏应用截图的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;number&gt; | 是 | 回调函数，返回文件描述符。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |
 
 
**示例**：
 
```text
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数注册
try {
  gameBuddyService.onGameSnapshot((fd) => {
    hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册
let snapShotCallback = (fd: number) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};
try {
  gameBuddyService.onGameSnapshot(snapShotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
 
  

#### offGameSnapshot

**支持设备：** Phone | Tablet | TV

offGameSnapshot(callback?: Callback&lt;number&gt;): void
 
取消游戏应用截图的事件监听。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_GAME_BUDDY_SERVICE
 
**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;number&gt; | 否 | 回调函数，返回文件描述符。需与注册时传入的回调函数是同一个。若不设置该参数，则取消注册所有的回调函数监听事件。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
 
 
**示例**：
 
```text
import {gameBuddyService} from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数或无回调调用，取消该事件所有监听
// 无回调
try {
  gameBuddyService.offGameSnapshot();
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 匿名函数
try {
  gameBuddyService.offGameSnapshot((fd) => {
    hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册，则仅取消该特定函数的监听
let snapShotCallback = (fd: number) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};
try {
  gameBuddyService.offGameSnapshot(snapShotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
