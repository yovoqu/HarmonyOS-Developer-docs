# DeviceVerify（应用设备状态检测）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-api
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供应用设备状态检测能力，对应用在某台设备上的使用状态进行管理和检测，用于判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等的状态检测，以支撑业务进行新用户营销活动。
 
**起始版本：** 5.0.0(12)
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { deviceCertificate } from '@kit.DeviceSecurityKit';
```
 
  

#### getDeviceToken

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDeviceToken(): Promise&lt;string&gt;
 
获取本设备的DeviceToken。使用Promise异步回调。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/rIMe9U3PS_iAEK9ub091UQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260730T071610Z&HW-CC-Expire=86400&HW-CC-Sign=0C0766C0A4135CA926976F587C2FD08712B4A9CE1BA4006ADEB668FBB98C78C6)
 
 
该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。
  

 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Security.DeviceCertificate
 
**起始版本：** 5.0.0(12)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回本设备的DeviceToken。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-deviceverify)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 201 | has no permission. |
| 1003300005 | internal error. |
| 1003300006 | access cloud server fail. |
 
 
**示例：**
 
```text
import { deviceCertificate } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "DeviceCertificateJsTest";

// 请求deviceToken，并处理结果
try {
  deviceCertificate.getDeviceToken().then((token) => {
    hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
    // 开发者处理deviceToken
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
}
```
