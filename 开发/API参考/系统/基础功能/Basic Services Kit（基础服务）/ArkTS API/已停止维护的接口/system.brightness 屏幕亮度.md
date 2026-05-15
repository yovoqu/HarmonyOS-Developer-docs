# @system.brightness (屏幕亮度)

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-brightness
**支持设备：** Wearable / lite_wearable

该模块提供屏幕亮度和模式的查询、调节接口。


## 导入模块
**支持设备：** Wearable / lite_wearable


```text
import brightness, { BrightnessModeResponse, BrightnessResponse } from '@system.brightness';
```


## brightness.getValue(deprecated)
**支持设备：** Wearable / lite_wearable

getValue(options?: GetBrightnessOptions): void

获得设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetBrightnessOptions](#getbrightnessoptionsdeprecated) | 否 | 获取屏幕亮度的参数对象。可选，默认为空。 |


**示例：**


```text
brightness.getValue({
success: (data: BrightnessResponse) => {
console.info('success get brightness value:' + data.value);
},
fail: (data: string, code: number) => {
console.error('get brightness fail, code: ' + code + ', data: ' + data);
}
});
```


## brightness.setValue(deprecated)
**支持设备：** Wearable / lite_wearable

setValue(options?: SetBrightnessOptions): void

设置设备当前的屏幕亮度值。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetBrightnessOptions](#setbrightnessoptionsdeprecated) | 否 | 设置屏幕亮度的参数对象。可选，默认为空。 |


**示例：**


```text
brightness.setValue({
value: 100,
success: () => {
console.info('handling set brightness success.');
},
fail: (data: string, code: number) => {
console.error('handling set brightness value fail, code:' + code + ', data: ' + data);
}
});
```


## brightness.getMode(deprecated)
**支持设备：** Wearable / lite_wearable

getMode(options?: GetBrightnessModeOptions): void

获得当前屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetBrightnessModeOptions](#getbrightnessmodeoptionsdeprecated) | 否 | 获取屏幕亮度模式的参数对象。可选，默认为空。 |


**示例：**


```text
brightness.getMode({
success: (data: BrightnessModeResponse) => {
console.info('success get mode:' + data.mode);
},
fail: (data: string, code: number) => {
console.error('handling get mode fail, code:' + code + ', data: ' + data);
}
});
```


## brightness.setMode(deprecated)
**支持设备：** Wearable / lite_wearable

setMode(options?: SetBrightnessModeOptions): void

设置设备当前的屏幕亮度模式。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetBrightnessModeOptions](#setbrightnessmodeoptionsdeprecated) | 否 | 设置屏幕亮度模式的参数对象。可选，默认为空。 |


**示例：**


```text
brightness.setMode({
mode: 1,
success: () => {
console.info('handling set mode success.');
},
fail: (data: string, code: number) => {
console.error('handling set mode fail, code:' + code + ', data: ' + data);
}
});
```


## brightness.setKeepScreenOn(deprecated)
**支持设备：** Wearable / lite_wearable

setKeepScreenOn(options?: SetKeepScreenOnOptions): void

除Lite Wearable外，从API version 7开始不再维护，建议使用[window.setWindowKeepScreenOn()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowkeepscreenon9)替代。

设置屏幕是否保持常亮状态，开启常亮模式推荐在onShow()阶段调用。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Wz98pg-fRp-lViq-9rCoyA/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084645Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FC41D519CAF9371CA79F939AFB86E4200CF9B20337EEA80BB50979F831433CF)
在Lite Wearable上，该接口仅能阻止系统无活动超时灭屏（自动），无法阻止用户主动操作（如盖屏）、常亮时刻结束等导致的灭屏。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SetKeepScreenOnOptions](#setkeepscreenonoptionsdeprecated) | 否 | 设置屏幕常亮的参数对象。可选，默认为空。 |


**示例：**


```text
brightness.setKeepScreenOn({
keepScreenOn: true,
success: () => {
console.info('handling set keep screen on success.');
},
fail: (data: string, code: number) => {
console.error('handling set keep screen on fail, code:' + code + ', data: ' + data);
}
});
```


## GetBrightnessOptions(deprecated)
**支持设备：** Wearable / lite_wearable

获取屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [BrightnessResponse](#brightnessresponsedeprecated)) =&gt; void | 否 | 接口调用成功的回调函数。data为[BrightnessResponse](#brightnessresponsedeprecated)类型的返回值。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |


## SetBrightnessOptions(deprecated)
**支持设备：** Wearable / lite_wearable

设置屏幕亮度的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 屏幕亮度，值为1-255之间的整数。          - 如果值小于等于0，系统按1处理。          - 如果值大于255，系统按255处理。          - 如果值为小数，系统将处理为整数。例如设置为8.1，系统按8处理。 |
| success | () =&gt; void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |


## BrightnessResponse(deprecated)
**支持设备：** Wearable / lite_wearable

包含屏幕亮度的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 是 | 否 | 屏幕亮度，范围：1到255。 |


## GetBrightnessModeOptions(deprecated)
**支持设备：** Wearable / lite_wearable

获取屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [BrightnessModeResponse](#brightnessmoderesponsedeprecated)) =&gt; void | 否 | 接口调用成功的回调函数。data为[BrightnessModeResponse](#brightnessmoderesponsedeprecated)类型的返回值。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |


## SetBrightnessModeOptions(deprecated)
**支持设备：** Wearable / lite_wearable

设置屏幕亮度模式的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | number | 是 | 0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。 |
| success | () =&gt; void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |


## BrightnessModeResponse(deprecated)
**支持设备：** Wearable / lite_wearable

包含屏幕亮度模式的对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| mode | number | 是 | 否 | 0表示手动调节屏幕亮度模式，1表示自动调节屏幕亮度模式。 |


## SetKeepScreenOnOptions(deprecated)
**支持设备：** Wearable / lite_wearable

设置屏幕常亮的参数对象。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepScreenOn | boolean | 是 | true表示保持屏幕常亮，false表示取消屏幕常亮。 |
| success | () =&gt; void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) =&gt; void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () =&gt; void | 否 | 接口调用结束的回调函数。 |
