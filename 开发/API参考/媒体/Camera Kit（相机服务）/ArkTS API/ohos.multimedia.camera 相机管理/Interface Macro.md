# Interface (Macro)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Macro继承自[MacroQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery)。

提供使能微距能力的接口。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## enableMacro19+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

enableMacro(enabled: boolean): void

使能当前的微距能力。


> [!NOTE]
> 使用该接口前，需要先通过[isMacroSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery#ismacrosupported19)接口查询当前设备是否支持微距能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启微距能力。true表示开启微距能力，false表示关闭微距能力。 |


**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。


| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |


**示例：**


```ts
function enableMacro(photoSession: camera.PhotoSession): void {
  let isSupported: boolean = photoSession.isMacroSupported();
  if (isSupported) {
    photoSession.enableMacro(true);
  }
}
```
