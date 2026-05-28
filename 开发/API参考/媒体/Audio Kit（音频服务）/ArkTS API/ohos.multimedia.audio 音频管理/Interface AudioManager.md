# Interface (AudioManager)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

音频音量和设备管理。
 
在使用AudioManager的接口之前，需先通过[getAudioManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-f#audiogetaudiomanager)获取AudioManager实例。
 
> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { audio } from '@kit.AudioKit';
```
 
  

#### getAudioScene8+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioScene(callback: AsyncCallback&lt;AudioScene&gt;): void
 
获取音频场景模式。使用callback异步回调。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AudioScene&gt; | 是 | 回调函数。当获取音频场景模式成功，err为undefined，data为获取到的音频场景模式；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene((err: BusinessError, value: audio.AudioScene) => {
  if (err) {
    console.error(`Failed to obtain the audio scene mode. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the audio scene mode is obtained ${value}.`);
});
```
 
  

#### getAudioScene8+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioScene(): Promise&lt;AudioScene&gt;
 
获取音频场景模式。使用Promise异步回调。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;AudioScene&gt; | Promise对象，返回音频场景模式。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene().then((value: audio.AudioScene) => {
  console.info(`Promise returned to indicate that the audio scene mode is obtained ${value}.`);
}).catch ((err: BusinessError) => {
  console.error(`Failed to obtain the audio scene mode ${err}`);
});
```
 
  

#### getAudioSceneSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioSceneSync(): AudioScene
 
获取音频场景模式。同步返回结果。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioScene | 音频场景模式。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioScene = audioManager.getAudioSceneSync();
  console.info(`indicate that the audio scene mode is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the audio scene mode ${error}`);
}
```
 
  

#### on('audioSceneChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'audioSceneChange', callback: Callback&lt;AudioScene&gt;): void
 
监听音频场景变化事件。使用callback异步回调。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'，当音频场景模式发生变化时，触发该事件。 |
| callback | Callback&lt;AudioScene&gt; | 是 | 回调函数，返回当前音频场景模式。 |
 
 
**示例：**
 
```text
audioManager.on('audioSceneChange', (audioScene: audio.AudioScene) => {
  console.info(`audio scene : ${audioScene}.`);
});
```
 
  

#### off('audioSceneChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'audioSceneChange', callback?: Callback&lt;AudioScene&gt;): void
 
取消监听音频场景变化事件。使用callback异步回调。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'，当取消监听当前音频场景变化事件时，触发该事件。 |
| callback | Callback&lt;AudioScene&gt; | 否 | 回调函数，返回当前音频场景模式。 |
 
 
**示例：**
 
```text
// 取消该事件的所有监听。
audioManager.off('audioSceneChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSceneChangeCallback = (audioScene: audio.AudioScene) => {
  console.info(`audio scene : ${audioScene}.`);
};

audioManager.on('audioSceneChange', audioSceneChangeCallback);

audioManager.off('audioSceneChange', audioSceneChangeCallback);
```
 
  

#### getVolumeManager9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getVolumeManager(): AudioVolumeManager
 
获取音频音量管理器。
 
**元服务API：** 从API version 23开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioVolumeManager | AudioVolumeManager实例。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
```
 
  

#### getStreamManager9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getStreamManager(): AudioStreamManager
 
获取音频流管理器。
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioStreamManager | AudioStreamManager实例。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let audioStreamManager: audio.AudioStreamManager = audioManager.getStreamManager();
```
 
  

#### getRoutingManager9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRoutingManager(): AudioRoutingManager
 
获取音频路由管理器。
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioRoutingManager | AudioRoutingManager实例。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let audioRoutingManager: audio.AudioRoutingManager = audioManager.getRoutingManager();
```
 
  

#### getSessionManager12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSessionManager(): AudioSessionManager
 
获取音频会话管理器。
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioSessionManager | AudioSessionManager实例。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
```
 
  

#### getSpatializationManager18+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getSpatializationManager(): AudioSpatializationManager
 
获取空间音频管理器。
 
**系统能力：** SystemCapability.Multimedia.Audio.Spatialization
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioSpatializationManager | AudioSpatializationManager实例。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';
let audioSpatializationManager: audio.AudioSpatializationManager = audioManager.getSpatializationManager();
```
 
  

#### setAudioParameter(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setAudioParameter(key: string, value: string, callback: AsyncCallback&lt;void&gt;): void
 
音频参数设置。使用callback异步回调。
 
接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 被设置的音频参数的键。 |
| value | string | 是 | 被设置的音频参数的值。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当音频参数设置成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioParameter('key_example', 'value_example', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the audio parameter. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the audio parameter.');
});
```
 
  

#### setAudioParameter(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setAudioParameter(key: string, value: string): Promise&lt;void&gt;
 
音频参数设置。使用Promise异步回调。
 
接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 被设置的音频参数的键。 |
| value | string | 是 | 被设置的音频参数的值。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.setAudioParameter('key_example', 'value_example').then(() => {
  console.info('Promise returned to indicate a successful setting of the audio parameter.');
});
```
 
  

#### getAudioParameter(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioParameter(key: string, callback: AsyncCallback&lt;string&gt;): void
 
获取指定音频参数值。使用callback异步回调。
 
本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待获取的音频参数的键。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。当获取指定音频参数值成功，err为undefined，data为获取到的指定音频参数值；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioParameter('key_example', (err: BusinessError, value: string) => {
  if (err) {
    console.error(`Failed to obtain the value of the audio parameter. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the value of the audio parameter is obtained ${value}.`);
});
```
 
  

#### getAudioParameter(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioParameter(key: string): Promise&lt;string&gt;
 
获取指定音频参数值。使用Promise异步回调。
 
本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待获取的音频参数的键。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回获取的音频参数值。 |
 
 
**示例：**
 
```text
audioManager.getAudioParameter('key_example').then((value: string) => {
  console.info(`Promise returned to indicate that the value of the audio parameter is obtained ${value}.`);
});
```
 
  

#### setVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback&lt;void&gt;): void
 
设置指定流的音量等级。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请查看API文档： 音量面板 。

 
**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY
 
仅设置铃声（即volumeType为AudioVolumeType.RINGTONE）在静音和非静音状态切换时需要该权限。
 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| volume | number | 是 | 音量等级，可设置范围通过getMinVolume和getMaxVolume获取。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置指定流的音量成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});
