# @ohos.telephony.observer (observer)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-observer
**支持设备：** Phone | Tablet | Wearable

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | Tablet | Wearable

```text
import { observer } from '@kit.TelephonyKit';
```



#### NetworkState

**支持设备：** Phone | Tablet | Wearable

type NetworkState = radio.NetworkState

网络注册状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| radio.NetworkState | 网络注册状态。 |




#### SignalInformation

**支持设备：** Phone | Tablet | Wearable

type SignalInformation = radio.SignalInformation

网络信号强度信息对象。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| radio.SignalInformation | 网络信号强度信息对象。 |




#### DataConnectState

**支持设备：** Phone | Tablet | Wearable

type DataConnectState = data.DataConnectState

描述蜂窝数据链路连接状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| data.DataConnectState | 描述蜂窝数据链路连接状态。 |




#### RatType

**支持设备：** Phone | Tablet | Wearable

type RatType = radio.RadioTechnology

无线接入技术。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| radio.RadioTechnology | 无线接入技术。 |




#### DataFlowType

**支持设备：** Phone | Tablet | Wearable

type DataFlowType = data.DataFlowType

描述蜂窝数据流类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| data.DataFlowType | 描述蜂窝数据流类型。 |




#### CallState

**支持设备：** Phone | Tablet | Wearable

type CallState = call.CallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| call.CallState | 通话状态码（去电过程仅通知CALL_STATE_OFFHOOK状态）。 |




#### CCallState23+

**支持设备：** Phone | Tablet | Wearable

type CCallState = call.CCallState

运营商通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| call.CCallState | 通话状态码（运营商通话状态码）。 |




#### CardType

**支持设备：** Phone | Tablet | Wearable

type CardType = sim.CardType

卡类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| sim.CardType | 卡类型。 |




#### SimState

**支持设备：** Phone | Tablet | Wearable

type SimState = sim.SimState

SIM卡状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| sim.SimState | SIM卡状态。 |




#### TelCallState21+

**支持设备：** Phone | Tablet | Wearable

type TelCallState = call.TelCallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| call.TelCallState | 通话状态码（去电过程通知去电号码状态TEL_CALL_STATE_OFFHOOK和去电接通状态TEL_CALL_STATE_CONNECTED）。 |




#### observer.on('networkStateChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'networkStateChange', callback: Callback&lt;NetworkState&gt;): void

订阅网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| callback | Callback&lt;NetworkState&gt; | 是 | 回调函数，返回网络状态对象。参考radio的NetworkState。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
observer.on('networkStateChange', (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});
```



#### observer.on('networkStateChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'networkStateChange', options: ObserverOptions, callback: Callback&lt;NetworkState&gt;): void

订阅指定卡槽位的网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback&lt;NetworkState&gt; | 是 | 回调函数，返回网络状态对象。参考radio的NetworkState。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('networkStateChange', options, (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});
```



#### observer.off('networkStateChange')

**支持设备：** Phone | Tablet | Wearable

off(type: 'networkStateChange', callback?: Callback&lt;NetworkState&gt;): void

