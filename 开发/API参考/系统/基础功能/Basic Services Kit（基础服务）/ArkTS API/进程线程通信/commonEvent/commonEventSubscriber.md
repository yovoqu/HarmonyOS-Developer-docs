# commonEventSubscriber

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### CommonEventSubscriber

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示公共事件的订阅者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent



#### 使用说明

在使用CommonEventSubscriber的功能前，需要通过commonEventManager.createSubscriber获取subscriber对象。

```text
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};
// 创建订阅者
subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
```



#### getCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCode(callback: AsyncCallback&lt;number&gt;): void

获取有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数。返回有序公共事件传递的数据（number类型）。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
subscriber.getCode((err: BusinessError, code: number) => {
  if (err) {
    console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
});
```



#### getCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCode(): Promise&lt;number&gt;

获取有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回有序公共事件传递的数据（number类型）。 |


**示例：**

```json
subscriber.getCode().then((code: number) => {
  console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
});
```



#### getCodeSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCodeSync(): number

获取有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 表示有序公共事件传递的数据（number类型）。 |


**示例：**

```json
let code: number = subscriber.getCodeSync();
console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
```



#### setCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCode(code: number, callback: AsyncCallback&lt;void&gt;): void

设置有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置有序公共事件传递的数据（number类型）成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setCode(1, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting code.`);
});
```



#### setCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCode(code: number): Promise&lt;void&gt;

设置有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setCode(1).then(() => {
  console.info(`Succeeded in setting code.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
});
```



#### setCodeSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCodeSync(code: number): void

设置有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
try {
  subscriber.setCodeSync(1);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
}
```



#### getData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getData(callback: AsyncCallback&lt;string&gt;): void

获取有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数。返回有序公共事件传递的数据（string类型）。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
// 获取有序公共事件传递的数据（string类型）回调
subscriber.getData((err: BusinessError, data: string) => {
  if (err) {
    console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
});
```



#### getData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getData(): Promise&lt;string&gt;

获取有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回有序公共事件传递的数据（string类型）。 |


**示例：**

```json
subscriber.getData().then((data: string) => {
  console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
});
```



#### getDataSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDataSync(): string

获取有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 有序公共事件传递的数据（string类型）。 |


**示例：**

```text
let data: string = subscriber.getDataSync();
console.info(`Succeeded in getting data, data is ${data}`);
```



#### setData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setData(data: string, callback: AsyncCallback&lt;void&gt;): void

设置有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置有序公共事件传递的数据（string类型）成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setData('publish_data_changed', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting data.`);
});
```



#### setData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setData(data: string): Promise&lt;void&gt;

设置有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setData('publish_data_changed').then(() => {
  console.info(`Succeeded in setting data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
});
```



#### setDataSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDataSync(data: string): void

设置有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
try {
  subscriber.setDataSync('publish_data_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
}
```



#### setCodeAndData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCodeAndData(code: number, data: string, callback:AsyncCallback&lt;void&gt;): void

