# accessoryAccessManager（配件接入管理）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/accessory-accessoryaccessmanager
**支持设备：** Phone | PC/2in1 | Tablet

配件接入管理模块面向华为生态合作配件设备及其生态应用提供关联唤醒、系统服务关联、按需调度和安全授信管理等能力。

**起始版本：** 26.0.0


#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { accessoryAccessManager } from '@kit.AccessoryKit';
```



#### DiscoveryType

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，配件设备被主机设备发现和识别的通信类型。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARTNER_BLE_CONNECT | 0 | 使用开发者提供的BLE MAC地址来创建BLE GATT关系。 |




#### ServiceName

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，设备关联的服务名称。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARTNER_APP_ACCESSORY_COLLABORATION | 'P_AppAccessoryCollaboration' | 该应用和配件之间会相互交互，唤醒彼此并传输数据。 |
| PARTNER_SHARE_SERVICE | 'P_ShareService' | 接收从配件共享的文件。 |
| PARTNER_DISTRIBUTED_CAMERA_SERVICE | 'P_DCameraService' | 将该配件用作分布式摄像头。 |




#### WakeupType

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，唤醒应用的方式。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START_ABILITY_BY_CALL | 0 | 通过startAbilityByCall唤醒应用。 |




#### StringResourceInfo

**支持设备：** Phone | PC/2in1 | Tablet

被唤醒应用信息的简要说明。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 是 | 包名。 |
| moduleName | string | 否 | 否 | 模块名。 |
| stringResourceId | number | 否 | 否 | 资源编号。 |




#### WakeupInfo

**支持设备：** Phone | PC/2in1 | Tablet

唤醒类型以及被唤醒应用的信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wakeupType | WakeupType | 否 | 否 | 唤醒类型。 |
| bundleName | string | 否 | 否 | 包名。 |
| abilityName | string | 否 | 否 | 能力名称。 |
| briefDesc | StringResourceInfo | 否 | 否 | 简要说明，内容包含bundleName，moduleName和stringResourceId，用于获取对应用的简要描述。 |




#### ServiceInfo

**支持设备：** Phone | PC/2in1 | Tablet

关联的服务类型和对应的服务参数。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceName | ServiceName | 否 | 否 | 设备关联的服务名称。 |
| parameters | Record<string, Object> | 否 | 是 | 关联服务的相关参数。 |




#### PickerItemInfo

**支持设备：** Phone | PC/2in1 | Tablet

配件的信息及配件关联的服务。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| discoveryType | DiscoveryType | 否 | 否 | 配件发现类型。 |
| hasScreen | boolean | 否 | 是 | 该字段表示设备是否具有用于显示PIN码等内容的屏幕。true代表有屏设备，false代表无屏设备。默认值为false。 |
| bleAddress | string | 否 | 是 | BLE地址。 |
| bleMtuSize | number | 否 | 是 | 最大传输单元（MTU）大小。 |
| productId | string | 否 | 是 | 产品编号。 |
| subProductId | string | 否 | 是 | 子产品编号。 |
| displayName | string | 否 | 否 | 弹窗显示的设备名称。 |
| displayImage | image.PixelMap | 否 | 否 | 弹窗显示的设备图片。 |
| requestAttachServiceInfo | Array&lt;ServiceInfo&gt; | 否 | 否 | 配件认证通过后，关联的业务信息。 |




#### AccessoryInfo

**支持设备：** Phone | PC/2in1 | Tablet

配件信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessoryId | string | 否 | 是 | 配件编号。 |
| bleAddress | string | 否 | 是 | BLE地址。 |
| displayName | string | 否 | 否 | 配件展示的名称。 |
| productId | string | 否 | 是 | 产品编号。 |




#### AccessEvent

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，配件设备接入事件。触发参考[showAccessPicker接口事件回调数据结构说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessory-dev-guides#showaccesspicker接口事件回调数据结构说明)。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PICKER_PRESENT | 0 | 选择器出现事件。 |
| PICKER_DISMISS | 1 | 选择器消失事件。 |
| PICKER_END_SUCC | 2 | 选择器成功结束事件。 |
| PICKER_END_FAIL | 3 | 选择器失败结束事件。 |
| SERVICE_ATTACHING | 300 | 服务挂载事件。 |
| SERVICE_ATTACH_SUCC | 301 | 服务挂载成功事件。 |
| SERVICE_ATTACH_FAIL | 302 | 服务挂载失败事件。 |




#### AttachServiceInfo

**支持设备：** Phone | PC/2in1 | Tablet

挂载配件信息和服务信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attachId | number | 否 | 否 | 挂载服务的编号。 |
| accessoryInfo | AccessoryInfo | 否 | 否 | 配件信息。 |
| serviceInfo | ServiceInfo | 否 | 否 | 服务信息。 |




#### AccessEventInfo

**支持设备：** Phone | PC/2in1 | Tablet

配件接入事件信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessEvent | AccessEvent | 否 | 否 | 配件设备接入事件，事件触发流程参考showAccessPicker接口事件回调数据结构说明。 |
| attachServiceInfo | AttachServiceInfo | 否 | 是 | 挂载服务信息。 |
| errorCode | number | 否 | 是 | 接入事件错误码。 0：正常结果； 10000：用户取消，正常流程下，点击X按钮； 10001：超时； 10002：鉴权失败，需检查productId是否正确； 10003：弹窗异常； 10004：发起授信异常； 10005：授信失败； 10006：服务挂载失败。 |
| errorDesc | string | 否 | 是 | 接入事件错误描述。 |




#### DetachServiceEvent

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，移除配件服务状态。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SERVICE_DETACH_SUCC | 0 | 移除服务成功。 |
| SERVICE_DETACH_FAIL | 1 | 移除服务失败。 |




#### AccessManager

**支持设备：** Phone | PC/2in1 | Tablet

配件接入管理器。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0



#### showAccessPicker

**支持设备：** Phone | PC/2in1 | Tablet

showAccessPicker(items: Array&lt;PickerItemInfo&gt;, callback: Callback&lt;AccessEventInfo&gt;): number

接入配件设备信息及其关联的服务信息。使用Callback异步回调。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;PickerItemInfo&gt; | 是 | 接入的选择项信息数组，当前支持数量为1，传入多个时默认取第一个。 |
| callback | Callback&lt;AccessEventInfo&gt; | 是 | 回调函数，返回配件接入事件信息对象。回调结果参考showAccessPicker接口事件回调数据结构说明。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 操作结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```text
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const TAG = 'Demo';