取消订阅网络状态变化事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| callback | Callback&lt;NetworkState&gt; | 否 | 回调函数，返回网络状态对象。参考radio的NetworkState。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let callback: (data: observer.NetworkState) => void = (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
}
observer.on('networkStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('networkStateChange', callback);
observer.off('networkStateChange');
```



#### observer.on('signalInfoChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'signalInfoChange', callback: Callback<Array&lt;SignalInformation&gt;>): void

订阅信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| callback | Callback<Array&lt;SignalInformation&gt;> | 是 | 回调函数，返回信号强度对象。参考radio的SignalInformation。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { radio } from '@kit.TelephonyKit';

observer.on('signalInfoChange', (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});
```



#### observer.on('signalInfoChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array&lt;SignalInformation&gt;>): void

订阅指定卡槽位的信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<Array&lt;SignalInformation&gt;> | 是 | 回调函数，返回信号强度对象。参考radio的SignalInformation。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { radio } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('signalInfoChange', options, (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});
```



#### observer.off('signalInfoChange')

**支持设备：** Phone | Tablet | Wearable

off(type: 'signalInfoChange', callback?: Callback<Array&lt;SignalInformation&gt;>): void

取消订阅信号状态变化事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| callback | Callback<Array&lt;SignalInformation&gt;> | 否 | 回调函数，返回信号强度对象。参考radio的SignalInformation。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { radio } from '@kit.TelephonyKit';

let callback: (data: Array<radio.SignalInformation>) => void = (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
}
observer.on('signalInfoChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('signalInfoChange', callback);
observer.off('signalInfoChange');
```



#### observer.on('callStateChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'callStateChange', callback: Callback&lt;CallStateInfo&gt;): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback&lt;CallStateInfo&gt; | 是 | 回调函数，返回通话状态信息对象。 应用可获取到CallStateInfo。 其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
observer.on('callStateChange', (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```



#### observer.on('callStateChange')

**支持设备：** Phone | Tablet | Wearable

on(type: 'callStateChange', options: ObserverOptions, callback: Callback&lt;CallStateInfo&gt;): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback&lt;CallStateInfo&gt; | 是 | 回调函数，返回通话状态信息对象。 应用可获取到CallStateInfo。 其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('callStateChange', options, (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```



#### observer.off('callStateChange')

**支持设备：** Phone | Tablet | Wearable

off(type: 'callStateChange', callback?: Callback&lt;CallStateInfo&gt;): void

取消订阅通话状态变化事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback&lt;CallStateInfo&gt; | 否 | 回调函数，返回通话状态信息对象。参考call的CallState。 number：电话号码。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let callback: (data: observer.CallStateInfo) => void = (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
}
observer.on('callStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('callStateChange', callback);
observer.off('callStateChange');
```



#### observer.on('callStateChangeEx')21+

**支持设备：** Phone | Tablet | Wearable

on(type: 'callStateChangeEx', callback: Callback&lt;TelCallState&gt;, options?: ObserverOptions): void

订阅通话状态变化拓展事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChangeEx'。 |
| callback | Callback&lt;TelCallState&gt; | 是 | 回调函数，返回通话状态对象。 应用可获取到TelCallState。 |
| options | ObserverOptions | 否 | 电话相关事件订阅参数可选项。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |


**示例：**

```json
import { call } from '@kit.TelephonyKit';

let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.on('callStateChangeEx', callback, options);
observer.on('callStateChangeEx', callback);
```



#### observer.off('callStateChangeEx')21+

**支持设备：** Phone | Tablet | Wearable

off(type: 'callStateChangeEx', callback?: Callback&lt;TelCallState&gt;): void

取消订阅通话状态变化拓展事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback&lt;TelCallState&gt; | 否 | 回调函数，返回通话状态对象。参考call的TelCallState。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |


**示例：**

```json
import { call } from '@kit.TelephonyKit';
let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
observer.on('callStateChangeEx', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('callStateChangeEx', callback);
observer.off('callStateChangeEx');
```



#### observer.on('cellularDataConnectionStateChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'cellularDataConnectionStateChange', callback: Callback&lt;DataConnectionStateInfo&gt;): void

订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| callback | Callback&lt;DataConnectionStateInfo&gt; | 是 | 回调函数，返回蜂窝数据链路连接状态信息对象。参考data的DataConnectState，radio的RadioTechnology。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
observer.on('cellularDataConnectionStateChange', (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```



#### observer.on('cellularDataConnectionStateChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'cellularDataConnectionStateChange', options: ObserverOptions, callback: Callback&lt;DataConnectionStateInfo&gt;): void

订阅指定卡槽位的蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback&lt;DataConnectionStateInfo&gt; | 是 | 回调函数，返回蜂窝数据链路连接状态信息对象。参考data的DataConnectState，radio的RadioTechnology。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataConnectionStateChange', options, (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```



#### observer.off('cellularDataConnectionStateChange')7+

**支持设备：** Phone | Tablet | Wearable

off(type: 'cellularDataConnectionStateChange', callback?: Callback&lt;DataConnectionStateInfo&gt;): void

移除订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| callback | Callback&lt;DataConnectionStateInfo&gt; | 否 | 回调函数，返回蜂窝数据链路连接状态信息对象。参考data的DataConnectState，radio的RadioTechnology。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let callback: (data: observer.DataConnectionStateInfo) => void = (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataConnectionStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('cellularDataConnectionStateChange', callback);
observer.off('cellularDataConnectionStateChange');
```



#### observer.on('cellularDataFlowChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'cellularDataFlowChange', callback: Callback&lt;DataFlowType&gt;): void

订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| callback | Callback&lt;DataFlowType&gt; | 是 | 回调函数，返回数据流状态对象。参考data的DataFlowType。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { data } from '@kit.TelephonyKit';

observer.on('cellularDataFlowChange', (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```



#### observer.on('cellularDataFlowChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback&lt;DataFlowType&gt;): void

订阅指定卡槽位的蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback&lt;DataFlowType&gt; | 是 | 回调函数，返回数据流状态对象。参考data的DataFlowType。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { data } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataFlowChange', options, (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```



#### observer.off('cellularDataFlowChange')7+

**支持设备：** Phone | Tablet | Wearable

off(type: 'cellularDataFlowChange', callback?: Callback&lt;DataFlowType&gt;): void

移除订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| callback | Callback&lt;DataFlowType&gt; | 否 | 回调函数，返回数据流状态对象。参考data的DataFlowType。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { data } from '@kit.TelephonyKit';

let callback: (data: data.DataFlowType) => void = (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataFlowChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('cellularDataFlowChange', callback);
observer.off('cellularDataFlowChange');
```



#### observer.on('simStateChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'simStateChange', callback: Callback&lt;SimStateData&gt;): void

订阅sim状态更改事件，使用callback方式作为异步方法。

> [!NOTE]
> 此接口不包含sim卡的激活状态，具体请参见 sim.isSimActive 接口。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| callback | Callback&lt;SimStateData&gt; | 是 | 回调函数，返回卡状态数据对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
observer.on('simStateChange', (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});
```



#### observer.on('simStateChange')7+

**支持设备：** Phone | Tablet | Wearable

on(type: 'simStateChange', options: ObserverOptions, callback: Callback&lt;SimStateData&gt;): void

订阅指定卡槽位的sim状态更改事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| options | ObserverOptions | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback&lt;SimStateData&gt; | 是 | 回调函数，返回卡状态数据对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('simStateChange', options, (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});
```



#### observer.off('simStateChange')7+

**支持设备：** Phone | Tablet | Wearable

off(type: 'simStateChange', callback?: Callback&lt;SimStateData&gt;): void

移除订阅sim状态更改事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| callback | Callback&lt;SimStateData&gt; | 否 | 回调函数，返回卡状态数据对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
let callback: (data: observer.SimStateData) => void = (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
}
observer.on('simStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('simStateChange', callback);
observer.off('simStateChange');
```



#### observer.on('iccAccountInfoChange')10+

**支持设备：** Phone | Tablet | Wearable

on(type: 'iccAccountInfoChange', callback: Callback&lt;void&gt;): void

订阅卡帐户变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 卡帐户变化事件，参数固定为'iccAccountInfoChange'。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数。当卡账户改变成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```text
observer.on('iccAccountInfoChange', () => {
    console.info("on iccAccountInfoChange success");
});
```



#### observer.off('iccAccountInfoChange')10+

**支持设备：** Phone | Tablet | Wearable

off(type: 'iccAccountInfoChange', callback?: Callback&lt;void&gt;): void

移除订阅卡帐户变化事件，使用callback方式作为异步方法。

> [!NOTE]
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。


**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 卡帐户变化事件，参数固定为'iccAccountInfoChange'。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数。当卡账户改变成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```text
let callback: () => void = () => {
    console.info("on iccAccountInfoChange success");
}
observer.on('iccAccountInfoChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('iccAccountInfoChange', callback);
observer.off('iccAccountInfoChange');
```



#### observer.onGetSimActiveState23+

**支持设备：** Phone | Tablet | Wearable

onGetSimActiveState(slotId: number, callback: Callback&lt;boolean&gt;): void

SIM卡激活状态变化的监听，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | Callback&lt;boolean&gt; | 是 | 回调函数，返回SIM卡是否激活。 - true：激活。 - false：未激活。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let sislotId = 0;
let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
    console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
}
observer.onGetSimActiveState(sislotId, simActiveState);
```



#### observer.offGetSimActiveState23+

**支持设备：** Phone | Tablet | Wearable

offGetSimActiveState(callback?: Callback&lt;boolean&gt;): void

取消SIM卡激活状态变化的监听，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 否 | 回调函数，返回SIM卡是否激活。 - true：激活。 - false：未激活。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
    console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
}
observer.offGetSimActiveState(simActiveState);
```



#### observer.onCCallStateChange23+

**支持设备：** Phone | Tablet | Wearable

onCCallStateChange(callback: Callback&lt;CCallStateInfo&gt;, options?: ObserverOptions): void

三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**需要权限**：ohos.permission.MANAGE_CALL_FOR_DEVICES

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;CCallStateInfo&gt; | 是 | 回调函数，返回通话状态信息对象。 应用可获取到CCallState。 |
| options | ObserverOptions | 否 | 电话相关事件订阅参数可选项。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |


**示例：**

```json
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.onCCallStateChange(callback, options);
observer.onCCallStateChange(callback);
```



#### observer.offCCallStateChange23+

**支持设备：** Phone | Tablet | Wearable

offCCallStateChange(callback?: Callback&lt;CCallStateInfo&gt;): void

取消三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**需要权限**：ohos.permission.MANAGE_CALL_FOR_DEVICES

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;CCallStateInfo&gt; | 否 | 回调函数，返回通话状态信息对象。 应用可获取到CCallState。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |


**示例：**

```json
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}

observer.offCCallStateChange(callback);
observer.offCCallStateChange();
```



#### LockReason8+

**支持设备：** Phone | Tablet | Wearable

SIM卡锁类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIM_NONE | 0 | 无锁。 |
| SIM_PIN | 1 | PIN锁。 |
| SIM_PUK | 2 | PUK锁。 |
| SIM_PN_PIN | 3 | 网络PIN锁。 |
| SIM_PN_PUK | 4 | 网络PUK锁。 |
| SIM_PU_PIN | 5 | 子网PIN锁。 |
| SIM_PU_PUK | 6 | 子网PUK锁。 |
| SIM_PP_PIN | 7 | 服务提供商PIN锁。 |
| SIM_PP_PUK | 8 | 服务提供商PUK锁。 |
| SIM_PC_PIN | 9 | 组织PIN锁。 |
| SIM_PC_PUK | 10 | 组织PUK锁。 |
| SIM_SIM_PIN | 11 | SIM PIN锁。 |
| SIM_SIM_PUK | 12 | SIM PUK锁。 |




#### SimStateData7+

**支持设备：** Phone | Tablet | Wearable

SIM卡类型和状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | CardType | 否 | 否 | SIM卡类型。 |
| state | SimState | 否 | 否 | SIM卡状态。 |
| reason8+ | LockReason | 否 | 否 | SIM卡锁类型。 |




#### CallStateInfo11+

**支持设备：** Phone | Tablet | Wearable

通话状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | CallState | 否 | 否 | 通话类型。 |
| number | string | 否 | 否 | 电话号码。 |




#### CCallStateInfo23+

**支持设备：** Phone | Tablet | Wearable

通话状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | CCallState | 否 | 否 | 通话类型。 |
| teleNumber | string | 否 | 否 | 电话号码。 |




#### DataConnectionStateInfo11+

**支持设备：** Phone | Tablet | Wearable

数据连接状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | DataConnectState | 否 | 否 | 数据连接状态。 |
| network | RatType | 否 | 否 | 网络类型。 |




#### ObserverOptions11+

**支持设备：** Phone | Tablet | Wearable

电话相关事件订阅参数可选项。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotId | number | 否 | 否 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
