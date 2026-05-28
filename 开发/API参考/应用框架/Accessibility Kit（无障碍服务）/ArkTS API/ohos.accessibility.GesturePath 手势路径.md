# @ohos.accessibility.GesturePath (手势路径)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

GesturePath表示手势路径信息。
 
本模块用于创建辅助功能注入手势所需的手势路径信息。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### 导入模块

```text
import { GesturePath } from '@kit.AccessibilityKit';
```
 
  

##### GesturePath

表示手势路径信息。
 
**系统能力**：SystemCapability.BarrierFree.Accessibility.Core
 
  

##### 属性
 
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| points | Array&lt;GesturePoint&gt; | 否 | 否 | 手势触摸点。 |
| durationTime | number | 否 | 否 | 手势总耗时，单位为毫秒。 |
 
 
  

##### constructor(deprecated)

constructor(durationTime: number);
 
构造函数。
 
> [!NOTE]
> 从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

 
**系统能力**：SystemCapability.BarrierFree.Accessibility.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| durationTime | number | 是 | 手势总耗时，单位为毫秒。 |
 
 
**示例：**
 
```text
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```
