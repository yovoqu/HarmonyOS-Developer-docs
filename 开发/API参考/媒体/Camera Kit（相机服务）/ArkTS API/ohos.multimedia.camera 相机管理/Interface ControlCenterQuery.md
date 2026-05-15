# Interface (ControlCenterQuery)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

控制中心类，用于查询是否支持相机控制器。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## isControlCenterSupported20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isControlCenterSupported(): boolean

查询是否支持相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持相机控制器。true表示支持，false表示不支持。 |


**示例：**


```ts
function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
  let isSupported: boolean = videoSession.isControlCenterSupported();
  return isSupported;
}
```


## getSupportedEffectTypes20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSupportedEffectTypes(): Array<ControlCenterEffectType>

查询相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;[ControlCenterEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#controlcentereffecttype20)&gt; | 支持的效果类型。 |


**示例：**


```ts
function getSupportedEffectTypes(
  videoSession: camera.VideoSession,
): Array<camera.ControlCenterEffectType> {
  let effectTypes: Array<camera.ControlCenterEffectType> = [];
  effectTypes = videoSession.getSupportedEffectTypes();
  return effectTypes;
}
```
