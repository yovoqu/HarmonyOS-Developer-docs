# Interface (FocusQuery)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focusquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供了查询是否支持当前对焦模式的方法。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## isFocusModeSupported11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isFocusModeSupported(afMode: FocusMode): boolean

检测对焦模式是否支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#focusmode) | 是 | 指定的焦距模式。传参为null或者undefined，作为0处理，手动对焦模式。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 检测对焦模式是否支持。true表示支持，false表示不支持。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#cameraerrorcode)。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    status = photoSession.isFocusModeSupported(
      camera.FocusMode.FOCUS_MODE_AUTO,
    );
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(
      `The isFocusModeSupported call failed. error code: ${err.code}`,
    );
  }
  return status;
}
```
