# 证书链校验时从PKCS #12文件构造TrustAnchor对象数组

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-trustanchor-from-p12

证书链校验时从PKCS #12文件构造TrustAnchor对象数组。


#### 开发步骤
1. 导入[证书模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert)。
2. 基于现有的PKCS #12文件数据，调用[cert.createTrustAnchorsWithKeyStore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert#certcreatetrustanchorswithkeystore12)创建[X509TrustAnchor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert#x509trustanchor11)数组对象，并返回结果。

```ArkTS
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

function test() {
  // ...
  try {
    cert.createTrustAnchorsWithKeyStore(p12Data, '123456').then((data) => {
      console.info('createTrustAnchorsWithKeyStore result: success, the num of result is :' + data.length);
    }).catch((err: BusinessError) => {
      console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${error.code}, message: ${error.message}`);
  }
}
```
