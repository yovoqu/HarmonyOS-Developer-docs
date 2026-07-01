# ECC密钥如何转化为非压缩十六进制字符串

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-58

## ECC密钥如何转化为非压缩十六进制字符串
 


##### 问题现象

其他端生成的ECC的公钥字符串长度为65字节（130位16进制字符串），ArkTS中使用generateKeyPairSync生成的KeyPair里面的公钥二进制数据长度远多于65字节，如何通过KeyPair获取非压缩16进制的公私钥字符串？
 
 

##### 背景知识

[使用ECC压缩/非压缩点格式转换(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-compressed-or-uncompressed-ecc-point)：支持将压缩/非压缩的点数据转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。
 
服务端使用的是非压缩16进制私钥和公钥，需要提取参数转化成非压缩私钥公钥与服务端交互。
 
- ECC公钥长度一般为65字节，其中前导04是固定的，代表非压缩格式。
- 32个字节的私钥在某些情况下被省略了前导的零，需要手动在前面补上0才能构成完整的私钥。

 
 

##### 解决方案

通过密钥获取密钥参数X和Y合成非压缩公钥，获取SK参数转化成私钥。SM2也是基于椭圆曲线的公钥密码算法，公钥结构与ECC相同，是ECC算法的一种具体实现，demo以SM2算法为例。
 
```text
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Uint8Array to hexadecimal
function uint8ArrayToHexStr(data: Uint8Array): string {
  let hexString = '';
  let i: number;
  for (i = 0; i  {
          gen();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
