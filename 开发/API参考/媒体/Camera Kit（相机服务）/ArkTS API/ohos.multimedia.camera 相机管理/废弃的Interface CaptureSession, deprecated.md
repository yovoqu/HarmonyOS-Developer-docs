# 废弃的Interface (CaptureSession, deprecated)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturesession
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

拍照会话类，保存一次相机运行所需要的所有资源[CameraInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput)、[CameraOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameraoutput)，并向相机设备申请完成相机功能(录像，拍照)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 PhotoSession 、 VideoSession 替代。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { camera } from '@kit.CameraKit';
```



##### beginConfig(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

beginConfig(): void

开始配置会话。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.beginConfig 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400105 | Session config locked. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function beginConfig(captureSession: camera.CaptureSession): void {
  try {
    captureSession.beginConfig();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The beginConfig call failed. error code: ${err.code}`);
  }
}
```



##### commitConfig(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

commitConfig(callback: AsyncCallback&lt;void&gt;): void

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.commitConfig 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当提交配置信息成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig((err: BusinessError) => {
    if (err) {
      console.error(`The commitConfig call failed. error code: ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate the commit config success.');
  });
}
```



##### commitConfig(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

commitConfig(): Promise&lt;void&gt;

提交配置信息。使用Promise异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.commitConfig 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig().then(() => {
    console.info('Promise returned to indicate the commit config success.');
  }).catch((error: BusinessError) => {
    // 失败返回错误码error.code并处理。
    console.error(`The commitConfig call failed. error code: ${error.code}`);
  });
}
```



##### addInput(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

addInput(cameraInput: CameraInput): void

把[CameraInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput)加入到会话。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.addInput 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraInput | CameraInput | 是 | 需要添加的CameraInput实例。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function addInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.addInput(cameraInput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The addInput call failed. error code: ${err.code}`);
  }
}
```



##### removeInput(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

removeInput(cameraInput: CameraInput): void

移除[CameraInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.removeInput 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraInput | CameraInput | 是 | 需要移除的CameraInput实例。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function removeInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.removeInput(cameraInput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The removeInput call failed. error code: ${err.code}`);
  }
}
```



##### addOutput(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

addOutput(cameraOutput: CameraOutput): void

把[CameraOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameraoutput)加入到会话。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.addOutput 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraOutput | CameraOutput | 是 | 需要添加的CameraOutput实例。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function addOutput(captureSession: camera.CaptureSession, cameraOutput: camera.CameraOutput): void {
  try {
    captureSession.addOutput(cameraOutput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The addOutput call failed. error code: ${err.code}`);
  }
}
```



##### removeOutput(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

removeOutput(cameraOutput: CameraOutput): void

从会话中移除[CameraOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameraoutput)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.removeOutput 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraOutput | CameraOutput | 是 | 需要移除的CameraOutput实例。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function removeOutput(captureSession: camera.CaptureSession, previewOutput: camera.PreviewOutput): void {
  try {
    captureSession.removeOutput(previewOutput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The removeOutput call failed. error code: ${err.code}`);
  }
}
```



##### start(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(callback: AsyncCallback&lt;void&gt;): void

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.start 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当开始会话工作成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}
```



##### start(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(): Promise&lt;void&gt;

开始会话工作。使用Promise异步回调。

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
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start the session, error code: ${err.code}.`);
  });
}
```



##### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(callback: AsyncCallback&lt;void&gt;): void

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.stop 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当停止会话工作成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}
```



##### stop(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(): Promise&lt;void&gt;

停止会话工作。使用Promise异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.stop 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop the session, error code: ${err.code}.`);
  });
}
```



##### release(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(callback: AsyncCallback&lt;void&gt;): void

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.release 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当释放会话资源成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate that the CaptureSession instance is released successfully.');
  });
}
```



##### release(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): Promise&lt;void&gt;

释放会话资源。使用Promise异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Session.release 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release().then(() => {
    console.info('Promise returned to indicate that the CaptureSession instance is released successfully.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
  });
}
```



##### hasFlash(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

hasFlash(): boolean

检测是否有闪光灯。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Flash.hasFlash 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设备支持闪光灯。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function hasFlash(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.hasFlash();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The hasFlash call failed. error code: ${err.code}`);
  }
  return status;
}
```



##### isFlashModeSupported(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isFlashModeSupported(flashMode: FlashMode): boolean

检测闪光灯模式是否支持。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Flash.isFlashModeSupported 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | FlashMode | 是 | 指定闪光灯模式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测闪光灯模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function isFlashModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFlashModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```



##### setFlashMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFlashMode(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：
1. 设备是否支持闪光灯，可使用方法[hasFlash](#hasflashdeprecated)。
2. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](#isflashmodesupporteddeprecated)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Flash.setFlashMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | FlashMode | 是 | 指定闪光灯模式。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setFlashMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFlashMode call failed. error code: ${err.code}`);
  }
}
```



##### getFlashMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFlashMode(): FlashMode

获取当前设备的闪光灯模式。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Flash.getFlashMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FlashMode | 获取当前设备的闪光灯模式。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getFlashMode(captureSession: camera.CaptureSession): camera.FlashMode | undefined {
  let flashMode: camera.FlashMode | undefined = undefined;
  try {
    flashMode = captureSession.getFlashMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFlashMode call failed.error code: ${err.code}`);
  }
  return flashMode;
}
```



##### isExposureModeSupported(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isExposureModeSupported(aeMode: ExposureMode): boolean

查询曝光模式是否支持。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.isExposureModeSupported 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | ExposureMode | 是 | 曝光模式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 获取是否支持曝光模式。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function isExposureModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isExposureModeSupported(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isExposureModeSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```



##### getExposureMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExposureMode(): ExposureMode

获取当前曝光模式。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.getExposureMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ExposureMode | 获取当前曝光模式。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(captureSession: camera.CaptureSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = captureSession.getExposureMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureMode call failed. error code: ${err.code}`);
  }
  return exposureMode;
}
```



##### setExposureMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setExposureMode(aeMode: ExposureMode): void

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法[isExposureModeSupported](#isexposuremodesupporteddeprecated)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.setExposureMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | ExposureMode | 是 | 曝光模式。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setExposureMode call failed. error code: ${err.code}`);
  }
}
```



##### getMeteringPoint(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMeteringPoint(): Point

查询曝光区域中心点。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.getMeteringPoint 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Point | 获取当前曝光点。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = captureSession.getMeteringPoint();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
  }
  return exposurePoint;
}
```



##### setMeteringPoint(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setMeteringPoint(point: Point): void

设置曝光区域中心点，曝光点应位于0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.setMeteringPoint 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 曝光点，x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(captureSession: camera.CaptureSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setMeteringPoint(point);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
  }
}
```



##### getExposureBiasRange(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExposureBiasRange(): Array&lt;number&gt;

查询曝光补偿范围。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.getExposureBiasRange 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;number&gt; | 获取补偿范围的数组。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureBiasRange(captureSession: camera.CaptureSession): Array<number> {
  let biasRangeArray: Array<number> = [];
  try {
    biasRangeArray = captureSession.getExposureBiasRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureBiasRange call failed. error code: ${err.code}`);
  }
  return biasRangeArray;
}
```



##### setExposureBias(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setExposureBias(exposureBias: number): void

设置曝光补偿，曝光补偿值（EV）。

进行设置之前，建议先通过方法[getExposureBiasRange](#getexposurebiasrangedeprecated)查询支持的范围。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.setExposureBias 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exposureBias | number | 是 | 曝光补偿，getExposureBiasRange查询支持的范围，如果设置超过支持范围的值，自动匹配到就近临界点。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。传参为null或者undefined，作为0处理，曝光补偿设置0。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(captureSession: camera.CaptureSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray[0];
    try {
      captureSession.setExposureBias(exposureBias);
    } catch (error) {
      // 失败返回错误码error.code并处理。
      let err = error as BusinessError;
      console.error(`The setExposureBias call failed. error code: ${err.code}`);
    }
  }
}
```



##### getExposureValue(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExposureValue(): number

查询当前的曝光值。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 AutoExposure.getExposureValue 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = captureSession.getExposureValue();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureValue call failed. error code: ${err.code}`);
  }
  return exposureValue;
}
```



##### isFocusModeSupported(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isFocusModeSupported(afMode: FocusMode): boolean

