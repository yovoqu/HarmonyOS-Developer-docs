# 离线匿名密钥证明(ArkTS)

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-offline-anon-attestation-arkts

## 离线匿名密钥证明(ArkTS)
   
    
从API版本26.0.0开始，HUKS支持离线匿名密钥证明。该接口用于在无网络环境下证明密钥的合法性，与在线匿名密钥证明相比，在离线证书有效期内不需要网络连接，推荐优先使用离线匿名密钥证明。离线证书是在该流程中由三级CA颁发的证书，其有效期为1个月。
    
     
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/cGBQ76MXRna37Wgw2RVrNQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025434Z&HW-CC-Expire=86400&HW-CC-Sign=24CFCD2B2F017DEED1E88C314EA4EEC458F267B22236E174E4942DE4FBEC0116)
      
      
 - 离线匿名密钥证明依赖网络，需要定期联网使用该接口以更新离线证书。
 - 离线匿名密钥证明需保证本地时间是准确的，否则可能导致对端校验证书超期失败。
      
     
    
    
          
##### 开发步骤
     
 - 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
 - 初始化参数集。
       [HuksParam[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksparam)中的HuksParam字段参数必须包含[HUKS_TAG_ATTESTATION_CHALLENGE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)属性，可选参数包含[HUKS_TAG_ATTESTATION_ID_VERSION_INFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)、[HUKS_TAG_ATTESTATION_ID_ALIAS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukstag)属性。
 - 生成非对称密钥，具体请参考[密钥生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。
 - 将密钥别名与参数集作为参数传入[anonAttestKeyItemOffline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksanonattestkeyitemoffline)方法中，即可进行离线匿名密钥证明。
     
    
    
          
##### 开发案例
     
```text
import { huks } from "@kit.UniversalKeystoreKit";
import { BusinessError } from "@kit.BasicServicesKit";

function StringToUint8Array(str: string) {
  let arr: number[] = new Array();
  for (let i = 0, j = str.length; i  = [
  { tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE, value: g_challenge },
  { tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS, value: g_keyAlias },
];

let gKeyParam: Array = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
]

let gKeyOption: huks.HuksOptions = { properties: gKeyParam };

async function AnonAttestKeyOfflineTest() {
  let testKeyAlias: string = "testKey";
  await huks.generateKeyItem(testKeyAlias, gKeyOption);

  await huks.anonAttestKeyItemOffline(testKeyAlias, gCommonParam).then((data) => {
    console.info("anonAttestKeyItemOffline success")
  }).catch((error: BusinessError) =>
    console.error(`anonAttestKeyItemOffline error ${JSON.stringify(error)}`))
}
```
