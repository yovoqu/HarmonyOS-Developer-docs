# 如何解决DH公钥在服务端协商报参数不兼容的问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-13

#### 问题现象

HarmonyOS使用ArkTS生成的DH公钥，在服务端协商失败，报错Incompatible parameters。
 
```text
class TestDh {
    public static void main(String[] args) throws Exception {
        <em>// </em><em>生成并初始化DH密钥</em>
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DH");
        keyPairGenerator.initialize(512);
        <em>/* 服务端公私钥 */</em>
        KeyPair keyPair= keyPairGenerator.generateKeyPair();
        DHPublicKey publicKey = (DHPublicKey) keyPair.getPublic();
        String serverPuk = Base64.getEncoder().encodeToString(publicKey.getEncoded());
        <em>// </em><em>HarmonyOS公钥</em>
        String pukClient = "替换为HarmonyOS的公钥";
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(Base64.getDecoder().decode(pukClient));
        <em>//</em> <em>根据DH算法获取KeyFactory</em>
        KeyFactory kf = KeyFactory.getInstance("DH");
        <em>// </em><em>通过KeyFactory创建公钥</em>
        PublicKey receivedPublicKey = kf.generatePublic(keySpec);
        <em>// </em><em>创建KeyAgreement对象</em>
        KeyAgreement keyAgreement = KeyAgreement.getInstance("DH");
        <em>//</em><em> 初始化协议，设置我方密钥</em>
        DHPrivateKey privateKey = (DHPrivateKey) keyPair.getPrivate();
        keyAgreement.init(privateKey);
        <em>// </em><em>添加对方的公钥</em>
        keyAgreement.doPhase((DHPublicKey)receivedPublicKey, true);
        <em>// </em><em>生成协商密钥</em>
        byte[] sharedSecret = keyAgreement.generateSecret();
        <em>// </em><em>输出协商的密钥</em>
    }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/VS0x-vEJTv6KCORPLMynUg/zh-cn_image_0000002658849153.png?HW-CC-KV=V1&HW-CC-Date=20260701T041425Z&HW-CC-Expire=86400&HW-CC-Sign=3258A1B39DF36533AC42FBAA3CF33165653D39C508059BA6CAF07774A9A57DCB)

 
 

#### 背景知识

[DH密钥协商算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-overview#dh)流程如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/0jsdf1ErT4KsXEZdG_BQ_Q/zh-cn_image_0000002628769786.png?HW-CC-KV=V1&HW-CC-Date=20260701T041425Z&HW-CC-Expire=86400&HW-CC-Sign=E5A92F6BD4FB859285A59F7DD3447C123BEF051A6805435A25B25510D7655ACD)

 
 

#### 定位思路
1. **检查公钥：**

  从DH算法的生成流程看，最关键的核心是密钥对的生成和交换，首先检查公钥的解析是否正确，核心代码：
```text
<em>// </em><em>来自服务端的公钥serverPubString</em>
let serverPubString ='替换下xxx';
const serverPubArray: Uint8Array = new util.Base64Helper().decodeSync(serverPubString);
```


  检查方法：查看serverPubArray的值是否成功生成。
2. **检查密钥：**

  检查密钥生成器的配置参数是否正确，即参数要写成“DH_modp1536”。
```text
let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
```

3. **检查密钥协商传参是否传错：**

  公钥和私钥的前后顺序不能错。
```text
keyAgreement.generateSecret(clientPair.priKey, serverPubKey.pubKey)
```


  通过以上步骤分析，发现服务端代码，密钥位数为512，而HarmonyOS侧提高了安全性，要求最低密钥长度为1536，导致协商失败。
 
 

#### 分析结论

DH密钥交换算法，务必按照定位思路中的三个步骤，逐个检查是否合法，如果参数不合法，将出现协商失败的情况。
 
 

#### 修改建议

将服务端代码密钥长度设置为1536后重新协商，即keyPairGenerator的initialize参数为initialize(1536)。
 
协商成功的截图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/KL14H8AGSZ67DuZj30BFxg/zh-cn_image_0000002628609890.png?HW-CC-KV=V1&HW-CC-Date=20260701T041425Z&HW-CC-Expire=86400&HW-CC-Sign=D8955C60021AFEA1EFD7372F50EB41F16CA82B00749CC331B70A24C40C1E72B0)

 
这里提供HarmonyOS密钥协商的正确代码实现：
 
```text
import { util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State res: string = 'init value';

  build() {
    Column() {
      Button('启动测试')
        .onClick(() => {
          dhCreate().then((result: string) => {
            this.res = result;
          });
        })
      Text('Result:\n' + this.res)
    }
    .height('100%')
    .width('100%')
  }
}

async function dhCreate(): Promise<string> {
  <em>// 生成客户端公私钥对</em>
  let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
  let clientPair = await keyGen.generateKeyPair();
  let clientPub = clientPair.pubKey.getEncoded();
  let base64Helper = new util.Base64Helper();
  <em>// 传给服务端的公钥:toServerPuk</em>
  let toServerPuk = base64Helper.encodeToStringSync(clientPub.data);
  hilog.debug(1, 'Index', `createKeyAgreement toServerPuk ${toServerPuk}`);
  <em>// 来自服务端的公钥serverPubString，以下为模拟key，非真实值！！！</em>
  let serverPubString =
    'MIIBoDCB1QYJKoZIhvcNAQMBMIHHAoHBAP//////////yQ/aoiFowjTExmKLgNwc0SkCTgiKZ8x0Agu+pjsTmyJRSgh5jjQE3e+VGbPNOkMbMCsKbfJfFDdP4TVtbVHCReSFtXZiXn7G9ExC6aY37WsL/1y29Aa37e44a/taiZ+lrp8kEXxLH+ZJKGZR7ORbPcIAfLihY78FmNpINhxV05ppFj+o/STPX4NlXSPco62WHGLzViCFUrue1SkHcJaWbWcMNU5KvJgE8XRsCMojcyf//////////wIBAgOBxQACgcEAnwrTwUX2xwrz0RYuYe2feqrD5wgJWDDeZSu0AnpIHFGZER1eYUJ1TTEZjE1gtBQAMbcVngSekfqFn5mHjDSA3JCLa7E2GK0GvhETtKv0m3BD/aR7bNpwwEqb0865ybD+y75P2ehYlre9XOiWcdMSs7Vc04ac0Ru1h/vyuN7ljtciJeSg8kvLJjEQSNF0QdZ5vMpOVRDLWpB0/fVRlfVdvUs2F2V95cPTK0SIXrmS9xN6quV5nDYwj+3+4rm0+VDs';
  const serverPubArray: Uint8Array = new util.Base64Helper().decodeSync(serverPubString);
  try {
    let serverPubKey = keyGen.convertKeySync({ data: serverPubArray }, null);
    let keyAgreement = cryptoFramework.createKeyAgreement('DH_modp1536');
    <em>// 使用服务端的公钥和客户端的私钥进行密钥协商</em>
    return keyAgreement.generateSecret(clientPair.priKey, serverPubKey.pubKey).then((reslove) => {
      let strBase = new util.Base64Helper().encodeToStringSync(reslove.data);
      hilog.debug(1, 'Index', 'result is:' + strBase);
      return strBase;
    }).catch((err: BusinessError) => {
      hilog.error(1, 'Index', 'createKeyAgreement error', err);
      return 'createKeyAgreement error';
    });
  } catch (err) {
    hilog.error(1, 'Index', 'dhCreate error', err);
    return 'dhCreate error';
  }
}
```
