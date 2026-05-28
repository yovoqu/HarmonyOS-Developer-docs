# Interface (AVTranscoder)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder
**支持设备：** Phone | PC/2in1 | Tablet | TV

视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过[createAVTranscoder()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateavtranscoder12)构建一个AVTranscoder实例。

视频转码demo可参考：[视频转码开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avtranscoder-for-transcodering)

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 12开始支持。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
import { media } from '@kit.MediaKit';
```



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | TV

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdSrc12+ | AVFileDescriptor | 否 | 否 | 源媒体文件描述，通过该属性设置数据源。 使用示例： 假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。 说明： - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。 |
| fdDst12+ | number | 否 | 否 | 目标媒体文件描述，通过该属性设置数据输出。在创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。 说明： - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。 |




#### prepare12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

prepare(config: AVTranscoderConfig): Promise&lt;void&gt;

进行视频转码的参数设置。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | AVTranscoderConfig | 是 | 配置视频转码的相关参数。 当config中设置的目标视频分辨率宽videoFrameWidth大于原视频的宽或目标视频分辨率高videoFrameHeight大于原视频的高时，会上报错误码401。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |
| 5400106 | Unsupported format. Returned by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  // 配置参数以实际硬件设备支持的范围为准。
  let avTranscoderConfig: media.AVTranscoderConfig = {
    audioBitrate : 200000,
    audioCodec : media.CodecMimeType.AUDIO_AAC,
    fileFormat : media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate : 3000000,
    videoCodec : media.CodecMimeType.VIDEO_AVC,
  };

  avTranscoder.prepare(avTranscoderConfig).then(() => {
    console.info('prepare success');
  }).catch((err: BusinessError) => {
    console.error('prepare failed and catch error is ' + err.message);
  });
}
```



#### start12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

start(): Promise&lt;void&gt;

开始视频转码。使用Promise异步回调。

需要[prepare()](#prepare12)事件成功触发后，才能调用start方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.start().then(() => {
    console.info('start AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('start AVTranscoder failed and catch error is ' + err.message);
  });
}
```



#### pause12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

pause(): Promise&lt;void&gt;

暂停视频转码。使用Promise异步回调。

需要[start()](#start12)事件成功触发后，才能调用pause方法，可以通过调用[resume()](#resume12)接口来恢复转码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.pause().then(() => {
    console.info('pause AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('pause AVTranscoder failed and catch error is ' + err.message);
  });
}
```



#### resume12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

resume(): Promise&lt;void&gt;

恢复视频转码。使用Promise异步回调。

需要在[pause()](#pause12)事件成功触发后，才能调用resume方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.resume().then(() => {
    console.info('resume AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('resume AVTranscoder failed and catch error is ' + err.message);
  });
}
```



#### cancel12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

cancel(): Promise&lt;void&gt;

取消视频转码。使用Promise异步回调。

需要在[prepare()](#prepare12)、[start()](#start12)、[pause()](#pause12)或[resume()](#resume12)事件成功触发后，才能调用cancel方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.cancel().then(() => {
    console.info('cancel AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('cancel AVTranscoder failed and catch error is ' + err.message);
  });
}
```



#### release12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

release(): Promise&lt;void&gt;

释放视频转码资源。使用Promise异步回调。

释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

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
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```



#### on('progressUpdate')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

on(type:'progressUpdate', callback: Callback&lt;number&gt;):void

注册转码进度更新事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'，在转码过程中系统会自动触发此事件。 |
| callback | Callback&lt;number&gt; | 是 | 回调函数，返回进度更新事件，函数中的参数number，表示当前转码百分比进度。 |


**示例：**

```text
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('progressUpdate', (progress: number) => {
    console.info('avTranscoder progressUpdate = ' + progress);
  });
}
```



#### off('progressUpdate')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

off(type:'progressUpdate', callback?: Callback&lt;number&gt;): void

取消注册转码进度更新事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'。 |
| callback | Callback&lt;number&gt; | 否 | 已注册的进度更新事件回调。由于当前回调注册时，仅会保留最后一次注册的回调，建议此参数缺省。 |


**示例：**

```text
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('progressUpdate');
}
```



#### on('error')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

on(type: 'error', callback: ErrorCallback): void

注册AVTranscoder的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，开发者需要通过[release()](#release12)退出转码操作。使用callback异步回调。

开发者只能订阅一个错误事件的回调方法，当开发者重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码错误事件回调类型'error'。 - 'error'：录制过程中发生错误，触发该事件。 |
| callback | ErrorCallback | 是 | 转码错误事件回调方法。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('error', (err: BusinessError) => {
    console.info('case avTranscoder.on(error) called, errMessage is ' + err.message);
  });
}
```



#### off('error')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

off(type:'error', callback?: ErrorCallback): void

取消注册转码错误事件，取消后不再接收到AVTranscoder的错误事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码错误事件回调类型'error'。 - 'error'：转码过程中发生错误，触发该事件。 |
| callback | ErrorCallback | 否 | 错误事件回调方法。 |


**示例：**

```text
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('error');
}
```



#### on('complete')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

on(type: 'complete', callback: Callback&lt;void&gt;): void

注册转码完成事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

当AVTranscoder上报complete事件时，当前转码操作已完成，开发者需要通过[release()](#release12)退出转码操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 完成事件回调类型，支持的事件：'complete'，在转码过程中系统会自动触发此事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，返回完成事件回调方法。 |


**示例：**

```text
import { media } from '@kit.MediaKit';

async function test() {
  let avTranscoder: media.AVTranscoder | undefined = undefined;
  // 创建转码实例。
  avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('complete', async () => {
    console.info('avTranscoder complete');
    if (avTranscoder != undefined) {
      // 开发者须在此监听转码完成事件。
      // 须等待avTranscoder.release()释放转码实例之后，再对转码后的文件进行转发、上传、转存等处理。
      await avTranscoder.release();
      avTranscoder = undefined;
    }
  });
}
```



#### off('complete')12+

**支持设备：** Phone | PC/2in1 | Tablet | TV

off(type:'complete', callback?: Callback&lt;void&gt;): void

取消注册转码完成事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 转码完成事件回调类型，支持的事件：'complete'。 |
| callback | Callback&lt;void&gt; | 否 | 完成事件回调方法。 |


**示例：**

```text
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('complete');
}
```
