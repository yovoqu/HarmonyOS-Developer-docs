# Interface (ColorManagementQuery)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagementquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

色彩管理类，用于查询色彩空间参数。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## getSupportedColorSpaces12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>

获取支持的色彩空间列表。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;[colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace)&gt; | 支持的色彩空间列表。若接口调用失败，返回undefined。 |


**示例：**


```ts
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getSupportedColorSpaces(
  session: camera.PhotoSession,
): Array<colorSpaceManager.ColorSpace> {
  let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
  colorSpaces = session.getSupportedColorSpaces();
  return colorSpaces;
}
```
