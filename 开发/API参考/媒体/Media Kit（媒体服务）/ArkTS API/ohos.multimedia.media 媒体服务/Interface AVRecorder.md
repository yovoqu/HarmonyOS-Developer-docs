# Interface (AVRecorder)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

音视频录制管理类，用于音视频媒体录制。在调用AVRecorder的方法前，需要先调用[createAVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateavrecorder9)接口构建一个AVRecorder实例。

音视频录制demo可参考：[音频录制开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avrecorder-for-recording)、[视频录制开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-recording)。

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 9开始支持。 相机视频录制功能需配合相机模块使用，相机模块接口的使用详情请参考 相机管理 。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { media } from '@kit.MediaKit';
```



##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state9+ | AVRecorderState | 是 | 否 | 音视频录制的状态。 元服务API： 从API version 12 开始，该接口支持在元服务中使用。 |




##### prepare9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;): void

音视频录制的参数设置。使用callback异步回调。

**需要权限：** ohos.permission.MICROPHONE

不涉及音频录制时，无需获取ohos.permission.MICROPHONE权限。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | AVRecorderConfig | 是 | 配置音视频录制的相关参数。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当prepare接口成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Return by callback. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数。
  metadata: videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in preparing');
  }
});
```



##### prepare9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

prepare(config: AVRecorderConfig): Promise&lt;void&gt;

音视频录制的参数设置。使用Promise异步回调。

**需要权限：** ohos.permission.MICROPHONE

