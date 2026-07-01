# 密钥生成(ArkTS)

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-generation-arkts

## 密钥生成(ArkTS)
   
    
从API版本26.0.0开始，在外部密钥管理扩展场景下，HUKS支持在扩展设备内生成密钥对。密钥用途等参数传递给Extension后，由Extension实现方根据业务场景自行处理，HUKS不做额外校验。
    
具体的场景介绍请参考[密钥生成与导入导出介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-generation-import-overview)。
    
          
##### 开发步骤
     
 - 通过[openAuthorizeDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
 - 调用[openResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptoopenresource)打开资源。
 - 调用[generateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9)生成密钥对，密钥参数中需指定[HUKS_TAG_KEY_CLASS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)为[HUKS_KEY_CLASS_EXTENSION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukskeyclasstype22)，表示该密钥由外部密钥管理扩展管理。
 - 关闭资源。
     
    
    
          
##### 开发案例
     
```text
import { huks, huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openResource(resourceId: string): Promise {
  try {
    await huksExternalCrypto.openResource(resourceId)
      .then(() => {
        console.info('promise: openResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: openResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: openResource input arg invalid.');
  }
}

async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions): Promise {
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info('promise: generateKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: generateKeyItem input arg invalid.');
  }
}

async function closeResource(resourceId: string): Promise {
  try {
    await huksExternalCrypto.closeResource(resourceId)
      .then(() => {
        console.info('promise: closeResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: closeResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: closeResource input arg invalid.');
  }
}

async function extensionKeyGeneration(): Promise {
  /* 1.准备资源ID（keyAlias使用resourceId） */
  const resourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });
  const keyAlias = resourceId;

  const properties: Array = [
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
      value: huks.HuksKeyClass.HUKS_KEY_CLASS_EXTENSION
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
    }
  ];
  const huksOptions: huks.HuksOptions = {
    properties: properties,
    inData: new Uint8Array([])
  };

  try {
    /* 2.打开资源 */
    await openResource(resourceId);
    
    /* 3.生成密钥 */
    await generateKeyItem(keyAlias, huksOptions);
    
    /* 4.关闭资源 */
    await closeResource(resourceId);
    
    console.info('promise: extensionKeyGeneration completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyGeneration input arg invalid.');
  }
}
```
