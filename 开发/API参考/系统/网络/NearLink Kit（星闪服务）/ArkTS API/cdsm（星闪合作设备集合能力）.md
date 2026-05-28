# cdsm（星闪合作设备集合能力）

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-cdsm
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供了查询星闪合作设备集合信息的功能。
 
**起始版本：** 6.1.1(24)
  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { cdsm } from '@kit.NearLinkKit';
```
 
  

##### createCdsmClient

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createCdsmClient(address: string): CdsmClient
 
创建cdsm客户端实例。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_NEARLINK
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 已配对连接的合作设备集合的成员设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| CdsmClient | cdsm客户端实例。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because the chip does not support it. |
| 1009700003 | Nearlink is off. |
| 1009700050 | Coordinated Devices Set Management not supported. |
| 1009700099 | Operation failed. |
 
 
**示例：**
 
```json
import { cdsm } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
let client: cdsm.CdsmClient;
try {
  client = cdsm.createCdsmClient(addr);
  console.info('client: ' + JSON.stringify(client));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
 
  

##### CdsmClient

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供获取远端设备的合作设备集合信息的方法，使用前需要使用cdsm.createCdsmClient方法创建一个CdsmClient实例。
 
一个应用针对一个远端设备只需要创建一次实例。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
 
  

##### getCdsmInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCdsmInfo(): CdsmInfo
 
查询远端设备的合作设备集合信息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_NEARLINK
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| CdsmInfo | 远端设备的合作设备集合信息。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1009700003 | Nearlink is off. |
| 1009700099 | Operation failed. |
 
 
**示例：**
 
```json
import { cdsm } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
let client: cdsm.CdsmClient;
try {
  client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
let cdsmInformation: cdsm.CdsmInfo = client.getCdsmInfo();
  console.info('cdsmInformation:' + JSON.stringify(cdsmInformation));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
 
  

##### onCdsmInfoChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCdsmInfoChange(callback: Callback&lt;CdsmInfo&gt;): void
 
订阅远端设备合作设备集合信息变化事件。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_NEARLINK
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;CdsmInfo&gt; | 是 | 表示远端设备合作设备集合信息变化回调函数的入参。回调函数由用户创建，通过该接口注册。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
 
 
**示例：**
 
```json
import { cdsm } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<cdsm.CdsmInfo> = (data: cdsm.CdsmInfo) => {
  console.info('CdsmInfo:' + JSON.stringify(data));
};

let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
let client: cdsm.CdsmClient;
try {
  client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.onCdsmInfoChange(callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
 
  

##### offCdsmInfoChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offCdsmInfoChange(callback?: Callback&lt;CdsmInfo&gt;): void
 
取消订阅远端设备合作设备集合信息变化事件。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**需要权限：** ohos.permission.ACCESS_NEARLINK
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;CdsmInfo&gt; | 否 | 回调函数，返回合作设备集合信息。 填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
 
 
**示例：**
 
```json
import { cdsm } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<cdsm.CdsmInfo> = (data: cdsm.CdsmInfo) => {
  console.info('CdsmInfo:' + JSON.stringify(data));
};

let addr: string = '00:11:22:33:AA:FF'; // 已配对连接的合作设备集合的成员设备地址
let client: cdsm.CdsmClient;
try {
  client = cdsm.createCdsmClient(addr); // 一个应用针对一个远端设备只需要创建一次实例
  client.onCdsmInfoChange(callback);
  client.offCdsmInfoChange(callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
 
  

##### CdsmInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示合作设备集合信息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| members | Array&lt;CdsmMemberInfo&gt; | 否 | 否 | 合作设备集合信息。 |
 
 
  

##### CdsmMemberInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示合作设备集合的成员信息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 成员设备地址。 |
| state | CdsmConnectionState | 否 | 否 | 成员设备连接状态。 |
 
 
  

##### CdsmConnectionState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示和远端设备的合作设备集合连接状态，为枚举值。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Communication.NearLink.Core
 
**起始版本：** 6.1.1(24)
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 表示已断连。 |
| CONNECTED | 1 | 表示已连接。 |
