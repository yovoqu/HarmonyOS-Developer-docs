# ssap（星闪SSAP连接能力）

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供了SSAP（SparkLink Service Access Protocol）连接功能。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)


##### 导入模块

```text
import { ssap } from '@kit.NearLinkKit';
```



##### ConnectionState

type ConnectionState = constant.ConnectionState

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| constant.ConnectionState | 和远端设备的连接状态。 |




##### createClient

createClient(address: string): Client

创建ssap客户端实例。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 远端服务端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Client | ssap客户端实例。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr);
  console.info('client: ' + JSON.stringify(client));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### createServer

createServer(): Server

创建ssap服务端实例。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Server | ssap服务端实例。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  console.info('server: ' + JSON.stringify(server));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### Client

> [!NOTE]
> 提供和远端设备ssap数据交互操作方法，使用前需要使用 ssap.createClient 方法创建一个 Client 实例。 一个应用针对一个远端设备只需要创建一次实例。


**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)



##### connect

connect(): Promise&lt;void&gt;

向服务端发起连接。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### disconnect

disconnect(): Promise&lt;void&gt;

向服务端发起断连，断开已有连接或者终止正在建立的连接。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success'); // 建立连接
  });
  client.disconnect().then(() => {
    console.info('disconnect success'); // 断开连接
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### close

close(): void

关闭客户端。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.close();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### getServices

getServices(): Promise<Array&lt;Service&gt;>

获取服务端支持的服务列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise‌<‌Array‌<‌Service‌>‌> | Promise对象，返回服务端支持的服务列表。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
  // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
  setTimeout(() => {
    client.getServices().then((result: Array<ssap.Service>) => {
      console.info('getServices successfully:' + JSON.stringify(result));
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### readProperty

readProperty(property: Property): Promise&lt;Property&gt;

读取服务端属性。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | Property | 是 | 服务端属性。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Property&gt; | Promise对象，返回服务端属性。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
  // 创建property，实际开发时需要通过getServices接口从服务端获取
  let arrayBufferC = new ArrayBuffer(8);
  let properV = new Uint8Array(arrayBufferC);
  properV[0] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
  setTimeout(()=>{
    client.readProperty(property).then((result: ssap.Property) => {
      console.info('readProperty successfully:' + JSON.stringify(result));
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### writeProperty

writeProperty(property: Property, writeType: PropertyWriteType): Promise&lt;void&gt;

写入服务端property值。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | Property | 是 | 服务端属性。 |
| writeType | PropertyWriteType | 是 | 写类型，支持服务端回复响应和不回复响应两种方式。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
  // 创建property,实际开发时需要通过getServices接口从服务端获取
  let arrayBufferC = new ArrayBuffer(8);
  // 期望写入的property值
  let properV = new Uint8Array(arrayBufferC);
  properV[0] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
  setTimeout(()=>{
    client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
      console.info('writeProperty success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### setPropertyNotification

setPropertyNotification(property: Property, enable: boolean): Promise&lt;void&gt;

设置Property变化通知。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | Property | 是 | 服务端属性。 |
| enable | boolean | 是 | true: 打开通知功能。false: 关闭通知功能。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
  // 创建property,实际开发时需要通过getServices接口从服务端获取
  let arrayBufferC = new ArrayBuffer(8);
  // 期望写入的property值
  let properV = new Uint8Array(arrayBufferC);
  properV[0] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
  setTimeout(()=>{
    client.setPropertyNotification(property, true).then(() => {
      console.info('setPropertyNotification success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### requestMtuSize

requestMtuSize(mtu: number): Promise&lt;void&gt;

发起MTU协商请求。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | MTU参数，取值范围[22, 512]。默认值为256字节 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.connect().then(() => {
    console.info('connect success');
  });
  // 连接耗时较长，等待连接完成才能获取服务，实际开发者根据连接速度调整定时器长度
  setTimeout(()=>{
    client.requestMtuSize(128).then(() => {
      console.info('requestMtuSize success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'propertyChange')

on(type: 'propertyChange', callback: Callback&lt;Property&gt;): void

订阅Property变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyChange'，表示Property变化事件。 当client端收到server端属性内容变更的通知时，触发该事件。 |
| callback | Callback&lt;Property&gt; | 是 | 回调函数，返回服务的Property。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
  console.info('data:' + JSON.stringify(data));
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.on('propertyChange', onPropertyChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'propertyChange')

off(type: 'propertyChange', callback?: Callback&lt;Property&gt;): void

取消订阅属性变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyChange'，表示Property变化事件。 |
| callback | Callback&lt;Property&gt; | 否 | 回调函数，返回服务的Property。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
  console.info('data:' + JSON.stringify(data));
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.off('propertyChange', onPropertyChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'connectionStateChange')

on(type: 'connectionStateChange', callback: Callback&lt;ConnectionChangeState&gt;): void

订阅连接状态变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。 当client和server端之间的连接状态发生变化时，触发该事件。 当client端调用Client.connect或Client.disconnect时，可能引起连接状态生变化。 |
| callback | Callback&lt;ConnectionChangeState&gt; | 是 | 回调函数，返回连接状态上报参数。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:' + JSON.stringify(data));
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.on('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback&lt;ConnectionChangeState&gt;): void

取消订阅连接状态变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。 |
| callback | Callback&lt;ConnectionChangeState&gt; | 否 | 回调函数，返回连接状态上报参数。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:' + JSON.stringify(data));
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.off('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'mtuChange')

on(type: 'mtuChange', callback: Callback&lt;number&gt;): void

订阅MTU变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'mtuChange'，表示MTU变化事件。 当调用Client.requestMtuSize方法，client端发起MTU大小协商后，会触发该事件。 |
| callback | Callback&lt;number&gt; | 是 | 回调函数，返回协商后的MTU大小。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:' + data);
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.on('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'mtuChange')

off(type: 'mtuChange', callback?: Callback&lt;number&gt;): void

取消订阅MTU变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'mtuChange'，表示MTU变化事件。 |
| callback | Callback&lt;number&gt; | 否 | 回调函数，返回协商后的MTU大小。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:' + data);
}
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.off('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### Server

> [!NOTE]
> 提供和远端设备ssap数据交互操作方法，使用前需要使用createServer方法创建一个Server实例。 一个应用针对一个远端设备只需要创建一次实例。


**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)



##### addService

addService(service: Service): void

服务端添加服务。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | Service | 是 | 服务端提供的服务信息，支持添加多个服务，根据不同的UUID区分。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造descriptor
let descriptorsArray: Array<ssap.PropertyDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue[0] = 11;
descValue[1] = 22;
let descriptor: ssap.PropertyDescriptor = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBuffer,
  descriptorType: ssap.PropertyDescriptorType.PROPERTY,
  isWriteable: true
};
descriptorsArray[0] = descriptor;
// 构造properties
let propertiesArray: Array<ssap.Property> = [];
let arrayBufferProperty = new ArrayBuffer(8);
let properValue = new Uint8Array(arrayBufferProperty);
properValue[0] = 1;
let property1: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBufferProperty,
  descriptors:descriptorsArray
};
let property2: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000003421',
  value: arrayBufferProperty,
  descriptors:descriptorsArray,
  operation:12
};
propertiesArray[0] = property1;
propertiesArray[1] = property2;
// 构造服务
let Service: ssap.Service = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  properties:propertiesArray
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.addService(Service);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### removeService

removeService(serviceUuid: string): void

服务端删除服务。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 服务UUID，用户添加服务时的UUID号，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  // 服务已通过addService添加，可以通过指定UUID进行删除
  let serviceUuid = '37bea880-fc70-11ea-b720-000000004386';
  server.removeService(serviceUuid);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### close

close(): void

关闭服务端。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  server.close();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### notifyPropertyChanged

notifyPropertyChanged(address: string, property: Property): Promise&lt;void&gt;

通知客户端property值更新。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| property | Property | 是 | 发生值变化的Property。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造descriptor
let descriptorsArray: Array<ssap.PropertyDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue[0] = 11;
descValue[1] = 22;
let descriptor: ssap.PropertyDescriptor = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBuffer,
  descriptorType:ssap.PropertyDescriptorType.PROPERTY,
  isWriteable:true
};
descriptorsArray[0] = descriptor;
// 构造properties
let arrayBufferProperty = new ArrayBuffer(8);
let properValue = new Uint8Array(arrayBufferProperty);
properValue[0] = 123; // 本次更新后的值
let property: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBufferProperty,
  descriptors:descriptorsArray
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  // 地址是服务端缓存的已连接的客户端设备
  server.notifyPropertyChanged('00:11:22:33:AA:FF', property).then(() => {
    console.info('notifyPropertyChanged success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### sendResponse

sendResponse(response: ServerResponse): void

回复客户端读写请求。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | ServerResponse | 是 | 回复客户端的响应数据。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 订阅客户端的读写请求，收到请求后通过该接口回复
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue[0] = 11;
descValue[1] = 22;
let resp: ssap.ServerResponse = {
  address: '00:11:22:33:AA:FF', // 请求方的客户端地址
  requestId: 1, // 请求方传入
  value: arrayBuffer // 回复的数据
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  // 地址是服务端缓存的已连接的客户端设备
  server.sendResponse(resp);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on('connectionStateChange')

on(type: 'connectionStateChange', callback: Callback&lt;ConnectionChangeState&gt;): void

订阅连接状态变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。 当client和server端之间的连接状态发生变化时，触发该事件。 例如：收到连接请求或者断连请求时，可能引起连接状态发生变化。 |
| callback | Callback&lt;ConnectionChangeState&gt; | 是 | 回调函数，返回连接状态上报参数。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback&lt;ConnectionChangeState&gt;): void

取消订阅连接状态变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。 |
| callback | Callback&lt;ConnectionChangeState&gt; | 否 | 回调函数，返回连接状态上报参数。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'propertyRead')

on(type: 'propertyRead', callback: Callback&lt;PropertyReadRequest&gt;): void

订阅客户端的读属性请求事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyRead'，表示读属性请求事件。 当收到client端设备的读属性请求时，触发该事件。 |
| callback | Callback&lt;PropertyReadRequest&gt; | 是 | 回调函数，返回客户端的Property读请求参数。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('propertyRead', onPropertyReadRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'propertyRead')

off(type: 'propertyRead', callback?: Callback&lt;PropertyReadRequest&gt;): void

取消订阅客户端的读属性请求事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyRead'，表示读属性请求事件。 |
| callback | Callback&lt;PropertyReadRequest&gt; | 否 | 回调函数，返回客户端的Property读请求参数。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('propertyRead', onPropertyReadRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'propertyWrite')

on(type: 'propertyWrite', callback: Callback&lt;PropertyWriteRequest&gt;): void

订阅客户端的写属性请求事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyWrite'，表示写属性请求事件。 当收到client端设备的写属性请求时，触发该事件。 |
| callback | Callback&lt;PropertyWriteRequest&gt; | 是 | 回调函数，返回客户端的Property写请求参数。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('propertyWrite', onPropertyWriteRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'propertyWrite')

off(type: 'propertyWrite', callback?: Callback&lt;PropertyWriteRequest&gt;): void

取消订阅客户端的写属性请求事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'propertyWrite'，表示写属性请求事件。 |
| callback | Callback&lt;PropertyWriteRequest&gt; | 否 | 回调函数，返回客户端的Property写请求参数。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```json
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  console.info('data:' + JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('propertyWrite', onPropertyWriteRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### on( 'mtuChange')

on(type: 'mtuChange', callback: Callback&lt;number&gt;): void

订阅MTU（Maximum Transmission Unit）变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'mtuChange'，表示MTU变化事件。 当收到了client端发起了MTU协商请求时，触发该事件。 |
| callback | Callback&lt;number&gt; | 是 | 回调函数，返回协商后的MTU大小。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:' + data);
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### off( 'mtuChange')

off(type: 'mtuChange', callback?: Callback&lt;number&gt;): void

取消订阅MTU变化事件。使用callback异步回调。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'mtuChange'，表示MTU变化事件。 |
| callback | Callback&lt;number&gt; | 否 | 回调函数，返回协商后的MTU大小。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |


**示例：**

```text
import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:' + data);
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```



##### Service

表示星闪服务。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |
| properties | Array&lt;Property&gt; | 否 | 否 | 表示服务的Property列表。 |




##### Property

表示服务的Property。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示Property的数据值。 |
| descriptors | Array&lt;PropertyDescriptor&gt; | 否 | 是 | 表示当前Property的描述符列表。若未配置则默认不携带该字段。 |
| operation | number | 否 | 是 | 表示Property支持的操作方式，默认值为0，即不支持操作。如要使属性支持相应的操作，需要对该字段赋值，例如赋值为：READABLE\|WRITE_NO_RESPONSE。取值范围[0, 15]，各比特位对应的操作方式详见Operation。 |




##### PropertyDescriptor

表示Property的描述符。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示描述符的数据值。 |
| descriptorType | PropertyDescriptorType | 否 | 否 | 表示Property的描述符类型。 |
| isWriteable | boolean | 否 | 是 | 表示描述符是否是可写的。true：可写，false：不可写。默认值为true。 |




##### PropertyReadRequest

表示客户端的Property读请求参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| requestId | number | 否 | 否 | 表示请求ID。取值范围[0, 65535]。 |




##### PropertyWriteRequest

表示客户端的Property写请求参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| serviceUuid | string | 否 | 否 | 表示服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考星闪标准服务UUID。 |
| propertyUuid | string | 否 | 否 | 表示Property的UUID，数据格式同serviceUuid。 |
| value | ArrayBuffer | 否 | 否 | 表示客户端写入的值。 |
| requestId | number | 否 | 否 | 表示客户端的写请求ID，服务端回复响应时需携带该ID。取值范围[0, 65535]。 |
| writeType | PropertyWriteType | 否 | 否 | 表示客户端写Property类型。 |




##### ServerResponse

表示回复客户端请求的响应。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示客户端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| requestId | number | 否 | 否 | 表示请求ID。取值范围[0, 65535]。 |
| value | ArrayBuffer | 否 | 否 | 表示回复的数据值。 |




##### ConnectionChangeState

表示连接状态上报参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示远端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
| state | ConnectionState | 否 | 否 | 表示和远端设备的连接状态。 |




##### PropertyDescriptorType

表示Property的描述符类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROPERTY | 1 | 表示Property。 |
| CLIENT_PROPERTY_CONFIG | 2 | 表示客户端Property配置。 |
| SERVER_PROPERTY_CONFIG | 3 | 表示服务端Property配置。 |
| PROPERTY_FORMAT | 4 | 表示Property格式。 |
| TYPE_VENDOR | 255 | 表示厂商自定义字段。 |




##### Operation

表示Property支持的操作类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READABLE | 0x01 | 表示可读。 |
| WRITE_NO_RESPONSE | 0x02 | 表示支持无响应的写请求。 |
| WRITE_WITH_RESPONSE | 0x04 | 表示支持有响应的写请求。 |
| NOTIFY | 0x08 | 表示支持通知。 |




##### PropertyWriteType

表示Property支持的写类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WRITE | 1 | 表示写属性请求并等待服务端响应回复。 |
| WRITE_NO_RESPONSE | 2 | 表示写属性请求，无需服务端响应回复。 |
