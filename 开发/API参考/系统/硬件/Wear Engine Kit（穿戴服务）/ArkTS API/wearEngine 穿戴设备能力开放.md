# wearEngine (穿戴设备能力开放)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api
**支持设备：** Phone | Tablet | Wearable

本模块提供手机与穿戴设备侧的交互能力。应用可调用模块内接口实现如下功能：

 - 获取与当前设备已连接配对的设备列表、与对端设备互通消息互送文件等。
 - 查询穿戴设备状态、向穿戴设备发送模板化通知、接收穿戴设备传感器的相关数据等。


> [!NOTE]
> 针对系统能力SystemCapability.Health.WearEngine，请先使用 canIUse() 接口判断当前设备是否支持此syscap及对应接口。


**起始版本**：5.0.0(12)


##### 导入模块

**支持设备：** Phone | Tablet | Wearable

```text
import { wearEngine } from '@kit.WearEngine';
```



##### wearEngine.getAuthClient

**支持设备：** Phone | Tablet | Wearable

getAuthClient(context: common.Context): AuthClient

用于获取权限管理的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| AuthClient | 权限管理客户端，存储了权限模块的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting auth client`);
```



##### AuthClient

**支持设备：** Phone | Tablet | Wearable

权限管理客户端类，由[wearEngine.getAuthClient](#wearenginegetauthclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### requestAuthorization

**支持设备：** Phone | Tablet | Wearable

requestAuthorization(request: AuthorizationRequest): Promise&lt;AuthorizationResponse&gt;

向手机用户申请需要授权的权限，返回申请的权限中用户已授权的权限，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | AuthorizationRequest | 是 | 权限请求类。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AuthorizationResponse&gt; | Promise对象，返回权限响应类。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

let request: wearEngine.AuthorizationRequest = {
  permissions: [wearEngine.Permission.USER_STATUS]
}

authClient.requestAuthorization(request).then(result => {
  console.info(`Succeeded in requesting authorize, authorized permissions is ${result.permissions}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to request authorize. Code is ${error.code}, message is ${error.message}`);
})
```



##### getAuthorization

**支持设备：** Phone | Tablet | Wearable

getAuthorization(): Promise&lt;AuthorizationResponse&gt;

获取用户已授权的权限，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AuthorizationResponse&gt; | Promise对象，返回权限响应类。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1008500001 | Network error. The network is unavailable. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

authClient.getAuthorization().then(result => {
  console.info(`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}`);
})
```



##### AuthorizationBase

**支持设备：** Phone | Tablet | Wearable

权限控制模块输入输出的基类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | Permission[] | 否 | 否 | 权限枚举类型的数组。 |




##### Permission

**支持设备：** Phone | Tablet | Wearable

权限枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER_STATUS | 2 | 获取用户状态权限。如：穿戴设备的佩戴状态。 |
| MOTION_SENSOR | 3 | 获取对端设备运动传感器数据权限。如：加速度传感器数据。 |
| HEALTH_SENSOR | 4 | 获取对端设备人体传感器数据权限。如：心率传感器数据。 |
| DEVICE_IDENTIFIER | 6 | 获取已连接穿戴设备的序列号。 |




##### AuthorizationRequest

**支持设备：** Phone | Tablet | Wearable

