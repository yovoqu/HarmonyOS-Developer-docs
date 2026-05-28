# Interface (PreviewOutput)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

预览输出类。继承[CameraOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameraoutput)。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { camera } from '@kit.CameraKit';
```



#### on('frameStart')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void

监听预览帧启动，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，previewOutput创建成功可监听。底层第一次开始曝光时触发该事件并返回。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，用于获取结果。只要有该事件返回就证明预览开始。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info('Preview frame started');
}

function registerPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameStart', callback);
}
```



#### off('frameStart')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void

注销预览帧启动的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，previewOutput创建成功可监听。 |
| callback | AsyncCallback&lt;void&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameStart');
}
```



#### on('frameEnd')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void

监听预览帧结束，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，previewOutput创建成功可监听。预览完全结束最后一帧时触发该事件并返回。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，用于获取结果。只要有该事件返回就证明预览结束。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info('Preview frame ended');
}

function registerPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameEnd', callback);
}
```



#### off('frameEnd')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void

注销监听预览帧结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，previewOutput创建成功可监听。 |
| callback | AsyncCallback&lt;void&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameEnd');
}
```



#### on('error')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', callback: ErrorCallback): void

监听预览输出的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，previewOutput创建成功可监听。预览接口使用错误时触发该事件，比如调用Session.start，CameraOutput.release等接口发生错误时返回对应错误信息。 |
| callback | ErrorCallback | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型CameraErrorCode。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(previewOutputError: BusinessError): void {
  console.error(`Preview output error code: ${previewOutputError.code}`);
}

function registerPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('error', callback)
}
```



#### off('error')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'error', callback?: ErrorCallback): void

注销监听预览输出的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，previewOutput创建成功可监听。 |
| callback | ErrorCallback | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('error');
}
```



#### getSupportedFrameRates12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSupportedFrameRates(): Array&lt;FrameRateRange&gt;

查询支持的帧率范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;FrameRateRange&gt; | 支持的帧率范围列表。若接口调用失败，返回undefined。 |


**示例：**

```text
function getSupportedFrameRates(previewOutput: camera.PreviewOutput): Array<camera.FrameRateRange> {
  let supportedFrameRatesArray: Array<camera.FrameRateRange> = previewOutput.getSupportedFrameRates();
  return supportedFrameRatesArray;
}
```



#### setFrameRate12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFrameRate(minFps: number, maxFps: number): void

设置预览流帧率范围，设置的范围必须在支持的帧率范围内。

进行设置前，可通过[getSupportedFrameRates](#getsupportedframerates12)接口查询支持的帧率范围。

> [!NOTE]
> 仅在 PhotoSession 或 VideoSession 模式下支持。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minFps | number | 是 | 最小帧率（单位：fps），当传入的最大值小于最小值时，传参异常，接口不生效。 |
| maxFps | number | 是 | 最大帧率（单位：fps），当传入的最小值大于最大值时，传参异常，接口不生效。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400110 | Unresolved conflicts with current configurations. |


**示例：**

```text
function setFrameRateRange(previewOutput: camera.PreviewOutput, frameRateRange: Array<number>): void {
  previewOutput.setFrameRate(frameRateRange[0], frameRateRange[1]);
}
```



#### getActiveFrameRate12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getActiveFrameRate(): FrameRateRange

获取已设置的帧率范围。

使用[setFrameRate](#setframerate12)接口对预览流设置过帧率后可查询。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FrameRateRange | 帧率范围 |


**示例：**

```text
function getActiveFrameRate(previewOutput: camera.PreviewOutput): camera.FrameRateRange {
  let activeFrameRate: camera.FrameRateRange = previewOutput.getActiveFrameRate();
  return activeFrameRate;
}
```



#### getActiveProfile12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getActiveProfile(): Profile

获取当前生效的配置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Profile | 当前生效的配置信息 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function testGetActiveProfile(previewOutput: camera.PreviewOutput): camera.Profile | undefined {
  let activeProfile: camera.Profile | undefined = undefined;
  try {
    activeProfile = previewOutput.getActiveProfile();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.getActiveProfile call failed. error code: ${err.code}`);
  }
  return activeProfile;
}
```



#### getPreviewRotation12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getPreviewRotation(displayRotation?: number): ImageRotation

获取预览旋转角度。

 - 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。
 - 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。
 - [屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction#section737072712182)：显示设备的屏幕顺时针旋转角度。


**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayRotation | number | 否 | 显示设备的屏幕旋转角度，通过display.getDefaultDisplaySync获得。 从API version 23开始，入参displayRotation为可选参数，当不传入参数时，由系统获取displayRotation进行预览旋转角度计算。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImageRotation | 返回预览旋转角度。若接口调用失败，返回undefined。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function testGetPreviewRotation(previewOutput: camera.PreviewOutput, imageRotation : camera.ImageRotation): camera.ImageRotation {
  let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
  try {
    previewRotation = previewOutput.getPreviewRotation(imageRotation);
    console.info(`Preview rotation is: ${previewRotation}`);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.getPreviewRotation call failed. error code: ${err.code}`);
  }
  return previewRotation;
}

