# 通行密钥身份认证（ArkTS）

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-passkey-arkts

##### 接口说明

通行密钥服务主要接口如下表。

| 接口名 | 描述 |
| --- | --- |
| getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>> | 查询当前设备支持的客户端能力列表。 |
| getPlatformAuthenticators(context: common.Context): Promise<Array&lt;AuthenticatorMetadata&gt;> | 查询当前设备支持的平台认证器能力列表（人脸、指纹、PIN码）。 |
| register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAttestationCredential&gt; | 进行通行密钥的注册。 |
| authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAssertionCredential&gt; | 进行通行密钥的认证。 |




##### 开发步骤

通行密钥服务提供基于FIDO2标准协议的FIDO客户端实现，这里仅演示FIDO客户端相关API的使用，涉及FIDO服务器的相关处理由开发者自行实现，请参考[FIDO2标准协议](https://fidoalliance.org/passkeys/)（见[网站链接免责声明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-website-disclaimer)）。
1. 需要业务方自行根据FIDO2标准协议部署FIDO服务器。
2. 导入相关模块。

  
```text
import { common } from '@kit.AbilityKit';
import { fido2 } from '@kit.OnlineAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

3. 注册通行密钥。

  
 - 获取能力信息，调用getClientCapabilities接口获取客户端能力列表，并且调用getPlatformAuthenticators接口获取平台认证器能力信息。         
```text
@Entry
@Component
struct PasskeyInvokePage {
  private uiContext = this.getUIContext().getHostContext();

  private async invokeGetClientCapabilities() {
    try {
      // 获取客户端能力列表
      let clientCapabilities: Map<fido2.ClientCapability, boolean> = await fido2.getClientCapabilities(this.uiContext);
      console.info('Succeeded in doing getClientCapabilities.');
      // 业务处理clientCapabilities
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to call getClientCapabilities. Code is ${err.code}, message is ${err.message}`);
      // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
    }
  }

  private async invokeGetPlatformAuthenticators() {
    try {
      // 获取平台认证器能力
      let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
        await fido2.getPlatformAuthenticators(this.uiContext);
      console.info('Succeeded in doing getPlatformAuthenticators.');
      // 业务处理platformAuthenticators
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to call getPlatformAuthenticators. Code is ${err.code}, message is ${err.message}`);
      // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
    }
  }

  build() {
    // 业务UI界面
  }
}
```


4. 访问FIDO服务器，获取注册报文，调用register接口进行注册。         
```text
// pkOptions为应用从FIDO服务端获取的注册报文，credentialCreationOp为应用组装注册信息
let credentialCreationOp: fido2.CredentialCreationOptions = {
  publicKey: pkOptions
};

try {
  // 调用register进行通行密钥注册
  let publicKeyAttestationCredential: fido2.PublicKeyAttestationCredential =
    await fido2.register(this.uiContext, credentialCreationOp);
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`Failed to call register error code is ${code}, message is ${message}`);
  // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
}
```


5. 应用使用注册结果（publicKeyAttestationCredential）组装注册响应报文，发送至FIDO服务端进行验证，获取注册结果报文。
 - 使用通行密钥进行身份认证。

1. 获取能力信息，调用getClientCapabilities接口获取客户端能力列表，并且调用getPlatformAuthenticators接口获取平台认证器能力信息。         
```text
@Entry
@Component
struct PasskeyInvokePage {
  private uiContext = this.getUIContext().getHostContext();

  private async invokeGetClientCapabilities() {
    try {
      // 获取客户端能力列表
      let clientCapabilities: Map<fido2.ClientCapability, boolean> = await fido2.getClientCapabilities(this.uiContext);
      console.info('Succeeded in doing getClientCapabilities.');
      // 业务处理clientCapabilities
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to call getClientCapabilities. Code is ${err.code}, message is ${err.message}`);
      // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
    }
  }

  private async invokeGetPlatformAuthenticators() {
    try {
      // 获取平台认证器能力
      let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
        await fido2.getPlatformAuthenticators(this.uiContext);
      console.info('Succeeded in doing getPlatformAuthenticators.');
      // 业务处理platformAuthenticators
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to call getPlatformAuthenticators. Code is ${err.code}, message is ${err.message}`);
      // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
    }
  }

  build() {
    // 业务UI界面
  }
}
```


2. 访问FIDO服务器，获取认证报文，调用authenticate接口进行认证。         
```text
// authPub为应用从FIDO服务端获取的认证报文，authCredentialRequestOptions为应用组装的认证信息
let authCredentialRequestOptions: fido2.CredentialRequestOptions = {
  publicKey: authPub,
  mediation: 'optional' as fido2.CredentialMediationRequirement
};

try {
  // 调用authenticate接口进行认证
  let pkAssertionCredential: fido2.PublicKeyAssertionCredential =
    await fido2.authenticate(this.uiContext, authCredentialRequestOptions);
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`Failed to call authenticateerror code is ${code}, message is ${message}`);
  // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考
}
```


3. 应用使用认证结果（pkAssertionCredential）组装认证响应报文，发送至FIDO服务端进行验证，获取认证结果报文。
