# 如何获取应用指纹

更新时间：2026-07-21 07:44:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_faq-9

#### iOS手机侧应用

iOS手机侧应用没有指纹信息，需填写非空字符串作为指纹信息，更多请参考[手机侧应用发送点对点消息](https://developer.huawei.com/consumer/cn/doc/connectivity-Guides/phone-send-message-ios-0000001875158886#section795719274334)。
 
  

#### Android手机侧应用

Android手机侧应用开发时，应用指纹信息是SHA256指纹，操作如下。
 1. 生成签名证书，具体请参考[配置签名证书](https://developer.huawei.com/consumer/cn/doc/connectivity-Guides/addingappid-packagename-0000001050818013#section1041814153312)。
2. 使用JDK携带的Keytool工具导出签名证书中的SHA256信息。

  **Windows系统**

  a. 打开cmd命令行工具，执行cd命令进入keytool.exe所在的目录。

  b. 执行keytool -list -v -keystore <keystore-file>命令，其中<keystore-file>为应用签名证书的完整路径。

  示例：

  
```text
cd C:\Program Files\Java\jdk\bin
keytool -list -v -keystore C:\TestApp.jks
```
   **macOS系统**

  打开Terminal终端，执行命令keytool -list -v -keystore <keystore-file>，其中<keystore-file>为应用签名证书的完整路径，按提示进行操作。

  示例：

  
```text
keytool -list -v -keystore /Users/admin/Downloads/Demo.jks
```

3. 获取SHA256指纹，下图为Windows示例。

  
![](assets/使用AppInfo时，如何获取应用身份标识/file-20260514131354003-0.png)

 
  

#### HarmonyOS 5.0之前版本手机侧应用

HarmonyOS 5.0之前（如HarmonyOS 2.x/3.x/4.x）版本手机侧的应用开发时，应用指纹信息是SHA256指纹。具体请参考[Android手机侧应用](#android手机侧应用)。
 
  

#### HarmonyOS 5.0及之后版本的设备应用

- Phone/Tablet/Wearable设备的应用，应用指纹信息是AppGallery Connect平台提供的APP ID值。

  登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的APP ID。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-3jeYMw2TZm7SozYdqftiA/zh-cn_image_0000002677666427.png?HW-CC-KV=V1&HW-CC-Date=20260723T012148Z&HW-CC-Expire=86400&HW-CC-Sign=00C15757F1455CC097725BD185E7FD88FB8FE673F69FF741A43AF01EF0F1A05A)

- Lite Wearable设备的应用，应用指纹信息是应用包名_base64Encode(公钥)，操作如下。

1. 用文本格式打开[数字证书.cer文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)，将最后BEGIN CERTIFICATE、END CERTIFICATE以及中间信息复制到新的文本，创建一个新的.cer文件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/kfrxQytISuSpaKgaW9wTbw/zh-cn_image_0000002647746546.png?HW-CC-KV=V1&HW-CC-Date=20260723T012148Z&HW-CC-Expire=86400&HW-CC-Sign=AE886D038B13A740E6786E40D47600F0D2F880C61C30EF10F567818CCB99199D)


2. 获取公钥信息pubKey。

  **Windows系统** ：打开新的cer文件，点击“详细信息”，点击“公钥”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/NVMwZX6USMCgZ8PWFiCZ4g/zh-cn_image_0000002647586636.png?HW-CC-KV=V1&HW-CC-Date=20260723T012148Z&HW-CC-Expire=86400&HW-CC-Sign=481D85846EB0FF2035D5B0F261729FACB5778CD26342310827A3D9BF8DC40155)


  **MacOS系统**：执行penssl x509 -in test.cer -text -noout命令，其中test.cer替换为新cer文件的名称。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/O-hN5ApQQBC-PnobrhlvwQ/zh-cn_image_0000002677826277.png?HW-CC-KV=V1&HW-CC-Date=20260723T012148Z&HW-CC-Expire=86400&HW-CC-Sign=0FD20E7D9FE1A720CCA4DC7A2FD67A0E53E45C3B49AF3C2BC29146454416A018)


3. 将pubKey进行base64Encode编码。

  删除前一步获取的证书公钥信息中空格/冒号，删除后如04d929a057d784d95dcf7a15dcdea9d88aeb0a7b86fdafdf5b83bc5435917f2a3dcaa6f97b355462bc5301e00c4ed8aa4165e2111ec77f4b03abca02b06a212b，然后进行进行base64编码，结果为BNkXKaBX14TZXc96FdzeqdiK6wp7hv2v31uDvFQ1kX8qPcqm+Xs1VGK8UwHgDE7YqkFl4hEex39LA6vKArBqISs=。开发者可以通过第三方网站（如[tomeko.net](https://www.tomeko.net/online_tools/hex_to_base64.php?lang=en)）进行转码。

4. 指纹信息为应用包名_base64Encode(pubKey)，例如：com.huawei.wearengine_BC5Z9/29Yn93xSa9XkQ2HN5GikugmXjor9se0VwnOENK9t4uFK4VlRpOHv4B3lphjIa7P6Sh61CFRsT0MZNhuV8=。