查询对焦模式是否支持。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.isFocusModeSupported 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | FocusMode | 是 | 指定的焦距模式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测对焦模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFocusModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```



##### setFocusMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFocusMode(afMode: FocusMode): void

设置对焦模式。

进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](#isfocusmodesupporteddeprecated)。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.setFocusMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | FocusMode | 是 | 指定的焦距模式。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusMode call failed. error code: ${err.code}`);
  }
}
```



##### getFocusMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFocusMode(): FocusMode

获取当前的对焦模式。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.getFocusMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FocusMode | 获取当前设备的焦距模式。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusMode(captureSession: camera.CaptureSession): camera.FocusMode | undefined {
  let afMode: camera.FocusMode | undefined = undefined;
  try {
    afMode = captureSession.getFocusMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusMode call failed. error code: ${err.code}`);
  }
  return afMode;
}
```



##### setFocusPoint(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFocusPoint(point: Point): void

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.setFocusPoint 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 焦点。x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusPoint(captureSession: camera.CaptureSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setFocusPoint(focusPoint);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusPoint call failed. error code: ${err.code}`);
  }
}
```



##### getFocusPoint(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFocusPoint(): Point

查询焦点。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.getFocusPoint 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Point | 用于获取当前焦点。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let point: camera.Point | undefined = undefined;
  try {
    point = captureSession.getFocusPoint();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusPoint call failed. error code: ${err.code}`);
  }
  return point;
}
```



##### getFocalLength(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFocalLength(): number

查询焦距值。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Focus.getFocalLength 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 用于获取当前焦距。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getFocalLength(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let focalLength: number = invalidValue;
  try {
    focalLength = captureSession.getFocalLength();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocalLength call failed. error code: ${err.code}`);
  }
  return focalLength;
}
```



##### getZoomRatioRange(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getZoomRatioRange(): Array&lt;number&gt;

获取支持的变焦范围。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Zoom.getZoomRatioRange 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;number&gt; | 用于获取可变焦距比范围，返回的数组包括其最小值和最大值。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(captureSession: camera.CaptureSession): Array<number> {
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = captureSession.getZoomRatioRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
  }
  return zoomRatioRange;
}
```



##### setZoomRatio(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Zoom.setZoomRatio 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomRatio | number | 是 | 可变焦距比，通过getZoomRatioRange获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。传参为null或者undefined，作为0处理，变焦设置最小值。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(captureSession: camera.CaptureSession, zoomRatioRange: Array<number>): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange[0];
  try {
    captureSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setZoomRatio call failed. error code: ${err.code}`);
  }
}
```



##### getZoomRatio(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getZoomRatio(): number

获取当前的变焦比。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Zoom.getZoomRatio 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = captureSession.getZoomRatio();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatio call failed. error code: ${err.code}`);
  }
  return zoomRatio;
}
```



##### isVideoStabilizationModeSupported(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean

查询是否支持指定的视频防抖模式。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Stabilization.isVideoStabilizationModeSupported 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vsMode | VideoStabilizationMode | 是 | 视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回视频防抖模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function isVideoStabilizationModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isVideoStabilizationModeSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```



##### getActiveVideoStabilizationMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getActiveVideoStabilizationMode(): VideoStabilizationMode

查询当前正在使用的视频防抖模式。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Stabilization.getActiveVideoStabilizationMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| VideoStabilizationMode | 视频防抖是否正在使用。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(captureSession: camera.CaptureSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = captureSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
  }
  return vsMode;
}
```



##### setVideoStabilizationMode(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](#isvideostabilizationmodesupporteddeprecated)方法判断所设置的模式是否支持。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 Stabilization.setVideoStabilizationMode 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | VideoStabilizationMode | 是 | 需要设置的视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
  }
}
```



##### on('focusStateChange')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'focusStateChange', callback: AsyncCallback&lt;FocusState&gt;): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 VideoSession.on('focusStateChange') 替代。 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session 创建成功可监听。仅当自动对焦模式时,且相机对焦状态发生改变时可触发该事件。 |
| callback | AsyncCallback&lt;FocusState&gt; | 是 | 回调函数，用于获取当前对焦状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function registerFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
    if (err !== undefined && err.code !== 0) {
      console.error(`Callback Error, errorCode: ${err.code}`);
      return;
    }
    console.info(`Focus state: ${focusState}`);
  });
}
```



##### off('focusStateChange')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'focusStateChange', callback?: AsyncCallback&lt;FocusState&gt;): void

注销监听相机聚焦的状态变化。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 VideoSession.off('focusStateChange') 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session 创建成功可监听。 |
| callback | AsyncCallback&lt;FocusState&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.off('focusStateChange');
}
```



##### on('error')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', callback: ErrorCallback): void

监听拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。 从 API version 10开始支持，从API version 11开始废弃。建议使用 VideoSession.on('error') 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用beginConfig，commitConfig，addInput等接口发生错误时返回错误信息。 |
| callback | ErrorCallback | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型CameraErrorCode。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function registerCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.on('error', (error: BusinessError) => {
    console.error(`Capture session error code: ${error.code}`);
  });
}
```



##### off('error')(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'error', callback?: ErrorCallback): void

注销监听拍照会话的错误事件，通过注册回调函数获取结果。

> [!NOTE]
> 从 API version 10开始支持，从API version 11开始废弃。建议使用 VideoSession.off('error') 替代。


**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | ErrorCallback | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.off('error');
}
```
