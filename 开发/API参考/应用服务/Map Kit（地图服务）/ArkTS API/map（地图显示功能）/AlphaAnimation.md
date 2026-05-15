# AlphaAnimation

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-alphaanimation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { map } from '@kit.MapKit';
```


## AlphaAnimation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

控制透明度的动画类，继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)


### constructor
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

constructor(fromAlpha: number, toAlpha: number)

构造器，构造控制透明度的动画实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromAlpha | number | 是 | 起始透明度。透明度范围为[0, 1]，1为不透明，0为完全透明，异常值不处理。 |
| toAlpha | number | 是 | 目标透明度。透明度范围为[0, 1]，1为不透明，0为完全透明，异常值不处理。 |


**示例：**


```ts
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
```