权限请求类，继承自[AuthorizationBase](#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### AuthorizationResponse

**支持设备：** Phone | Tablet | Wearable

权限响应类，继承自[AuthorizationBase](#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### wearEngine.getDeviceClient

**支持设备：** Phone | Tablet | Wearable

getDeviceClient(context: common.Context): DeviceClient

用于获取Device模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| DeviceClient | Device客户端，存储了Device模块的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting device client.`);
```



##### DeviceClient

**支持设备：** Phone | Tablet | Wearable

Device客户端类。由接口[wearEngine.getDeviceClient](#wearenginegetdeviceclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### getConnectedDevices

**支持设备：** Phone | Tablet | Wearable

getConnectedDevices(): Promise<Device[]>

获取当前已连接且支持wearEngine能力集的设备，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Device[]> | Promise对象，返回设备列表。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1008500001 | Network error. The network is unavailable. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500006 | User privacy is not agreed. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
deviceClient.getConnectedDevices().then((devices) => {
  console.info(`Succeeded in getting devices, devices number is ${devices.length}.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get devices. Code is ${error.code}, message is ${error.message}.`);
})
```



##### Device

**支持设备：** Phone | Tablet | Wearable

穿戴设备信息类。由接口[getConnectedDevices](#getconnecteddevices)返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| randomId | string | 否 | 否 | 设备随机唯一标识符，每次绑定自动生成。 |
| category | DeviceCategory | 否 | 是 | 设备类型。 |
| name | string | 否 | 是 | 设备名称。 |
| softwareVersion | string | 否 | 是 | 设备软件版本号。 |
| model | string | 否 | 是 | 设备型号。 |
| isSmartWatch | boolean | 否 | 是 | 设备是否为智能表。true：是，false：不是。 |
| osCategory | OsCategory | 否 | 是 | 设备的操作系统类别。 起始版本： 5.1.0(18) |




##### isWearEngineCapabilitySupported

**支持设备：** Phone | Tablet | Wearable

isWearEngineCapabilitySupported(capability: WearEngineCapability): Promise&lt;boolean&gt;

通过[getConnectedDevices](#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备是否支持指定的[WearEngineCapability](#wearenginecapability)，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capability | WearEngineCapability | 是 | 指定的WearEngine能力。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回是否支持指定能力的查询结果。 true：支持，false：不支持。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500006 | User privacy is not agreed. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P_COMMUNICATION).then((isSupportP2P) => {
    console.info(`Succeeded in checking p2p capability, result is ${isSupportP2P}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}`);
  })
}
```



##### isDeviceCapabilitySupported

**支持设备：** Phone | Tablet | Wearable

isDeviceCapabilitySupported(capability: DeviceCapability): Promise&lt;boolean&gt;

通过[getConnectedDevices](#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备是否支持指定的[DeviceCapability](#devicecapability)，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capability | DeviceCapability | 是 | 指定的Device能力。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回是否支持指定能力的查询结果。 true：支持，false：不支持。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500006 | User privacy is not agreed. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.CBT_I).then((isSupportCBTI) => {
    console.info(`Succeeded in checking CBTI capability, result is ${isSupportCBTI}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to check CBTI capability. Code is ${error.code}, message is ${error.message}`);
  })
}
```



##### getSerialNumber

**支持设备：** Phone | Tablet | Wearable

getSerialNumber(): Promise&lt;string&gt;

通过[getConnectedDevices](#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备的SN，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回设备SN。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  device.getSerialNumber().then((sn) => {
    console.info(`Succeeded in getting device SN, result is ${sn}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get device SN. Code is ${error.code}, message is ${error.message}`);
  })
}
```



##### WearEngineCapability

**支持设备：** Phone | Tablet | Wearable

WearEngine能力集枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| P2P_COMMUNICATION | 1 | P2p(peer-to-peer)能力。 |
| MONITOR | 2 | Monitor能力。 |
| NOTIFICATION | 3 | Notify能力。 |
| SENSOR | 4 | Sensor能力。 |




##### DeviceCapability

**支持设备：** Phone | Tablet | Wearable

Device能力集枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP_INSTALLATION | 14 | 支持应用安装能力。 |
| CBT_I | 128 | CBTI数字疗法能力。 |




##### DeviceCategory

**支持设备：** Phone | Tablet | Wearable

设备类型枚举类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 1 | 手机或平板类型。 |
| WATCH | 2 | 手表类型。 |
| BAND | 3 | 手环类型。 |
| OTHER_DEVICES | 255 | 其它设备类型。 |




##### OsCategory

**支持设备：** Phone | Tablet | Wearable

设备的操作系统类型枚举类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HARMONYOS | 1 | HarmonyOS |
| IOS | 2 | IOS |
| OTHER_OS | 255 | 其他类型 |




##### wearEngine.getMonitorClient

**支持设备：** Phone | Tablet | Wearable

getMonitorClient(context: common.Context): MonitorClient

用于获取Monitor模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| MonitorClient | Monitor客户端，存储了Monitor模块的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting monitor client.`);
```



##### MonitorClient

**支持设备：** Phone | Tablet | Wearable

