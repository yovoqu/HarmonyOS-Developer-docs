# SafetyDetect（安全检测）

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


- 判断设备环境是否安全，比如是否被越狱、被模拟等，您可基于结果评估如何响应。
- 判断用户访问的URL是否为恶意网址，对于恶意网址，由您评估提示或拦截用户的访问风险。

**起始版本：** 5.0.0(12)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
```


## SysIntegrityRequest
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

系统完整性检测的请求参数。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nonce | string | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。 |


## SysIntegrityResponse
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

系统完整性检测返回值。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | string | 否 | 否 | JWS格式的系统完整性检测结果。JWS内容详见《Device Security Kit开发指南》中的系统完整性检测[开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sysintegrity-check#开发步骤)。 |


## UrlCheckRequest
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

URL检测请求参数。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| urls | Array&lt;string&gt; | 否 | 否 | 被检测的URL列表 |


## UrlCheckResponse
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

URL检测返回值。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| results | Array&lt;[UrlCheckResult](#urlcheckresult)&gt; | 否 | 否 | URL检测返回的检测结果 |


## UrlCheckResult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

URL检测结果详情。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 对应到输入参数中被检测的URL |
| threat | [UrlThreatType](#urlthreattype) | 否 | 否 | URL的威胁类型 |


## UrlThreatType
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

枚举URL威胁类型。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)


| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 未发现威胁。 |
| MALWARE | 1 | 恶意类型的URL。 |
| PHISHING | 2 | 钓鱼类型的URL |
| OTHERS | 3 | 其他威胁类型的URL |


## checkSysIntegrity
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

checkSysIntegrity(req: [SysIntegrityRequest](#sysintegrityrequest)): Promise<[SysIntegrityResponse](#sysintegrityresponse)>

获取本设备的系统完整性的在线检测结果。使用Promise异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iA9wlgUrTTuMxKKxfGfJNQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2819A8368986B4DF758B7B5617F9F82E2391587D5E6C243F9F3F31315C83A44F)
该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](#sysintegrityrequest) | 是 | 请求参数，包含nonce。          nonce长度必须16至66字节之间，有效值为base64编码范围。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[SysIntegrityResponse](#sysintegrityresponse)&gt; | Promise对象，返回系统完整性检测结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-arktsapi-errcode-safetydetect)。


| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters.          Possible causes:          1. Mandatory parameters are left unspecified.          2. Incorrect parameter types.          3. Parameter verification failed. |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |


**示例：**


```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求系统完整性检测，并处理结果
let req: safetyDetect.SysIntegrityRequest = {
  nonce: 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs', // 从服务器生成的随机的nonce值
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrity begin.');
  const data: safetyDetect.SysIntegrityResponse =
    await safetyDetect.checkSysIntegrity(req);
  hilog.info(
    0x0000,
    TAG,
    'Succeeded in checkSysIntegrity: %{public}s',
    data.result,
  );
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(
    0x0000,
    TAG,
    'CheckSysIntegrity failed: %{public}d %{public}s',
    e.code,
    e.message,
  );
}
```


## checkUrlThreat
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

checkUrlThreat(req: [UrlCheckRequest](#urlcheckrequest)): Promise<[UrlCheckResponse](#urlcheckresponse)>

检测URL是否为恶意网址。使用Promise异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/GSd7wPacQ6OA19vMUe2nyQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF250A859FC70F556B858CA1A044484D12D48FB1E29950C8131E13E4A72F4804)
该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [UrlCheckRequest](#urlcheckrequest) | 是 | 请求参数，包含被检测的URL列表。          传入的URL数量最多10个并且每个URL长度不大于4096字节。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[UrlCheckResponse](#urlcheckresponse)&gt; | Promise对象，返回URL检测结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-arktsapi-errcode-safetydetect)。


| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameters.          Possible causes:          1. Mandatory parameters are left unspecified.          2. Incorrect parameter types.          3. Parameter verification failed. |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |


**示例：**


```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求URL检测，并处理结果
let req: safetyDetect.UrlCheckRequest = {
  urls: ['https://test1.com'],
};
try {
  hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
  const data: safetyDetect.UrlCheckResponse =
    await safetyDetect.checkUrlThreat(req);
  hilog.info(
    0x0000,
    TAG,
    'Succeeded in checkUrlThreat: %{public}s %{public}d',
    data.results[0].url,
    data.results[0].threat,
  );
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(
    0x0000,
    TAG,
    'CheckUrlThreat failed: %{public}d %{public}s',
    e.code,
    e.message,
  );
}
```


## checkSysIntegrityOnLocal
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

checkSysIntegrityOnLocal(): Promise<string>

获取本设备的系统完整性的本地检测结果。使用Promise异步回调。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.1.0(18)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回JSON格式的系统完整性检测结果。JSON内容详见《Device Security Kit开发指南》中的本地系统完整性检测[开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sysintegrity-check-onlocal#开发步骤)。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-arktsapi-errcode-safetydetect)。


| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |


**示例：**


```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求本地系统完整性检测，并处理结果
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
  const result: string = await safetyDetect.checkSysIntegrityOnLocal();
  hilog.info(
    0x0000,
    TAG,
    'Succeeded in checkSysIntegrityOnLocal: %{public}s',
    result,
  );
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(
    0x0000,
    TAG,
    'CheckSysIntegrityOnLocal failed: %{public}d %{public}s',
    e.code,
    e.message,
  );
}
```


## checkSysIntegrityEnhanced
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

checkSysIntegrityEnhanced(req: [SysIntegrityRequest](#sysintegrityrequest)): Promise<[SysIntegrityResponse](#sysintegrityresponse)>

获取本设备的系统完整性的在线增强检测结果。使用Promise异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/7y_4lOmMTqyoUFjl9lZfUg/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A956184F66F804F9C0AE1A395E4C5FDAEA77703E98D7034B8863E50BDB476F4C)
该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 6.0.0(20)

**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](#sysintegrityrequest) | 是 | 请求参数，包含nonce。          nonce长度必须16至66字节之间，有效值为base64编码范围。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[SysIntegrityResponse](#sysintegrityresponse)&gt; | Promise对象，返回系统完整性增强检测结果。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-arktsapi-errcode-safetydetect)。


| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |


**示例：**


```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求系统完整性增强检测，并处理结果
let req: safetyDetect.SysIntegrityRequest = {
  nonce: 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs', // 从服务器生成的随机的nonce值
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityEnhanced begin.');
  const data: safetyDetect.SysIntegrityResponse =
    await safetyDetect.checkSysIntegrityEnhanced(req);
  hilog.info(
    0x0000,
    TAG,
    'Succeeded in checkSysIntegrityEnhanced: %{public}s',
    data.result,
  );
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(
    0x0000,
    TAG,
    'CheckSysIntegrityEnhanced failed: %{public}d %{public}s',
    e.code,
    e.message,
  );
}
```
