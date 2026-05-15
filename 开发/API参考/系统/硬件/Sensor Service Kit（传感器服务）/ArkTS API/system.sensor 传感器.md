# @system.sensor (传感器)

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-sensor
**支持设备：** Wearable / lite_wearable

sensor模块提供订阅传感器数据基本能力，主要包含查询传感器的列表、订阅/取消传感器的数据、执行控制命令等。

根据传感器的用途，可以将传感器分为六大类：运动类传感器、环境类传感器、方向类传感器、光线类传感器、健康类传感器、其他类传感器（如霍尔传感器），每一大类传感器包含不同类型的传感器，某种类型的传感器可能是单一的物理传感器，也可能是由多个物理传感器复合而成。


> [!NOTE]
> 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。该功能使用需要对应硬件支持，仅支持真机调试。


## 导入模块
**支持设备：** Wearable / lite_wearable


```ts
import { Sensor } from '@kit.SensorServiceKit';
```


## Sensor.subscribeAccelerometer
**支持设备：** Wearable / lite_wearable

subscribeAccelerometer(options: subscribeAccelerometerOptions): void

观察加速度数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[ACCELEROMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#accelerometer9)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER，该权限为系统权限

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [subscribeAccelerometerOptions](#subscribeaccelerometeroptions) | 是 | 监听加速度传感器数据的回调函数的执行频率。 |


**示例**：


```ts
import {
  Sensor,
  AccelerometerResponse,
  subscribeAccelerometerOptions,
} from '@kit.SensorServiceKit';

let accelerometerOptions: subscribeAccelerometerOptions = {
  interval: 'normal',
  success: (ret: AccelerometerResponse) => {
    console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
    console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
    console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeAccelerometer(accelerometerOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeAccelerometer
**支持设备：** Wearable / lite_wearable

unsubscribeAccelerometer(): void

取消订阅加速度数据。

除Lite Wearable外，从API Version8开始，推荐使用[ACCELEROMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#accelerometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER，该权限为系统权限

**示例**：


```ts
Sensor.unsubscribeAccelerometer();
```


## Sensor.subscribeCompass
**支持设备：** Wearable / lite_wearable

subscribeCompass(options: SubscribeCompassOptions): void

订阅罗盘数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#orientationdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeCompassOptions](#subscribecompassoptions) | 是 | 当罗盘传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  CompassResponse,
  SubscribeCompassOptions,
} from '@kit.SensorServiceKit';

let subscribeCompassOptions: SubscribeCompassOptions = {
  success: (ret: CompassResponse) => {
    console.info(
      'Succeeded in subscribing. Get data direction:' + ret.direction,
    );
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeCompass(subscribeCompassOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeCompass
**支持设备：** Wearable / lite_wearable

unsubscribeCompass(): void

取消订阅罗盘。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#orientationdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：


```ts
Sensor.unsubscribeCompass();
```


## Sensor.subscribeProximity
**支持设备：** Wearable / lite_wearable

subscribeProximity(options: SubscribeProximityOptions): void

订阅距离感应数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[PROXIMITY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#proximitydeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeProximityOptions](#subscribeproximityoptions) | 是 | 当距离传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  ProximityResponse,
  SubscribeProximityOptions,
} from '@kit.SensorServiceKit';

let subscribeProximityOptions: SubscribeProximityOptions = {
  success: (ret: ProximityResponse) => {
    console.info('Succeeded in subscribing. Get data distance:' + ret.distance);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeProximity(subscribeProximityOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeProximity
**支持设备：** Wearable / lite_wearable

unsubscribeProximity(): void

取消订阅距离感应。

除Lite Wearable外，从API Version8开始，推荐使用[PROXIMITY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#proximitydeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：


```ts
Sensor.unsubscribeProximity();
```


## Sensor.subscribeLight
**支持设备：** Wearable / lite_wearable

subscribeLight(options: SubscribeLightOptions): void

订阅环境光线感应数据变化。再次调用时，会覆盖前一次调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[AMBIENT_LIGHT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#ambient_lightdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeLightOptions](#subscribelightoptions) | 是 | 当环境光传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  LightResponse,
  SubscribeLightOptions,
} from '@kit.SensorServiceKit';

let subscribeLightOptions: SubscribeLightOptions = {
  success: (ret: LightResponse) => {
    console.info(
      'Succeeded in subscribing. Get data intensity:' + ret.intensity,
    );
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeLight(subscribeLightOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeLight
**支持设备：** Wearable / lite_wearable

unsubscribeLight(): void

取消订阅环境光线感应。

除Lite Wearable外，从API Version8开始，推荐使用[AMBIENT_LIGHT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#ambient_lightdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：


```ts
Sensor.unsubscribeLight();
```


## Sensor.subscribeStepCounter
**支持设备：** Wearable / lite_wearable

subscribeStepCounter(options: SubscribeStepCounterOptions): void

订阅计步传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[PEDOMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#pedometerdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACTIVITY_MOTION

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeStepCounterOptions](#subscribestepcounteroptions) | 是 | 当步进计数器传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  StepCounterResponse,
  SubscribeStepCounterOptions,
} from '@kit.SensorServiceKit';

let subscribeStepCounterOptions: SubscribeStepCounterOptions = {
  success: (ret: StepCounterResponse) => {
    console.info('Succeeded in subscribing. Get step value:' + ret.steps);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeStepCounter(subscribeStepCounterOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeStepCounter
**支持设备：** Wearable / lite_wearable

unsubscribeStepCounter(): void

取消订阅计步传感器。

除Lite Wearable外，从API Version8开始，推荐使用[PEDOMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#pedometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACTIVITY_MOTION

**示例**：


```ts
Sensor.unsubscribeStepCounter();
```


## Sensor.subscribeBarometer
**支持设备：** Wearable / lite_wearable

subscribeBarometer(options: SubscribeBarometerOptions): void

订阅气压计传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[BAROMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#barometerdeprecated-1)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeBarometerOptions](#subscribebarometeroptions) | 是 | 当气压计传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  BarometerResponse,
  SubscribeBarometerOptions,
} from '@kit.SensorServiceKit';

let subscribeBarometerOptions: SubscribeBarometerOptions = {
  success: (ret: BarometerResponse) => {
    console.info('Succeeded in subscribing. Get data value:' + ret.pressure);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeBarometer(subscribeBarometerOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeBarometer
**支持设备：** Wearable / lite_wearable

unsubscribeBarometer(): void

取消订阅气压计传感器。

除Lite Wearable外，从API Version8开始，推荐使用[BAROMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#barometerdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：


```ts
Sensor.unsubscribeBarometer();
```


## Sensor.subscribeHeartRate
**支持设备：** Wearable / lite_wearable

subscribeHeartRate(options: SubscribeHeartRateOptions): void

订阅心率传感器数据变化。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[HEART_RATE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#heart_ratedeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.READ_HEALTH_DATA

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeHeartRateOptions](#subscribeheartrateoptions) | 是 | 当心率传感器数据发生变化时调用。 |


**示例**：


```ts
import {
  Sensor,
  HeartRateResponse,
  SubscribeHeartRateOptions,
} from '@kit.SensorServiceKit';

let subscribeHeartRateOptions: SubscribeHeartRateOptions = {
  success: (ret: HeartRateResponse) => {
    console.info(
      'Succeeded in subscribing. Get heartRate value:' + ret.heartRate,
    );
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeHeartRate(subscribeHeartRateOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeHeartRate
**支持设备：** Wearable / lite_wearable

unsubscribeHeartRate(): void

取消订阅心率传感器。

除Lite Wearable外，从API Version8开始，推荐使用[HEART_RATE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#heart_ratedeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.READ_HEALTH_DATA

**示例**：


```ts
Sensor.unsubscribeHeartRate();
```


## Sensor.subscribeOnBodyState
**支持设备：** Wearable / lite_wearable

subscribeOnBodyState(options: SubscribeOnBodyStateOptions): void

订阅设备佩戴状态。针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效。

除Lite Wearable外，从API Version8开始，推荐使用[WEAR_DETECTION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#wear_detectiondeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeOnBodyStateOptions](#subscribeonbodystateoptions) | 是 | 当穿着状态改变时调用。 |


**示例**：


```ts
import {
  Sensor,
  OnBodyStateResponse,
  SubscribeOnBodyStateOptions,
} from '@kit.SensorServiceKit';

let subscribeOnBodyStateOptions: SubscribeOnBodyStateOptions = {
  success: (ret: OnBodyStateResponse) => {
    console.info(
      'Succeeded in subscribing. Get on-body state value:' + ret.value,
    );
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeOnBodyState(subscribeOnBodyStateOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeOnBodyState
**支持设备：** Wearable / lite_wearable

unsubscribeOnBodyState(): void

取消订阅设备佩戴状态。

除Lite Wearable外，从API Version8开始，推荐使用[WEAR_DETECTION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#wear_detectiondeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**示例**：


```ts
Sensor.unsubscribeOnBodyState();
```


## Sensor.getOnBodyState
**支持设备：** Wearable / lite_wearable

getOnBodyState(options: GetOnBodyStateOptions): void

获取设备佩戴状态。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetOnBodyStateOptions](#getonbodystateoptions) | 是 | 获取传感器所在设备穿戴状态时调用。 |


**示例**：


```ts
import {
  Sensor,
  OnBodyStateResponse,
  GetOnBodyStateOptions,
} from '@kit.SensorServiceKit';

let getOnBodyStateOptions: GetOnBodyStateOptions = {
  success: (ret: OnBodyStateResponse) => {
    console.info('Succeeded in subscribing. On body state: ' + ret.value);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.getOnBodyState(getOnBodyStateOptions);
```


## Sensor.subscribeDeviceOrientation6+
**支持设备：** Wearable / lite_wearable

subscribeDeviceOrientation(options: SubscribeDeviceOrientationOptions): void

观察设备方向传感器数据变化。

针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效；针对同一个方法内，不支持多次调用。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#orientationdeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeDeviceOrientationOptions](#subscribedeviceorientationoptions6) | 是 | 用于监听设备方向传感器数据的回调函数的执行频率。 |


**示例**：


```ts
import {
  Sensor,
  DeviceOrientationResponse,
  SubscribeDeviceOrientationOptions,
} from '@kit.SensorServiceKit';

let subscribeDeviceOrientationOptions: SubscribeDeviceOrientationOptions = {
  interval: 'normal',
  success: (ret: DeviceOrientationResponse) => {
    console.info('Succeeded in subscribing. Alpha data: ' + ret.alpha);
    console.info('Succeeded in subscribing. Beta data: ' + ret.beta);
    console.info('Succeeded in subscribing. Gamma data: ' + ret.gamma);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeDeviceOrientation(subscribeDeviceOrientationOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeDeviceOrientation6+
**支持设备：** Wearable / lite_wearable

unsubscribeDeviceOrientation(): void

取消订阅设备方向传感器数据。

除Lite Wearable外，从API Version8开始，推荐使用[ORIENTATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#orientationdeprecated-2)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。

**示例**：


```ts
Sensor.unsubscribeDeviceOrientation();
```


## Sensor.subscribeGyroscope6+
**支持设备：** Wearable / lite_wearable

subscribeGyroscope(options: SubscribeGyroscopeOptions): void

观察陀螺仪传感器数据变化。

针对同一个应用，多次点击调用时，会覆盖前面的调用效果，即仅最后一次调用生效；针对同一个方法内，不支持多次调用。

除Lite Wearable外，从API Version8开始，推荐使用[GYROSCOPE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#gyroscopedeprecated)。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.GYROSCOPE，该权限为系统权限

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeGyroscopeOptions](#subscribegyroscopeoptions6) | 是 | 用于侦听陀螺仪传感器数据的回调函数的执行频率。 |


**示例**：


```ts
import {
  Sensor,
  GyroscopeResponse,
  SubscribeGyroscopeOptions,
} from '@kit.SensorServiceKit';

let subscribeGyroscopeOptions: SubscribeGyroscopeOptions = {
  interval: 'normal',
  success: (ret: GyroscopeResponse) => {
    console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
    console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
    console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
  },
  fail: (data: string, code: number) => {
    console.error(`Failed to subscribe. Code: ${code}, data: ${data}`);
  },
};
Sensor.subscribeGyroscope(subscribeGyroscopeOptions);
```


> [!NOTE]
> 建议在页面销毁时，即onDestroy回调中，取消数据订阅，避免不必要的性能开销。


## Sensor.unsubscribeGyroscope6+
**支持设备：** Wearable / lite_wearable

unsubscribeGyroscope(): void

取消订阅陀螺仪传感器数据。

除Lite Wearable外，从API Version8开始，推荐使用[GYROSCOPE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor#gyroscopedeprecated-2)。

**系统能力**���SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.GYROSCOPE，该权限为系统权限

**示例**：


```ts
Sensor.unsubscribeGyroscope();
```


## subscribeAccelerometerOptions
**支持设备：** Wearable / lite_wearable

用于监听加速度传感器数据的回调函数的执行频率。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，加速度的回调函数执行频率。 默认为normal，可选值有： game：极高的回调频率，20ms/次，适用于游戏。 ui：较高的回调频率，60ms/次，适用于UI更新。 normal：普通的回调频率，200ms/次，低功耗。 |
| success | [AccelerometerResponse](#accelerometerresponse) | 是 | 感应到加速度数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## AccelerometerResponse
**支持设备：** Wearable / lite_wearable

感应到加速度数据变化后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**需要权限**：ohos.permission.ACCELEROMETER


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴的加速度。 |
| y | number | 是 | y轴的加速度。 |
| z | number | 是 | z轴的加速度。 |


## SubscribeCompassOptions
**支持设备：** Wearable / lite_wearable

当罗盘传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [CompassResponse](#compassresponse) | 是 | 罗盘数据改变后触发的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## CompassResponse
**支持设备：** Wearable / lite_wearable

罗盘数据改变后触发的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 设备面对的方向度数。 |


## SubscribeProximityOptions
**支持设备：** Wearable / lite_wearable

当距离传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [ProximityResponse](#proximityresponse) | 是 | 距离感应数据改变后调用的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## ProximityResponse
**支持设备：** Wearable / lite_wearable

距离感应数据改变后调用的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | number | 是 | 可见物体相对于设备显示屏的接近或远离状态。 |


## SubscribeLightOptions
**支持设备：** Wearable / lite_wearable

当环境光传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [LightResponse](#lightresponse) | 是 | 光线感应数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## LightResponse
**支持设备：** Wearable / lite_wearable

光线感应数据改变后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intensity | number | 是 | 光线强度，单位为lux。 |


## SubscribeStepCounterOptions
**支持设备：** Wearable / lite_wearable

当步进计数器传感器数据发生变化时调用。

**需要权限**：ohos.permission.ACTIVITY_MOTION

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [StepCounterResponse](#stepcounterresponse) | 是 | 计步传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## StepCounterResponse
**支持设备：** Wearable / lite_wearable

计步传感器数据改变后的回调函数。

**需要权限**：ohos.permission.ACTIVITY_MOTION

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| steps | number | 是 | 计步传感器重启后累计记录的步数。 |


## SubscribeBarometerOptions
**支持设备：** Wearable / lite_wearable

当气压计传感器数据发生变化时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [BarometerResponse](#barometerresponse) | 是 | 气压计传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## BarometerResponse
**支持设备：** Wearable / lite_wearable

气压计传感器数据改变后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pressure | number | 是 | 气压值，单位：帕斯卡。 |


## SubscribeHeartRateOptions
**支持设备：** Wearable / lite_wearable

当心率传感器数据发生变化时调用。

**需要权限**：ohos.permission.READ_HEALTH_DATA

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [HeartRateResponse](#heartrateresponse) | 是 | 心率传感器数据改变后的回调函数，默认频率5s/次。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## HeartRateResponse
**支持设备：** Wearable / lite_wearable

心率传感器数据改变后的回调函数，默认频率5s/次。

**需要权限**：ohos.permission.READ_HEALTH_DATA

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| heartRate | number | 是 | 心率值。 |


## SubscribeOnBodyStateOptions
**支持设备：** Wearable / lite_wearable

当传感器所在设备穿戴状态改变时调用，分为已穿戴和未穿戴。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [OnBodyStateResponse](#onbodystateresponse) | 是 | 传感器所在设备穿戴状态改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## OnBodyStateResponse
**支持设备：** Wearable / lite_wearable

传感器所在设备是否穿戴。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否已佩戴设备，当返回true表示已佩戴，否则未佩戴。 |


## GetOnBodyStateOptions
**支持设备：** Wearable / lite_wearable

获取传感器所在设备穿戴状态时调用。

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | [OnBodyStateResponse](#onbodystateresponse) | 是 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


## SubscribeDeviceOrientationOptions6+
**支持设备：** Wearable / lite_wearable

用于监听设备方向传感器数据的回调函数的执行频率。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，设备方向传感器的回调函数执行频率。 默认为normal，可选值有： - game：极高的回调频率，20ms/次，适用于游戏。 - ui：较高的回调频率，60ms/次，适用于UI更新。 - normal：普通的回调频率，200ms/次，低功耗。 |
| success | [DeviceOrientationResponse](#deviceorientationresponse6) | 是 | 感应到设备方向传感器数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## DeviceOrientationResponse6+
**支持设备：** Wearable / lite_wearable

感应到设备方向传感器数据变化后的回调函数。

**系统能力**：SystemCapability.Sensors.Sensor.Lite

**设备行为差异**：该接口在Lite Wearable中无效果，在其他设备类型中可正常调用。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | 当设备坐标 X/Y 和地球 X/Y 重合时，绕着 Z 轴转动的夹角为 alpha。 |
| beta | number | 是 | 当设备坐标 Y/Z 和地球 Y/Z 重合时，绕着 X 轴转动的夹角为 beta。 |
| gamma | number | 是 | 当设备 X/Z 和地球 X/Z 重合时，绕着 Y 轴转动的夹角为 gamma。 |


## SubscribeGyroscopeOptions6+
**支持设备：** Wearable / lite_wearable

用于侦听陀螺仪传感器数据的回调函数的执行频率。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | string | 是 | 频率参数，陀螺仪的回调函数执行频率。 默认为normal，可选值有： game：极高的回调频率，20ms/次，适用于游戏。 ui：较高的回调频率，60ms/次，适用于UI更新。 normal：普通的回调频率，200ms/次，低功耗。 |
| success | [GyroscopeResponse](#gyroscoperesponse6) | 是 | 感应到陀螺仪数据变化后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


## GyroscopeResponse6+
**支持设备：** Wearable / lite_wearable

感应到陀螺仪传感器数据变化后的回调函数。

**需要权限**：ohos.permission.GYROSCOPE

**系统能力**：SystemCapability.Sensors.Sensor.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴的旋转角速度。 |
| y | number | 是 | y轴的旋转角速度。 |
| z | number | 是 | z轴的旋转角速度。 |