Monitor客户端类。由接口[wearEngine.getMonitorClient](#wearenginegetmonitorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### queryStatus

**支持设备：** Phone | Tablet | Wearable

queryStatus(deviceRandomId: string, item: MonitorItem): Promise&lt;MonitorData&gt;

查询指定设备的指定状态，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次查询的设备。 |
| item | MonitorItem | 是 | 可查询的设备状态枚举，用于指定本次查询的状态。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;MonitorData&gt; | Promise对象，返回查询的结果。不同状态返回值的含义请参考MonitorItem。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  monitorClient.queryStatus(device.randomId, wearEngine.MonitorItem.WEAR_STATUS).then((result) => {
    console.info(`Succeeded in querying wear status, result is ${result.code}.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to query wear status. Code is ${error.code}, message is ${error.message}.`);
  })
}
```



##### subscribeEvent

**支持设备：** Phone | Tablet | Wearable

subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;

监听指定设备的指定状态变化事件，当状态发生变化时，使用callback异步回调，订阅成功与否，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在Wearable中可以订阅设备连接状态变化事件，订阅其他事件返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| type | MonitorEvent | 是 | 可订阅的设备状态枚举，用于指定本次订阅监听的设备状态。 |
| callback | Callback&lt;MonitorEventData&gt; | 是 | 回调函数，返回设备对应状态变化后的信息。 状态发生变化后执行，建议保证回调函数的生命周期延长至取消监听时。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  let callback = (monitorEventData: wearEngine.MonitorEventData) => {
    console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`)
  }
  monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
    console.info(`Succeeded in subscribing wear status.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.`);
  })
}
```



##### unsubscribeEvent

**支持设备：** Phone | Tablet | Wearable

unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;

取消订阅监听指定设备的指定状态变化事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在Wearable中可以取消订阅设备连接状态变化事件，取消订阅其他事件返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次取消订阅的设备。 |
| type | MonitorEvent | 是 | 可订阅的设备状态枚举，用于指定本次取消订阅监听的设备状态。 |
| callback | Callback&lt;MonitorEventData&gt; | 是 | 回调函数，返回设备对应状态变化后的信息。 此处需保证传入的对象与调用subscribeEvent接口时传入的回调函数为同一个对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  // 解注册时回调函数需要保证和注册时为同一个对象
  let callback = (monitorEventData: wearEngine.MonitorEventData) => {
    console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`)
  }
  // 创建待删除的订阅任务
  await monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback);
  // 删除之前创建的订阅任务
  monitorClient.unsubscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
    console.info(`Succeeded in unsubscribing wear status`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.`);
  })
}
```



##### MonitorItem

**支持设备：** Phone | Tablet | Wearable

设备状态的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WEAR_STATUS | wearStatus | 佩戴状态。返回值含义： 1：佩戴 2：未佩戴 |
| POWER_STATUS | powerStatus | 电量状态。返回值含义：剩余电量百分比（0~100）。 |
| CHARGE_STATUS | chargeStatus | 充电状态。返回值含义： 1：正在充电 2：未充电 3：电量已充满 |
| AVAILABLE_STORAGE_SPACE | availableStorageSpace | 可用存储空间。返回值含义：用户可用空间（KB）。 |
| POWER_MODE | powerMode | 电源模式。返回值含义： -1：设备不区分电源模式 0：智能模式 1：超长续航模式 |
| SPORT_STATUS | sportStatus | 运动状态。返回值含义： 3：运动开始 4：运动暂停 5：运动中 6：运动结束 起始版本： 6.1.1(24) |




##### MonitorEvent

**支持设备：** Phone | Tablet | Wearable

设备状态变化事件的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT_CONNECTION_STATUS_CHANGED | connectionStatus | 设备连接状态变化。 返回值含义：2：连接成功；3：连接断开；5：设备解绑 |
| EVENT_BATTERY_LEVEL_DROPPED | lowPower | 设备电量降低。 返回值含义：剩余电量百分比（0~100）。 |
| EVENT_WEAR_STATUS_CHANGED | wearStatus | 设备佩戴状态变化。 返回值含义：1：佩戴，2：未佩戴。 |
| EVENT_HEART_RATE_ALARM | heartRateAlarm | 心率告警。 返回值含义：1：静态心率过高，2：静态心率过低，3：运动心率过高，4：运动心率过低。 |
| EVENT_CHARGE_STATUS_CHANGED | chargeStatus | 充电状态变化。 返回值含义：1：充电开始，2：充电结束，3：充电完成。 |
| EVENT_POWER_MODE_CHANGED | powerMode | 电源模式切换。 返回值含义：0：切换至智能模式，1：切换至超长续航模式。 |




##### MonitorData

**支持设备：** Phone | Tablet | Wearable

作为[queryStatus](#querystatus)接口的返回值与[subscribeEvent](#subscribeevent)接口回调函数的入参，返回设备的状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 当使用queryStatus接口查询设备状态时，返回值含义请见MonitorItem。 当使用subscribeEvent接口订阅监听时，返回值含义请见MonitorEvent。 |
| data | string | 否 | 是 | 扩展字段。 |




##### MonitorEventData

**支持设备：** Phone | Tablet | Wearable

作为[subscribeEvent](#subscribeevent)接口的返回值，当订阅监听的事件触发时，作为入参将设备对应状态变化后的信息传递给回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | MonitorEvent | 否 | 否 | 回调函数注册的订阅监听事件枚举值。 |
| data | MonitorData | 否 | 否 | 设备状态发生变化后的状态信息。 |




##### wearEngine.getP2pClient

**支持设备：** Phone | Tablet | Wearable

getP2pClient(context: common.Context): P2pClient

用于获取P2p模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| P2pClient | P2p客户端，存储了P2p模块的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting p2p client.`);
```



##### P2pClient

**支持设备：** Phone | Tablet | Wearable

P2p客户端类。由接口[wearEngine.getP2pClient](#wearenginegetp2pclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### isRemoteAppInstalled

**支持设备：** Phone | Tablet | Wearable

isRemoteAppInstalled(deviceRandomId: string, remoteBundleName: string): Promise&lt;boolean&gt;

判断穿戴设备是否已安装指定的应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待查询的设备侧指定应用名称。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。表示设备侧应用是否安装。true：已安装，false：未安装。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 将设备侧应用包名定义为remoteBundleName
    let remoteBundleName: string = '';

    p2pClient.isRemoteAppInstalled(device.randomId, remoteBundleName).then((isInstall) => {
      console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### getRemoteAppVersion

**支持设备：** Phone | Tablet | Wearable

getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise&lt;number&gt;

获取穿戴设备指定应用的版本号，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.1.0(23)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。 对于6.1.1(24)及之后版本，该接口在Phone、Tablet、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待查询版本号的设备侧应用名称。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回设备侧应用的版本号。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 将设备侧应用包名定义为remoteBundleName
    let remoteBundleName: string = '';

    p2pClient.getRemoteAppVersion(device.randomId, remoteBundleName).then((version) => {
      console.info(`Succeeded in getting remote app version, version is ${version}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### startRemoteApp

**支持设备：** Phone | Tablet | Wearable

startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise&lt;P2pResult&gt;

拉起穿戴设备的指定应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待拉起的设备侧应用名称。 |
| transformLocalBundleName | boolean | 否 | 是否需要将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。默认值：false。 true：转换，false：不转换。 待兼容应用设置请参考申请接入Wear Engine服务。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;P2pResult&gt; | Promise对象，返回P2p通信的结果。 属性中的code字段表示本次拉起应用的结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 将设备侧应用包名定义为remoteBundleName
    let remoteBundleName: string = '';

    // transformLocalBundleName不传入参数时，默认为false
    p2pClient.startRemoteApp(device.randomId, remoteBundleName).then((p2pResult) => {
      console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to start remote app. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### startRemoteApp

**支持设备：** Phone | Tablet | Wearable

startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise&lt;P2pResult&gt;

拉起对端设备的指定应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 在wearable中可正常调用，支持拉起HarmonyOS 5.0及以上版本Phone设备的[DISTRIBUTED_SERVICE](#entrytype)组件，HarmonyOS 3.1/4.0版本Phone设备的[SERVICE](#entrytype)组件，Android设备的[SERVICE](#entrytype)组件，在其它系统和设备中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| remoteApp | AppInfo | 是 | 待拉起的对端设备的应用信息。 |
| startConfig | StartConfig | 是 | 待拉起的对端设备应用的配置参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;P2pResult&gt; | Promise对象，返回P2pResult对象。 其属性中的code字段表示本次消息发送的结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备，第一位即为目标设备且具备相关能力)
    let device: wearEngine.Device = devices[0];
    // 设置设备侧应用的应用信息：包名与指纹
    let remoteApp: wearEngine.AppInfo = {
      bundleName: 'example_bundleName',
      fingerprint: 'example_fingerprint'
    }
    
    // 设置拉起对端设备侧应用的组件类型
    let startConfig: wearEngine.StartConfig = {
      entryType: wearEngine.EntryType.DISTRIBUTED_SERVICE,
      entryName: 'example_entryName'
    };
    
    p2pClient.startRemoteApp(device.randomId, remoteApp, startConfig).then((p2pResult) => {
      console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to start remote app. Code is ${error.code}, message is ${error.message}.`);
    })
}
```



##### sendMessage

**支持设备：** Phone | Tablet | Wearable

sendMessage(deviceRandomId: string, appParam: P2pAppParam, message: P2pMessage): Promise&lt;P2pResult&gt;

向对端设备的指定应用发送消息，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 指定的设备侧应用参数。 |
| message | P2pMessage | 是 | 需要传输的消息内容，取值范围：[1，4096)，单位字节。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;P2pResult&gt; | Promise对象，返回P2pResult对象。 其属性中的code字段表示本次消息发送的结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }

    // 设置需要发送的消息内容
    let messageContent: string = 'this is message';
    let textEncoder: util.TextEncoder = new util.TextEncoder;
    let message: wearEngine.P2pMessage = {
      content: textEncoder.encodeInto(messageContent)
    }

    p2pClient.sendMessage(device.randomId, appParam, message).then((p2pResult) => {
      console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### transferFile

**支持设备：** Phone | Tablet | Wearable

transferFile(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile, callback: AsyncCallback&lt;P2pResult&gt;): void

向对端设备的指定应用发送文件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 指定的设备侧应用参数。 |
| file | P2pFile | 是 | 需要传输的文件。 |
| callback | AsyncCallback&lt;P2pResult&gt; | 是 | 回调函数，返回P2p通信的结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500011 | File is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件
    let p2pFile: wearEngine.P2pFile = {
      file: fileIo.openSync('')
    }

    p2pClient.transferFile(device.randomId, appParam, p2pFile,
      (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
      // callback处理逻辑
      if (error) {
        console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
        return;
      }
      if (p2pResult.code) {
        if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
          console.info(`Succeeded in transfering file, the result is ${p2pResult.code}.`);
        }
        console.info(`Failed to transfer file, the error code is ${p2pResult.code}.`);
      }
      if (p2pResult.progress) {
        console.info(`Succeeded in transfering file, the progress is ${p2pResult.progress}.`);
      }
    });
    fileIo.close(p2pFile.file);
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### cancelFileTransfer

**支持设备：** Phone | Tablet | Wearable

cancelFileTransfer(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile): Promise&lt;P2pResult&gt;

取消向对端设备的指定应用发送文件，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 指定设备侧应用参数。 |
| file | P2pFile | 是 | 需要传输的文件。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;P2pResult&gt; | Promise对象，返回P2p通信的结果。 属性中的code字段表示本次取消文件发送的结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500011 | File is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件信息
    let p2pFile: wearEngine.P2pFile = {
      file: fileIo.openSync('')
    }

    p2pClient.transferFile(device.randomId, appParam, p2pFile, () => {
      // 回调函数执行逻辑
    })

    p2pClient.cancelFileTransfer(device.randomId, appParam, p2pFile).then((p2pResult) => {
      if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
        console.info(`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.`);
      }
    }).catch((error: BusinessError) => {
      console.error(`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.`);
    })
    fileIo.close(p2pFile.file);
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### registerMessageReceiver

**支持设备：** Phone | Tablet | Wearable

registerMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;

订阅对端设备应用向本端设备发送消息的事件，接收到对端应用发送的消息时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 设备侧应用参数。 |
| callback | Callback&lt;P2pMessage&gt; | 是 | 回调函数，返回对端设备应用发送的消息。 接收到设备侧应用发送的消息后执行的回调函数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名
    }
    // 设置需要发送的文件信息
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`)
    }

    p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in registering message receiver.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### registerFileReceiver

**支持设备：** Phone | Tablet | Wearable

registerFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;

订阅对端设备向本端设备发送文件的事件，接收到对端设备发送的文件时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 设备侧应用参数。 |
| callback | Callback&lt;P2pFile&gt; | 是 | 回调函数，返回对端设备应用发送的文件。 接收到设备侧应用发送的文件后执行的回调函数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件信息
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(`Succeeded in receiving file.`)
    }

    p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in registering file receiver.`)
    }).catch((error: BusinessError) => {
      console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### registerFileReceiverWithProgress

**支持设备：** Phone | Tablet | Wearable

registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;

订阅对端设备向本端设备发送文件和文件传输进度的事件，接收到对端设备发送的文件和文件传输进度时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 设备侧应用参数。 |
| callback | Callback&lt;P2pFile&gt; | 是 | 回调函数，返回对端设备应用发送的文件类。 接收到设备侧应用发送的文件或者传输进度后执行的回调函数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件信息和传输进度
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      if (!p2pMessage.file) {
        console.info(`progress is ${p2pMessage.progress}`)
      } else {
        console.info(`Succeeded in receiving file.`)
      }
    }

    p2pClient.registerFileReceiverWithProgress(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in registering file receiver.`)
    }).catch((error: BusinessError) => {
      console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### unregisterMessageReceiver

**支持设备：** Phone | Tablet | Wearable

unregisterMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;

取消订阅对端应用向本端应用发送消息的事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 设备侧应用参数。 |
| callback | Callback&lt;P2pMessage&gt; | 是 | 回调函数，返回对端设备应用发送的消息。 需要同订阅监听时的回调函数为同一个对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件信息
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`)
    }

    p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in registering message receiver.`)
    }).catch((error: BusinessError) => {
      console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
    })

    p2pClient.unregisterMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in unregistering message receiver.`)
    }).catch((error: BusinessError) => {
      console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### unregisterFileReceiver

**支持设备：** Phone | Tablet | Wearable

unregisterFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;

取消订阅对端应用向本端应用发送文件的事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| appParam | P2pAppParam | 是 | 设备侧应用参数。 |
| callback | Callback&lt;P2pFile&gt; | 是 | 回调函数，返回对端设备应用发送的文件。 需要同订阅监听时的回调函数为同一个对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // 挑选支持应用安装的设备
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
    // 设置设备侧应用的应用信息：包名与指纹
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // 将设备侧应用参数类定义为appParam
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // transformLocalAppInfo默认为false，不转换包名指纹
    }
    // 设置需要发送的文件信息
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(`Succeeded in receiving file.`)
    }

    p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in registering file receiver.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
    })

    p2pClient.unregisterFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(`Succeeded in unregistering file receiver.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
    })
  }
  if (idx === deviceList.length - 1) {
    // 若不存在目标设备则抛出错误
    throw new Error('cannot find target device');
  }
})
```



##### AppInfo

**支持设备：** Phone | Tablet | Wearable

设备侧应用信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用名称。 |
| fingerprint | string | 否 | 否 | 应用指纹，用于标识应用的唯一身份。 |




##### P2pResultCode

**支持设备：** Phone | Tablet | Wearable

存储P2p通信的返回值枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REMOTE_APP_NOT_INSTALLED | 200 | 设备侧应用未安装。 |
| REMOTE_APP_NOT_RUNNING | 201 | 设备侧应用未运行。 |
| REMOTE_APP_RUNNING | 202 | 设备侧应用运行中。 |
| UNKNOWN_ERROR | 203 | 未知错误。 |
| COMMUNICATION_FAILURE | 206 | 与设备侧应用通信失败。 |
| COMMUNICATION_SUCCESS | 207 | 与设备侧应用通信成功。 |




##### P2pResult

**支持设备：** Phone | Tablet | Wearable

存储P2p通信的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 是 | 用于返回除文件传输外的P2p通信结果，返回值含义见P2pResultCode。 |
| progress | number | 否 | 是 | 仅用于上报文件传输进度，返回值范围：0-100。 |




##### P2pMessage

**支持设备：** Phone | Tablet | Wearable

本端设备应用向对端设备应用发送的消息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | Uint8Array | 否 | 否 | 传输消息的内容，格式为Uint8Array（二进制字节数组）类型数据。 |




##### P2pFile

**支持设备：** Phone | Tablet | Wearable

本端设备应用向对端设备应用发送的文件类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| file | fs.File | 否 | 否 | 文件对象。 |
| progress | number | 否 | 是 | 文件传输进度。 起始版本： 6.1.1(24) |




##### P2pAppParam

**支持设备：** Phone | Tablet | Wearable

P2p通信过程中可用的设备侧应用参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remoteApp | AppInfo | 否 | 否 | 设备侧应用信息类。 |
| transformLocalAppInfo | boolean | 否 | 是 | 是否需要将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。默认值：false。 true：转换；false：不转换。 待兼容应用设置请参考申请接入Wear Engine服务。 |




##### StartConfig

**支持设备：** Phone | Tablet | Wearable

待拉起的对端设备应用的配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entryType | EntryType | 否 | 否 | 需要拉起的对端设备应用的组件类型。 |
| entryName | string | 否 | 是 | 需要拉起的对端设备应用的组件名称。 |




##### EntryType

**支持设备：** Phone | Tablet | Wearable

待拉起的对端设备应用的组件类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISTRIBUTED_SERVICE | DistributedService | 分布式服务组件，当要启动分布式服务组件时需设置此值。 |
| SERVICE | Service | 服务组件，当要拉起服务时需设置此值。 |
| UI | UI | UI组件，当要启动UI组件时需要设置此值。 |




##### wearEngine.getNotifyClient

**支持设备：** Phone | Tablet | Wearable

getNotifyClient(context: common.Context): NotifyClient

用于获取Notify模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| NotifyClient | 模板化通知客户端，存储了发送模板化通知的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting notify client`);
```



##### NotifyClient

**支持设备：** Phone | Tablet | Wearable

Notify客户端类，由[wearEngine.getNotifyClient](#wearenginegetnotifyclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### notify

**支持设备：** Phone | Tablet | Wearable

notify(deviceRandomId: string, options: NotificationOptions): Promise&lt;void&gt;

向穿戴设备发送模板化通知，返回是否发送成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次查询的设备。 |
| options | NotificationOptions | 是 | 模板化通知配置参数类。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  let button1: wearEngine.NotificationButton = {
    buttonId: wearEngine.ButtonId.FIRST_BUTTON,
    content: 'button_1'
  }
  let type1Notification: wearEngine.Notification = {
    type: wearEngine.NotificationType.NOTIFICATION_WITH_ONE_BUTTON,
    bundleName: 'bundleName',
    title: 'title',
    text: 'text',
    buttons: [button1]
  }
  let options: wearEngine.NotificationOptions = {
    notification: type1Notification,
    onAction: (feedback: wearEngine.NotificationFeedback) => {
      console.info(`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}`);
    }
  }

  notifyClient.notify(device.randomId, options).then(result => {
    console.info(`Succeeded in sending notification.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to send notification. Code is ${error.code}, message is ${error.message}`);
  })
}
```



