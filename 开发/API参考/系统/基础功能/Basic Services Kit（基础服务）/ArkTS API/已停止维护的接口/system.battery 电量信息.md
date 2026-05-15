# @system.battery (电量信息)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-battery
**支持设备：** Wearable / lite_wearable

该模块提供充电状态及剩余电量的查询功能。


## 导入模块
**支持设备：** Wearable / lite_wearable


```text
import {Battery, BatteryResponse } from '@kit.BasicServicesKit';
```


## Battery.getStatus(deprecated)
**支持设备：** Wearable / lite_wearable

getStatus(options?: GetStatusOptions): void;

获取设备当前的充电状态及剩余电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetStatusOptions](#getstatusoptionsdeprecated) | 否 | 包含接口调用结果的对象。可选，默认为空。 |


**示例：**


```text
Battery.getStatus({
success: (data: BatteryResponse) => {
console.info('success get battery level:' + data.level);
},
fail: (data: string, code: number) => {
console.error('fail to get battery level code:' + code + ', data: ' + data);
}
});
```


## GetStatusOptions(deprecated)
**支持设备：** Wearable / lite_wearable

包含接口调用结果的对象。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Lite


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [BatteryResponse](#batteryresponsedeprecated)) =&gt; void | 否 | 接口调用成功的回调函数，data为[BatteryResponse](#batteryresponsedeprecated)类型的返回值。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |


## BatteryResponse(deprecated)
**支持设备：** Wearable / lite_wearable

包含充电状态及剩余电量的对象。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Lite


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| charging | boolean | 否 | 否 | 当前电池是否在充电中。true表示在充电，false表示没有充电，默认为false。 说明： 除Lite Wearable外，从API Version 6开始不再维护，建议使用[batteryInfo.chargingStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info#常量)替代。 |
| level | number | 否 | 否 | 当前电池的电量，取值范围：0.00 - 1.00 。  说明： 除Lite Wearable外，从API Version 6开始不再维护，建议使用[batteryInfo.batterySOC](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info#常量)替代。 |
