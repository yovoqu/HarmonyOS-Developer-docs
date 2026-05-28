# realNameService(身份验证服务)

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-realnameservice
**支持设备：** Phone | PC/2in1 | Tablet

本模块提供身份验证服务，包括“实名信息验证”、“实名信息授权”和“人脸核身实人验证”三种功能。
 
**模型约束：** 本模块接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Payment.RealNameService
 
**起始版本：** 5.1.1(19)
  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { realNameService } from '@kit.PaymentKit';
```
 
  

##### startRealNameVerification

**支持设备：** Phone | PC/2in1 | Tablet

startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise&lt;string&gt;
 
该方法提供实名信息验证功能，调用该方法后会拉起实名信息验证授权组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。
 
**模型约束**：此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Payment.RealNameService
 
**起始版本：** 5.1.1(19)
 
**参数**：
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext \| common.UIExtensionContext | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考实名信息预验证。 |
 
 
**返回值**：
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回实名信息验证ID，用于实名信息验证结果查询。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |
 
 
**示例**：
 
示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)
 
```text
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartRealNameVerificationPromise() {
    // 请使用开发者真实的预验证ID（preVerifyId）
    let preVerifyId = 'your_pre_verify_id';
    realNameService.startRealNameVerification(this.context, preVerifyId)
      .then((verifyResultId: string) => {
        // 验证成功
        console.info(`succeeded in verifying, verifyResultId: ${verifyResultId}`);
      })
  }

  build() {
    Column() {
      Button('requestStartRealNameVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartRealNameVerificationPromise();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 
  

##### startRealNameAuth

**支持设备：** Phone | PC/2in1 | Tablet

startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise&lt;string&gt;
 
该方法提供实名信息授权功能，调用该方法后会拉起实名信息授权组件，授权完成后使用Promise异步返回。调用该方法前请确保网络已连接。
 
**模型约束**：此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Payment.RealNameService
 
**起始版本：** 5.1.1(19)
 
**参数**：
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext \| common.UIExtensionContext | 是 | UIAbility上下文。 |
 
 
**返回值**：
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回实名信息授权ID，用于实名信息授权结果查询。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
 
 
**示例**：
 
示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)
 
```text
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartRealNameAuthPromise() {
    realNameService.startRealNameAuth(this.context)
      .then((realNameAuthId: string) => {
        // 授权成功
        console.info(`succeeded in authorizing, realNameAuthId: ${realNameAuthId}`);
      })
  }

  build() {
    Column() {
      Button('requestStartRealNameAuthPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartRealNameAuthPromise();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 
  

##### startFaceVerification

**支持设备：** Phone | PC/2in1 | Tablet

startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise&lt;string&gt;
 
该方法提供人脸核身实人验证功能，调用该方法后会拉起人脸核身实人验证组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。
 
**模型约束**：此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Payment.RealNameService
 
**起始版本：** 5.1.1(19)
 
**参数**：
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext \| common.UIExtensionContext | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考人脸核身实人预验证。 |
 
 
**返回值**：
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回验证结果ID，用于人脸核身实人验证结果查询。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100006 | The camera permission is not granted. |
| 1020100007 | The liveness detection failed. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |
 
 
**示例**：
 
示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)
 
```text
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartFaceVerificationPromise() {
    // 请使用开发者真实的预验证ID（preVerifyId）
    let preVerifyId = 'your_pre_verify_id';
    realNameService.startFaceVerification(this.context, preVerifyId)
      .then((verifyResultId:string) => {
        // 人脸验证成功
        console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
      })
  }

  build() {
    Column() {
      Button('requestStartFaceVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartFaceVerificationPromise();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
