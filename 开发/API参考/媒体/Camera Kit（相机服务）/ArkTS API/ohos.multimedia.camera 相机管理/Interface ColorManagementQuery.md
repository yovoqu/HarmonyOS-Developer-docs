# Interface (ColorManagementQuery)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagementquery
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

色彩管理类，用于查询色彩空间参数。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 12开始支持。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { camera } from '@kit.CameraKit';
```



##### getSupportedColorSpaces12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>

获取支持的色彩空间列表。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<colorSpaceManager.ColorSpace> | 支持的色彩空间列表。若接口调用失败，返回undefined。 |


**示例：**

```text
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
  let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
  colorSpaces = session.getSupportedColorSpaces();
  return colorSpaces;
}
```
