# Interface (ManualIsoQuery)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualisoquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

手动ISO查询对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## getSupportedIsoRange24+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSupportedIsoRange(): number[]

获取支持的标准ISO感光度值数组。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number[] | ISO感光度值数组。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config, only throw in session usage. |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedIsoRange(photoSession: camera.PhotoSession): number[] {
  let isoRange: number[] = [];
  try {
    isoRange = photoSession.getSupportedIsoRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(
      `The getSupportedIsoRange call failed. error code: ${err.code}`,
    );
  }
  return isoRange;
}
```
