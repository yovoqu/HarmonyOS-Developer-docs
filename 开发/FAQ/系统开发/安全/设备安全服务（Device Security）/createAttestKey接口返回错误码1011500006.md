# createAttestKey接口返回错误码1011500006

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-6

## createAttestKey接口返回错误码1011500006
 


##### 问题现象

调用[trustedAppService.createAttestKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api#section81796536265)接口异常，返回错误码1011500006。官网错误信息：IPC communication failed.
 
[1011500006 IPC通信失败](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-arktsapi-errcode-taas#section2791195012317)可能原因和处理措施，无法指导开发者解决：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/cDV-zRruT46NkolcH9-8mg/zh-cn_image_0000002628610322.png?HW-CC-KV=V1&HW-CC-Date=20260701T025752Z&HW-CC-Expire=86400&HW-CC-Sign=2AE732A135536B71386CD3A05FBB2728B615A145040CF8A9A08664C554CC7732)

 
 

##### 背景知识

[可信应用服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api)提供应用数据的安全证明服务，支持创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话和获取安全地理位置，能够为安全摄像头和安全地理位置功能提供安全证明能力，确保图像或位置数据未被篡改。
 
 

##### 问题定位

- 检查是否开启相关服务。
- 若开启服务，是否有重新申请profile。
- 检查接口参数是否错误。

 
 

##### 分析结论

[Device Security Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b060#device-security-kit)为规范安全摄像头和安全地理位置的使用场景，使用可信应用服务接口前需要通过白名单审核，审核通过后方可开通可信应用服务。在API 12变更，要求开发者优先申请“可信应用服务”白名单，审核通过后开通可信应用服务才可以正常使用接口，否则调用接口会抛出异常，已上架的应用需要开通服务后重新上架。
 
 

##### 修改建议

参考[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)，引导开发者执行以下步骤：
 
- 申请“可信应用服务”白名单：将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到AGC官方邮箱。AGC运营将审核相关材料，通过后将配置受限开放服务使用的名单，审核周期为1-3个工作日。
- “可信应用服务”白名单申请通过后，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)上开通可信应用服务。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/QkYOQdf0QkCwSy5q_qYibw/zh-cn_image_0000002658849579.png?HW-CC-KV=V1&HW-CC-Date=20260701T025752Z&HW-CC-Expire=86400&HW-CC-Sign=E4F36C57F09B49EB30093DDAA4695E3A6E381E17749D9B1B4AE291B5CE62CDE7)

- 在开通服务后，[重新申请profile（.p7b）文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。
- 本地替换profile签名文件，重新编译执行。
