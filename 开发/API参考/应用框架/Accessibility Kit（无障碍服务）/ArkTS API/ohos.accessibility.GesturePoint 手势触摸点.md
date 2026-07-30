# @ohos.accessibility.GesturePoint (手势触摸点)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

GesturePoint表示手势触摸点，是构成手势路径GesturePath的基本单元。
 
本模块用于创建手势路径的触摸点信息，供辅助功能注入手势使用。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { GesturePoint } from '@kit.AccessibilityKit';
```
 
  

#### GesturePoint

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

表示手势触摸点，是构成GesturePath路径节点的基本单元，用于定义辅助功能注入手势轨迹中的触摸位置。详细使用方式请参见[GesturePath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath)。
 
**系统能力：** SystemCapability.BarrierFree.Accessibility.Core
 
  

#### 属性
 
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| positionX | number | 否 | 否 | 触摸点X坐标，单位为像素（px）。 |
| positionY | number | 否 | 否 | 触摸点Y坐标，单位为像素（px）。 |
 
 
  

#### constructor(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

constructor(positionX: number, positionY: number)
 
根据传入的X坐标和Y坐标创建GesturePoint实例。
 
> [!NOTE]
> 从API version 9开始支持，从API version 12开始废弃。

 
**系统能力：** SystemCapability.BarrierFree.Accessibility.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| positionX | number | 是 | 触摸点X坐标，单位为像素（px）。 |
| positionY | number | 是 | 触摸点Y坐标，单位为像素（px）。 |
 
 
**示例：**
 
```text
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```
