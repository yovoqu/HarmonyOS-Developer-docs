# Interface (Photo)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

全质量图对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { camera } from '@kit.CameraKit';
```


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main11+ | [image.Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image) | 否 | 否 | 全质量图Image。 |


## release11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**示例：**


```ts
async function releasePhoto(photo: camera.Photo): Promise<void> {
  await photo.release();
}
```