##### NotificationOptions

**支持设备：** Phone | Tablet | Wearable

模板化通知的配置参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notification | Notification | 否 | 否 | 模板化通知的通知体参数类。 |




##### onAction

**支持设备：** Phone | Tablet | Wearable

onAction(feedback: NotificationFeedback): void

设备侧对应用发出的通知做相关操作后执行的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feedback | NotificationFeedback | 是 | 设备侧操作通知的反馈类。 |




##### Notification

**支持设备：** Phone | Tablet | Wearable

模板化通知的通知体参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | NotificationType | 否 | 否 | 通知的模板类型。 |
| bundleName | string | 否 | 否 | 发送通知应用的包名。 |
| title | string | 否 | 否 | 通知的标题，取值范围：[1，28)，单位字节。 |
| text | string | 否 | 否 | 通知的内容，取值范围：[1，400)，单位字节。 |
| buttons | NotificationButton[] | 否 | 是 | 通知按钮信息类，若未填写，默认为空。 |




##### NotificationType

**支持设备：** Phone | Tablet | Wearable

模板化通知的模板类型枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION_WITHOUT_BUTTONS | 50 | 没有按钮的通知类型。 |
| NOTIFICATION_WITH_ONE_BUTTON | 51 | 拥有一个按钮的通知类型。 |
| NOTIFICATION_WITH_TWO_BUTTONS | 52 | 拥有两个按钮的通知类型。 |
| NOTIFICATION_WITH_THREE_BUTTONS | 53 | 拥有三个按钮的通知类型。 |




