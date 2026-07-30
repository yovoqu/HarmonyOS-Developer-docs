# @ohos.nearlink.manager (星闪开关能力)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-manager
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供了管理星闪基础能力，包括获取设备信息、订阅状态变化事件等。

**起始版本：** 26.0.0


#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { manager } from '@kit.ConnectivityKit';
```



#### manager.getState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getState(): NearlinkState

查询星闪开关状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NearlinkState | 表示星闪开关状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NearLink错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink-service)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |


**示例：**

```json
import { manager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let state: manager.NearlinkState = manager.getState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



#### manager.isNearLinkSupported

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isNearLinkSupported(): boolean

查询当前设备是否支持星闪服务。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前设备是否支持星闪。返回true：设备支持星闪。返回false：设备不支持星闪。 |


**示例：**

```text
import { manager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupported: boolean = manager.isNearLinkSupported();
  if (isSupported) {
    console.info('NearLink is supported on this device.');
  } else {
    console.info('NearLink is not supported on this device.');
  }
} catch (err) {
  console.error('Error occurred: ' + (err as BusinessError).code + ', ' + (err as BusinessError).message);
}
```



#### manager.getLocalName

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getLocalName(): string

查询本机星闪名称。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示星闪设备本地名称。最大长度为30。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NearLink错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink-service)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |


**示例：**

```json
import { manager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let name: string = manager.getLocalName();
  console.info('name:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



#### manager.getPairedDevices

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getPairedDevices(): string[]

获取与当前设备配对的设备列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 配对设备地址的列表。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NearLink错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink-service)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |


**示例：**

```json
import { manager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let pairedDevices: string[] = manager.getPairedDevices();
  if (pairedDevices.length > 0) {
        console.info('getPairedDevices return: ' + JSON.stringify(pairedDevices));
    } else {
        console.info('No Paired Devices found.');
    }
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



#### manager.onStateChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onStateChange(callback: Callback&lt;NearlinkState&gt;): void

订阅星闪开关状态变化事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;NearlinkState&gt; | 是 | 回调函数，返回星闪的开关状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NearLink错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink-service)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |


**示例：**

```text
import { manager } from '@kit.ConnectivityKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.NearlinkState> = (data: manager.NearlinkState) => {
  if (data === manager.NearlinkState.STATE_TURNING_ON) {
    console.info('nearlink STATE_TURNING_ON');
  } else if (data === manager.NearlinkState.STATE_ON) {
    console.info('nearlink STATE_ON');
  } else if (data === manager.NearlinkState.STATE_TURNING_OFF) {
    console.info('nearlink STATE_TURNING_OFF');
  } else if (data === manager.NearlinkState.STATE_OFF) {
    console.info('nearlink STATE_OFF');
  }
};
try {
  manager.onStateChange(callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



#### manager.offStateChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offStateChange(callback?: Callback&lt;NearlinkState&gt;): void

取消订阅星闪开关状态变化事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;NearlinkState&gt; | 否 | 回调函数，返回星闪的开关状态。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NearLink错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink-service)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |


**示例：**

```text
import { manager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.offStateChange();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



#### NearlinkState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

星闪的开关状态，为枚举值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_TURNING_ON | 0 | 表示星闪正在打开。 |
| STATE_ON | 1 | 表示星闪已打开。 |
| STATE_TURNING_OFF | 2 | 表示星闪正在关闭。 |
| STATE_OFF | 3 | 表示星闪已关闭。 |
