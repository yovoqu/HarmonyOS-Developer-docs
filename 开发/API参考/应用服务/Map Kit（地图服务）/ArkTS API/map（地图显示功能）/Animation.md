# Class (Animation)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { map } from '@kit.MapKit';
```
 
  

##### Animation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

动画抽象类。
 
> [!NOTE]
> 动画持续时间默认值为250ms； 动画执行完成后的状态，默认值为 AnimationFillMode .FORWARDS； 动画插值器，默认值为 Curve .Linear； 动画重复执行的次数，默认值为0； 重复执行的模式，默认值为 AnimationRepeatMode .RESTART。

 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**示例：**
 
```text
let animation = new map.RotateAnimation(0, 270);
// 动画执行时间
animation.setDuration(2000);

// 动画结束状态
animation.setFillMode(map.AnimationFillMode.BACKWARDS);

// 动画重复模式
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

// 动画重复次数
animation.setRepeatCount(100);

// 根据开发需要设置动画监听
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
```
 
  

##### setDuration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setDuration(duration: number): void
 
设置动画持续时间。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 动画持续时间，单位：ms，取值范围：大于等于0，异常值不处理。 |
 
 
**示例：**
 
```text
animation.setDuration(3000);
```
 
  

##### setFillMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setFillMode(fillMode: AnimationFillMode): void
 
设置动画执行完成后的状态。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillMode | AnimationFillMode | 是 | 动画执行完成后的状态。 |
 
 
**示例：**
 
```text
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
```
 
  

##### setInterpolator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setInterpolator(curve: Curves.Curve): void
 
设置动画插值器。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curve | Curves.Curve | 是 | 动画插值器。 |
 
 
**示例：**
 
```text
animation.setInterpolator(Curve.Linear);
```
 
  

##### setRepeatCount

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setRepeatCount(repeatCount: number): void
 
设置动画重复执行的次数。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| repeatCount | number | 是 | 动画重复执行的次数。 正数：根据值重复执行 0：动画不重复执行 -1：执行次数是无限 小于-1或其他异常值，取值默认为0 |
 
 
**示例：**
 
```text
animation.setRepeatCount(100);
```
 
  

##### setRepeatMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setRepeatMode(repeatMode: AnimationRepeatMode): void
 
设置重复执行的模式，默认从前往后执行。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| repeatMode | AnimationRepeatMode | 是 | 重复执行的模式。 |
 
 
**示例：**
 
```text
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
```
 
  

##### on('start')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

on(type: 'start', callback: Callback&lt;void&gt;): void
 
监听动画开始事件。使用callback异步回调。
 
建议使用[animation.on(type: 'animationStart')](#onanimationstart)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'start'：动画开始事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。 |
 
 
**示例：**
 
```text
animation.on("start", () => {
  console.info(`start alphaAnimation`);
});
```
 
  

##### off('start')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

off(type: 'start', callback: Callback&lt;void&gt;): void
 
取消监听动画开始事件。使用callback异步回调。
 
建议使用[animation.off(type: 'animationStart')](#offanimationstart)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'start'：动画开始事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。 |
 
 
**示例：**
 
```text
animation.off("start", () => {
  console.info(`start alphaAnimation`);
});
```
 
  

##### on('end')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

on(type: 'end', callback: Callback&lt;void&gt;): void
 
监听动画结束事件。使用callback异步回调。
 
建议使用[animation.on(type: 'animationEnd')](#onanimationend)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'end'：动画结束事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。 |
 
 
**示例：**
 
```text
animation.on("end", () => {
  console.info(`end alphaAnimation`);
});
```
 
  

##### off('end')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

off(type: 'end', callback: Callback&lt;void&gt;): void
 
取消监听动画结束事件。使用callback异步回调。
 
建议使用[animation.off(type: 'animationEnd')](#offanimationend)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'end'：动画结束事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。 |
 
 
**示例：**
 
```text
animation.off("end", () => {
  console.info(`end alphaAnimation`);
});
```
 
  

##### on('animationStart')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

on(type: 'animationStart', callback: Callback&lt;void&gt;): void
 
监听动画开始事件。支持传递多个callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'animationStart'：监听动画开始事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。监听动画开始事件。 |
 
 
**示例：**
 
```text
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);
```
 
  

##### off('animationStart')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

off(type: 'animationStart', callback?: Callback&lt;void&gt;): void
 
取消监听动画开始事件。支持传递多个callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'animationStart'：监听动画开始事件。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数，无返回结果。取消监听动画开始事件。 - callback为空：取消所有callback回调。 - callback非空：取消指定的callback回调。 |
 
 
**示例：**
 
```text
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);

// 只取消callback1对象的事件响应，当animationStart事件发生时，callback2和callback3会正常被调用
animation.off('animationStart', callback1);
// 取消全部animationStart事件响应
animation.off('animationStart');
```
 
  

##### on('animationEnd')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

on(type: 'animationEnd', callback: Callback&lt;void&gt;): void
 
监听动画结束事件。支持传递多个callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'animationEnd'：动画结束事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。监听动画结束事件。 |
 
 
**示例：**
 
```text
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);
```
 
  

##### off('animationEnd')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

off(type: 'animationEnd', callback?: Callback&lt;void&gt;): void
 
取消监听动画结束事件。支持传递多个callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'animationEnd'：监听动画结束事件。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数，无返回结果。取消监听动画结束事件。 - callback为空：取消所有callback回调。 - callback非空：取消指定的callback回调。 |
 
 
**示例：**
 
```text
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);

// 只取消callback1对象的事件响应，当animationEnd事件发生时，callback2和callback3会正常被调用
animation.off('animationEnd', callback1);
// 取消全部animationEnd事件响应
animation.off('animationEnd');
```