##### NotificationButton

**支持设备：** Phone | Tablet | Wearable

通知按钮信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttonId | ButtonId | 否 | 否 | 按钮Id枚举类。 |
| content | string | 否 | 否 | 按钮上的文字内容，取值范围：[1，12)，单位字节。 |




##### ButtonId

**支持设备：** Phone | Tablet | Wearable

模板化通知的按钮Id枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRST_BUTTON | firstButton | 第一个按钮的Id。 |
| SECOND_BUTTON | secondButton | 第二个按钮的Id。 |
| THIRD_BUTTON | thirdButton | 第三个按钮的Id。 |




##### NotificationFeedback

**支持设备：** Phone | Tablet | Wearable

设备侧操作通知的反馈类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | NotificationAction | 否 | 是 | 设备侧对通知的操作反馈枚举类。 |
| errorCode | number | 否 | 是 | 错误码，含义请见NotificationErrorCode。 |




##### NotificationAction

**支持设备：** Phone | Tablet | Wearable

设备侧对通知的操作反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION_SWITCHED_TO_BACKGROUND | 0 | 用户使用Home键退出或熄屏，通知退回后台。 |
| NOTIFICATION_DELETED | 1 | 通知被用户删除。 |
| FIRST_BUTTON_CLICKED | 2 | 用户点击通知的第一个按钮。 |
| SECOND_BUTTON_CLICKED | 3 | 用户点击通知的第二个按钮。 |
| THIRD_BUTTON_CLICKED | 4 | 用户点击通知的第三个按钮。 |