let briefDesc: accessoryAccessManager.StringResourceInfo = {
  'bundleName': 'com.huawei.accessoryDemo',
  'moduleName': 'entry',
  'stringResourceId': $r('app.string.EntryAbility_desc').id,
}
let wakeupInfo: accessoryAccessManager.WakeupInfo = {
  'wakeupType': accessoryAccessManager.WakeupType.START_ABILITY_BY_CALL,
  'bundleName': 'com.huawei.accessoryDemo',
  'abilityName': 'EntryAbility',
  'briefDesc': briefDesc
}

let shareBriefDesc: accessoryAccessManager.StringResourceInfo = {
  'bundleName': 'com.huawei.accessoryDemo',
  'moduleName': 'entry',
  'stringResourceId': $r('app.string.EntryAbility_desc').id,
}

let shareWakeupInfo: accessoryAccessManager.WakeupInfo = {
  'wakeupType': accessoryAccessManager.WakeupType.START_ABILITY_BY_CALL,
  'bundleName': 'com.huawei.accessoryDemo',
  'abilityName': 'EntryAbility',
  'briefDesc': shareBriefDesc
}

let serviceInfo: Array<accessoryAccessManager.ServiceInfo> = [
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_APP_ACCESSORY_COLLABORATION,
    parameters: {
      'serviceName': wakeupInfo
    }
  },
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_SHARE_SERVICE,
    parameters: {
      'bundleName': 'com.huawei.accessoryDemo',
    }
  }
];

// 此处创建了一张空图，开发时可自行换成所需图片
const color: ArrayBuffer = new ArrayBuffer(96);
let bufferArr: Uint8Array = new Uint8Array(color);
for (let i = 0; i < bufferArr.length; i++) {
  bufferArr[i] = 0x80;
}
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.BGRA_8888,
  size: { height: 4, width: 6 },
  alphaType: image.AlphaType.UNPREMUL
}
let pixelMap: image.PixelMap | undefined = undefined;
image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
  pixelMap = srcPixelMap;
})