```
 
  

#### setVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVolume(volumeType: AudioVolumeType, volume: number): Promise&lt;void&gt;
 
设置指定流的音量等级。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请查看API文档： 音量面板 。

 
**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY
 
仅设置铃声（即volumeType为AudioVolumeType.RINGTONE）在静音和非静音状态切换时需要该权限。
 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| volume | number | 是 | 音量等级，可设置范围通过getMinVolume和getMaxVolume获取。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```
 
  

#### getVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback&lt;number&gt;): void
 
获取指定流的音量等级。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getVolume 替代；API version 20及以后，建议使用 getVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过getMinVolume和getMaxVolume获取。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume is obtained.');
});
```
 
  

#### getVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getVolume(volumeType: AudioVolumeType): Promise&lt;number&gt;
 
获取指定流的音量等级。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getVolume 替代；API version 20及以后，建议使用 getVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过getMinVolume和getMaxVolume获取。 |
 
 
**示例：**
 
```text
audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promise returned to indicate that the volume is obtained ${value} .`);
});
```
 
  

#### getMinVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback&lt;number&gt;): void
 
获取指定流的最小音量等级。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getMinVolume 替代；API version 20及以后，建议使用 getMinVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the minimum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the minimum volume is obtained. ${value}`);
});
```
 
  

#### getMinVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMinVolume(volumeType: AudioVolumeType): Promise&lt;number&gt;
 