##### NotificationErrorCode

**支持设备：** Phone | Tablet | Wearable

通知在设备侧发生错误的反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL_ERROR | 255 | Wear Engine内部错误。通过在线提单提交问题，华为支持人员会及时处理。 |




##### wearEngine.getSensorClient

**支持设备：** Phone | Tablet | Wearable

getSensorClient(context: common.Context): SensorClient

用于获取Sensor模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：UIAbilityContext）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| SensorClient | Sensor客户端，存储了Sensor模块的相关方法。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting sensor client`);
```



##### SensorClient

**支持设备：** Phone | Tablet | Wearable

Sensor客户端类。由接口[wearEngine.getSensorClient](#wearenginegetsensorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)



##### getSensorList

**支持设备：** Phone | Tablet | Wearable

getSensorList(deviceRandomId: string): Promise<Sensor[]>

获取设备侧可用的传感器列表，返回对应的传感器列表，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定设备。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Sensor[]> | Promise对象，返回设备侧可用的传感器列表。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
  let device: wearEngine.Device = devices[0];

  sensorClient.getSensorList(device.randomId).then((sensorList) => {
    console.info(`Succeeded in getting sensor list, result is ${sensorList}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
  })
}
```



##### subscribeSensor

**支持设备：** Phone | Tablet | Wearable

subscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;

订阅指定的传感器数据上报，返回是否订阅成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次订阅的设备。 |
| type | SensorType | 是 | 传感器类别，用于指定本次订阅的传感器。 |
| callback | Callback&lt;SensorResult&gt; | 是 | 回调函数，返回传感器上报结果。 用于处理传感器上报的数据。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备，第一位即为目标设备且具备相关能力)
  let device: wearEngine.Device = devices[0];
  let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
  sensorList.forEach((sensor, idx, arr) => {
    if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
      let callback = (sensorResult: wearEngine.SensorResult) => {
        console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
      }
      // 订阅加速度传感器数据上报
      sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(`Succeeded in subscribing sensor data.`);
      }).catch((error: BusinessError) => {
        console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
      })
    }
  })
}
```



##### unsubscribeSensor

**支持设备：** Phone | Tablet | Wearable

unsubscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;

取消订阅指定的传感器数据上报，返回是否取消成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | Device的随机标识符，用于指定本次取消订阅的设备。 |
| type | SensorType | 是 | 传感器类别，用于指定本次取消订阅的传感器。 |
| callback | Callback&lt;SensorResult&gt; | 是 | 回调函数，返回传感器上报结果。 需要同订阅监听时的回调函数为同一个对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1008500001 | Network error. The network is unavailable. |
| 1008500002 | No device is bound. |
| 1008500003 | Device disconnected. |
| 1008500004 | App has not applied for the Wear Engine service. |
| 1008500005 | The HUAWEI ID is not authorized. |
| 1008500006 | User privacy is not agreed. |
| 1008500007 | The device capability is not supported. |
| 1008500008 | Account error. The user has not logged in with HUAWEI ID. |
| 1008500009 | Account error. Failed to obtain account information with HUAWEI ID. |
| 1008500010 | Device ID is invalid. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备，第一位即为目标设备且具备相关能力)
  let device: wearEngine.Device = devices[0];
  let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
  sensorList.forEach((sensor, idx, arr) => {
    if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
      let callback = (sensorResult: wearEngine.SensorResult) => {
        console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
      }
      // 订阅加速度传感器数据上报
      sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(`Succeeded in subscribing sensor data.`);
      }).catch((error: BusinessError) => {
        console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
      })
      // 取消加速度传感器数据上报, 注意传入的回调函数需与订阅时为同一对象
      sensorClient.unsubscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(`Succeeded in unsubscribing sensor data.`);
      }).catch((error: BusinessError) => {
        console.error(`Failed to unsubscribe sensor data. Code is ${error.code}, message is ${error.message}`);
      })
    }
  })
}
```