let items: Array<accessoryAccessManager.PickerItemInfo> = [
  {
    discoveryType: accessoryAccessManager.DiscoveryType.PARTNER_BLE_CONNECT,
    hasScreen: true,
    bleAddress: 'XX:XX:XX:XX:XX:XX',
    bleMtuSize: 1,
    productId: 'XXXXX',
    subProductId: '',
    displayName: 'xxxx',
    displayImage: pixelMap,
    requestAttachServiceInfo: serviceInfo
  },
  {
    discoveryType: accessoryAccessManager.DiscoveryType.PARTNER_BLE_CONNECT,
    hasScreen: true,
    bleAddress: 'XX:XX:XX:XX:XX:XX',
    bleMtuSize: 1,
    productId: 'XXXXX',
    subProductId: '',
    displayName: 'xxxx',
    displayImage: pixelMap,
    requestAttachServiceInfo: serviceInfo
  }
];
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.showAccessPicker(items, (event: accessoryAccessManager.AccessEventInfo) => {
  if (!event) {
    hilog.error(0x0000, TAG, `showAccessPicker failed`);
    return;
  }
  hilog.info(0x0000, TAG, `showAccessPicker callback result: ${event.accessEvent}`);
});
hilog.info(0x0000, TAG, `showAccessPicker result: ${result}`);
```



#### modifyDisplayName

**支持设备：** Phone | PC/2in1 | Tablet

modifyDisplayName(accessoryId: string, displayName: string): number

重命名配件，用于修改配件设备的展示名称。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessoryId | string | 是 | 设备编号。 |
| displayName | string | 是 | 展示名称。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 重命名结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```text
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let deviceId = 'deviceIdTest';
let deviceName = 'deviceNameTest';
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.modifyDisplayName(deviceId, deviceName);
hilog.info(0x0000, TAG, `modifyDisplayName code: ${result}`);
```



#### queryAttachedService

**支持设备：** Phone | PC/2in1 | Tablet

queryAttachedService(): Array&lt;AttachServiceInfo&gt;

查询已经关联的配件和服务信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;AttachServiceInfo&gt; | 已挂载成功的服务信息数组。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```text
import { accessoryAccessManager } from '@kit.AccessoryKit';

