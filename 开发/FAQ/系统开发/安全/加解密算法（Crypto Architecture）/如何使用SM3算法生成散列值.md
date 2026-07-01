# 如何使用SM3算法生成散列值

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-29

调用[cryptoFramework.createMd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd)方法，传入SM3，可参考如下代码：
 
```text
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util, buffer } from '@kit.ArkTS';

let base64 = new util.Base64Helper();

@Entry
@Component
struct SM3Encrypted {
  stringToUint8Array(str: string) {
    return new Uint8Array(buffer.from(str, 'utf-8').buffer);
  }

  <em>// Complete the summary in Promise format</em>
  doMdByPromise() {
    <em>// Summary algorithm name.</em>
    let mdAlgName = 'SM3';
    <em>// The data to be summarized.</em>
    let message = 'Hello,world';
    let md = cryptoFramework.createMd(mdAlgName);
    console.info('[Promise]: Md algName is: ' + md.algName);
    let promiseMdUpdate = md.update({ data: this.stringToUint8Array(message) });
    promiseMdUpdate.then(() => {
      <em>// Call digest() to return the result.</em>
      let PromiseMdDigest = md.digest();
      return PromiseMdDigest;
    }).then(digestOutput => {
      let mdOutput = digestOutput.data;
      <em>// Uint8Array to base64</em>
      let str2 = base64.encodeToStringSync(mdOutput);
      <em>// Convert to hexadecimal</em>
      let str = this.uint8ArrayToHexStr(mdOutput);
      console.info('[Promise]: MD result: ' + mdOutput);
      let mdLen = md.getMdLength();
      console.info('[Promise]: MD len: ' + mdLen);
    }).catch((error: BusinessError) => {
      console.error('[Promise]: error: ' + error.message);
    });
  }

  <em>// The summary result is Uint8Array type, converted to hexadecimal string data</em>
  uint8ArrayToHexStr(data: Uint8Array): string {
    let hexString = '';
    let i: number;
    for (i = 0; i < data.length; i++) {
      let char = ('00' + data[i].toString(16)).slice(-2);
      hexString += char;
    }
    return hexString;
  }

  build() {
    Column({ space: 10 }) {
      Button('使用SM3加密')
        .onClick(() => {
          this.doMdByPromise();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