##### SensorType

**支持设备：** Phone | Tablet | Wearable

传感器类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ELECTROCARDIOGRAPHY | 0 | ECG（electrocardiograph）传感器。 |
| PHOTOPLETHYSMOGRAPHY | 1 | PPG（photoplethysmogram）传感器。 |
| ACCELEROMETER | 2 | 加速度传感器。 |
| GYROSCOPE | 3 | 陀螺仪传感器。 |
| MAGNETIC_FIELD | 4 | 磁力传感器。 |
| HEART_RATE | 6 | 心率传感器。 |




##### Sensor

**支持设备：** Phone | Tablet | Wearable

传感器信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 传感器名称。 |
| id | number | 否 | 否 | 传感器ID。 |
| type | SensorType | 否 | 否 | 传感器类型。 |
| accuracy | number | 否 | 是 | 传感器采样周期，单位毫秒。 |
| resolution | number | 否 | 是 | 传感器分辨率，当前仅作为Sensor对象的返回值信息。 |
| isUtcTimestampSupported | boolean | 否 | 否 | 传感器是否支持UTC（ Coordinated Universal Time）时间戳。true：支持，false：不支持。 |




##### SensorData

**支持设备：** Phone | Tablet | Wearable

传感器上报数据类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorType | SensorType | 否 | 否 | 传感器类型。 |
| data | number[] | 否 | 否 | 数据内容，格式及含义请参考穿戴设备传感器数据格式及样例。 |
| channel | number | 否 | 是 | 传感器通道ID，为大于0的整数。 |
| timestamp | number | 否 | 是 | 计时时间戳。 |
| utcTimestamp | number | 否 | 是 | UTC时间戳。 |




