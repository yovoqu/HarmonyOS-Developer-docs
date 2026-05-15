# Interface (AudioVolumeGroupManager)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

管理音频组音量。

在使用AudioVolumeGroupManager的接口之前，需先通过[getVolumeGroupManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumegroupmanager9)获取AudioVolumeGroupManager实例。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { audio } from '@kit.AudioKit';
```


## getVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量等级。使用callback异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(
  audio.AudioVolumeType.MEDIA,
  (err: BusinessError, value: number) => {
    if (err) {
      console.error(
        `Failed to get volume. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(`Succeeded in getting volume. Volume: ${value}.`);
  },
);
```


## getVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量等级。使用Promise异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |


**示例：**


```ts
audioVolumeGroupManager
  .getVolume(audio.AudioVolumeType.MEDIA)
  .then((value: number) => {
    console.info(`Succeeded in getting volume. Volume: ${value}.`);
  });
```


## getVolumeSync(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getVolumeSync(volumeType: AudioVolumeType): number

获取指定流的音量等级。同步返回结果。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getVolumeSync(
    audio.AudioVolumeType.MEDIA,
  );
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to get volume. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## getMinVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量等级。使用callback异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMinVolume(
  audio.AudioVolumeType.MEDIA,
  (err: BusinessError, value: number) => {
    if (err) {
      console.error(
        `Failed to get minVolume. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
  },
);
```


## getMinVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量等级。使用Promise异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最小音量等级。 |


**示例：**


```ts
audioVolumeGroupManager
  .getMinVolume(audio.AudioVolumeType.MEDIA)
  .then((value: number) => {
    console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
  });
```


## getMinVolumeSync(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMinVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最小音量等级。同步返回结果。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回最小音量等级。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMinVolumeSync(
    audio.AudioVolumeType.MEDIA,
  );
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to get minVolume. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## getMaxVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量等级。使用callback异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMaxVolume(
  audio.AudioVolumeType.MEDIA,
  (err: BusinessError, value: number) => {
    if (err) {
      console.error(
        `Failed to get maxVolume. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
  },
);
```


## getMaxVolume(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量等级。使用Promise异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最大音量等级。 |


**示例：**


```ts
audioVolumeGroupManager
  .getMaxVolume(audio.AudioVolumeType.MEDIA)
  .then((value: number) => {
    console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
  });
```


## getMaxVolumeSync(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMaxVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最大音量等级。同步返回结果。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回最大音量等级。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMaxVolumeSync(
    audio.AudioVolumeType.MEDIA,
  );
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to get maxVolume. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## isMute(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流静音状态。使用callback异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取指定音量流静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMute(
  audio.AudioVolumeType.MEDIA,
  (err: BusinessError, value: boolean) => {
    if (err) {
      console.error(
        `Failed to use isMute function. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
  },
);
```


## isMute(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流是否被静音。使用Promise异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示静音；返回false表示非静音。 |


**示例：**


```ts
audioVolumeGroupManager
  .isMute(audio.AudioVolumeType.MEDIA)
  .then((value: boolean) => {
    console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
  });