function testGetPreviewRotationWithOutParam(previewOutput: camera.PreviewOutput): camera.ImageRotation {
  let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
  try {
    previewRotation = previewOutput.getPreviewRotation();
    console.info(`Preview rotation is: ${previewRotation}`);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.testGetPreviewRotationWithOutParam call failed. error code: ${err.code}`);
  }
  return previewRotation;
}
```



#### setPreviewRotation12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void

设置预览旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| previewRotation | ImageRotation | 是 | 预览旋转角度 |
| isDisplayLocked | boolean | 否 | Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。详情请参考SurfaceRotationOptions |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function testSetPreviewRotation(previewOutput: camera.PreviewOutput, previewRotation : camera.ImageRotation, isDisplayLocked: boolean): void {
  try {
    previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.setPreviewRotation call failed. error code: ${err.code}`);
  }
  return;
}
```



#### start(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(callback: AsyncCallback&lt;void&gt;): void

开始输出预览流，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.start 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当开始输出预览流成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with preview output started.');
  });
}
```



#### start(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(): Promise&lt;void&gt;

开始输出预览流。使用Promise异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.start 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start().then(() => {
    console.info('Promise returned with preview output started.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output start, error code: ${error.code}.`);
  });
}
```



#### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(callback: AsyncCallback&lt;void&gt;): void

停止输出预览流，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.stop 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当停止输出预览流成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Returned with preview output stopped.');
  })
}
```



#### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(): Promise&lt;void&gt;

停止输出预览流。使用Promise异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.stop 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop().then(() => {
    console.info('Callback returned with preview output stopped.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output stop, error code: ${error.code}.`);
  });
}
```



#### isBandwidthCompressionSupported23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isBandwidthCompressionSupported(): boolean

检查是否支持预览带宽压缩（指通过编码减少数据量，降低其在传输链路中的带宽占用）。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持预览带宽压缩。true表示支持，false表示不支持。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function isBandwidthCompressionSupported(previewOutput: camera.PreviewOutput): boolean {
  let supported: boolean = false;
  try {
    supported = previewOutput.isBandwidthCompressionSupported();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.isBandwidthCompressionSupported call failed. error code: ${err.code}`);
  }
  return supported;
}
```



#### enableBandwidthCompression23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

enableBandwidthCompression(enabled: boolean): void

使能预览带宽压缩。

使能之前，可先使用方法[isBandwidthCompressionSupported](#isbandwidthcompressionsupported23)对设备是否支持预览带宽压缩进行检查。

> [!NOTE]
> 该接口只能在使用 Session.commitConfig 接口之前调用，否则会影响预览流出流格式。


**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否使能预览带宽压缩。true表示使能，false表示不使能。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function enableBandwidthCompression(previewOutput: camera.PreviewOutput, enabled: boolean): void {
  try {
    previewOutput.enableBandwidthCompression(enabled);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.enableBandwidthCompression call failed. error code: ${err.code}`);
  }
}
```



#### addDeferredSurface24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

addDeferredSurface(surfaceId: string): void

配置延迟预览的Surface，可以在[commitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11-1)配流和[start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#start11-1)启流之后运行。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 从XComponent组件获取的surfaceId。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function preview(cameraManager: camera.CameraManager, cameraInfo: camera.CameraDevice, previewProfile: camera.Profile, photoProfile: camera.Profile, mode: camera.SceneMode, previewSurfaceId: string): Promise<void> {
  let cameraInput: camera.CameraInput = cameraManager.createCameraInput(cameraInfo);
  let previewOutput: camera.PreviewOutput = cameraManager.createDeferredPreviewOutput(previewProfile);
  let photoOutput: camera.PhotoOutput = cameraManager.createPhotoOutput(photoProfile);
  let session: camera.Session  = cameraManager.createSession(mode);
  session.beginConfig();
  session.addInput(cameraInput);
  session.addOutput(previewOutput);
  session.addOutput(photoOutput);
  await session.commitConfig();
  try {
    await session.start();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`start session failed. error code: ${err.code}`);
  }
  previewOutput.addDeferredSurface(previewSurfaceId);
}
```