##### SensorErrorCode

**支持设备：** Phone | Tablet | Wearable

传感器类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE_NOT_BEING_WORN | 300 | 设备未佩戴。 |
| DEVICE_LEAD_OFF | 301 | 设备引线脱落。 |
| SENSOR_TURNED_OFF_MANUALLY | 302 | 传感器被手动关闭。 |
| SENSOR_OCCUPIED | 303 | 传感器被占用。 |
| SENSOR_NOT_SUPPORTED | 304 | 传感器不支持。 |




##### SensorResult

**支持设备：** Phone | Tablet | Wearable

传感器上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | SensorData[] | 否 | 是 | 传感器正常上报的数据内容。 |
| errorCode | number | 否 | 是 | 错误码，含义请见SensorErrorCode。 |




##### on/off订阅事件

**支持设备：** Phone | Tablet | Wearable



##### wearEngine.on

**支持设备：** Phone | Tablet | Wearable

on(type: 'serviceDie', callback: Callback&lt;void&gt;): void

订阅服务端消亡事件。使用callback异步回调。调用[wearEngine.destroy](#wearenginedestroy)接口主动发起的消亡事件不会触发执行回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie(服务端消亡事件)。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 1008500012 | Too many callbacks of the same type. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(`The service destruction event`);
}
try {
  wearEngine.on('serviceDie', callback);
  console.info(`Succeeded in subscribing the service destruction event.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to subscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
}
```



##### wearEngine.off

**支持设备：** Phone | Tablet | Wearable

off(type: 'serviceDie', callback?: Callback&lt;void&gt;): void

取消订阅服务端消亡事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie(服务端消亡事件)。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数，无返回结果。 需要同订阅监听时的回调函数为同一个对象。 当该参数为空时，会取消掉之前所有的订阅。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(`The service destruction event`);
}
wearEngine.on('serviceDie', callback);

try {
  wearEngine.off('serviceDie', callback);
  console.info(`Succeeded in unsubscribing the service destruction event.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to unsubscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
}
```



##### wearEngine.destroy

**支持设备：** Phone | Tablet | Wearable

destroy(): Promise&lt;void&gt;

主动销毁服务端，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1008509999 | Internal error. |


**示例：**

```text
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

wearEngine.destroy().then(() => {
  console.info(`Succeeded in destroying wear engine channel.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to destroy wear engine channel. Code is ${error.code}, message is ${error.message}.`);
})
```