获取指定流的最小音量等级。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getMinVolume 替代；API version 20及以后，建议使用 getMinVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最小音量等级。 |
 
 
**示例：**
 
```text
audioManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promised returned to indicate that the minimum volume is obtained. ${value}`);
});
```
 
  

#### getMaxVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback&lt;number&gt;): void
 
获取指定流的最大音量等级。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getMaxVolume 替代；API version 20及以后，建议使用 getMaxVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the maximum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the maximum volume is obtained. ${value}`);
});
```
 
  

#### getMaxVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMaxVolume(volumeType: AudioVolumeType): Promise&lt;number&gt;
 
获取指定流的最大音量等级。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 getMaxVolume 替代；API version 20及以后，建议使用 getMaxVolumeByStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最大音量等级。 |
 
 
**示例：**
 
```text
audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
  console.info('Promised returned to indicate that the maximum volume is obtained.');
});
```
 
  

#### mute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback&lt;void&gt;): void
 
设置指定音量流静音。使用callback异步回调。
 
当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| mute | boolean | 是 | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置指定音量流静音成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.mute(audio.AudioVolumeType.MEDIA, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the stream. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the stream is muted.');
});
```
 
  

#### mute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mute(volumeType: AudioVolumeType, mute: boolean): Promise&lt;void&gt;
 
设置指定音量流静音。使用Promise异步回调。
 
当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| mute | boolean | 是 | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.mute(audio.AudioVolumeType.MEDIA, true).then(() => {
  console.info('Promise returned to indicate that the stream is muted.');
});
```
 
  

#### isMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isMute(volumeType: AudioVolumeType, callback: AsyncCallback&lt;boolean&gt;): void
 
获取指定音量流的静音状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 isMute 替代；API version 20及以后，建议使用 isSystemMutedForStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取指定音量流的静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the stream is obtained. ${value}`);
});
```
 
  

#### isMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isMute(volumeType: AudioVolumeType): Promise&lt;boolean&gt;
 
获取指定音量流的静音状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 isMute 替代；API version 20及以后，建议使用 isSystemMutedForStream 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示静音；返回false表示非静音。 |
 
 
**示例：**
 
```text
audioManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the stream is obtained ${value}.`);
});
```
 
  

#### isActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isActive(volumeType: AudioVolumeType, callback: AsyncCallback&lt;boolean&gt;): void
 
获取指定音量流的活跃状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 isActive 替代；API version 20及以后，建议使用 isStreamActive 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取指定音量流的活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the active status of the stream. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the active status of the stream is obtained ${value}.`);
});
```
 
  

#### isActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isActive(volumeType: AudioVolumeType): Promise&lt;boolean&gt;
 
获取指定音量流的活跃状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用 isActive 替代；API version 20及以后，建议使用 isStreamActive 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Volume
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | AudioVolumeType | 是 | 音频音量类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |
 
 
**示例：**
 
```text
audioManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Promise returned to indicate that the active status of the stream is obtained ${value}.`);
});
```
 
  

#### setRingerMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setRingerMode(mode: AudioRingMode, callback: AsyncCallback&lt;void&gt;): void
 
设置铃声模式。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY
 
仅在静音和非静音状态切换时需要该权限。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | AudioRingMode | 是 | 音频铃声模式。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置铃声模式成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the ringer mode. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the ringer mode.');
});
```
 
  

#### setRingerMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setRingerMode(mode: AudioRingMode): Promise&lt;void&gt;
 
设置铃声模式。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY
 