不涉及音频录制时，无需获取ohos.permission.MICROPHONE权限。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | AVRecorderConfig | 是 | 配置音视频录制的相关参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Return by promise. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数。
  metadata : videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig).then(() => {
  console.info('Succeeded in preparing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### getInputSurface9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getInputSurface(callback: AsyncCallback&lt;string&gt;): void

获得录制需要的surface。使用callback异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](#prepare9)接口成功调用后，才能调用getInputSurface接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。当获取surface成功，err为undefined，data为获取到的surfaceId，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceID: string; // 该surfaceID用于传递给相机接口创建videoOutput。

avRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
  if (err) {
    console.error(`Failed to do getInputSurface and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in doing getInputSurface');
    surfaceID = surfaceId;
  }
});
```



##### getInputSurface9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getInputSurface(): Promise&lt;string&gt;

获得录制需要的surface。使用Promise异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](#prepare9-1)接口成功调用后，才能调用getInputSurface接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回surface中获取的surfaceBuffer。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceID: string; // 该surfaceID用于传递给相机接口创建videoOutput。

avRecorder.getInputSurface().then((surfaceId: string) => {
  console.info('Succeeded in getting InputSurface');
  surfaceID = surfaceId;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to get InputSurface and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### updateRotation12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

updateRotation(rotation: number): Promise&lt;void&gt;

更新视频旋转角度。使用Promise异步回调。

当且仅当[prepare](#prepare9-1)接口成功调用后，且在[start](#start9)接口之前，才能调用updateRotation接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | number | 是 | 旋转角度，取值仅支持0、90、180、270度。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let rotation = 90;

avRecorder.updateRotation(rotation).then(() => {
  console.info('Succeeded in doing updateRotation');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to do updateRotation and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### setWillMuteWhenInterrupted20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise&lt;void&gt;

设置当前录制音频流是否启用静音打断模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muteWhenInterrupted | boolean | 是 | 设置当前录制音频流是否启用静音打断模式, true表示启用，false表示不启用，保持为默认打断模式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.setWillMuteWhenInterrupted(true).then(() => {
  console.info('Succeeded in doing setWillMuteWhenInterrupted');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to do setWillMuteWhenInterrupted and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### start9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(callback: AsyncCallback&lt;void&gt;): void

开始视频录制。使用callback异步回调。

纯音频录制需在[prepare](#prepare9)接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在[getInputSurface](#getinputsurface9)接口成功调用后，才能调用start接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当开始录制视频成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start((err: BusinessError) => {
  if (err) {
    console.error(`Failed to start AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in starting AVRecorder');
  }
});
```



##### start9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(): Promise&lt;void&gt;

开始视频录制。使用Promise异步回调。

纯音频录制需在[prepare](#prepare9-1)接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在[getInputSurface](#getinputsurface9-1)接口成功调用后，才能调用start接口。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start().then(() => {
  console.info('Succeeded in starting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to start AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### pause9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pause(callback: AsyncCallback&lt;void&gt;): void

暂停视频录制。使用callback异步回调。

需要[start](#start9)接口成功调用后，才能调用pause接口，可以通过调用[resume](#resume9)接口来恢复录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当暂停视频录制成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause((err: BusinessError) => {
  if (err) {
    console.error(`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in pausing');
  }
});
```



##### pause9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pause(): Promise&lt;void&gt;

暂停视频录制。使用Promise异步回调。

需要[start](#start9-1)接口成功调用后，才能调用pause接口，可以通过调用[resume](#resume9-1)接口来恢复录制。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### resume9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

resume(callback: AsyncCallback&lt;void&gt;): void

恢复视频录制。使用callback异步回调。

需要在[pause](#pause9)接口成功调用后，才能调用resume接口。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当恢复视频录制成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume((err: BusinessError) => {
  if (err) {
    console.error(`Failed to resume AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in resuming AVRecorder');
  }
});
```



##### resume9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

resume(): Promise&lt;void&gt;

恢复视频录制。使用Promise异步回调。

需要在[pause](#pause9-1)接口成功调用后，才能调用resume接口。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume().then(() => {
  console.info('Succeeded in resuming AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to resume AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### stop9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(callback: AsyncCallback&lt;void&gt;): void

停止视频录制。使用callback异步回调。

需要在[start](#start9)或[pause](#pause9)接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](#prepare9)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](#prepare9)和[getInputSurface](#getinputsurface9)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当停止视频录制成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop((err: BusinessError) => {
  if (err) {
    console.error(`Failed to stop AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in stopping AVRecorder');
  }
});
```



##### stop9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(): Promise&lt;void&gt;

停止视频录制。使用Promise异步回调。

需要在[start](#start9-1)或[pause](#pause9-1)接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](#prepare9-1)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](#prepare9-1)和[getInputSurface](#getinputsurface9-1)接口才能重新录制。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop().then(() => {
  console.info('Succeeded in stopping AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to stop AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### reset9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

reset(callback: AsyncCallback&lt;void&gt;): void

重置音视频录制。使用callback异步回调。

纯音频录制时，需要重新调用[prepare](#prepare9)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](#prepare9)和[getInputSurface](#getinputsurface9)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当重置音视频录制成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset((err: BusinessError) => {
  if (err) {
    console.error(`Failed to reset AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in resetting AVRecorder');
  }
});
```



##### reset9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

reset(): Promise&lt;void&gt;

重置音视频录制。使用Promise异步回调。

纯音频录制时，需要重新调用[prepare](#prepare9-1)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare](#prepare9-1)和[getInputSurface](#getinputsurface9-1)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset().then(() => {
  console.info('Succeeded in resetting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to reset AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### release9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(callback: AsyncCallback&lt;void&gt;): void

释放音视频录制资源。使用callback异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当释放音视频录制资源成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});
```



##### release9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): Promise&lt;void&gt;

释放音视频录制资源。使用Promise异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### getCurrentAudioCapturerInfo11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void

获取当前音频采集参数。使用callback异步回调。

在[prepare](#prepare9)接口成功调用后，才能调用此接口。在[stop](#stop9)接口成功调用后，调用此接口会报错。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<audio.AudioCapturerChangeInfo> | 是 | 回调函数。当获取音频采集参数成功时，err为undefined，data为获取到的audio.AudioCapturerChangeInfo，否则为错误对象。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by callback. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';

let currentCapturerInfo: audio.AudioCapturerChangeInfo;

avRecorder.getCurrentAudioCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerChangeInfo) => {
  if (err) {
    console.error(`Failed to get CurrentAudioCapturerInfo and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in getting CurrentAudioCapturerInfo');
    currentCapturerInfo = capturerInfo;
  }
});
```



##### getCurrentAudioCapturerInfo11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>

获取当前音频采集参数。使用Promise异步回调。

在[prepare](#prepare9)接口成功调用后，才能调用此接口。在[stop](#stop9)接口成功调用后，调用此接口会报错。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<audio.AudioCapturerChangeInfo> | Promise对象，返回获取的当前音频采集参数。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by promise. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';

let currentCapturerInfo: audio.AudioCapturerChangeInfo;

avRecorder.getCurrentAudioCapturerInfo().then((capturerInfo: audio.AudioCapturerChangeInfo) => {
  console.info('Succeeded in getting CurrentAudioCapturerInfo');
  currentCapturerInfo = capturerInfo;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to get CurrentAudioCapturerInfo and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### getAudioCapturerMaxAmplitude11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioCapturerMaxAmplitude(callback: AsyncCallback&lt;number&gt;): void

获取当前音频最大振幅。使用callback异步回调。

在[prepare](#prepare9)接口成功调用后，才能调用此接口。在[stop](#stop9)接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。获取当前音频最大振幅成功时，err为undefined，data为获取到的最大振幅，否则为错误对象。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';

let maxAmplitude: number;

avRecorder.getAudioCapturerMaxAmplitude((err: BusinessError, amplitude: number) => {
  if (err) {
    console.error(`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in getting AudioCapturerMaxAmplitude');
    maxAmplitude = amplitude;
  }
});
```



##### getAudioCapturerMaxAmplitude11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAudioCapturerMaxAmplitude(): Promise&lt;number&gt;

获取当前音频最大振幅。使用Promise异步回调。

在[prepare](#prepare9)接口成功调用后，才能调用此接口。在[stop](#stop9)接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回获取的当前音频最大振幅。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';

let maxAmplitude: number;

avRecorder.getAudioCapturerMaxAmplitude().then((amplitude: number) => {
  console.info('Succeeded in getting AudioCapturerMaxAmplitude');
  maxAmplitude = amplitude;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### getAvailableEncoder11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAvailableEncoder(callback: AsyncCallback<Array&lt;EncoderInfo&gt;>): void

获取可用的编码器参数。使用callback异步回调。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array&lt;EncoderInfo&gt;> | 是 | 回调函数。获取可用的编码器参数成功时，err为undefined，data为获取到的编码器参数，否则为错误对象。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';

let encoderInfo: media.EncoderInfo;

avRecorder.getAvailableEncoder((err: BusinessError, info: media.EncoderInfo[]) => {
  if (err) {
    console.error(`Failed to get AvailableEncoder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in getting AvailableEncoder');
    if (info.length > 0) {
      encoderInfo = info[0];
    } else {
      console.error('No available encoder');
    }
  }
});
```



##### getAvailableEncoder11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAvailableEncoder(): Promise<Array&lt;EncoderInfo&gt;>

获取可用的编码器参数。使用Promise异步回调。

**系统能力**：SystemCapability.Multimedia.Media.AVRecorder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;EncoderInfo&gt;> | Promise对象，返回获取的可用的编码器参数。 |


**错误码**：

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |


**示例**：

```text
import { BusinessError } from '@kit.BasicServicesKit';

let encoderInfo: media.EncoderInfo;

avRecorder.getAvailableEncoder().then((info: media.EncoderInfo[]) => {
  console.info('Succeeded in getting AvailableEncoder');
    if (info.length > 0) {
      encoderInfo = info[0];
    } else {
      console.error('No available encoder');
    }
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to get AvailableEncoder and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### getAVRecorderConfig11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVRecorderConfig(callback: AsyncCallback&lt;AVRecorderConfig&gt;): void

获取实时的配置参数。使用callback异步回调。

只能在[prepare](#prepare9)接口调用成功后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AVRecorderConfig&gt; | 是 | 回调函数。获取实时配置的参数成功时，err为undefined，data为获取到的配置参数，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let avConfig: media.AVRecorderConfig;

avRecorder.getAVRecorderConfig((err: BusinessError, config: media.AVRecorderConfig) => {
  if (err) {
    console.error(`Failed to get avConfig and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in getting AVRecorderConfig');
    avConfig = config;
  }
});
```



##### getAVRecorderConfig11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVRecorderConfig(): Promise&lt;AVRecorderConfig&gt;;

获取实时的配置参数。使用Promise异步回调。

只能在[prepare](#prepare9-1)接口调用成功后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AVRecorderConfig&gt; | Promise对象。返回实时配置参数。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let avConfig: media.AVRecorderConfig;

avRecorder.getAVRecorderConfig().then((config: media.AVRecorderConfig) => {
  console.info('Succeeded in getting AVRecorderConfig');
  avConfig = config;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to get AVRecorderConfig and error is: Code: ${error.code}, message: ${error.message}`);
});
```



##### on('stateChange')9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void

订阅录制状态机AVRecorderState切换的事件，当AVRecorderState状态机发生变化时，会通过订阅的回调方法通知用户。用户只能订阅一个录制状态机切换事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback | OnAVRecorderStateChangeHandler | 是 | 回调函数，返回录制状态机切换事件。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
avRecorder.on('stateChange', async (state: media.AVRecorderState, reason: media.StateChangeReason) => {
  console.info('case state has changed, new state is: ' + state + ', and reason is: ' + reason);
});
```



##### off('stateChange')9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void

取消订阅录制状态机[AVRecorderState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9)切换的事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback12+ | OnAVRecorderStateChangeHandler | 否 | 回调函数，返回录制状态机切换事件。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 从API version 12开始支持此参数。 |


**示例：**

```text
avRecorder.off('stateChange');
```



##### on('error')9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', callback: ErrorCallback): void

订阅AVRecorder的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时[AVRecorderState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9)也切换至error状态，用户需要通过[reset](#reset9)或者[release](#release9)接口退出录制操作。使用callback异步回调。

用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。 - 'error'：录制过程中发生错误，触发该事件。 |
| callback | ErrorCallback | 是 | 回调函数，返回录制错误事件。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |
| 5400107 | Audio interrupted. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.on('error', (err: BusinessError) => {
  console.error(`case avRecorder.on(error) called. Code: ${err.code}, message: ${err.message}`);
});
```



##### off('error')9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'error', callback?: ErrorCallback): void

取消订阅录制错误事件，取消后不再接收到AVRecorder的错误事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录制错误事件回调类型'error'。 - 'error'：录制过程中发生错误，触发该事件。 |
| callback12+ | ErrorCallback | 否 | 回调函数，返回录制错误事件。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 从API version 12开始支持此参数。 |


**示例：**

```text
avRecorder.off('error');
```



##### on('audioCapturerChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void

订阅录音配置变化的回调，任意录音配置的变化会触发变化后的录音配置全量信息回调。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'audioCapturerChange'。 |
| callback | Callback<audio.AudioCapturerChangeInfo> | 是 | 回调函数，返回变化后的录音配置全量信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**

```text
import { audio } from '@kit.AudioKit'

let capturerChangeInfo: audio.AudioCapturerChangeInfo;

avRecorder.on('audioCapturerChange',  (audioCapturerChangeInfo: audio.AudioCapturerChangeInfo) => {
  console.info('audioCapturerChange called');
  capturerChangeInfo = audioCapturerChangeInfo;
});
```



##### off('audioCapturerChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void

取消订阅录音变化的回调事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'audioCapturerChange'。 |
| callback12+ | Callback<audio.AudioCapturerChangeInfo> | 否 | 回调函数，返回变化后的录音配置全量信息。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 从API version 12开始支持此参数。 |


**示例：**

```text
avRecorder.off('audioCapturerChange');
```



##### on('photoAssetAvailable')12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void

订阅媒体资源回调事件，当[FileGenerationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#filegenerationmode12)枚举设置为系统创建媒体文件时，会在[stop](#stop9)操作结束后把[PhotoAsset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset)对象回调给应用。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录像资源的回调类型，支持的事件：'photoAssetAvailable'。 |
| callback | Callback<photoAccessHelper.PhotoAsset> | 是 | 回调函数，返回系统创建的资源文件对应的PhotoAsset对象。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |


**示例：**

```text
import { photoAccessHelper } from '@kit.MediaLibraryKit';
let photoAsset: photoAccessHelper.PhotoAsset;

// 例：处理photoAsset回调，保存video。
async function saveVideo(context: Context, asset: photoAccessHelper.PhotoAsset) {
  console.info("saveVideo called");
  try {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
    assetChangeRequest.saveCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply saveVideo successfully');
  } catch (err) {
    console.error(`apply saveVideo failed with error: ${err.code}, ${err.message}`);
  }
}
// 注册photoAsset监听。
avRecorder.on('photoAssetAvailable', (asset: photoAccessHelper.PhotoAsset) => {
  console.info('photoAssetAvailable called');
  if (asset != undefined) {
    photoAsset = asset;
    // 处理photoAsset回调。
    // 例：this.saveVideo(context, asset);
  } else {
    console.error('photoAsset is undefined');
  }
});
```



##### off('photoAssetAvailable')12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void

取消订阅媒体资源的回调类型。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 录音配置变化的回调类型，支持的事件：'photoAssetAvailable'。 |
| callback | Callback<photoAccessHelper.PhotoAsset> | 否 | 回调函数，返回系统创建的资源文件对应的PhotoAsset对象。如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 |


**示例：**

```text
avRecorder.off('photoAssetAvailable');
```
