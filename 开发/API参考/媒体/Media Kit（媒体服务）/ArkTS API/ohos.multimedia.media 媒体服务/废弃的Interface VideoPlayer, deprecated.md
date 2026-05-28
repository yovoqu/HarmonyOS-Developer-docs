# 废弃的Interface (VideoPlayer, deprecated)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过[createVideoPlayer()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreatevideoplayerdeprecated)构建一个VideoPlayer实例。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer 替代。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { media } from '@kit.MediaKit';
```



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url8+ | string | 否 | 否 | 视频媒体URL，支持当前主流的视频格式(mp4、mpeg-ts、mkv)。 支持路径示例： 1. fd类型播放：fd://xx 2. http网络播放: http://xx 3. https网络播放: https://xx 4. hls网络播放路径：http://xx或者https://xx 5. file类型: file://xx 说明： 从API version 11开始不支持webm。 |
| fdSrc9+ | AVFileDescriptor | 否 | 否 | 视频媒体文件描述，使用场景：应用中的视频资源被连续存储在同一个文件中。 使用示例： 假设一个连续存储的音乐文件: 视频1(地址偏移:0，字节长度:100) 视频2(地址偏移:101，字节长度:50) 视频3(地址偏移:151，字节长度:150) 1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; } 2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; } 3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; } 假设是一个独立的视频文件: 请使用src=fd://xx |
| loop8+ | boolean | 否 | 否 | 视频循环播放属性，设置为'true'表示循环播放。 |
| videoScaleType9+ | VideoScaleType | 否 | 是 | 视频缩放模式。默认值为VIDEO_SCALE_TYPE_FIT。 |
| audioInterruptMode9+ | audio.InterruptMode | 否 | 是 | 音频焦点模式。 |
| currentTime8+ | number | 是 | 否 | 视频的当前播放位置，单位为毫秒（ms）。 |
| duration8+ | number | 是 | 否 | 视频时长，单位为毫秒（ms），返回-1表示直播模式。 |
| state8+ | VideoPlayState | 是 | 否 | 视频播放的状态。 |
| width8+ | number | 是 | 否 | 视频宽，单位为像素（px）。 |
| height8+ | number | 是 | 否 | 视频高，单位为像素（px）。 |




#### setDisplaySurface(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDisplaySurface(surfaceId: string, callback: AsyncCallback&lt;void&gt;): void

设置SurfaceId。通过回调函数获取返回值。

> [!NOTE]
> SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.surfaceId 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考XComponent。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置SurfaceId成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set DisplaySurface!');
  } else {
    console.info('Succeeded in setting DisplaySurface!');
  }
});
```



#### setDisplaySurface(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDisplaySurface(surfaceId: string): Promise&lt;void&gt;

设置SurfaceId。通过Promise获取返回值。

> [!NOTE]
> SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.surfaceId 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考XComponent。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 设置SurfaceId的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId).then(() => {
  console.info('Succeeded in setting DisplaySurface');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### prepare(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

prepare(callback: AsyncCallback&lt;void&gt;): void

准备播放视频。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.prepare 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当准备播放视频成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});
```



#### prepare(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

prepare(): Promise&lt;void&gt;

准备播放视频。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.prepare 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 准备播放视频的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### play(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

play(callback: AsyncCallback&lt;void&gt;): void

开始播放视频。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.play 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当开始播放视频成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play((err: BusinessError) => {
  if (err) {
    console.error('Failed to play!');
  } else {
    console.info('Succeeded in playing!');
  }
});
```



#### play(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

play(): Promise&lt;void&gt;

开始播放视频。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.play 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 开始播放视频的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play().then(() => {
  console.info('Succeeded in playing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### pause(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pause(callback: AsyncCallback&lt;void&gt;): void

通过回调方式暂停播放视频。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.pause 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当暂停播放视频成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});
```



#### pause(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pause(): Promise&lt;void&gt;

暂停播放视频。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.pause 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 暂停播放视频的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(callback: AsyncCallback&lt;void&gt;): void

通过回调方式停止播放视频。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.stop 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当停止播放视频成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop((err: BusinessError) => {
  if (err) {
    console.error('Failed to stop!');
  } else {
    console.info('Succeeded in stopping!');
  }
});
```



#### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(): Promise&lt;void&gt;

停止播放视频。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.stop 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 停止播放视频的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop().then(() => {
  console.info('Succeeded in stopping');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### reset(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

reset(callback: AsyncCallback&lt;void&gt;): void

重置播放视频。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.reset 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当重置播放视频成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset((err: BusinessError) => {
  if (err) {
    console.error('Failed to reset!');
  } else {
    console.info('Succeeded in resetting!');
  }
});
```



#### reset(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

reset(): Promise&lt;void&gt;

重置播放视频。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.reset 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset().then(() => {
  console.info('Succeeded in resetting');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### seek(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(timeMs: number, callback: AsyncCallback&lt;number&gt;): void

跳转到指定播放位置，默认跳转到指定时间点的上一个关键帧。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.seek 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});

let seekTime: number = 5000;
videoPlayer.seek(seekTime, (err: BusinessError, result: number) => {
  if (err) {
    console.error('Failed to do seek!');
  } else {
    console.info('Succeeded in doing seek!');
  }
});
```



#### seek(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(timeMs: number, mode:SeekMode, callback: AsyncCallback&lt;number&gt;): void

跳转到指定播放位置。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.seek 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | SeekMode | 是 | 跳转模式。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to do seek!');
    } else {
      console.info('Succeeded in doing seek!');
    }
  });
}
```



#### seek(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(timeMs: number, mode?:SeekMode): Promise&lt;number&gt;

跳转到指定播放位置，如果没有设置mode则跳转到指定时间点的上一个关键帧。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.seek 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | SeekMode | 否 | 基于视频I帧的跳转模式，默认为SEEK_PREV_SYNC模式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | 跳转到指定播放位置的Promise返回值，单位ms。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime表示seek完成后的时间点。
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });

  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC).then((seekDoneTime: number) => {
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });
}
```



#### setVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVolume(vol: number, callback: AsyncCallback&lt;void&gt;): void

设置音量。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.setVolume 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置音量成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set Volume!');
  } else {
    console.info('Succeeded in setting Volume!');
  }
});
```



#### setVolume(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVolume(vol: number): Promise&lt;void&gt;

设置音量。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.setVolume 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 设置音量的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol).then(() => {
  console.info('Succeeded in setting Volume');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### release(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(callback: AsyncCallback&lt;void&gt;): void

释放视频资源。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.release 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当释放视频资源成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```



#### release(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): Promise&lt;void&gt;

释放视频资源。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.release 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 释放视频资源的Promise返回值。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### getTrackDescription(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getTrackDescription(callback: AsyncCallback<Array&lt;MediaDescription&gt;>): void

获取视频轨道信息。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.getTrackDescription 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array&lt;MediaDescription&gt;> | 是 | 回调函数。获取视频轨道信息成功时，err为undefined，data为获取到的视频轨道信息MediaDescription数组，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if ((arrList) != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(`Failed to get TrackDescription, error:${error}`);
  }
});
```



#### getTrackDescription(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getTrackDescription(): Promise<Array&lt;MediaDescription&gt;>

获取视频轨道信息。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.getTrackDescription 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;MediaDescription&gt;> | Promise对象，返回获取的视频轨道信息MediaDescription数组。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error('Failed to get TrackDescription');
  }
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```



#### setSpeed(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setSpeed(speed: number, callback: AsyncCallback&lt;number&gt;): void

设置播放速度。通过回调函数获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.setSpeed 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见PlaybackSpeed。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。设置播放速度成功时，err为undefined，data为设置的播放速度，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to set Speed!');
    } else {
      console.info('Succeeded in setting Speed!');
    }
  });
}
```



#### setSpeed(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setSpeed(speed: number): Promise&lt;number&gt;

设置播放速度。通过Promise获取返回值。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.setSpeed 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见PlaybackSpeed。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回设置的播放速度，具体见PlaybackSpeed。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed).then((result: number) => {
    console.info('Succeeded in setting Speed');
  }).catch((error: BusinessError) => {
    console.error(`Failed to set Speed, error:${error}`);// todo:: error.
  });
}
```



#### on('playbackCompleted')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'playbackCompleted', callback: Callback&lt;void&gt;): void

开始监听视频播放完成事件。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('stateChange') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放完成事件回调类型，支持的事件：'playbackCompleted'。 |
| callback | Callback&lt;void&gt; | 是 | 视频播放完成事件回调方法。 |


**示例：**

```text
videoPlayer.on('playbackCompleted', () => {
  console.info('playbackCompleted called!');
});
```



#### on('bufferingUpdate')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void

开始监听视频缓存更新事件。仅网络播放支持该订阅事件。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('bufferingUpdate') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | function | 是 | 视频缓存事件回调方法。 BufferingInfoTypevalue值固定为0。 |


**示例：**

```text
videoPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
  console.info('video bufferingInfo type: ' + infoType);
  console.info('video bufferingInfo value: ' + value);
});
```



#### on('startRenderFrame')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'startRenderFrame', callback: Callback&lt;void&gt;): void

开始监听视频播放首帧送显上报事件。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('startRenderFrame') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放首帧送显上报事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | Callback&lt;void&gt; | 是 | 视频播放首帧送显上报事件回调方法。 |


**示例：**

```text
videoPlayer.on('startRenderFrame', () => {
  console.info('startRenderFrame called!');
});
```



#### on('videoSizeChanged')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void

开始监听视频播放宽高变化事件。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('videoSizeChange') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChanged'。 |
| callback | function | 是 | 视频播放宽高变化事件回调方法，width表示宽，height表示高。 |


**示例：**

```text
videoPlayer.on('videoSizeChanged', (width: number, height: number) => {
  console.info('video width is: ' + width);
  console.info('video height is: ' + height);
});
```



#### on('audioInterrupt')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void

监听音频焦点变化事件，参考[audio.InterruptEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)。

> [!NOTE]
> 从API version 9开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('audioInterrupt') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | function | 是 | 音频焦点变化事件回调方法。 |


**示例：**

```text
import { audio } from '@kit.AudioKit';

videoPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
  console.info('audioInterrupt called,and InterruptEvent info is:' + info);
});
```



#### on('error')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', callback: ErrorCallback): void

开始监听视频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。

> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用 AVPlayer.on('error') 替代。


**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放错误事件回调类型，支持的事件包括：'error'。 - 'error'：视频播放中发生错误，触发该事件。 |
| callback | ErrorCallback | 是 | 播放错误事件回调方法。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`video error called, error: ${error}`);
});
videoPlayer.url = 'fd://error';  // 设置错误的播放地址，触发'error'事件。
```