设置有序公共事件数据。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置有序公共事件传递的数据成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setCodeAndData(1, 'publish_data_changed', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting code and data.`);
});
```



#### setCodeAndData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCodeAndData(code: number, data: string): Promise&lt;void&gt;

设置有序公共事件传递的数据。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.setCodeAndData(1, 'publish_data_changed').then(() => {
  console.info(`Succeeded in setting code and data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
});
```



#### setCodeAndDataSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCodeAndDataSync(code: number, data: string): void

设置有序公共事件传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
try {
  subscriber.setCodeAndDataSync(1, 'publish_data_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
}
```



#### isOrderedCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isOrderedCommonEvent(callback: AsyncCallback&lt;boolean&gt;): void

查询当前公共事件是否为有序公共事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。返回true表示有序公共事件；返回false表示无序公共事件。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
subscriber.isOrderedCommonEvent((err: BusinessError, isOrdered:boolean) => {
  if (err) {
    console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
});
```



#### isOrderedCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isOrderedCommonEvent(): Promise&lt;boolean&gt;

查询当前公共事件是否为有序公共事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示有序公共事件；返回false表示无序公共事件。 |


**示例：**

```json
subscriber.isOrderedCommonEvent().then((isOrdered:boolean) => {
  console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
}).catch((err: BusinessError) => {
  console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
});
```



#### isOrderedCommonEventSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isOrderedCommonEventSync(): boolean

查询当前公共事件是否为有序公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示有序公共事件；返回false表示无序公共事件。 |


**示例：**

```json
let isOrdered: boolean = subscriber.isOrderedCommonEventSync();
console.info(`isOrderedCommonEventSync ${JSON.stringify(isOrdered)}`);
```



#### isStickyCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isStickyCommonEvent(callback: AsyncCallback&lt;boolean&gt;): void

检查当前公共事件是否为一个粘性事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
subscriber.isStickyCommonEvent((err: BusinessError, isSticky:boolean) => {
  if (err) {
    console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
});
```



#### isStickyCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isStickyCommonEvent(): Promise&lt;boolean&gt;

检查当前公共事件是否为一个粘性事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |


**示例：**

```json
subscriber.isStickyCommonEvent().then((isSticky:boolean) => {
  console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
}).catch((err: BusinessError) => {
  console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
});
```



#### isStickyCommonEventSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isStickyCommonEventSync(): boolean

检查当前公共事件是否为一个粘性事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |


**示例：**

```json
let isSticky: boolean = subscriber.isStickyCommonEventSync();
console.info(`isStickyCommonEventSync ${JSON.stringify(isSticky)}`);
```



#### abortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

abortCommonEvent(callback: AsyncCallback&lt;void&gt;): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当添加有序公共事件中止状态成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.abortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in aborting common event.`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```



#### abortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

abortCommonEvent(): Promise&lt;void&gt;

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**

```text
subscriber.abortCommonEvent().then(() => {
  console.info(`Succeeded in aborting common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```



#### abortCommonEventSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

abortCommonEventSync(): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```text
subscriber.abortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```



#### clearAbortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

clearAbortCommonEvent(callback: AsyncCallback&lt;void&gt;): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当清理有序公共事件中止状态成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.clearAbortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in clearing abort common event.`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```



#### clearAbortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

clearAbortCommonEvent(): Promise&lt;void&gt;

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**

```text
subscriber.clearAbortCommonEvent().then(() => {
  console.info(`Succeeded in clearing abort common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```



#### clearAbortCommonEventSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

clearAbortCommonEventSync(): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```text
subscriber.clearAbortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```



#### getAbortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAbortCommonEvent(callback: AsyncCallback&lt;boolean&gt;): void

获取当前有序公共事件是否处于中止状态。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
subscriber.getAbortCommonEvent((err: BusinessError, abortEvent: boolean) => {
  if (err) {
    console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
});
```



#### getAbortCommonEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAbortCommonEvent(): Promise&lt;boolean&gt;

获取当前有序公共事件是否处于中止状态。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |


**示例：**

```json
subscriber.getAbortCommonEvent().then((abortEvent: boolean) => {
  console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
});
```



#### getAbortCommonEventSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAbortCommonEventSync(): boolean

获取当前有序公共事件是否处于中止状态。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |


**示例：**

```json
let abortEvent: boolean = subscriber.getAbortCommonEventSync();
console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
```



#### getSubscribeInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSubscribeInfo(callback: AsyncCallback&lt;CommonEventSubscribeInfo&gt;): void

获取订阅者的订阅信息。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;CommonEventSubscribeInfo&gt; | 是 | 回调函数。返回订阅者的订阅信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```json
subscriber.getSubscribeInfo((err: BusinessError, subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  if (err) {
    console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
});
```



#### getSubscribeInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSubscribeInfo(): Promise&lt;CommonEventSubscribeInfo&gt;

获取订阅者的订阅信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CommonEventSubscribeInfo&gt; | Promise对象。返回订阅者的订阅信息。 |


**示例：**

```json
subscriber.getSubscribeInfo().then((subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
});
```



#### getSubscribeInfoSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSubscribeInfoSync(): CommonEventSubscribeInfo

获取订阅者的订阅信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CommonEventSubscribeInfo | 表示订阅者的订阅信息。 |


**示例：**

```json
let subscribeInfo1: commonEventManager.CommonEventSubscribeInfo = subscriber.getSubscribeInfoSync();
console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo1)}`);
```



#### finishCommonEvent9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

finishCommonEvent(callback: AsyncCallback&lt;void&gt;): void

用于订阅者结束对当前有序公共事件的处理。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当订阅者结束当前有序公共事件成功时，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |


**示例：**

```text
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```



#### finishCommonEvent9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

finishCommonEvent(): Promise&lt;void&gt;

用于订阅者结束对当前有序公共事件的处理。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**

```text
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```