仅在静音和非静音状态切换时需要该权限。
 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | AudioRingMode | 是 | 音频铃声模式。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL).then(() => {
  console.info('Promise returned to indicate a successful setting of the ringer mode.');
});
```
 
  

#### getRingerMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRingerMode(callback: AsyncCallback&lt;AudioRingMode&gt;): void
 
获取铃声模式。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 getRingerMode 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AudioRingMode&gt; | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to obtain the ringer mode. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the ringer mode is obtained ${value}.`);
});
```
 
  

#### getRingerMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRingerMode(): Promise&lt;AudioRingMode&gt;
 
获取铃声模式。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 getRingerMode 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Communication
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;AudioRingMode&gt; | Promise对象，返回系统的铃声模式。 |
 
 
**示例：**
 
```text
audioManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Promise returned to indicate that the ringer mode is obtained ${value}.`);
});
```
 
  

#### getDevices(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback&lt;AudioDeviceDescriptors&gt;): void
 
获取音频设备列表。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 getDevices 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | 是 | 音频设备类型。 |
| callback | AsyncCallback&lt;AudioDeviceDescriptors&gt; | 是 | 回调函数。当获取音频设备列表成功，err为undefined，data为获取到的音频设备列表；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (err: BusinessError, value: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(`Failed to obtain the device list. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the device list is obtained.');
});
```
 
  

#### getDevices(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDevices(deviceFlag: DeviceFlag): Promise&lt;AudioDeviceDescriptors&gt;
 
获取音频设备列表。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 getDevices 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | 是 | 音频设备类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;AudioDeviceDescriptors&gt; | Promise对象，返回设备列表。 |
 
 
**示例：**
 
```text
audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data: audio.AudioDeviceDescriptors) => {
  console.info('Promise returned to indicate that the device list is obtained.');
});
```
 
  

#### setDeviceActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback&lt;void&gt;): void
 
设置设备激活状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 setCommunicationDevice 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | ActiveDeviceType | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置设备激活状态成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the active status of the device. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the device is set to the active status.');
});
```
 
  

#### setDeviceActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise&lt;void&gt;
 
设置设备激活状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 setCommunicationDevice 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | ActiveDeviceType | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true).then(() => {
  console.info('Promise returned to indicate that the device is set to the active status.');
});
```
 
  

#### isDeviceActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback&lt;boolean&gt;): void
 
获取指定设备的激活状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 isCommunicationDeviceActive 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | ActiveDeviceType | 是 | 活跃音频设备类型。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取指定设备的激活状态成功，err为undefined，data为true表示激活，false表示未激活；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the active status of the device. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the active status of the device is obtained.');
});
```
 
  

#### isDeviceActive(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isDeviceActive(deviceType: ActiveDeviceType): Promise&lt;boolean&gt;
 
获取指定设备的激活状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 isCommunicationDeviceActive 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | ActiveDeviceType | 是 | 活跃音频设备类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示设备已激活；返回false表示设备未激活。 |
 
 
**示例：**
 
```text
audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER).then((value: boolean) => {
  console.info(`Promise returned to indicate that the active status of the device is obtained ${value}.`);
});
```
 
  

#### setMicrophoneMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setMicrophoneMute(mute: boolean, callback: AsyncCallback&lt;void&gt;): void
 
设置麦克风静音状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.MICROPHONE
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the microphone. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the microphone is muted.');
});
```
 
  

#### setMicrophoneMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setMicrophoneMute(mute: boolean): Promise&lt;void&gt;
 
设置麦克风静音状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

 
**需要权限：** ohos.permission.MICROPHONE
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
audioManager.setMicrophoneMute(true).then(() => {
  console.info('Promise returned to indicate that the microphone is muted.');
});
```
 
  

#### isMicrophoneMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isMicrophoneMute(callback: AsyncCallback&lt;boolean&gt;): void
 
获取麦克风静音状态。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 isMicrophoneMute 替代。

 
**需要权限：** ohos.permission.MICROPHONE
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status of the microphone. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the microphone is obtained ${value}.`);
});
```
 
  

#### isMicrophoneMute(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isMicrophoneMute(): Promise&lt;boolean&gt;
 
获取麦克风静音状态。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 isMicrophoneMute 替代。

 
**需要权限：** ohos.permission.MICROPHONE
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |
 
 
**示例：**
 
```text
audioManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the microphone is obtained ${value}.`);
});
```
 
  

