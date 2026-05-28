# Interface (PhotoSession)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photosession
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PhotoSession继承自[Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session)、[Flash](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash)、[AutoExposure](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposure)、[WhiteBalance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalance)、[Focus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focus)、[Zoom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoom)、[ColorManagement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagement)、[AutoDeviceSwitch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitch)、[Macro](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro)、[ManualExposure](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposure)、[ManualFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocus)、[ManualIso](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualiso)、[OIS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-ois)、[Aperture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperture)。

普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间、微距、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。

默认的拍照模式，用于拍摄标准照片。支持多种照片格式和分辨率，适合大多数日常拍摄场景。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 11开始支持。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { camera } from '@kit.CameraKit';
```



##### canPreconfig12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean

查询当前Session是否支持指定的预配置类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | PreconfigType | 是 | 指定配置预期分辨率。 |
| preconfigRatio | PreconfigRatio | 否 | 可选画幅比例，默认为4:3。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持指定预配置类型。true表示支持，false表示不支持。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function testCanPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    let result = photoSession.canPreconfig(preconfigType, preconfigRatio);
    console.info(`canPreconfig ${preconfigType} ${preconfigRatio} result is : ${result}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The canPreconfig call failed. error code: ${err.code}`);
  }
}
```



##### preconfig12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void

对当前Session进行预配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | PreconfigType | 是 | 指定配置预期分辨率。 |
| preconfigRatio | PreconfigRatio | 否 | 可选画幅比例，默认为4:3。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function testPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    photoSession.preconfig(preconfigType, preconfigRatio);
    console.info(`preconfig success preconfigType: ${preconfigType}, preconfigRatio: ${preconfigRatio}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The preconfig call failed. error code: ${err.code}`);
  }
}
```



##### on('error')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'error', callback: ErrorCallback): void

监听普通拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用beginConfig，commitConfig，addInput等接口发生错误时返回错误信息。 |
| callback | ErrorCallback | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型CameraErrorCode。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Photo session error code: ${err.code}`);
}

function registerSessionError(photoSession: camera.PhotoSession): void {
  photoSession.on('error', callback);
}
```



##### off('error')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'error', callback?: ErrorCallback): void

注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | ErrorCallback | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterSessionError(photoSession: camera.PhotoSession): void {
  photoSession.off('error');
}
```



##### on('focusStateChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'focusStateChange', callback: AsyncCallback&lt;FocusState&gt;): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。 |
| callback | AsyncCallback&lt;FocusState&gt; | 是 | 回调函数，用于获取当前对焦状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, focusState: camera.FocusState): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`Focus state: ${focusState}`);
}

function registerFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.on('focusStateChange', callback);
}
```



##### off('focusStateChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'focusStateChange', callback?: AsyncCallback&lt;FocusState&gt;): void

注销监听相机聚焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。 |
| callback | AsyncCallback&lt;FocusState&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.off('focusStateChange');
}
```



##### on('smoothZoomInfoAvailable')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback&lt;SmoothZoomInfo&gt;): void

监听相机平滑变焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback&lt;SmoothZoomInfo&gt; | 是 | 回调函数，用于获取当前平滑变焦状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`The duration of smooth zoom: ${smoothZoomInfo.duration}`);
}

function registerSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.on('smoothZoomInfoAvailable', callback);
}
```



##### off('smoothZoomInfoAvailable')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback&lt;SmoothZoomInfo&gt;): void

注销监听相机平滑变焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback&lt;SmoothZoomInfo&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('smoothZoomInfoAvailable');
}
```



##### on('autoDeviceSwitchStatusChange')13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback&lt;AutoDeviceSwitchStatus&gt;): void

监听相机自动切换镜头状态变化，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback&lt;AutoDeviceSwitchStatus&gt; | 是 | 回调函数，用于获取当前自动切换镜头的状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
}

