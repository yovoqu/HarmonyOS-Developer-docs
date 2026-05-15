# Interface (ManualFocusQuery)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocusquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

手动对焦查询对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## isFocusDistanceSupported24+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isFocusDistanceSupported(): boolean

检测是否支持设置对焦距离。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否支持对焦距离。返回true表示支持，返回false表示不支持。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusDistanceSupported(photoSession: camera.PhotoSession): boolean {
  let isSupported = false;
  try {
    isSupported = photoSession.isFocusDistanceSupported();
  } catch (error) {
    let err = error as BusinessError;
    console.error(
      `The isFocusDistanceSupported call failed. error code: ${err.code}`,
    );
  }
  return isSupported;
}
```
