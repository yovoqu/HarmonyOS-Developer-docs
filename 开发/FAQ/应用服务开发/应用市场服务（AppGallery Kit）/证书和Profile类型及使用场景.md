# 证书和Profile类型及使用场景

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-81

## 证书和Profile类型及使用场景
 


##### 问题现象

编译HarmonyOS应用需要使用证书和Profile文件。证书和Profile有哪些类型？如何根据不同场景选择相应的证书和Profile类型？
 
 

##### 背景知识

- HarmonyOS软件包签名必须使用到证书和Profile文件，同时根据不同的安装方式，使用的证书和Profile类型也不同。
- 根据不同的发布方式和设备类型，相应的证书和Profile类型也不同。通常Profile类型是根据证书类型不同做相应适配，证书类型和Profile类型是需要保持一致的。
- 申请证书的通用步骤：
登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
- 在左侧导航栏选择“证书、APP ID和Profile > 证书”，进入“证书”页面，点击“新增证书”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/exr93n2RRvefh5dDRpWb8w/zh-cn_image_0000002628554532.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=7751FF4823B10DC63467B63F0E86017F9F84D62302148ABB819A8CEFECE8146D)

- 在弹出的“新增证书”窗口选择证书类型，填写要申请的证书信息，点击“提交”。

 - 申请Profile的通用步骤：
登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
- 在左侧导航栏选择“证书、APP ID和Profile > Profile”，进入“Profile”页面，点击右上角“添加”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/imtfgXl7T72cFXaGXAzWMg/zh-cn_image_0000002658913851.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=18879CC7D9EC6BDEE69FFD8F529DACCAB2276E771284D0AD7E8A49F310DC82F3)

- 在“添加Profile”页面，选择证书，根据证书类型选择Profile类型，填写应用名称、Profile名称等必填信息。

 
 
 

##### 解决方案

按照安装方式，设备类型，账号类型，应用类型，上架类型等多个维度来阐述证书和Profile的类型和使用场景：
 
- 调试证书和调试Profile。**适用场景**：本地调试应用。
 
本地通过HDC命令即可安装的应用需要申请调试证书和调试Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“调试证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1JR-NjCbT7WuTvfLsBKw8A/zh-cn_image_0000002658793911.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=8F1F5B8CF59E2DFC1904593EA6C66E6CCE88D25A60017A0F6970CD37474C65F0)

- 调试证书除了登录AppGallery Connect手动申请，也可以通过DevEco Studio自动签名方式从AppGallery Connect申请。详细操作可参考[自动签名。](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section18815157237)申请成功也可登录AppGallery Connect查看，证书名称以“auto_debug”开头：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/xU2uD6UeQ6qy1JEpKJ2Pgg/zh-cn_image_0000002628394642.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=D0AA8F01356009E50364A07C0D1FF75B9F4E7EA36E42584158437DB250CC3972)

- [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)时，对应的证书类型选择“调试”。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9_nRf02YS6-D_9Gm8ktSfA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=3596BDE7DE621F4904AA5249CB7162D0BF5C8EF775667A638AAB144FD467CDE4)
 

每个账号最多可申请3个调试证书。
 
一个应用最多可申请100个Profile文件。
 

 - 发布证书和发布Profile。
**适用场景**：上架应用市场。包括正式上架，非公开发布，公开测试，邀请测试等。
HarmonyOS应用上架应用市场必须申请发布证书和发布Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/aHM4iiauRYuihBqfA65mSQ/zh-cn_image_0000002628554534.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=9DCD7AF8383AB007FF587A5C35421FF79163BE9991526647B5E28E03E538EA5A)

- [申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)时，对应的证书类型选择“发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“发布”。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/aM-pltsiTLKct8a9eLVimQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=F97A59361A827C1AEC758AB5A637073864B42F8987C76CD1ABC543C6630D1C17)
 

每个账号最多可申请3个发布证书。
 
一个应用最多可申请100个Profile文件。
 

 
 - In-house发布证书和In-house发布Profile。
**适用场景**：[发布In-house应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-0000002281532696)。适用于在企业内部网络环境中分发专属应用给内部员工的场景，In-house应用不适合在任何公开渠道发布。
In-house应用打包需要申请In-house发布证书，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“In-house发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_Hkg9bE3QJqxhnPP2BAb_g/zh-cn_image_0000002658913853.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=779CBCDDAF978327FFB229F033E04EE85119E11753B31EE36F7C221668D9ECA3)

- [申请In-house发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-profile-0000002283340021)时，对应的证书类型选择“In-house发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“In-house发布”。

 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/LqsxFYTPRRi9MK_Qc9ToLw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=EC91EDBE141722F07342E86C814B3EC942008FB4523161B158F8C9B260F65632)
 

In-house受限开放。使用In-house发布前，需要分别完成账号和应用权限申请，详情参考发布In-house应用[准备工作。](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-0000002281532696#section6267104872410)
 
每个账号仅可申请1个In-house发布证书。
 

 - 二进制证书。
**适用场景**：涉及二进制程序，需使用华为颁发的二进制证书签名，才能在PC上正常运行。
二进制程序需使用华为颁发的二进制证书签名，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“二进制证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/RXaOm-bSTNa78WsXiQ4CBw/zh-cn_image_0000002658793913.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=DA3EE671E4569DA44DA08B21789B1B253AB7E8BC0329F31E2A1BB19D2C7166E5)


 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/LSGcxD0DQLG53xVZS5OvcA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=31553E36ECCBE5F51216C5BAA8864B21DFE8E92BB6A80E64C31D653AA702A278)
 

二进制证书目前为受限开放，如需体验可[申请开通权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-binary-cert-0000002408063605#section149371737114211)。
 
二进制证书仅支持企业开发者使用，且每个账号最多可申请3个二进制证书。
 

 - 企业MDM应用发布证书和企业MDM应用发布Profile。
**适用场景**：发布企业MDM应用。
发布企业MDM应用时，需要使用企业MDM应用发布证书和企业MDM应用发布Profile手动签名后，才能编译构建正式发布包。登录AppGallery Connect申请证书时，弹窗界面证书类型选择“企业MDM应用发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Vh3Jbub_Smed2NIJo3GszQ/zh-cn_image_0000002628394644.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=A94291F9A35933A3C3DC512F9774C854A676033E5491205351D681086E4C8CCF)

- [申请企业MDM应用发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-profile-0000002248341094)时，对应的证书类型选择“企业MDM应用发布”。

 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/L3msNpxySvOEAe3s9rJkqw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025904Z&HW-CC-Expire=86400&HW-CC-Sign=745AE66B2B6DF103FFE8FBA480157D83C68790CEC3527A1CFBB927C37302D3A4)
 

企业MDM应用发布证书受限开放，需要满足[申请开通条件。](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-cert-0000002283256801#section55531120183018)
 
每个账号最多申请1个企业MDM应用发布证书。
 
申请Profile类型选择“企业MDM应用发布”时，证书类型只能选择“企业MDM应用发布”。
 

 
 
 

##### 常见FAQ

Q：In-house账号能否申请调试证书，进行本地HDC命令安装测试？
 
A：In-house账号可以申请“调试证书”和“调试Profile”构建软件包本地HDC命令安装，也可以申请“In-house发布证书”和“指定设备发布Profile”，构建的软件包也可以本地HDC命令安装。
