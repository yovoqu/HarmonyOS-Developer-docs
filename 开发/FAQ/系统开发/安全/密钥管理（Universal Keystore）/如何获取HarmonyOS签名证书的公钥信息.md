# 如何获取HarmonyOS签名证书的公钥信息

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-7

获取HarmonyOS签名可以参考指南手动签名章节，公钥用于给数据加密，用公钥加密的数据只能使用私钥解密，可以通过以下命令获取公钥信息（需要提前安装安全套接字层密码库Openssl）：

```bash
openssl x509 -in xxx.cer -pubkey -noout
```

参考链接

手动签名