function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
  photoSession.on('autoDeviceSwitchStatusChange', callback);
}
```



##### off('autoDeviceSwitchStatusChange')13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback&lt;AutoDeviceSwitchStatus&gt;): void

注销监听相机自动切换镜头状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback&lt;AutoDeviceSwitchStatus&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('autoDeviceSwitchStatusChange');
}
```



##### on('systemPressureLevelChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'systemPressureLevelChange', callback: AsyncCallback&lt;SystemPressureLevel&gt;): void

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。

> [!NOTE]
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。


**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemPressureLevelChange'，session创建成功可监听。 |
| callback | AsyncCallback&lt;SystemPressureLevel&gt; | 是 | 回调函数，用于获取当前系统压力状态. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`systemPressureLevel: ${systemPressureLevel}`);
}

function registerSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
    photoSession.on('systemPressureLevelChange', callback);
}
```



##### off('systemPressureLevelChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'systemPressureLevelChange', callback?: AsyncCallback&lt;SystemPressureLevel&gt;): void

注销监听系统压力状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'systemPressureLevelChange'，session创建成功可触发此事件。 |
| callback | AsyncCallback&lt;SystemPressureLevel&gt; | 否 | 回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。 |


**示例：**

```text
function unregisterSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
  photoSession.off('systemPressureLevelChange');
}
```



##### on('macroStatusChanged')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'macroStatusChanged', callback: AsyncCallback&lt;boolean&gt;): void

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'macroStatusChanged'，session创建成功可监听。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数，用于获取当前微距状态，返回true为开启状态，返回false为禁用状态。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, macroStatus: boolean): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`Macro state: ${macroStatus}`);
}

function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.on('macroStatusChanged', callback);
}
```



##### off('macroStatusChanged')20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'macroStatusChanged', callback?: AsyncCallback&lt;boolean&gt;): void

注销相机微距状态变化的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'macroStatusChanged'，session创建成功可触发此事件。 |
| callback | AsyncCallback&lt;boolean&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则参数默认为空，取消所有callback。 |


**示例：**

```text
function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.off('macroStatusChanged');
}
```



##### onIsoInfoChange24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onIsoInfoChange(callback: Callback&lt;IsoInfo&gt;): void

订阅ISO信息变化事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;IsoInfo&gt; | 是 | 回调函数，用于获取ISO信息变化信息。 |


**示例：**

```text
function onIsoInfoChange(photoSession: camera.PhotoSession): void {
  photoSession.onIsoInfoChange((isoInfo: camera.IsoInfo) => {
    console.info(`ISO info changed, iso: ${isoInfo.iso}`);
  });
}
```



##### offIsoInfoChange24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offIsoInfoChange(callback?: Callback&lt;IsoInfo&gt;): void

取消订阅ISO信息变化事件回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;IsoInfo&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function offIsoInfoChange(photoSession: camera.PhotoSession): void {
  photoSession.offIsoInfoChange();
}
```



##### onExposureInfoChange24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onExposureInfoChange(callback: Callback&lt;ExposureInfo&gt;): void

订阅曝光信息变化事件回调。曝光参数更改后，系统将返回更新后的曝光信息。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;ExposureInfo&gt; | 是 | 回调函数，用于获取曝光值变化信息。 |


**示例：**

```text
function onExposureInfoChange(photoSession: camera.PhotoSession): void {
  photoSession.onExposureInfoChange((exposureInfo: camera.ExposureInfo) => {
    console.info(`Exposure info changed, exposureTime: ${exposureInfo.exposureTime}`);
  });
}
```



##### offExposureInfoChange24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offExposureInfoChange(callback?: Callback&lt;ExposureInfo&gt;): void

取消订阅曝光信息变化事件回调。如果订阅了曝光信息，请在释放相机前取消订阅。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;ExposureInfo&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |


**示例：**

```text
function offExposureInfoChange(photoSession: camera.PhotoSession): void {
  photoSession.offExposureInfoChange();
}
```
