# Interface (Zoom)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoom
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Zoom继承自[ZoomQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery)。

变焦类，对设备变焦操作。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## setZoomRatio11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomRatio | number | 是 | 可变焦距比，通过[getZoomRatioRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery#getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。 设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(
  photoSession: camera.PhotoSession,
  zoomRatioRange: Array<number>,
): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange[0];
  try {
    photoSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setZoomRatio call failed. error code: ${err.code}`);
  }
}
```


## getZoomRatio11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getZoomRatio(): number

获取当前的变焦比。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#cameraerrorcode)。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = photoSession.getZoomRatio();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatio call failed. error code: ${err.code}`);
  }
  return zoomRatio;
}
```


## setSmoothZoom11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void

触发平滑变焦。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetRatio | number | 是 | 目标值。通过[getZoomRatioRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery#getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。 |
| mode | [SmoothZoomMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#smoothzoommode11) | 否 | 平滑变焦模式。默认为0。 |


**示例：**


```ts
function setSmoothZoom(
  sessionExtendsZoom: camera.Zoom,
  targetZoomRatio: number,
  mode: camera.SmoothZoomMode,
): void {
  sessionExtendsZoom.setSmoothZoom(targetZoomRatio, mode);
}
```
