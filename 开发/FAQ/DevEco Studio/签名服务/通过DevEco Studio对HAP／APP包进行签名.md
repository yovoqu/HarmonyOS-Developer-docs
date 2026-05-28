# 通过DevEco Studio对HAP/APP包进行签名

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-17

通过DevEco Studio自带的签名工具，可以对已打包的HAP/APP包进行签名，具体步骤如下。
 
> [!NOTE]
> 建议使用DevEco Studio 6.0.2 Beta1及以上的版本。

1. 通过DevEco Studio生成密钥和证书请求文件，并向AppGallery Connect申请发布证书和Profile文件，具体请参考[准备签名文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section793484619307)。
2. 准备好签名工具hap_sign_tool.jar，在${DevEco Studio安装目录}/sdk/default/openharmony/toolchains/lib下。
3. 在签名工具目录下，使用如下命令进行签名。详细的签名工具指导请参考[应用包签名工具](https://gitcode.com/openharmony/developtools_hapsigner)。
```bash
java -jar hap-sign-tool.jar sign-app -keyAlias "demo_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "D:\demo.cer" -profileFile "D:\demo.p7b" -inFile "D:\hap-unsigned.hap" -keystoreFile "D:\demo.p12" -outFile "D:\hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
```
 关于该命令中需要修改的参数说明如下，其余参数不需要修改：

  
**keyAlias**：密钥别名。
4. **appCertFile**：申请的发布证书文件，格式为.cer。
5. **profileFile**：申请的发布Profile文件，格式为.p7b。
6. **inFile**：通过Hvigor打包生成的未携带签名信息的HAP。
7. **keystoreFile**：密钥库文件，格式为.p12。
8. **outFile**：经过签名后生成的携带签名信息的HAP。
9. **keyPwd**：密钥密码。
10. **keystorePwd**：密钥库密码。
