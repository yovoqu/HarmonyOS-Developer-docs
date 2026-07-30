# createAttestKey接口返回错误码1011500006

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-6

#### 问题现象

调用[trustedAppService.createAttestKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api#createattestkey)接口异常，返回错误码1011500006。官网错误信息：IPC communication failed.
 
[1011500006 IPC通信失败](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-taas#section1011500006-ipc通信失败)可能原因和处理措施，无法指导开发者解决：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/lHbmPsFYTAuSrPSG5YSoIQ/zh-cn_image_0000002661522207.png?HW-CC-KV=V1&HW-CC-Date=20260730T072545Z&HW-CC-Expire=86400&HW-CC-Sign=B5E9058A9FB9A50078DEFFB3E2BCEECCBCAF058A1A4C358168A1E301F2055660)

 
 

#### 背景知识

[可信应用服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api)提供应用数据的安全证明服务，支持创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话和获取安全地理位置，能够为安全摄像头和安全地理位置功能提供安全证明能力，确保图像或位置数据未被篡改。
 
 

#### 问题定位

- 检查是否开启相关服务。
- 若开启服务，是否有重新申请profile。
- 检查接口参数是否错误。

 
 

#### 分析结论

[Device Security Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b060#device-security-kit)为规范安全摄像头和安全地理位置的使用场景，使用可信应用服务接口前需要通过白名单审核，审核通过后方可开通可信应用服务。在API 12变更，要求开发者优先申请“可信应用服务”白名单，审核通过后开通可信应用服务才可以正常使用接口，否则调用接口会抛出异常，已上架的应用需要开通服务后重新上架。
 
 

#### 修改建议

参考[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)，引导开发者执行以下步骤：
 1. 申请“可信应用服务”白名单：将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到AGC官方邮箱。AGC运营将审核相关材料，通过后将配置受限开放服务使用的名单，审核周期为1-3个工作日。
2. “可信应用服务”白名单申请通过后，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)上开通可信应用服务。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/WOulb_uWQJ6Mx42eHeHU9A/zh-cn_image_0000002661522755.png?HW-CC-KV=V1&HW-CC-Date=20260730T072545Z&HW-CC-Expire=86400&HW-CC-Sign=B3FE3EB0DF74DEC41D8DA4AD6CE17090F519980AF0B30A31A152D69D51AC92AC)

3. 在开通服务后，[重新申请profile（.p7b）文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。
4. 本地替换profile签名文件，重新编译执行。
