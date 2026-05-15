# Interface (AudioSessionManager)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

音频会话管理。

在使用AudioSessionManager的接口之前，需先通过[getSessionManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager#getsessionmanager12)获取AudioSessionManager实例。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { audio } from '@kit.AudioKit';
```


## activateAudioSession12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

activateAudioSession(strategy: AudioSessionStrategy): Promise<void>

激活音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [AudioSessionStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessionstrategy12) | 是 | 音频会话策略。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800301 | System error. Returned by promise. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS,
};

audioSessionManager
  .activateAudioSession(strategy)
  .then(() => {
    console.info('activateAudioSession SUCCESS');
  })
  .catch((err: BusinessError) => {
    console.error(`ERROR: ${err}`);
  });
```


## deactivateAudioSession12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

deactivateAudioSession(): Promise<void>

停用音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | System error. Returned by promise. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager
  .deactivateAudioSession()
  .then(() => {
    console.info('deactivateAudioSession SUCCESS');
  })
  .catch((err: BusinessError) => {
    console.error(`ERROR: ${err}`);
  });
```


## isAudioSessionActivated12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isAudioSessionActivated(): boolean

检查音频会话是否已激活。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 音频会话是否处于激活状态。true表示已激活，false表示已停用。 |


**示例：**


```ts
let isActivated = audioSessionManager.isAudioSessionActivated();
```


## on('audioSessionDeactivated')12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当音频会话停用时，触发该事件。 |
| callback | Callback&lt;[AudioSessionDeactivatedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessiondeactivatedevent12)&gt; | 是 | 回调函数，返回音频会话停用原因。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
audioSessionManager.on(
  'audioSessionDeactivated',
  (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
    console.info(
      `reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `,
    );
  },
);
```


## off('audioSessionDeactivated')12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void

取消监听音频会话停用事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当取消监听音频会话停用事件时，触发该事件。 |
| callback | Callback&lt;[AudioSessionDeactivatedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessiondeactivatedevent12)&gt; | 否 | 回调函数，返回音频会话停用原因。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
// 取消该事件的所有监听。
audioSessionManager.off('audioSessionDeactivated');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionDeactivatedCallback = (
  audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent,
) => {
  console.info(
    `reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `,
  );
};

audioSessionManager.on(
  'audioSessionDeactivated',
  audioSessionDeactivatedCallback,
);

audioSessionManager.off(
  'audioSessionDeactivated',
  audioSessionDeactivatedCallback,
);
```


## setAudioSessionScene20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAudioSessionScene(scene: AudioSessionScene): void

设置音频会话场景参数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [AudioSessionScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiosessionscene20) | 是 | 音频会话场景。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
audioSessionManager.setAudioSessionScene(
  audio.AudioSessionScene.AUDIO_SESSION_SCENE_MEDIA,
);
```


## on('audioSessionStateChanged')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback&lt;[AudioSessionStateChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessionstatechangedevent20)&gt; | 是 | 回调函数，返回音频会话变更提示信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
audioSessionManager.on(
  'audioSessionStateChanged',
  (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
    console.info(
      `hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `,
    );
  },
);
```


## off('audioSessionStateChanged')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void

取消监听音频会话状态变更事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | ��型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback&lt;[AudioSessionStateChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessionstatechangedevent20)&gt; | 否 | 回调函数，返回音频会话变更提示信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
// 取消该事件的所有监听。
audioSessionManager.off('audioSessionStateChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionStateChangedCallback = (
  audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent,
) => {
  console.info(
    `hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `,
  );
};

audioSessionManager.on(
  'audioSessionStateChanged',
  audioSessionStateChangedCallback,
);

audioSessionManager.off(
  'audioSessionStateChanged',
  audioSessionStateChangedCallback,
);
```


## setDefaultOutputDevice20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

设置默认发声设备。使用Promise方式进行异步回调。


**系统能力：** SystemCapability.Multimedia.Audio.Device

**设备行为差异：** 当该接口在无听筒的设备上设置默认发声设备为听筒时，将继续从扬声器发声。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。          仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800102 | Allocate memory failed. Return by promise. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager
  .setDefaultOutputDevice(audio.DeviceType.SPEAKER)
  .then(() => {
    console.info('setDefaultOutputDevice Success!');
  })
  .catch((err: BusinessError) => {
    console.error(`setDefaultOutputDevice Fail: ${err}`);
  });
```


## getDefaultOutputDevice20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getDefaultOutputDevice(): DeviceType

获取通过[setDefaultOutputDevice](#setdefaultoutputdevice20)设置的默认发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**


| 类型 | 说明 |
| --- | --- |
| DeviceType | 设备类型。          仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. Return by promise. |


**示例：**


```ts
let deviceType = audioSessionManager.getDefaultOutputDevice();
```


## on('currentOutputDeviceChanged')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备变更时触发。 |
| callback | Callback&lt;[CurrentOutputDeviceChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#currentoutputdevicechangedevent20)&gt; | 是 | 回调函数，返回当前输出设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { audio } from '@kit.AudioKit';

let currentOutputDeviceChangedCallback = (
  currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent,
) => {
  console.info(
    `reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `,
  );
};

audioSessionManager.on(
  'currentOutputDeviceChanged',
  currentOutputDeviceChangedCallback,
);
```


## off('currentOutputDeviceChanged')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void

取消监听当前输出设备的变化事件，并使用callback进行异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备发生变化时，触发该事件。 |
| callback | Callback&lt;[CurrentOutputDeviceChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#currentoutputdevicechangedevent20)&gt; | 否 | 回调函数，用于返回当前输出设备变化的信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
// 取消该事件的所有监听。
audioSessionManager.off('currentOutputDeviceChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentOutputDeviceChangedCallback = (
  currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent,
) => {
  console.info(
    `reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `,
  );
};

audioSessionManager.on(
  'currentOutputDeviceChanged',
  currentOutputDeviceChangedCallback,
);

audioSessionManager.off(
  'currentOutputDeviceChanged',
  currentOutputDeviceChangedCallback,
);
```


## getAvailableDevices21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors

获取音频可选设备列表。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiodevicedescriptors) | 返回设备列表。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors =
    audioSessionManager.getAvailableDevices(
      audio.DeviceUsage.MEDIA_OUTPUT_DEVICES,
    );
  console.info('Succeeded in doing getAvailableDevices.');
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## on('availableDeviceChange')21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当音频可选设备连接状态发生变化时，触发该事件。 |
| deviceUsage | [DeviceUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |
| callback | Callback&lt;[DeviceChangeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#devicechangeaction)&gt; | 是 | 回调函数，返回设备更新详情。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
audioSessionManager.on(
  'availableDeviceChange',
  audio.DeviceUsage.MEDIA_INPUT_DEVICES,
  (deviceChanged: audio.DeviceChangeAction) => {
    console.info('device change type : ' + deviceChanged.type);
    console.info(
      'device descriptor size : ' + deviceChanged.deviceDescriptors.length,
    );
    console.info(
      'device change descriptor : ' +
        deviceChanged.deviceDescriptors[0].deviceRole,
    );
    console.info(
      'device change descriptor : ' +
        deviceChanged.deviceDescriptors[0].deviceType,
    );
  },
);
```


## off('availableDeviceChange')21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频可选设备连接状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当取消监听音频可选设备连接变化事件时，触发该事件。 |
| callback | Callback&lt;[DeviceChangeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#devicechangeaction)&gt; | 否 | 回调函数，返回可选设备更新详情。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
// 取消该事件的所有监听。
audioSessionManager.off('availableDeviceChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let availableDeviceChangeCallback = (
  deviceChanged: audio.DeviceChangeAction,
) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info(
    'device descriptor size : ' + deviceChanged.deviceDescriptors.length,
  );
  console.info(
    'device change descriptor : ' +
      deviceChanged.deviceDescriptors[0].deviceRole,
  );
  console.info(
    'device change descriptor : ' +
      deviceChanged.deviceDescriptors[0].deviceType,
  );
};

audioSessionManager.on(
  'availableDeviceChange',
  audio.DeviceUsage.MEDIA_INPUT_DEVICES,
  availableDeviceChangeCallback,
);

audioSessionManager.off('availableDeviceChange', availableDeviceChangeCallback);
```


## selectMediaInputDevice21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>

设置媒体输入设备。使用Promise异步回调。


**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputAudioDevice | [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 是 | 媒体输入设备。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed, for example, the selected device does not exist. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors =
    audioSessionManager.getAvailableDevices(
      audio.DeviceUsage.MEDIA_OUTPUT_DEVICES,
    );
  console.info('Succeeded in doing getAvailableDevices.');

  if (data[0]) {
    audioSessionManager
      .selectMediaInputDevice(data[0])
      .then(() => {
        console.info('Succeeded in doing selectMediaInputDevice.');
      })
      .catch((selectErr: BusinessError) => {
        console.error(
          `Failed to selectMediaInputDevice. Code: ${selectErr.code}, message: ${selectErr.message}`,
        );
      });
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## getSelectedMediaInputDevice21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSelectedMediaInputDevice(): AudioDeviceDescriptor

获得通过[selectMediaInputDevice](#selectmediainputdevice21)设置的媒体输入设备。如果没有设置，返回一个deviceType属性为INVALID的设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 媒体输入设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let device: audio.AudioDeviceDescriptor =
    audioSessionManager.getSelectedMediaInputDevice();
  console.info('Succeeded in doing getSelectedMediaInputDevice.');
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to getSelectedMediaInputDevice. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## clearSelectedMediaInputDevice21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

clearSelectedMediaInputDevice(): Promise<void>

清空通过[selectMediaInputDevice](#selectmediainputdevice21)设置的媒体输入设备。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager
  .clearSelectedMediaInputDevice()
  .then(() => {
    console.info('Succeeded in doing clearSelectedMediaInputDevice.');
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to clearSelectedMediaInputDevice. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## setBluetoothAndNearlinkPreferredRecordCategory21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。使用Promise异步回调。


**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#bluetoothandnearlinkpreferredrecordcategory21) | 是 | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

const category =
  audio.BluetoothAndNearlinkPreferredRecordCategory.PREFERRED_LOW_LATENCY;
audioSessionManager
  .setBluetoothAndNearlinkPreferredRecordCategory(category)
  .then(() => {
    console.info(
      'Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.',
    );
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to setBluetoothAndNearlinkPreferredRecordCategory. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## getBluetoothAndNearlinkPreferredRecordCategory21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory

获取通过[setBluetoothAndNearlinkPreferredRecordCategory](#setbluetoothandnearlinkpreferredrecordcategory21)设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [BluetoothAndNearlinkPreferredRecordCategory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#bluetoothandnearlinkpreferredrecordcategory21) | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let category: audio.BluetoothAndNearlinkPreferredRecordCategory =
    audioSessionManager.getBluetoothAndNearlinkPreferredRecordCategory();
  console.info(
    'Succeeded in doing getBluetoothAndNearlinkPreferredRecordCategory.',
  );
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to getBluetoothAndNearlinkPreferredRecordCategory. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## on('currentInputDeviceChanged')21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback&lt;[CurrentInputDeviceChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#currentinputdevicechangedevent21)&gt; | 是 | 回调函数，返回当前输入设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
import { audio } from '@kit.AudioKit';

let currentInputDeviceChangedCallback = (
  currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent,
) => {
  console.info(
    `reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `,
  );
};

audioSessionManager.on(
  'currentInputDeviceChanged',
  currentInputDeviceChangedCallback,
);
```


## off('currentInputDeviceChanged')21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void

取消监听当前输入设备的变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback&lt;[CurrentInputDeviceChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#currentinputdevicechangedevent21)&gt; | 否 | 回调函数，用于返回当前输入设备变化的信息。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |


**示例：**


```ts
// 取消该事件的所有监听。
audioSessionManager.off('currentInputDeviceChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentInputDeviceChangedCallback = (
  currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent,
) => {
  console.info(
    `reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `,
  );
};

audioSessionManager.on(
  'currentInputDeviceChanged',
  currentInputDeviceChangedCallback,
);

audioSessionManager.off(
  'currentInputDeviceChanged',
  currentInputDeviceChangedCallback,
);
```


## enableMuteSuggestionWhenMixWithOthers23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

enableMuteSuggestionWhenMixWithOthers(enable: boolean): void

启用混音播放下接收静音播放建议通知功能。

通常，当使用混音模式时，如果其他应用同时播放音频，会和其他应用进行混音播放。但在某些场景下（如游戏或广播），应用自身会通过静音自身的音频以给用户提供更好的体验。

如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过[AudioSessionStateChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiosessionstatechangedevent20)回调发送。收到静音建议表示其他应用程序开始播放音频，且播放的音频和本应用的音频不能混音。

此功能仅支持已设置[AudioSessionScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiosessionscene20)并激活模式模式为CONCURRENCY_MIX_WITH_OTHERS的音频会话使用。并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。

详细说明请参考[启用混音播放下静音建议通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-session-management#启用混音播放下静音建议通知)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用混音播放下接收静音播放建议通知功能。true表示启用，false表示不启用。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Function is called without setting [AudioSessionScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiosessionscene20) or called after audio session activation. |
| 6800301 | Audio client call audio service error, system internal error. |


**示例：**


```ts
audio
  .getAudioManager()
  .getSessionManager()
  .enableMuteSuggestionWhenMixWithOthers(true);
```


## setCapturerMuteHint24
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setCapturerMuteHint(mute: boolean): Promise<void>

应用将当前音频会话内录音流的自身静音状态传递给系统音频模块。该接口不会触发录音流静音，当前仅在部分PC/2in1设备上用于优化设备功耗。使用Promise异步回调。


**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 应用自身给系统音频模块上报的静音状态。true表示应用将当前流静音，false表示取消静音。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permitted at current state, there is no audio capturer running. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager
  .setCapturerMuteHint(true)
  .then(() => {
    console.info('Successfully set capturer mute hint.');
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to setCapturerMuteHint. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## isOtherMediaPlaying23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isOtherMediaPlaying(): boolean

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 是否有其他应用正在播放媒体类型的音频。true表示有，false表示没有。 |


**示例：**


```ts
let isExistence = audioSessionManager.isOtherMediaPlaying();
```


## setAudioSessionBehavior24+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAudioSessionBehavior(behavior: number): void

设置音频会话行为参数，支持多种标志位的组合使用。


> [!NOTE]
> 当音频会话在激活状态时调用此接口后，必须重新调用接口[activateAudioSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#activateaudiosession12)使其生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| behavior | number | 是 | 用于设置音频会话行为。          该参数可以是单个标志，也可以是多个标志的按位OR组合。          当前支持的音频会话行为详见[AudioSessionBehaviorFlags](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiosessionbehaviorflags24)中定义的标志。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permitted in the current state. |


**示例：**


```ts
let behavior: number = audio.AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED;
audioSessionManager.setAudioSessionBehavior(behavior);
```
