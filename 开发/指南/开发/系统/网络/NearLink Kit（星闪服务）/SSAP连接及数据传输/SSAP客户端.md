# SSAP客户端

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-ssap-client-connect

> [!NOTE]
> 提供SSAP（SparkLink Service Access Protocol）客户端相关的连接、数据传输和服务操作功能。



#### 场景介绍

提供设备作为客户端的能力，客户端可连接服务端进行数据传输。



#### 接口说明

| 接口名 | 描述 |
| --- | --- |
| createClient(address: string): Client | 创建ssap客户端实例。 |
| connect(): Promise&lt;void&gt; | 向服务端发起连接。 |
| getServices(): Promise<Array&lt;Service&gt;> | 获取服务端支持的服务列表。使用Promise异步回调。 |
| readProperty(property: Property): Promise&lt;Property&gt; | 读取服务端属性。使用Promise异步回调。 |
| writeProperty(property: Property, writeType: PropertyWriteType): Promise&lt;void&gt; | 写入服务端属性。使用Promise异步回调。 |
| setPropertyNotification(property: Property, enable: boolean): Promise&lt;void&gt; | 启用/禁用某个属性变化的通知。 |
| on(type: 'propertyChange', callback: Callback&lt;Property&gt;): void | 订阅属性变化事件。使用callback异步回调。 |
| on(type: 'connectionStateChange', callback: Callback&lt;ConnectionChangeState&gt;): void | 订阅连接状态变化事件。使用callback异步回调。 |




#### 开发步骤
1. 导入相关模块。

  
```text
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scan, ssap, dataTransfer, constant, remoteDevice } from '@kit.NearLinkKit';
```

2. 创建ssap客户端实例。其中参数addr是通过[扫描流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-scan)获取的远端设备地址。

  
```json
let client: ssap.Client;
@State chosenDeviceAddr: string = '00:11:22:33:AA:FF';
try {
  client = ssap.createClient(chosenDeviceAddr);
  hilog.info(this.domainId, this.logTag, `client: ${JSON.stringify(client)}`);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

3. 订阅连接状态变化事件。其中client对象在步骤2创建，后续步骤中使用的client对象也是一样，不再赘述。

  
```json
let connectionStateChangeCallback:(data: ssap.ConnectionChangeState) => void =
  (data: ssap.ConnectionChangeState) => {
  hilog.info(this.domainId, this.logTag, `Connection state: ${JSON.stringify(data)}`);
};
try {
  client.on('connectionStateChange', connectionStateChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

4. 订阅属性变化事件。

  
```json
let propertyChangeCallback:(data: ssap.Property) => void = (data: ssap.Property) => {
  hilog.info(this.domainId, this.logTag, `Property changed: ${JSON.stringify(data)}`);
  // ...
};
try {
  client.on('propertyChange', propertyChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

5. 向服务端发起连接。连接成功后会收到步骤3中订阅的连接状态变化的回调，之后可以进行数据交互。

  
```text
try {
  client.connect().then(() => {
    hilog.info(this.domainId, this.logTag, `Connect success`);
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

6. 获取服务端支持的服务列表。

  
```json
try {
  client.getServices().then((result: Array<ssap.Service>) => {
    // ...
    hilog.info(this.domainId, this.logTag, `Get services successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

7. 读取指定服务的属性值，参数property中的[serviceUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)以及[propertyUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)通过步骤6获取。

  
```json
const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';

let arrayBufferProperty = new ArrayBuffer(1);
let properV = new Uint8Array(arrayBufferProperty);
properV[0] = 1;
let property: ssap.Property = {
  serviceUuid: SERVICE_UUID,
  propertyUuid: PROPERTY_UUID,
  value: arrayBufferProperty
};
// ...
try {
  client.readProperty(property).then((result: ssap.Property) => {
    hilog.info(this.domainId, this.logTag, `Read property successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

8. 写入指定服务的属性值，参数property中的[serviceUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)以及[propertyUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)通过步骤6获取。

  
```text
try {
  let properValue = new Uint8Array(arrayBufferProperty);
  properValue[0] = 1;
  client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
    hilog.info(this.domainId, this.logTag, `Write property success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

9. 设置支持属性变化通知，参数property中的[serviceUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)以及[propertyUuid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap#property)通过步骤6获取。

  之后如果服务端属性值发生变化，则客户端通过步骤4订阅的事件接收新数据。

  
```text
try {
  client.setPropertyNotification(property, true).then(() => {
    hilog.info(this.domainId, this.logTag, `setPropertyNotification success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```




#### 示例代码

SSAP客户端功能可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/SsapClientPage.ets中的实现方法。
