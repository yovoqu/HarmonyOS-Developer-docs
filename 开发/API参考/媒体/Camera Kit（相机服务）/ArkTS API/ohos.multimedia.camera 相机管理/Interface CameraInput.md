# Interface (CameraInput)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

相机设备输入对象。

会话中[Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session)使用的相机信息。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { camera } from '@kit.CameraKit';
```



##### open

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(callback: AsyncCallback&lt;void&gt;): void

打开相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当打开相机成功，err为undefined，否则为错误对象，错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open((err: BusinessError) => {
    if (err) {
      console.error(`Failed to open camera, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with camera opened.');
  });
}
```



##### open

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(): Promise&lt;void&gt;

打开相机，使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open().then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open camera, error code: ${error.code}.`);
  });
}
```



##### open12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(isSecureEnabled: boolean): Promise&lt;bigint&gt;

打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSecureEnabled | boolean | 是 | 设置true为使能以安全的方式打开相机，设置false则反之。接口调用失败会返回相应错误码，错误码类型CameraErrorCode。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;bigint&gt; | Promise对象，返回安全相机的句柄。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(true).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open camera, error code: ${error.code}.`);
  });
}
```



##### open18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(type: CameraConcurrentType): Promise&lt;void&gt;

以指定的并发类型打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | CameraConcurrentType | 是 | 以指定的并发类型打开相机。接口调用失败会返回相应错误码。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(0).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open camera, error code: ${error.code}.`);
  });
}
```



##### close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(callback: AsyncCallback&lt;void&gt;): void

关闭相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当关闭相机成功，err为undefined，否则为错误对象。错误码类型CameraErrorCode。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close((err: BusinessError) => {
    if (err) {
      console.error(`Failed to close the cameras, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with camera closed.');
  });
}
```



##### close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): Promise&lt;void&gt;

关闭相机，使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close().then(() => {
    console.info('Promise returned with camera closed.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to close the cameras, error code: ${error.code}.`);
  });
}
```



##### on('error')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void

监听CameraInput的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。 |
| camera | CameraDevice | 是 | CameraDevice对象。 |
| callback | ErrorCallback | 是 | 回调函数，用于获取结果。返回错误码，错误码类型CameraErrorCode。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Camera input error code: ${err.code}`);
}

function registerCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.on('error', camera, callback);
}
```



##### off('error')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void

注销监听CameraInput的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。 |
| camera | CameraDevice | 是 | CameraDevice对象。 |
| callback | ErrorCallback | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.off('error', camera);
}
```



##### isPhysicalCameraOrientationVariable22+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isPhysicalCameraOrientationVariable(): boolean

查询设备不同折叠状态下，相机物理镜头角度是否可变。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 查询设备不同折叠状态下，相机物理镜头角度是否可变。true表示可变，false表示不可变。若接口调用失败，返回undefined。 |


**示例：**

```text
function isPhysicalCameraOrientationVariable(cameraInput: camera.CameraInput): boolean {
  let isVariable: boolean = cameraInput.isPhysicalCameraOrientationVariable();
  return isVariable;
}
```



##### getPhysicalCameraOrientation22+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getPhysicalCameraOrientation(): number

获取设备当前折叠状态下的物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回设备当前折叠状态下的物理镜头角度。 |


**示例：**

```text
function getPhysicalCameraOrientation(cameraInput: camera.CameraInput): number {
  let physicalCameraOrientation: number = cameraInput.getPhysicalCameraOrientation();
  return physicalCameraOrientation;
}
```



##### usePhysicalCameraOrientation22+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

usePhysicalCameraOrientation(isUsed: boolean): void

选择是否使用物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isUsed | boolean | 是 | 选择是否使用物理镜头角度。true表示使用，false表示不使用。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function usePhysicalCameraOrientation(cameraInput: camera.CameraInput, isUsed: boolean): void {
  try {
    cameraInput.usePhysicalCameraOrientation(isUsed);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The usePhysicalCameraOrientation call failed. error code: ${err.code}`);
  }
}
```



##### on('cameraOcclusionDetection')23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'cameraOcclusionDetection', callback: AsyncCallback&lt;CameraOcclusionDetectionResult&gt;): void

监听CameraInput的镜头遮挡或脏污事件，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraOcclusionDetection'，CameraInput对象创建成功可监听。相机镜头被遮挡或有脏污可触发该事件并返回结果。 |
| callback | AsyncCallback&lt;CameraOcclusionDetectionResult&gt; | 是 | 回调函数，用于获取结果。返回遮挡状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, result: camera.CameraOcclusionDetectionResult): void {
  if (err !== undefined && err.code !== 0) {
      console.error('cameraOcclusionDetection with errorCode = ' + err.code);
      return;
  }
  if (!result) {
      console.error(`cameraOcclusionDetection result: undefined`);
      return;
  }
  console.info(`onCameraOcclusionDetection isCameraOccluded: ${result.isCameraOccluded}`);
  console.info(`onCameraOcclusionDetection isCameraLensDirty: ${result.isCameraLensDirty}`);
}

function registerCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
  cameraInput.on('cameraOcclusionDetection', callback);
}
```



##### off('cameraOcclusionDetection')23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'cameraOcclusionDetection', callback?: AsyncCallback&lt;CameraOcclusionDetectionResult&gt;): void

注销监听CameraInput的镜头遮挡或脏污事件。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraOcclusionDetection'，CameraInput对象创建成功可监听。相机镜头被遮挡或有脏污可触发该事件并返回结果。 |
| callback | AsyncCallback&lt;CameraOcclusionDetectionResult&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function callback(err: BusinessError, result: camera.CameraOcclusionDetectionResult): void {
  if (err !== undefined && err.code !== 0) {
      console.error('cameraOcclusionDetection with errorCode = ' + err.code);
      return;
  }
  if (!result) {
      console.error(`cameraOcclusionDetection result: undefined`);
      return;
  }
  console.info(`onCameraOcclusionDetection isCameraOccluded: ${result.isCameraOccluded}`);
  console.info(`onCameraOcclusionDetection isCameraLensDirty: ${result.isCameraLensDirty}`);
}

function unregisterCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
    cameraInput.off('cameraOcclusionDetection', callback);
}

function unregisterAllCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
    cameraInput.off('cameraOcclusionDetection');
}
```
