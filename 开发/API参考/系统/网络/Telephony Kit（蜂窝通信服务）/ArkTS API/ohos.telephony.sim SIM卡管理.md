# @ohos.telephony.sim (SIM卡管理)

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim
**支持设备：** Phone | Tablet | Wearable

SIM卡管理模块提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | Tablet | Wearable

```text
import { sim } from '@kit.TelephonyKit';
```



#### sim.isSimActive7+

**支持设备：** Phone | Tablet | Wearable

isSimActive(slotId: number, callback: AsyncCallback&lt;boolean&gt;): void

获取指定卡槽SIM卡是否激活。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。返回指定卡槽是否激活。 - true:激活。 - false：未激活。 |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.isSimActive7+

**支持设备：** Phone | Tablet | Wearable

isSimActive(slotId: number): Promise&lt;boolean&gt;

获取指定卡槽SIM卡是否激活。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | 以Promise形式返回指定卡槽是否激活。 - true:激活。 - false：未激活。 |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0).then((data: boolean) => {
    console.info(`isSimActive success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isSimActive failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.isSimActiveSync10+

**支持设备：** Phone | Tablet | Wearable

isSimActiveSync(slotId: number): boolean

获取指定卡槽SIM卡是否激活。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定卡槽是否激活。 - true:激活。 - false：未激活。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(`the sim is active:` + isSimActive);
```



#### sim.getDefaultVoiceSlotId7+

**支持设备：** Phone | Tablet | Wearable

getDefaultVoiceSlotId(callback: AsyncCallback&lt;number&gt;): void

获取默认语音业务的卡槽ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。 - 0：卡槽1。 - 1：卡槽2。 - -1：未设置或服务不可用。 |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getDefaultVoiceSlotId7+

**支持设备：** Phone | Tablet | Wearable

getDefaultVoiceSlotId(): Promise&lt;number&gt;

获取默认语音业务的卡槽ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | 以Promise形式返回默认语音业务的卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 - -1：未设置或服务不可用。 |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId().then((data: number) => {
    console.info(`getDefaultVoiceSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.hasOperatorPrivileges7+

**支持设备：** Phone | Tablet | Wearable

hasOperatorPrivileges(slotId: number, callback: AsyncCallback&lt;boolean&gt;): void

检查应用(调用者)是否已被授予运营商权限。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。 返回检查应用（调用者）是否已被授予运营商权限。 - true：授权。 - false：未授权（未插入SIM卡或停用）。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.hasOperatorPrivileges7+

**支持设备：** Phone | Tablet | Wearable

hasOperatorPrivileges(slotId: number): Promise&lt;boolean&gt;

检查应用(调用者)是否已被授予运营商权限。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | 以Promise形式返回检查应用(调用者)是否已被授予运营商权限。 - true：授权。 - false：未授权（未插入SIM卡或停用）。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0).then((data: boolean) => {
    console.info(`hasOperatorPrivileges success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`hasOperatorPrivileges failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getISOCountryCodeForSim

**支持设备：** Phone | Tablet | Wearable

getISOCountryCodeForSim(slotId: number, callback: AsyncCallback&lt;string&gt;): void

获取指定卡槽SIM卡的ISO国家码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。返回国家码，例如：CN(中国)。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getISOCountryCodeForSim

**支持设备：** Phone | Tablet | Wearable

getISOCountryCodeForSim(slotId: number): Promise&lt;string&gt;

获取指定卡槽SIM卡的ISO国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 以Promise形式返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0).then((data: string) => {
    console.info(`getISOCountryCodeForSim success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getISOCountryCodeForSim failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getISOCountryCodeForSimSync10+

**支持设备：** Phone | Tablet | Wearable

getISOCountryCodeForSimSync(slotId: number): string

获取指定卡槽SIM卡的ISO国家码。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let countryCode: string = sim.getISOCountryCodeForSimSync(0);
console.info(`the country ISO is:` + countryCode);
```



#### sim.getSimOperatorNumeric

**支持设备：** Phone | Tablet | Wearable

getSimOperatorNumeric(slotId: number, callback: AsyncCallback&lt;string&gt;): void

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。返回指定卡槽SIM卡的归属PLMN号。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getSimOperatorNumeric

**支持设备：** Phone | Tablet | Wearable

getSimOperatorNumeric(slotId: number): Promise&lt;string&gt;

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 以Promise形式返回获取指定卡槽SIM卡的归属PLMN号。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0).then((data: string) => {
    console.info(`getSimOperatorNumeric success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimOperatorNumeric failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getSimOperatorNumericSync10+

**支持设备：** Phone | Tablet | Wearable

getSimOperatorNumericSync(slotId: number): string

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的归属PLMN号。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(`the sim operator numeric is:` + numeric);
```



#### sim.getSimSpn

**支持设备：** Phone | Tablet | Wearable

getSimSpn(slotId: number, callback: AsyncCallback&lt;string&gt;): void

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。返回指定卡槽SIM卡的SPN。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getSimSpn

**支持设备：** Phone | Tablet | Wearable

getSimSpn(slotId: number): Promise&lt;string&gt;

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 以Promise形式返回获取指定卡槽SIM卡的SPN。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0).then((data: string) => {
    console.info(`getSimSpn success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimSpn failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getSimSpnSync10+

**支持设备：** Phone | Tablet | Wearable

getSimSpnSync(slotId: number): string

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的SPN。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let spn: string = sim.getSimSpnSync(0);
console.info(`the sim card spn is:` + spn);
```



#### sim.getSimState

**支持设备：** Phone | Tablet | Wearable

getSimState(slotId: number, callback: AsyncCallback&lt;SimState&gt;): void

获取指定卡槽的SIM卡状态。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;SimState&gt; | 是 | 回调函数。参考SimState。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0, (err: BusinessError, data: sim.SimState) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getSimState

**支持设备：** Phone | Tablet | Wearable

getSimState(slotId: number): Promise&lt;SimState&gt;

获取指定卡槽的SIM卡状态。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;SimState&gt; | 以Promise形式返回获取指定卡槽的SIM卡状态。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0).then((data: sim.SimState) => {
    console.info(`getSimState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getSimStateSync10+

**支持设备：** Phone | Tablet | Wearable

getSimStateSync(slotId: number): SimState

获取指定卡槽的SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| SimState | 返回获取指定卡槽的SIM卡状态。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```



#### sim.getCardType7+

**支持设备：** Phone | Tablet | Wearable

getCardType(slotId: number, callback: AsyncCallback&lt;CardType&gt;): void

获取指定卡槽SIM卡的卡类型。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;CardType&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0, (err: BusinessError, data: sim.CardType) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getCardType7+

**支持设备：** Phone | Tablet | Wearable

getCardType(slotId: number): Promise&lt;CardType&gt;

获取指定卡槽SIM卡的卡类型。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CardType&gt; | 以Promise形式返回指定卡槽SIM卡的卡类型。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0).then((data: sim.CardType) => {
    console.info(`getCardType success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCardType failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getCardTypeSync10+

**支持设备：** Phone | Tablet | Wearable

getCardTypeSync(slotId: number): CardType

获取指定卡槽SIM卡的卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| CardType | 返回指定卡槽SIM卡的卡类型。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(`the card type is:` + cardType);
```



#### sim.hasSimCard7+

**支持设备：** Phone | Tablet | Wearable

hasSimCard(slotId: number, callback: AsyncCallback&lt;boolean&gt;): void

获取指定卡槽SIM卡是否插卡。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调返回指定卡槽是否插卡。 - true:插卡。 - false：未插卡。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.hasSimCard7+

**支持设备：** Phone | Tablet | Wearable

hasSimCard(slotId: number): Promise&lt;boolean&gt;

获取指定卡槽SIM卡是否插卡。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | 以Promise形式返回指定卡槽是否插卡。 - true:插卡。 - false：未插卡。 |


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
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0).then((data: boolean) => {
    console.info(`hasSimCard success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`hasSimCard failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.hasSimCardSync10+

**支持设备：** Phone | Tablet | Wearable

hasSimCardSync(slotId: number): boolean

获取指定卡槽SIM卡是否插卡。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定卡槽是否插卡。 - true:插卡。 - false：未插卡。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

let hasSimCard: boolean = sim.hasSimCardSync(0);
console.info(`has sim card: ` + hasSimCard);
```



#### sim.getSimAccountInfo10+

**支持设备：** Phone | Tablet | Wearable

getSimAccountInfo(slotId: number, callback: AsyncCallback&lt;IccAccountInfo&gt;): void

获取SIM卡账户信息。使用callback异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

> [!NOTE]
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。


**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;IccAccountInfo&gt; | 是 | 回调函数。返回指定卡槽SIM卡的账户信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getSimAccountInfo10+

**支持设备：** Phone | Tablet | Wearable

getSimAccountInfo(slotId: number): Promise&lt;IccAccountInfo&gt;

获取SIM卡账户信息。使用Promise异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

> [!NOTE]
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。


**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;IccAccountInfo&gt; | 以Promise形式返回指定卡槽SIM卡的账户信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
    console.info(`getSimAccountInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getActiveSimAccountInfoList10+

**支持设备：** Phone | Tablet | Wearable

getActiveSimAccountInfoList(callback: AsyncCallback<Array&lt;IccAccountInfo&gt;>): void

获取激活SIM卡账户信息列表。使用callback异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

> [!NOTE]
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。


**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array&lt;IccAccountInfo&gt;> | 是 | 回调函数。返回激活SIM卡账户信息列表。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getMaxSimCount7+

**支持设备：** Phone | Tablet | Wearable

getMaxSimCount(): number

获取卡槽数量。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 卡槽数量。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```



#### sim.getActiveSimAccountInfoList10+

**支持设备：** Phone | Tablet | Wearable

getActiveSimAccountInfoList(): Promise<Array&lt;IccAccountInfo&gt;>

获取激活SIM卡账户信息列表。使用Promise异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

> [!NOTE]
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。


**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;IccAccountInfo&gt;> | 以Promise形式返回激活卡槽SIM卡的账户信息列表。 |


**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
    console.info(`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getOpKey9+

**支持设备：** Phone | Tablet | Wearable

getOpKey(slotId: number, callback: AsyncCallback&lt;string&gt;): void

获取指定卡槽中SIM卡的opkey。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpKey(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpKey failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpKey successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpKey err: " + JSON.stringify(err));
}
```



#### sim.getOpKey9+

**支持设备：** Phone | Tablet | Wearable

getOpKey(slotId: number): Promise&lt;string&gt;

获取指定卡槽中SIM卡的opkey。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 以Promise形式返回指定卡槽中SIM卡的opkey。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpKey(0).then((data: string) => {
    console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOpKey failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getOpKeySync10+

**支持设备：** Phone | Tablet | Wearable

getOpKeySync(slotId: number): string

获取指定卡槽中SIM卡的opkey。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定卡槽中SIM卡的opkey。 |


**示例：**

```json
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpKeySync(0);
console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
```



#### sim.getOpName9+

**支持设备：** Phone | Tablet | Wearable

getOpName(slotId: number, callback: AsyncCallback&lt;string&gt;): void

获取指定卡槽中SIM卡的OpName。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpName(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpName failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpName successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpName err: " + JSON.stringify(err));
}
```



#### sim.getOpName9+

**支持设备：** Phone | Tablet | Wearable

getOpName(slotId: number): Promise&lt;string&gt;

获取指定卡槽中SIM卡的OpName。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 以Promise形式返回指定卡槽中SIM卡的OpName。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpName(0).then((data: string) => {
    console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOpName failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getOpNameSync10+

**支持设备：** Phone | Tablet | Wearable

getOpNameSync(slotId: number): string

获取指定卡槽中SIM卡的OpName。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定卡槽中SIM卡的OpName。 |


**示例：**

```json
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpNameSync(0);
console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
```



#### sim.getDefaultVoiceSimId10+

**支持设备：** Phone | Tablet | Wearable

getDefaultVoiceSimId(callback: AsyncCallback&lt;number&gt;): void

获取默认语音业务的SIM卡ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。 与SIM卡绑定，从1开始递增。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getDefaultVoiceSimId10+

**支持设备：** Phone | Tablet | Wearable

getDefaultVoiceSimId(): Promise&lt;number&gt;

获取默认语音业务的SIM卡ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | 以Promise形式返回默认语音业务的SIM卡ID。 与SIM卡绑定，从1开始递增。 |


**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let promise = sim.getDefaultVoiceSimId();
promise.then((data: number) => {
    console.info(`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getSimLabel20+

**支持设备：** Phone | Tablet | Wearable

getSimLabel(slotId: number, callback: AsyncCallback&lt;SimLabel&gt;): void

查看卡槽ID和SIM卡的对应关系：

 - 卡槽1对应SIM卡1或SIM卡2
 - 卡槽2对应SIM卡2或ESIMX


**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |
| callback | AsyncCallback&lt;SimLabel&gt; | 是 | 回调函数。获取SIM卡标签信息。 |


**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0, (err: BusinessError, data: sim.SimLabel) => {
  console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```



#### sim.getSimLabel20+

**支持设备：** Phone | Tablet | Wearable

getSimLabel(slotId: number): Promise&lt;SimLabel&gt;

获取SIM卡的标签信息。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SimLabel > | 回调函数。获取SIM卡标签信息。 |


**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0).then((data: sim.SimLabel) => {
  console.info(`getSimLabel success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
});
```



#### sim.getSimLabelSync20+

**支持设备：** Phone | Tablet | Wearable

getSimLabelSync(slotId: number): SimLabel

通过传入SIM卡槽的ID，获取对应的SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。 - 0：卡槽1。 - 1：卡槽2。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| SimLabel | SIM卡标签。 |


**示例：**

```text
import { sim } from '@kit.TelephonyKit';


let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
console.info(`The sim state is:` + simLabel);
```



#### SimType20+

**支持设备：** Phone | Tablet | Wearable

SIM卡类型的枚举。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PSIM | 0 | 实体SIM卡。 |
| ESIM | 1 | 电子SIM卡。 |




#### SimLabel20+

**支持设备：** Phone | Tablet | Wearable

SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| simType | SimType | 否 | 否 | 表示SIM卡类型的枚举。 |
| index | number | 否 | 否 | SIM卡的唯一标识索引值。 |




#### SimState

**支持设备：** Phone | Tablet | Wearable

SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIM_STATE_UNKNOWN | 0 | SIM卡状态未知，即无法获取准确的状态。 |
| SIM_STATE_NOT_PRESENT | 1 | 表示SIM卡处于not present状态，即卡槽中没有插入SIM卡。 |
| SIM_STATE_LOCKED | 2 | 表示SIM卡处于locked状态，即SIM卡被PIN、PUK或网络锁锁定。 |
| SIM_STATE_NOT_READY | 3 | 表示SIM卡处于not ready状态，即SIM卡在位但无法正常工作。 |
| SIM_STATE_READY | 4 | 表示SIM卡处于ready状态，即SIM卡在位且工作正常。 |
| SIM_STATE_LOADED | 5 | 表示SIM卡处于loaded状态，即SIM卡在位且所有卡文件加载完毕。 |




#### CardType7+

**支持设备：** Phone | Tablet | Wearable

卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN_CARD | -1 | 未知类型。 |
| SINGLE_MODE_SIM_CARD | 10 | 单SIM卡。 |
| SINGLE_MODE_USIM_CARD | 20 | 单USIM卡。 |
| SINGLE_MODE_RUIM_CARD | 30 | 单RUIM卡。 |
| DUAL_MODE_CG_CARD | 40 | 双卡模式C+G。 |
| CT_NATIONAL_ROAMING_CARD | 41 | 中国电信内部漫游卡。 |
| CU_DUAL_MODE_CARD | 42 | 中国联通双模卡。 |
| DUAL_MODE_TELECOM_LTE_CARD | 43 | 双模式电信LTE卡。 |
| DUAL_MODE_UG_CARD | 50 | 双模式UG卡。 |
| SINGLE_MODE_ISIM_CARD8+ | 60 | 单一ISIM卡类型。 |




#### IccAccountInfo10+

**支持设备：** Phone | Tablet | Wearable

Icc账户信息。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| simId | number | 否 | 否 | SIM卡ID。 |
| slotIndex | number | 否 | 否 | 卡槽ID。 |
| isEsim | boolean | 否 | 否 | 标记卡是否是eSim。 - true:是eSim。 - false：不是eSim。 |
| isActive | boolean | 否 | 否 | 卡是否被激活。 - true:激活。 - false：未激活。 |
| iccId | string | 否 | 否 | ICCID号码。 |
| showName | string | 否 | 否 | SIM卡显示名称。 |
| showNumber | string | 否 | 否 | SIM卡显示号码。 |