```


## isMuteSync(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMuteSync(volumeType: AudioVolumeType): boolean

获取指定音量流是否被静音。同步返回结果。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 流静音状态。返回true表示静音，返回false表示非静音。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMuteSync(
    audio.AudioVolumeType.MEDIA,
  );
  console.info(`Succeeded in using isMuteSync function. MuteState: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to use isMuteSync function. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## getRingerMode9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)&gt; | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode(
  (err: BusinessError, value: audio.AudioRingMode) => {
    if (err) {
      console.error(
        `Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
  },
);
```


## getRingerMode9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)&gt; | Promise对象，返回系统的铃声模式。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager
  .getRingerMode()
  .then((value: audio.AudioRingMode) => {
    console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## getRingerModeSync10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRingerModeSync(): AudioRingMode

获取铃声模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode) | 返回系统的铃声模式。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to get ringerMode. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## on('ringerModeChange')9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void

监听铃声模式变化事件（当[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当铃声模式发生变化时，触发该事件。 |
| callback | Callback&lt;[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)&gt; | 是 | 回调函数，返回变化后的铃音模式。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
audioVolumeGroupManager.on(
  'ringerModeChange',
  (ringerMode: audio.AudioRingMode) => {
    console.info(
      `Succeeded in using on function. AudioRingMode: ${ringerMode}.`,
    );
  },
);
```


## off('ringerModeChange')18+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void

取消监听铃声模式变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当取消监听铃声模式变化事件时，触发该事件。 |
| callback | Callback&lt;[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)&gt; | 否 | 回调函数，返回变化后的铃音模式。 |


**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
// 取消该事件的所有监听。
audioVolumeGroupManager.off('ringerModeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let ringerModeChangeCallback = (ringerMode: audio.AudioRingMode) => {
  console.info(
    `Succeeded in using on or off function. AudioRingMode: ${ringerMode}.`,
  );
};

audioVolumeGroupManager.on('ringerModeChange', ringerModeChangeCallback);

audioVolumeGroupManager.off('ringerModeChange', ringerModeChangeCallback);
```


## isMicrophoneMute9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute(
  (err: BusinessError, value: boolean) => {
    if (err) {
      console.error(
        `Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`,
      );
      return;
    }
    console.info(
      `Succeeded in using isMicrophoneMute function. MuteState: ${value}.`,
    );
  },
);
```


## isMicrophoneMute9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager
  .isMicrophoneMute()
  .then((value: boolean) => {
    console.info(
      `Succeeded in using isMicrophoneMute function. MuteState: ${value}.`,
    );
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## isMicrophoneMuteSync10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMicrophoneMuteSync(): boolean

获取麦克风静音状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 系统麦克风静音状态。返回true表示静音，返回false表示非静音。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
  console.info(
    `Succeeded in using isMicrophoneMuteSync function. MuteState: ${value}.`,
  );
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to use isMicrophoneMuteSync function. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## on('micStateChange')9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。

目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当检测到系统麦克风状态发生改变时，触发该事件。 |
| callback | Callback&lt;[MicStateChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#micstatechangeevent9)&gt; | 是 | 回调函数，返回变更后的麦克风状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
audioVolumeGroupManager.on(
  'micStateChange',
  (micStateChange: audio.MicStateChangeEvent) => {
    console.info(
      `Succeeded in using on function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`,
    );
  },
);
```


## off('micStateChange')12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void

取消监听系统麦克风状态更改事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当取消监听系统麦克风状态更改事件时，触发该事件。 |
| callback | Callback&lt;[MicStateChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#micstatechangeevent9)&gt; | 否 | 回调函数，返回变更后的麦克风状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
// 取消该事件的所有监听。
audioVolumeGroupManager.off('micStateChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let micStateChangeCallback = (micStateChange: audio.MicStateChangeEvent) => {
  console.info(
    `Succeeded in using on or off function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`,
  );
};

audioVolumeGroupManager.on('micStateChange', micStateChangeCallback);

audioVolumeGroupManager.off('micStateChange', micStateChangeCallback);
```


## isVolumeUnadjustable10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isVolumeUnadjustable(): boolean

获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 固定音量模式开关状态。返回true表示固定音量模式，返回false表示非固定音量模式。 |


**示例：**


```ts
let volumeAdjustSwitch: boolean =
  audioVolumeGroupManager.isVolumeUnadjustable();
console.info(
  `Succeeded in using isVolumeUnadjustable function. VolumeUnadjustable: ${volumeAdjustSwitch}.`,
);
```


## getSystemVolumeInDb(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void

获取音量增益dB值。使用callback异步回调。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取音量增益dB值成功，err为undefined，data为获取到的音量增益dB值；否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(
  audio.AudioVolumeType.MEDIA,
  3,
  audio.DeviceType.SPEAKER,
  (err: BusinessError, value: number) => {
    if (err) {
      console.error(
        `Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`,
      );
    } else {
      console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
    }
  },
);
```


## getSystemVolumeInDb(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>

获取音量增益dB值。使用Promise异步回调。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回对应的音量增益dB值。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager
  .getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER)
  .then((value: number) => {
    console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## getSystemVolumeInDbSync(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number

获取音量增益dB值。同步返回结果。


> [!NOTE]
> 从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回对应的音量增益dB值。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(
    audio.AudioVolumeType.MEDIA,
    3,
    audio.DeviceType.SPEAKER,
  );
  console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(
    `Failed to get system volume in db. Code: ${error.code}, message: ${error.message}`,
  );
}
```


## getMaxAmplitudeForInputDevice12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>

获取输入设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回对应设备的电平值，大小在[0, 1]之间。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0, // 音频采集器标志。
};

audio
  .getAudioManager()
  .getRoutingManager()
  .getPreferredInputDeviceForCapturerInfo(capturerInfo)
  .then((data) => {
    audioVolumeGroupManager
      .getMaxAmplitudeForInputDevice(data[0])
      .then((value) => {
        console.info(
          `Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`,
        );
      })
      .catch((err: BusinessError) => {
        console.error(
          `Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`,
        );
      });
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## getMaxAmplitudeForOutputDevice12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>

获取输出设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回对应设备的电平值，大小在[0, 1]之间。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0, // 音频渲染器标志。
};

audio
  .getAudioManager()
  .getRoutingManager()
  .getPreferOutputDeviceForRendererInfo(rendererInfo)
  .then((data) => {
    audioVolumeGroupManager
      .getMaxAmplitudeForOutputDevice(data[0])
      .then((value) => {
        console.info(
          `Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`,
        );
      })
      .catch((err: BusinessError) => {
        console.error(
          `Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`,
        );
      });
  })
  .catch((err: BusinessError) => {
    console.error(
      `Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`,
    );
  });
```


## setMicrophoneMute(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(
      `Failed to set microphone mute. Code: ${err.code}, message: ${err.message}`,
    );
    return;
  }
  console.info('Succeeded in setting microphone mute.');
});
```


## setMicrophoneMute(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**


```ts
audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
  console.info('Succeeded in setting microphone mute.');
});
```
