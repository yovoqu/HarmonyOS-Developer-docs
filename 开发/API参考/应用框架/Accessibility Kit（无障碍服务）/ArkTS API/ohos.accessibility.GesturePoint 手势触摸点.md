# @ohos.accessibility.GesturePoint (手势触摸点)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

GesturePoint表示手势触摸点。

本模块用于创建辅助功能注入手势所需的手势路径的触摸点信息。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { GesturePoint } from '@kit.AccessibilityKit';
```


## GesturePoint
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

表示手势触摸点。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core


### 属性


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| positionX | number | 否 | 否 | 触摸点X坐标。 |
| positionY | number | 否 | 否 | 触摸点Y坐标。 |


### constructor(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

constructor(positionX: number, positionY: number);

构造函数。


> [!NOTE]
> 从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionX | number | 是 | 触摸点X坐标。 |
| positionY | number | 是 | 触摸点Y坐标。 |


**示例：**


```ts
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```
