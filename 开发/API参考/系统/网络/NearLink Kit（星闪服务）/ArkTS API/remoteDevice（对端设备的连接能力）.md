# remoteDevice（对端设备的连接能力）

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-remote-device

支持设备：Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供了查询远端设备信息、发起配对等功能。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

#### 导入模块

```ts
import { remoteDevice } from '@kit.NearLinkKit';
```

#### PairingState
type PairingState = constant.PairingState
表示和远端设备的配对状态，为枚举值。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.PairingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#pairingstate) | 和远端设备的配对状态。 |

#### ConnectionState
type ConnectionState = constant.ConnectionState
表示和远端设备的连接状态，为枚举值。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#connectionstate) | 和远端设备的连接状态。 |

#### DeviceClass
type DeviceClass = constant.DeviceClass
表示设备类型，为枚举值。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.DeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#deviceclass) | 设备类型。 |

#### AcbState
type AcbState = constant.AcbState
表示和远端设备的逻辑链路连接状态，为枚举值。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.AcbState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#acbstate) | 和远端设备的逻辑链路连接状态。 |

#### createRemoteDevice
createRemoteDevice(address: string): RemoteDevice
创建远端设备实例。
**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 远端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RemoteDevice](#remotedevice) | 远端设备实例。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  console.info('device: ' + JSON.stringify(device));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### RemoteDevice

> [!NOTE] 说明
> 提供远端设备的操作方法，使用前需要使用remoteDevice.createRemoteDevice方法创建一个远端设备RemoteDevice实例。一个设备只需要创建一次，无需多次创建。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

#### startPairing
startPairing(): Promise&lt;void&gt;
发起与远端设备的配对。使用Promise异步回调。发起配对后，将依据本端与远端设备的输入输出能力标识弹出不同类型的弹窗，需使用者进一步确认。
**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

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

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  device.startPairing().then(()=>{
    console.info('start pairing success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getPairingState
getPairingState(): PairingState
获取和远端设备的配对状态。
**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PairingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#pairingstate) | 和远端设备的配对状态。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.PairingState = device.getPairingState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getDeviceName
getDeviceName(): string
获取远端设备名称。
**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 远端设备名称。最大长度为30。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let name: string = device.getDeviceName();
  console.info('state:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getDeviceClass
getDeviceClass(): DeviceClass
获取远端设备类型。
**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#deviceclass) | 远端设备类型。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let type: remoteDevice.DeviceClass = device.getDeviceClass();
  console.info('type:' + JSON.stringify(type));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getConnectionState
getConnectionState(): ConnectionState
获取本端设备和远端设备的连接状态。
**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#connectionstate) | 本端设备和远端设备的连接状态。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.ConnectionState = device.getConnectionState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getAcbState
getAcbState(): AcbState
获取和远端设备的逻辑链路连接状态。
**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AcbState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant#acbstate) | 和远端设备的逻辑链路连接状态。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.AcbState = device.getAcbState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getDeviceInformation
getDeviceInformation(): DeviceInformation
获取远端设备的设备信息。
**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceInformation](#deviceinformation) | 远端设备的设备信息。 |

**错误码：**
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |

**示例：**

```ts
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let deviceInfo: remoteDevice.DeviceInformation = device.getDeviceInformation();
  console.info('deviceInfo.manufacturerData:' + buffer.from(deviceInfo.manufacturerData, 'binary').toString('hex'));
  console.info('deviceInfo.modelData:' + buffer.from(deviceInfo.modelData, 'binary').toString('hex'));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### DeviceInformation
表示远端设备信息。
**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturerData | string | 否 | 否 | 厂商信息。 |
| modelData | string | 否 | 否 | 设备型号信息。 |
