# 密钥导入(ArkTS)

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-import-arkts

## 密钥导入(ArkTS)
   
    
从API版本26.0.0开始，在外部密钥管理扩展场景下，密钥导入能力支持将加密封装的密钥对导入到扩展设备中。密钥用途等参数传递给Extension后，由Extension实现方根据业务场景自行处理，HUKS不做额外校验。
    
具体的场景介绍请参考[密钥生成与导入导出介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-generation-import-overview)。
    
          
##### 开发步骤
     
 - 通过[openAuthorizeDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
 - 调用[openResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptoopenresource)打开资源。
 - 调用[importWrappedKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksimportwrappedkeyitem9)导入加密封装的密钥对，密钥参数中需指定[HUKS_TAG_KEY_CLASS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)为[HUKS_KEY_CLASS_EXTENSION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukskeyclasstype22)，表示该密钥由外部密钥管理扩展管理。
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

async function importWrappedKeyItem(
  keyAlias: string,
  wrappingKeyAlias: string,
  huksOptions: huks.HuksOptions
): Promise {
  try {
    await huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
      .then(() => {
        console.info('promise: importWrappedKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: importWrappedKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: importWrappedKeyItem input arg invalid.');
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

async function extensionKeyImport(): Promise {
  /* 1.准备资源ID（keyAlias和wrappingKeyAlias使用resourceId） */
  const resourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });
  const keyAlias = resourceId;
  const wrappingKeyAlias = resourceId;

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
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
    }
  ];
  // 加密封装的密钥数据（由Extension实现方定义格式）
  const wrappedKeyData: Uint8Array = new Uint8Array([/* 封装密钥数据 */]);
  const huksOptions: huks.HuksOptions = {
    properties: properties,
    inData: wrappedKeyData
  };

  try {
    /* 2.打开资源 */
    await openResource(resourceId);
    
    /* 3.导入加密封装的密钥 */
    await importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions);
    
    /* 4.关闭资源 */
    await closeResource(resourceId);
    
    console.info('promise: extensionKeyImport completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyImport input arg invalid.');
  }
}
```