let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let resultArr: Array<accessoryAccessManager.AttachServiceInfo> = accessoryManager.queryAttachedService();
```



#### detachService

**支持设备：** Phone | PC/2in1 | Tablet

detachService(attachId: number, callback: Callback&lt;DetachServiceEvent&gt;): number

移除某个已关联的配件或配件关联的服务信息。使用Callback异步回调。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachId | number | 是 | 挂载编号。 |
| callback | Callback&lt;DetachServiceEvent&gt; | 是 | 回调函数，返回移除配件服务状态。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 操作结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```text
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let attachId = 1;
let result: number = accessoryManager.detachService(attachId, (event: accessoryAccessManager.DetachServiceEvent) => {
  if (!event) {
    hilog.error(0x0000, TAG, `detachService failed`);
    return;
  }
  hilog.info(0x0000, TAG, `detachService event: ${event}`);
});
hilog.info(0x0000, TAG, `detachService result: ${result}`);
```



#### ChannelType

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，连接的通道类型。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARTNER_WIFI_CHANNEL | 1 | Wi-Fi通道类型。 |




#### ChannelEvent

**支持设备：** Phone | PC/2in1 | Tablet

枚举类型，连接的通道状态。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTING | 0 | 连接中。 |
| CONNECTED | 1 | 已连接。 |
| CONNECT_FAIL | 2 | 连接失败。 |
| DISCONNECTED | 3 | 已断开连接。 |




#### ChannelEventInfo

**支持设备：** Phone | PC/2in1 | Tablet

连接的通道信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelEvent | ChannelEvent | 否 | 否 | 通道事件。 |
| attachId | number | 否 | 否 | 挂载编号。 |
| channelType | ChannelType | 否 | 否 | 通道类型。 |
| ip | string | 否 | 是 | IP地址。 |
| errorCode | number | 否 | 是 | 接入事件错误码。 |
| reason | string | 否 | 是 | 描述发生故障时错误的原因。 |




#### ConnectRequestInfo

**支持设备：** Phone | PC/2in1 | Tablet

连接请求的信息。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attachId | number | 否 | 否 | 挂载编号。 |
| channelType | ChannelType | 否 | 否 | 通道类型。 |
| serviceDesc | StringResourceInfo | 否 | 否 | 服务描述。 |




#### ConnectManager

**支持设备：** Phone | PC/2in1 | Tablet

连接管理器。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 26.0.0



#### registerConnectListener

**支持设备：** Phone | PC/2in1 | Tablet

registerConnectListener(attachId: number, stateCallback: Callback&lt;ChannelEventInfo&gt;): number

注册一个连接事件监听器，将回调通道的建连和断连的状态。使用Callback异步回调。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachId | number | 是 | 挂载编号。 |
| stateCallback | Callback&lt;ChannelEventInfo&gt; | 是 | 回调函数，返回连接通道信息对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 注册监听器结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```json
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let attachId = 0;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result : number = connectManager.registerConnectListener(attachId, (event: accessoryAccessManager.ChannelEventInfo) => {
  hilog.info(0x0000, TAG, `registerConnectListener event result: ${JSON.stringify(event)}`);
  if (!event) {
    hilog.error(0x0000, TAG, `registerConnectListener callback event undefined`);
    return;
  }
  if ((event.channelEvent as accessoryAccessManager.ChannelEvent) ==
    accessoryAccessManager.ChannelEvent.CONNECTING) {
    attachId = event.attachId;
  }
  if ((event.channelEvent as accessoryAccessManager.ChannelEvent) ==
    accessoryAccessManager.ChannelEvent.CONNECTED) {
    attachId = event.attachId;
  }
});
hilog.info(0x0000, TAG, `modifyDisplayName code: ${result}`);
```



#### unregisterConnectListener

**支持设备：** Phone | PC/2in1 | Tablet

unregisterConnectListener(attachId: number): number

取消注册连接事件监听器，将停止接收通道连接状态的通知。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachId | number | 是 | 挂载编号。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 取消注册监听器结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```json
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.unregisterConnectListener(attachId);
hilog.info(0x0000, TAG, `unregisterConnectListener result: ${JSON.stringify(result)}`);
```



#### connect

**支持设备：** Phone | PC/2in1 | Tablet

connect(connectRequestInfo: ConnectRequestInfo): number

建立与配件的连接，通过[registerConnectListener](#registerconnectlistener)注册的回调通知连接状态。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connectRequestInfo | ConnectRequestInfo | 是 | 连接请求信息。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 建立与配件的连接结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```json
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let connectAttachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let shareDesc: accessoryAccessManager.StringResourceInfo = {
  bundleName: "com.huawei.accessoryDemo",
  moduleName: "entry",
  stringResourceId: $r('app.string.EntryAbility_desc').id
};
let info: accessoryAccessManager.ConnectRequestInfo =
  {
    attachId: connectAttachId,
    channelType: accessoryAccessManager.ChannelType.PARTNER_WIFI_CHANNEL,
    serviceDesc: shareDesc
  };
let result: number = connectManager.connect(info);
hilog.info(0x0000, TAG, `connect result: ${JSON.stringify(result)}`);
```



#### disconnect

**支持设备：** Phone | PC/2in1 | Tablet

disconnect(attachId: number): number

断开与配件的连接，通过[registerConnectListener](#registerconnectlistener)注册的回调通知断连状态。

**系统能力：** SystemCapability.Collaboration.Accessory.AccessManager

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**需要权限：** 如使用该接口需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放。权限申请方式请参考[申请受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachId | number | 是 | 挂载编号。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 断开与配件的连接结果：0成功，非0失败。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permissions check failed. |


**示例：**

```json
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'Demo';

let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.disconnect(attachId);
hilog.info(0x0000, TAG, `disconnect result: ${JSON.stringify(result)}`);
```
