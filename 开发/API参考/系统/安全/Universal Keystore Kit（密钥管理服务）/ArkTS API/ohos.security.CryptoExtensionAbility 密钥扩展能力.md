# @ohos.security.CryptoExtensionAbility (密钥扩展能力)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoextensionability
**支持设备：** Phone | PC/2in1 | Tablet

模块提供外部密钥扩展能力，包括资源管理、PIN码认证管理、密码操作、通用操作等接口能力。

ExtensionAbility功能与约束：
1. 设备管理，单个ExtensionAbility实现，最多支持10个UKey接入。
2. 句柄管理，针对同一个UKey资源（例如，容器下的密钥），支持应用维度资源句柄管理。      
支持多个HarmonyOS应用，打开同一个UKey密钥资源。例如：HarmonyOS应用1打开容器A后，HarmonyOS应用2也可以再次打开容器A。
3. 支持多个HarmonyOS应用，操作同一个UKey密钥资源。例如：HarmonyOS应用1操作容器A中的私钥签名后，HarmonyOS应用2也验证PIN码后，也可以操作容器A中的私钥进行签名，两者互不影响。
4. 密钥会话管理，支持三段式密钥管理操作，单次签名验签需通过[onInitSession](#oninitsession)/[onUpdateSession](#onupdatesession)/[onFinishSession](#onfinishsession)三个函数三步配合完成，需支持会话管理，缓存密钥会话状态。      
init操作，初始化密钥会话，并返回会话句柄信息。
5. update操作，传入分组数据，对分组数据进行密码操作，更新密钥会话信息后，将中间数据（如果有）返回。
6. finish操作，对传入最后一段分组数据，进行密钥返回操作，并结束密钥会话，将最终结果返回。
7. 认证状态管理，支持应用维度的认证状态管理。针对同一个UKey中的应用A，HarmonyOS应用1验证UKey应用A的PIN码后，HarmonyOS应用2如果要访问UKey应用A，也需要进行PIN码认证操作。
8. 证书查询，支持根据证书类型，枚举所有证书或查询单个容器中的证书。

> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet

CryptoExtensionAbility作为密钥管理扩展能力，为减少安全攻击面，保障CryptoExtensionAbility合理实现，系统对网络、蓝牙、位置等能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { huks, huksExternalCrypto, CryptoExtensionAbility } from '@kit.UniversalKeystoreKit';
```



#### HuksCryptoExtensionResultCode

**支持设备：** Phone | PC/2in1 | Tablet

[HuksCryptoExtensionResult](#hukscryptoextensionresult)中的resultCode枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL | 34800000 | 密钥扩展错误。可能的原因： 1. 输入参数无效。 2. 密钥扩展出现无法解决的错误状态。 |
| HUKS_CRYPTO_EXTENSION_ERR_UKEY_NOT_EXIST | 34800001 | UKey不存在。可能的原因： 1. UKey已被移除。 2. 密钥扩展陷入错误的UKey状态。 |
| HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL | 34800002 | UKey驱动出现未知错误。 |
| HUKS_CRYPTO_EXTENSION_ERR_PIN_NO_AUTH | 34800003 | UKey PIN码未认证，需要先通过onAuthUkeyPin认证UKey PIN码。 |
| HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST | 34800004 | 句柄不存在。可能的原因： 1. 句柄无效。 2. HUKS服务和密钥扩展的状态不一致。由于异常情况，HUKS服务持有的句柄未能释放。 |
| HUKS_CRYPTO_EXTENSION_ERR_HANDLE_UNAVAILABLE | 34800005 | 句柄不可用。可能的原因： 密钥扩展和UKey的状态不一致。 |
| HUKS_CRYPTO_EXTENSION_ERR_PIN_INCORRECT | 34800006 | UKey PIN码错误，需要检查输入的PIN码。 |
| HUKS_CRYPTO_EXTENSION_ERR_PIN_LOCKED | 34800007 | UKey PIN码被锁定。可能的原因： PIN码输入错误次数过多。 |




#### HuksCryptoExtensionCertInfo

**支持设备：** Phone | PC/2in1 | Tablet

[HuksCryptoExtensionResult](#hukscryptoextensionresult)中的certs数组中的元素。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| purpose | certificateManager.CertificatePurpose | 否 | 否 | 表示证书链对应密钥的使用类型。 |
| resourceId | string | 否 | 否 | 资源ID。JSON格式，能够映射到UKey中的某个资源。 |
| cert | Uint8Array | 否 | 否 | 证书。 |




#### HuksCryptoExtensionResult

**支持设备：** Phone | PC/2in1 | Tablet

接口返回值的通用类型。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 否 | 否 | 返回值的错误码。 |
| handle | string | 否 | 是 | 资源句柄。 |
| authState | number | 否 | 是 | 认证状态。 |
| retryCount | number | 否 | 是 | 重试次数，表示PIN码认证剩余可用次数，为0时表示无剩余重试机会。 |
| certs | Array&lt;HuksCryptoExtensionCertInfo&gt; | 否 | 是 | 证书。 |
| property | Array<huksExternalCrypto.HuksExternalCryptoParam> | 否 | 是 | 属性。 |
| outData | Uint8Array | 否 | 是 | 返回的数据。 |
| resourceId | string | 否 | 是 | 返回的资源ID。默认值为空。 起始版本： 26.0.0 模型约束： 此接口仅可在Stage模型下使用。 |
| errInfo | huksExternalCrypto.HuksExternalErrorInfo | 否 | 是 | 返回的详细错误信息。默认值为{0,""}。 起始版本： 26.0.0 模型约束： 此接口仅可在Stage模型下使用。 |




#### HuksCryptoExtensionParam

**支持设备：** Phone | PC/2in1 | Tablet

密钥扩展操作参数，用于指定操作的属性标签和对应值。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tag | huksExternalCrypto.HuksExternalCryptoTag \| huks.HuksTag \| number | 否 | 否 | 标签。 |
| value | boolean \| number \| bigint \| Uint8Array | 否 | 否 | 标签对应值。 |




#### HuksCryptoExtensionParams

**支持设备：** Phone | PC/2in1 | Tablet

密钥扩展操作参数集合，用于传递操作所需的属性和输入数据。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties | HuksCryptoExtensionParam[] | 否 | 否 | 属性，用于存储HuksCryptoExtensionParam的数组。默认为undefined。 |
| inData | Uint8Array | 否 | 是 | 输入数据。默认为undefined。 |




#### CryptoExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet

密钥扩展能力类，提供外部密钥管理扩展所需接口定义，包括打开/关闭资源、PIN码认证管理、密钥会话操作、证书管理、密钥生成与导入、通用操作等接口能力。驱动厂商需继承CryptoExtensionAbility并实现相关接口，通过[registerProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptoregisterprovider)完成能力注册后，由HUKS和证书管理将对应的密钥管理扩展能力开放给应用使用。

CryptoExtensionAbility可以隔离不同的UKey驱动厂商实现的差异。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension



#### onOpenResource

**支持设备：** Phone | PC/2in1 | Tablet

onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

根据参数中的resourceId，打开UKey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，handle携带资源句柄信息。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800001 UKey不存在。 34800002 UKey驱动错误。 34800004 句柄不存在。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析resourceId，打开底层句柄，并映射为新的句柄返回。
    let result: HuksCryptoExtensionResult = {
      resultCode: 0,
      handle: "test handle"
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onCloseResource

**支持设备：** Phone | PC/2in1 | Tablet

onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

根据参数中的handle，关闭UKey的密钥资源。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示关闭资源成功。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 执行句柄关闭操作。如果需要关闭底层句柄，则执行关闭操作。
    const result: HuksCryptoExtensionResult = {
        resultCode: 0,
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onGetProperty

**支持设备：** Phone | PC/2in1 | Tablet

onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

根据参数中的handle和propertyId获取属性。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| propertyId | string | 是 | 查找操作的属性名称，是GMT 0016-2023中定义的SKF接口名，要业务针对接口名适配。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的property成员非空，包含获取到的属性，由HUKS_EXT_CRYPTO_TAG_EXTRA_DATA参数携带。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800003 UKey PIN码未认证。 34800004 句柄不存在。 34800005 句柄不可用。 34800007 UKey PIN码被锁定。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 按照propertyId执行相关函数，函数参数从params中获取。输出数据封装到返回值的property字段中，由HUKS_EXT_CRYPTO_TAG_EXTRA_DATA携带。
    const emptyArray: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      property: emptyArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onSetProperty

**支持设备：** Phone | PC/2in1 | Tablet

onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

根据参数中的handle和propertyId设置属性。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| propertyId | string | 是 | 设置操作的属性名称，推荐使用GMT 0016-2023中定义的SKF接口名作为属性ID。 |
| params | HuksCryptoExtensionParam[] | 是 | 传入的参数，包含与propertyId相关的操作参数。应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示设置属性成功。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。可能的原因： 1. 输入参数无效。 2. 密钥扩展出现无法解决的错误状态。 34800002 UKey驱动错误。 34800003 UKey PIN码未认证，需要先认证UKey PIN码。 34800004 句柄不存在。可能的原因： 1. 句柄无效。 2. HUKS服务和密钥扩展的状态不一致。由于异常情况，HUKS服务持有的句柄未能释放。 34800005 句柄不可用。可能的原因： 密钥扩展和UKey的状态不一致。 34800007 UKey PIN码被锁定。可能的原因： PIN码输入错误次数过多。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 按照propertyId执行相关设置操作，操作参数从params中获取。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onAuthUkeyPin

**支持设备：** Phone | PC/2in1 | Tablet

onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

请求UKey认证PIN码。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，authState非0，表示认证请求成功。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 34800006 UKey PIN码错误。 34800007 UKey PIN码被锁定。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 执行PIN码认证操作，并且维护应用的PIN码认证状态。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      authState: 1
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onGetUkeyPinAuthState

**支持设备：** Phone | PC/2in1 | Tablet

onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

获取UKey的PIN码认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，HuksCryptoExtensionResult的authState成员非空，为获取的PIN码认证状态。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 查询PIN码认证状态。
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      authState: 1
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onClearUkeyPinAuthState

**支持设备：** Phone | PC/2in1 | Tablet

onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

清除应用维度PIN码的认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 会话句柄。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示清除PIN码认证状态成功。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onInitSession

**支持设备：** Phone | PC/2in1 | Tablet

onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise&lt;HuksCryptoExtensionResult&gt;

三段式初始化密钥会话操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 资源句柄。 |
| params | huks.HuksOptions \| HuksCryptoExtensionParams | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，handle成员非空。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800003 UKey PIN码未认证。 34800004 句柄不存在。 34800005 句柄不可用。 34800007 UKey PIN码被锁定。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      handle: "test handle"
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onUpdateSession

**支持设备：** Phone | PC/2in1 | Tablet

onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise&lt;HuksCryptoExtensionResult&gt;

三段式密钥会话更新数据操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | huks.HuksOptions \| HuksCryptoExtensionParams | 是 | 传入的参数，应用身份通过HUKS_EXT_CRYPTO_TAG_UID参数携带。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800003 UKey PIN码未认证。 34800004 句柄不存在。 34800005 句柄不可用。 34800007 UKey PIN码被锁定。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    let outBuffer: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: outBuffer
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onFinishSession

**支持设备：** Phone | PC/2in1 | Tablet

onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise&lt;HuksCryptoExtensionResult&gt;

三段式密钥会话结束操作。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| initHandle | string | 是 | 资源句柄。 |
| params | huks.HuksOptions \| HuksCryptoExtensionParams | 是 | 传入的参数，应用身份可通过HUKS_EXT_CRYPTO_TAG_UID参数携带，还包括算法参数（算法类型、填充模式等）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800003 UKey PIN码未认证。 34800004 句柄不存在。 34800005 句柄不可用。 34800007 UKey PIN码被锁定。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, HuksCryptoExtensionParams, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
    let outBuffer: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: outBuffer
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onExportCertificate

**支持设备：** Phone | PC/2in1 | Tablet

onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

查询指定resourceId下的证书。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID。会附带在HuksCryptoExtensionCertInfo中。 |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 否 | 操作属性。默认获取签名类型的证书，也可以通过参数HUKS_EXT_CRYPTO_TAG_PURPOSE指定获取证书类型，支持的类型包括签名验签、加解密等。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，certs成员非空，包含获取的单本证书。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800001 UKey不存在。 34800002 UKey驱动错误。 34800004 句柄不存在。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionResult,
  HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      certs: certInfoSetArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onEnumCertificates

**支持设备：** Phone | PC/2in1 | Tablet

onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

枚举Extension下所有UKey设备的证书信息。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<huksExternalCrypto.HuksExternalCryptoParam> \| HuksCryptoExtensionParam[] | 否 | 操作属性。默认获取签名类型的证书，也可以通过参数HUKS_EXT_CRYPTO_TAG_PURPOSE指定获取证书类型，支持的类型包括签名验签、加解密等。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，certs成员非空，包含获取的所有证书。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800001 UKey不存在。 34800002 UKey驱动错误。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huksExternalCrypto, HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      certs: certInfoSetArray
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onGetResourceId

**支持设备：** Phone | PC/2in1 | Tablet

onGetResourceId(params: HuksCryptoExtensionParam[]):Promise&lt;HuksCryptoExtensionResult&gt;

获取外部扩展设备内的资源ID。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | HuksCryptoExtensionParam[] | 是 | 获取资源ID所需的属性参数。必选TAG包括：HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO（厂商自定义的资源信息）、HUKS_EXT_CRYPTO_TAG_UID（调用方身份）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，resourceId携带资源ID信息。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { HuksCryptoExtensionParam, CryptoExtensionAbility, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGetResourceId(params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      resourceId: "test resourceId"
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onImportCertificate

**支持设备：** Phone | PC/2in1 | Tablet

onImportCertificate(handle: string, params: HuksCryptoExtensionParam[], certInfo: HuksCryptoExtensionCertInfo): Promise&lt;HuksCryptoExtensionResult&gt;

导入指定资源句柄的证书。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 导入证书的资源句柄。 |
| params | HuksCryptoExtensionParam[] | 是 | 导入证书所需的属性参数。 |
| certInfo | HuksCryptoExtensionCertInfo | 是 | 待导入的证书信息。需指定证书类型（purpose）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示导入证书成功。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800001 UKey不存在。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { CryptoExtensionAbility, HuksCryptoExtensionParam, HuksCryptoExtensionResult,
  HuksCryptoExtensionCertInfo } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onImportCertificate(handle: string, params: HuksCryptoExtensionParam[],
      certInfo: HuksCryptoExtensionCertInfo): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onGenerateKeyItem

**支持设备：** Phone | PC/2in1 | Tablet

onGenerateKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

用于在扩展设备内生成密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待生成密钥的资源句柄。 |
| params | HuksCryptoExtensionParam[] | 是 | 密钥生成操作的属性参数。必选TAG：HUKS_EXT_CRYPTO_TAG_UID（调用方身份）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示生成密钥成功。调用失败时，resultCode携带错误码信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onGenerateKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数
    let algorithm: huks.HuksKeyAlg | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
    let keySize: huks.HuksKeySize | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入参数，设置默认值
    if (algorithm === undefined) {
      algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA; // 默认RSA算法
    }
    if (keySize === undefined) {
      keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048; // 默认2048位
    }
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN; // 默认签名用途
    }

    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onExportKeyItem

**支持设备：** Phone | PC/2in1 | Tablet

onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise&lt;HuksCryptoExtensionResult&gt;

用于导出指定密钥的公钥。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待导出公钥的资源句柄。 |
| params | HuksCryptoExtensionParam[] | 是 | 导出公钥操作的属性参数。必选TAG：HUKS_EXT_CRYPTO_TAG_UID（调用方身份）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，outData携带导出的公钥数据。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';

export default class CryptoExtension extends CryptoExtensionAbility {
  onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数，推荐传入密钥用途
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入用途参数，设置默认值（推荐默认签名用途）
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;
    }

    let pubKey: Uint8Array = new Uint8Array(1024);
    const result: HuksCryptoExtensionResult = {
      resultCode: 0,
      outData: pubKey
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### onImportWrappedKeyItem

**支持设备：** Phone | PC/2in1 | Tablet

onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[], wrappedKey: Uint8Array): Promise&lt;HuksCryptoExtensionResult&gt;

用于导入加密封装的密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | string | 是 | 待导入密钥的资源句柄。 |
| wrappingHandle | string | 是 | 用于解封导入密钥的密钥资源句柄。 |
| params | HuksCryptoExtensionParam[] | 是 | 导入封装密钥操作的属性参数。必选TAG：HUKS_EXT_CRYPTO_TAG_UID（调用方身份）。 |
| wrappedKey | Uint8Array | 是 | 封装密钥数据，格式由密钥扩展定义。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksCryptoExtensionResult&gt; | Promise对象。当调用成功时，resultCode为0，表示导入密钥成功。调用失败时，resultCode携带错误码信息，errInfo携带详细错误信息。 可能返回的错误码值： 34800000 密钥扩展错误。 34800002 UKey驱动错误。 34800004 句柄不存在。 34800005 句柄不可用。 具体含义可查询HuksCryptoExtensionResultCode。 |


**示例：**

```text
import { huks, CryptoExtensionAbility, HuksCryptoExtensionResult, HuksCryptoExtensionParam } from '@kit.UniversalKeystoreKit';
export default class CryptoExtension extends CryptoExtensionAbility {
  onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[], wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult> {
    // 解析可选参数
    let algorithm: huks.HuksKeyAlg | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
    let keySize: huks.HuksKeySize | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
    let purpose: huks.HuksKeyPurpose | undefined = params.find(
      param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

    // 如未传入参数，设置默认值
    if (algorithm === undefined) {
      algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA;
    }
    if (keySize === undefined) {
      keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
    }
    if (purpose === undefined) {
      purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT;
    }

    const result: HuksCryptoExtensionResult = {
      resultCode: 0
    };

    // ...
    return Promise.resolve(result);
  }
}
```



#### 附录

**支持设备：** Phone | PC/2in1 | Tablet

CryptoExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | @ohos.wantAgent (WantAgent模块) |
| Ads Kit | @ohos.advertising.AdComponent (广告展示组件) |
| Ads Kit | @ohos.advertising.AdsServiceExtensionAbility(广告扩展服务) |
| Ads Kit | @ohos.advertising.AutoAdComponent (轮播广告展示组件) |
| Ads Kit | @ohos.advertising (广告服务框架) |
| AppGallery Kit | appInfoManager（应用元数据管理服务） |
| AppGallery Kit | attributionManager（应用归因服务） |
| AppGallery Kit | attributionTestManager（应用归因接入调试功能） |
| AppGallery Kit | commentManager（应用评论服务） |
| AppGallery Kit | moduleInstallManager (产品特性按需分发) |
| AppGallery Kit | privacyManager（隐私管理服务） |
| AppGallery Kit | productViewManager（应用市场推荐） |
| AppGallery Kit | updateManager（更新功能） |
| AR Engine Kit | arEngine（AR增强现实能力） |
| AR Engine Kit | ARView（AR场景可视化） |
| ArkUI | @ohos.atomicservice.AtomicServiceNavigation (AtomicServiceNavigation) |
| ArkUI | @ohos.atomicservice.AtomicServiceSearch (AtomicServiceSearch) |
| ArkUI | @ohos.atomicservice.AtomicServiceTabs (AtomicServiceTabs) |
| ArkUI | @ohos.atomicservice.AtomicServiceWeb (AtomicServiceWeb) |
| ArkUI | @ohos.atomicservice.HalfScreenLaunchComponent (HalfScreenLaunchComponent) |
| ArkUI | @ohos.atomicservice.InterstitialDialogAction (InterstitialDialogAction) |
| ArkUI | @ohos.atomicservice.NavPushPathHelper (NavPushPathHelper) |
| ArkUI | @ohos.PiPWindow (画中画窗口) |
| ArkUI | @ohos.mediaquery (媒体查询) |
| ArkUI | @ohos.screenshot (屏幕截图) |
| ArkWeb | @ohos.web.netErrorList (ArkWeb网络协议栈错误列表) |
| ArkWeb | @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability) |
| ArkWeb | @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context) |
| ArkWeb | @ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager) |
| ArkWeb | @ohos.web.webview |
| ArkWeb | @ohos.web.webview (WebView) |
| Audio Kit | @ohos.multimedia.audioHaptic (音振协同) |
| Audio Kit | @ohos.multimedia.systemSoundManager (系统声音管理) |
| Audio Kit | @ohos.multimedia.avVolumePanel (音量面板) |
| AVSession Kit | @ohos.multimedia.avCastPicker (投播组件) |
| AVSession Kit | @ohos.multimedia.avCastPickerParam (投播组件参数) |
| AVSession Kit | @ohos.multimedia.avInputCastPicker (录音设备选择组件) |
| Basic Service Kit | @ohos.pasteboard (剪贴板) |
| Basic Service Kit | @ohos.scan (扫描) |
| Basic Service Kit | @ohos.screenLock (锁屏管理) |
| Basic Service Kit | @ohos.wallpaper (壁纸) |
| Basic Service Kit | @ohos.settings (设置数据项名称) |
| Calendar Kit | @ohos.calendarManager (日程管理能力) |
| Call Service Kit | CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability) |
| Call Service Kit | CallerInfoQueryExtensionContext（来去电信息查询扩展Context） |
| Call Service Kit | voipCall（应用内通话管理） |
| Camera Kit | @ohos.multimedia.cameraPicker (相机选择器) |
| Cloud Foundation Kit | cloudCommon (公共模块) |
| Cloud Foundation Kit | cloudDatabase (云数据库模块) |
| Cloud Foundation Kit | cloudFunction (云函数模块) |
| Cloud Foundation Kit | cloudResPrefetch（预加载模块） |
| Cloud Foundation Kit | cloudStorage (云存储模块) |
| Connectivity Kit | @ohos.bluetooth.a2dp (蓝牙a2dp模块) |
| Connectivity Kit | @ohos.bluetooth.access (蓝牙access模块) |
| Connectivity Kit | @ohos.bluetooth.baseProfile (蓝牙baseProfile模块) |
| Connectivity Kit | @ohos.bluetooth.ble (蓝牙ble模块) |
| Connectivity Kit | @ohos.bluetooth.common (蓝牙common模块) |
| Connectivity Kit | @ohos.bluetooth.connection (蓝牙connection模块) |
| Connectivity Kit | @ohos.bluetooth.constant (蓝牙constant模块) |
| Connectivity Kit | @ohos.bluetooth (蓝牙) |
| Connectivity Kit | @ohos.bluetooth.hfp (蓝牙hfp模块) |
| Connectivity Kit | @ohos.bluetooth.hid (蓝牙hid模块) |
| Connectivity Kit | @ohos.bluetoothManager (蓝牙) |
| Connectivity Kit | @ohos.bluetooth.map (蓝牙map模块) |
| Connectivity Kit | @ohos.bluetooth.pan (蓝牙pan模块) |
| Connectivity Kit | @ohos.bluetooth.pbap (蓝牙pbap模块) |
| Connectivity Kit | @ohos.bluetooth.socket (蓝牙socket模块) |
| Connectivity Kit | @ohos.connectedTag (有源标签) |
| Connectivity Kit | @ohos.nfc.cardEmulation (标准NFC-cardEmulation) |
| Connectivity Kit | @ohos.nfc.controller (标准NFC) |
| Connectivity Kit | @ohos.nfc.tag (标准NFC-Tag) |
| Connectivity Kit | @ohos.wifi (WLAN) |
| Connectivity Kit | @ohos.wifiext (WLAN扩展接口) |
| Connectivity Kit | @ohos.wifiManager (WLAN) |
| Connectivity Kit | @ohos.wifiManagerExt (WLAN扩展接口) |
| Contacts Kit | @ohos.contact (联系人) |
| Core Speech Kit | speechRecognizer（语音识别） |
| Core Speech Kit | textToSpeech（文本转语音） |
| Core Vision Kit | faceComparator（人脸比对） |
| Core Vision Kit | faceDetector（人脸检测） |
| Core Vision Kit | textRecognition（文字识别） |
| Core Vision Kit | objectDetection（多目标识别） |
| Core Vision Kit | skeletonDetection（骨骼点检测） |
| Core Vision Kit | subjectSegmentation（主体分割） |
| Core Vision Kit | visionBase（Core Vision Kit基类） |
| Data Protection Kit | @ohos.dlpPermission (数据防泄漏) |
| Distributed Service Kit | @ohos.distributedDeviceManager (设备管理) |
| Distributed Service Kit | @ohos.distributedsched.abilityConnectionManager (应用多端协同管理) |
| Distributed Service Kit | @ohos.distributedsched.linkEnhance (增强连接) |
| Distributed Service Kit | @ohos.distributedsched.proxyChannelManager (代理通道管理) |
| DRM Kit | @ohos.multimedia.drm |
| Form Kit | @ohos.app.form.formBindingData (卡片数据绑定类) |
| Form Kit | @ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility) |
| Form Kit | @ohos.app.form.FormExtensionAbility (FormExtensionAbility) |
| Form Kit | @ohos.app.form.formInfo (formInfo) |
| Form Kit | @ohos.app.form.formProvider (formProvider) |
| Game Service Kit | gameNearbyTransfer（游戏近场快传） |
| Game Service Kit | gamePerformance（游戏场景感知） |
| Game Service Kit | gamePlayer（基础游戏服务） |
| Graphics Accelerate Kit | AssetAccelerationExtensionAbility（资源加速ExtensionAbility） |
| Graphics Accelerate Kit | AssetAccelerationExtensionContext（资源加速ExtensionContext） |
| Graphics Accelerate Kit | assetDownloadManager（资源包下载管理） |
| Graphics Accelerate Kit | launchAcceleration（游戏启动加速） |
| Image Kit | @ohos.multimedia.sendableImage (基于Sendable对象的图片处理) |
| Image Kit | @ohos.multimedia.videoProcessingEngine (视频处理引擎) |
| Intents Kit | InsightIntentUIExtensionAbility (意图调用UI扩展能力) |
| Location Kit | @ohos.geolocation (位置服务) |
| Location Kit | @ohos.geoLocationManager (位置服务) |
| Live View Kit | LiveViewLockScreenExtensionAbility |
| Live View Kit | LiveViewLockScreenExtensionContext |
| Live View Kit | liveViewManager |
| MDM Kit | @ohos.enterprise.accountManager（账号管理） |
| MDM Kit | @ohos.enterprise.adminManager（admin权限管理） |
| MDM Kit | @ohos.enterprise.applicationManager（应用管理） |
| MDM Kit | @ohos.enterprise.bluetoothManager（蓝牙管理） |
| MDM Kit | @ohos.enterprise.browser（浏览器管理） |
| MDM Kit | @ohos.enterprise.bundleManager（包管理） |
| MDM Kit | @ohos.enterprise.common（Enterprise公共模块） |
| MDM Kit | @ohos.enterprise.deviceControl（设备控制管理） |
| MDM Kit | @ohos.enterprise.deviceInfo（设备信息管理） |
| MDM Kit | @ohos.enterprise.deviceSettings （设备设置管理） |
| MDM Kit | @ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力） |
| MDM Kit | @ohos.enterprise.locationManager（位置服务管理） |
| MDM Kit | @ohos.enterprise.networkManager（网络管理） |
| MDM Kit | @ohos.enterprise.restrictions （限制类策略） |
| MDM Kit | @ohos.enterprise.securityManager（安全管理） |
| MDM Kit | @ohos.enterprise.systemManager （系统管理） |
| MDM Kit | @ohos.enterprise.telephonyManager（通话管理） |
| MDM Kit | @ohos.enterprise.usbManager（USB管理） |
| MDM Kit | @ohos.enterprise.wifiManager（Wi-Fi管理） |
| Media Library Kit | @ohos.multimedia.movingphotoview (动态照片) |
| Mechanic Kit | @ohos.distributedHardware.mechanicManager (机械体控制模块) |
| MindSpore Lite Kit | @ohos.ai.mindSporeLite (端侧AI框架) |
| Natural Language Kit | textProcessing（文本处理） |
| NearLink Kit | advertising（星闪广播能力） |
| NearLink Kit | dataTransfer（星闪数传能力） |
| NearLink Kit | remoteDevice（对端设备的连接能力） |
| NearLink Kit | scan（星闪扫描能力） |
| NearLink Kit | ssap（星闪SSAP连接能力） |
| Network Boost Kit | netHandover（连接迁移） |
| Network Boost Kit | netBoost（网络加速） |
| Network Boost Kit | netQuality（网络质量） |
| Network Kit | @ohos.net.connection (网络连接管理) |
| Network Kit | @ohos.net.eap (扩展认证) |
| Network Kit | @ohos.net.ethernet (以太网连接管理) |
| Network Kit | @ohos.net.http (数据请求) |
| Network Kit | @ohos.net.mdns (MDNS管理) |
| Network Kit | @ohos.net.netFirewall (网络防火墙) |
| Network Kit | @ohos.net.networkSecurity (网络安全校验) |
| Network Kit | @ohos.net.policy (网络策略管理) |
| Network Kit | @ohos.net.sharing (网络共享管理) |
| Network Kit | @ohos.net.socket (Socket连接) |
| Network Kit | @ohos.net.statistics (流量管理) |
| Network Kit | @ohos.net.vpn (VPN管理) |
| Network Kit | @ohos.net.vpnExtension (VPN增强管理) |
| Network Kit | @ohos.net.webSocket (WebSocket连接) |
| Payment Kit | ecnyPaymentService (数字人民币服务) |
| Payment Kit | paymentService (鸿蒙支付服务) |
| Payment Kit | realNameService(身份验证服务) |
| Payment Kit | thirdPaymentService(三方支付服务) |
| Push Kit | pushCommon（推送服务公共信息） |
| Push Kit | PushExtensionAbility（推送扩展Ability） |
| Push Kit | PushExtensionContext（推送扩展Context） |
| Push Kit | pushService（推送服务基础能力） |
| Push Kit | RemoteLocationExtensionAbility（定位扩展Ability） |
| Push Kit | RemoteLocationExtensionContext（定位扩展Context） |
| Push Kit | RemoteNotificationExtensionAbility（通知扩展Ability） |
| Push Kit | RemoteNotificationExtensionContext（通知扩展Context） |
| Push Kit | serviceNotification（服务通知） |
| Push Kit | VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃） |
| Push Kit | VoIPExtensionContext（应用内通话消息扩展Context）（废弃） |
| Remote Communication Kit | urpc（高性能rpc通信库） |
| Remote Communication Kit | rcp（数据请求） |
| Service Collaboration Kit | CollaborationService (跨设备互通组件) |
| Service Collaboration Kit | CollaborationCamera (跨设备互通组件) |
| Service Collaboration Kit | CollaborationDevicePicker（流转控件） |
| Service Collaboration Kit | devicePicker（设备选择控制器） |
| Share Kit | harmonyShare（华为分享） |
| Share Kit | systemShare（分享） |
| Speech Kit | TextReader（朗读控件） |
| Telephony Kit | @ohos.telephony.call (拨打电话) |
| Telephony Kit | @ohos.telephony.data (蜂窝数据) |
| Telephony Kit | @ohos.telephony.esim (eSIM卡管理) |
| Telephony Kit | @ohos.telephony.observer (observer) |
| Telephony Kit | @ohos.telephony.radio (网络搜索) |
| Telephony Kit | @ohos.telephony.sim (SIM卡管理) |
| Telephony Kit | @ohos.telephony.sms (短信服务) |
| Telephony Kit | @ohos.telephony.vcard (VCard模块) |
| Vision Kit | CardRecognition（卡证识别控件） |
| Vision Kit | DocumentScanner（文档扫描控件） |
| Vision Kit | interactiveLiveness（人脸活体检测） |
| Vision Kit | visionImageAnalyzer（AI识图控件） |
| Wallet Kit | walletPass（Pass卡片能力） |
| Wallet Kit | walletTransitCard（交通卡能力） |