#### on('deviceChange')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'deviceChange', callback: Callback&lt;DeviceChangeAction&gt;): void
 
监听音频设备连接变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 on('deviceChange') 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当音频设备连接状态发生变化时，触发该事件。 |
| callback | Callback&lt;DeviceChangeAction&gt; | 是 | 回调函数，返回设备更新详情。 |
 
 
**示例：**
 
```text
audioManager.on('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`device change type : ${deviceChanged.type} `);
  console.info(`device descriptor size : ${deviceChanged.deviceDescriptors.length} `);
  console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceRole} `);
  console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceType} `);
});
```
 
  

#### off('deviceChange')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'deviceChange', callback?: Callback&lt;DeviceChangeAction&gt;): void
 
取消监听音频设备连接变化事件。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 off('deviceChange') 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Device
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当取消监听音频设备连接变化事件时，触发该事件。 |
| callback | Callback&lt;DeviceChangeAction&gt; | 否 | 回调函数，返回设备更新详情。 |
 
 
**示例：**
 
```text
// 取消该事件的所有监听。
audioManager.off('deviceChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`device change type : ${deviceChanged.type} `);
  console.info(`device descriptor size : ${deviceChanged.deviceDescriptors.length} `);
  console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceRole} `);
  console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceType} `);
};

audioManager.on('deviceChange', deviceChangeCallback);

audioManager.off('deviceChange', deviceChangeCallback);
```
 
  

#### on('interrupt')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback&lt;InterruptAction&gt;): void
 
监听音频打断事件（当音频焦点发生变化时触发）。使用callback异步回调。
 
与[on('audioInterrupt')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onaudiointerrupt9)作用一致，均用于监听焦点变化。为无音频流的场景（未曾创建AudioRenderer对象），比如FM、语音唤醒等提供焦点变化监听功能。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，建议使用 on('audioInterrupt') 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Renderer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'，当音频焦点状态发生变化时，触发该事件。 |
| interrupt | AudioInterrupt | 是 | 音频打断事件类型的参数。 |
| callback | Callback&lt;InterruptAction&gt; | 是 | 回调函数，返回打断事件信息。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
  pauseWhenDucked: true
};

audioManager.on('interrupt', interAudioInterrupt, (interruptAction: audio.InterruptAction) => {
  if (interruptAction.actionType === 0) {
    console.info('An event to gain the audio focus starts.');
    console.info(`Focus hint: ${interruptAction.hint} `);
  }
  if (interruptAction.actionType === 1) {
    console.info('An audio interruption event starts.');
    console.info(`Audio interruption hint: ${interruptAction.hint} `);
  }
});
```
 
  

#### off('interrupt')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback&lt;InterruptAction&gt;): void
 
取消监听音频打断事件。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始支持，从API version 11开始废弃，建议使用 off('audioInterrupt') 替代。

 
**系统能力：** SystemCapability.Multimedia.Audio.Renderer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'，当取消监听音频打断事件时，触发该事件。 |
| interrupt | AudioInterrupt | 是 | 音频打断事件类型的参数。 |
| callback | Callback&lt;InterruptAction&gt; | 否 | 回调函数，返回打断事件信息。 |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
  pauseWhenDucked: true
};

// 取消该事件的所有监听。
audioManager.off('interrupt', interAudioInterrupt);

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let interruptCallback = (interruptAction: audio.InterruptAction) => {
  if (interruptAction.actionType === 0) {
    console.info('An event to gain the audio focus starts.');
    console.info(`Focus hint: ${interruptAction.hint} `);
  }
  if (interruptAction.actionType === 1) {
    console.info('An audio interruption event starts.');
    console.info(`Audio interruption hint: ${interruptAction.hint} `);
  }
};

audioManager.on('interrupt', interAudioInterrupt, interruptCallback);

audioManager.off('interrupt', interAudioInterrupt, interruptCallback);
```
