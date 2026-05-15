# ImageOverlay

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-imageoverlay
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { mapCommon } from '@kit.MapKit';
```


## ImageOverlay
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

图片覆盖物。继承[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**


```ts
let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 },
  },
  // 图标需存放在resources/rawfile目录下
  image: 'icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0,
};
let imageOverlay = await this.mapController.addImageOverlay(imageOverlayParams);
imageOverlay.setBearing(180);
let bearing: number = imageOverlay.getBearing();
```


### getBearing
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getBearing(): number

获取覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回覆盖物的旋转角度，单位：度。 |


**示例：**


```ts
let bearing: number = imageOverlay.getBearing();
```


### getBounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getBounds(): mapCommon.LatLngBounds

获取覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 获取覆盖物的矩形区域。 |


**示例：**


```ts
let bounds: mapCommon.LatLngBounds = imageOverlay.getBounds();
```


### getHeight
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getHeight(): number

获取覆盖物的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的高度，单位：m。 |


**示例：**


```ts
let height: number = imageOverlay.getHeight();
```


### getWidth
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getWidth(): number

获取覆盖物的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的宽度，单位：m。 |


**示例：**


```ts
let width: number = imageOverlay.getWidth();
```


### getPosition
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getPosition(): mapCommon.LatLng

获取覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 覆盖物的位置。 |


**示例：**


```ts
let position: mapCommon.LatLng = imageOverlay.getPosition();
```


### getTransparency
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

getTransparency(): number

获取覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。 |


**示例：**


```ts
let transparency: number = imageOverlay.getTransparency();
```


### isClickable
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

isClickable(): boolean

获取是否可点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 是否可点击。 - true：可点击 - false：不可点击 |


**示例：**


```ts
let click: boolean = imageOverlay.isClickable();
```


### setBearing
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setBearing(bearing: number): void

设置覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bearing | number | 是 | 覆盖物的旋转角度，单位：度。 以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |


**示例：**


```ts
imageOverlay.setBearing(180);
```


### setClickable
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setClickable(clickable: boolean): void

设置是否开启可点击开关。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 是否开启可点击开关。 - true：开启 - false：不开启 |


**示例：**


```ts
imageOverlay.setClickable(false);
```


### setDimensions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setDimensions(width: number, height?: number): void

设置覆盖物的宽度和高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 宽度，width为正整数，单位：m，异常值不处理。 |
| height | number | 否 | 高度，height为正整数，单位：m，异常值不处理。若不设置高度，则以覆盖物图片默认宽高比例显示高度。 |


**示例：**


```ts
imageOverlay.setDimensions(100000, 100000);
```


### setImage
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setImage(image: ResourceStr | image.PixelMap): Promise<void>

设置覆盖物的图像。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) \| [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 覆盖物的图像。 图片格式支持jpg、jpeg、png、gif、webp、svg。 说明： [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)为Resource和string两种格式，其中string类型入参支持两种格式： - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。 - toDataURL格式（如data:image/png;base64,&lt;图片的Base64字节编码值&gt;）。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**


```ts
// 图标需存放在resources/rawfile目录下
await imageOverlay.setImage('icon.png');
```


### setBounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setBounds(bounds: mapCommon.LatLngBounds): void

设置覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 是 | 覆盖物的矩形区域。 |


**示例：**


```ts
let bounds: mapCommon.LatLngBounds = {
  southwest: { longitude: 118, latitude: 31 },
  northeast: { longitude: 119, latitude: 32 },
};
imageOverlay.setBounds(bounds);
```


### setPosition
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setPosition(position: mapCommon.LatLng): void

设置覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 覆盖物的位置。 |


**示例：**


```ts
let position: mapCommon.LatLng = { longitude: 118, latitude: 31 };
imageOverlay.setPosition(position);
```


### setTransparency
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

setTransparency(transparency: number): void

设置覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transparency | number | 是 | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。异常值不处理。 |


**示例：**


```ts
imageOverlay.setTransparency(0.1);
```
