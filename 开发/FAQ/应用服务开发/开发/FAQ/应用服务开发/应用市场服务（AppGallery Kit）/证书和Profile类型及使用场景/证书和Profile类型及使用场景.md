# 证书和Profile类型及使用场景

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-81

#### 问题现象

编译HarmonyOS应用需要使用证书和Profile文件。证书和Profile有哪些类型？如何根据不同场景选择相应的证书和Profile类型？
 
 

#### 背景知识
1. HarmonyOS软件包签名必须使用到证书和Profile文件，同时根据不同的安装方式，使用的证书和Profile类型也不同。
2. 根据不同的发布方式和设备类型，相应的证书和Profile类型也不同。通常Profile类型是根据证书类型不同做相应适配，证书类型和Profile类型是需要保持一致的。
3. 申请证书的通用步骤：
登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
4. 在左侧导航栏选择“证书、APP ID和Profile > 证书”，进入“证书”页面，点击“新增证书”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/FK4Scq5HRAyfsk1OxvDReg/zh-cn_image_0000002628554532.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=677FE8EA38A417B071BACBFA791145A2F9A734EB8F1CF4738B6923A711E967D7)

5. 在弹出的“新增证书”窗口选择证书类型，填写要申请的证书信息，点击“提交”。
6. 申请Profile的通用步骤：
登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
7. 在左侧导航栏选择“证书、APP ID和Profile > Profile”，进入“Profile”页面，点击右上角“添加”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/pPmbWfEYS-6W4gwCYkdXhA/zh-cn_image_0000002658913851.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=9920D9F553DE6D450350AF2081D8723822BBD0FDF5171F5AEC574FE5E01038D0)

8. 在“添加Profile”页面，选择证书，根据证书类型选择Profile类型，填写应用名称、Profile名称等必填信息。
 
 

#### 解决方案

按照安装方式，设备类型，账号类型，应用类型，上架类型等多个维度来阐述证书和Profile的类型和使用场景：
 1. 调试证书和调试Profile。**适用场景**：本地调试应用。

  
本地通过HDC命令即可安装的应用需要申请调试证书和调试Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“调试证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/anqMXRFPTS-BcU_NWwWKaQ/zh-cn_image_0000002658793911.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=7511D263CDB3EBF91141AD3B861EEFFF971BFE3CD2D6789796DEC1B934924F55)

2. 调试证书除了登录AppGallery Connect手动申请，也可以通过DevEco Studio自动签名方式从AppGallery Connect申请。详细操作可参考[自动签名。](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section18815157237)申请成功也可登录AppGallery Connect查看，证书名称以“auto_debug”开头：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/IRGbY8yYSFaH0JwAEG6fAQ/zh-cn_image_0000002628394642.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=FD6CD64614EA251E1C8A8A3B521129D036618AF2DA922A75B757FEFCA4C2ED99)

3. [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)时，对应的证书类型选择“调试”。
4. 发布证书和发布Profile。

  **适用场景**：上架应用市场。包括正式上架，非公开发布，公开测试，邀请测试等。
HarmonyOS应用上架应用市场必须申请发布证书和发布Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/1dL878vgRvidYvegS8n8dQ/zh-cn_image_0000002628554534.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=810B96B2FD3F80A9B8AEAF487C3C109A1AF11D3BF86E35514576E5218FFD2E32)

5. [申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)时，对应的证书类型选择“发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“发布”。
6. In-house发布证书和In-house发布Profile。

  **适用场景**：[发布In-house应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-0000002281532696)。适用于在企业内部网络环境中分发专属应用给内部员工的场景，In-house应用不适合在任何公开渠道发布。
In-house应用打包需要申请In-house发布证书，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“In-house发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/W3l_Eqa_RYWujCL82gIJQg/zh-cn_image_0000002658913853.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=80FFA200F984D84036E9B25AA2BDC74E4BBE4C9515F18D3F7F2411B305E83889)

7. [申请In-house发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-profile-0000002283340021)时，对应的证书类型选择“In-house发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“In-house发布”。
8. 二进制证书。

  **适用场景**：涉及二进制程序，需使用华为颁发的二进制证书签名，才能在PC上正常运行。
二进制程序需使用华为颁发的二进制证书签名，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“二进制证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/gFQ5w0QVSmOhdGHfhipC2g/zh-cn_image_0000002658793913.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=BA368638DCDDD5B268A778B55A64BFB437937C00438D56BD7FCA03BE924EFFF0)

9. 企业MDM应用发布证书和企业MDM应用发布Profile。

  **适用场景**：发布企业MDM应用。
发布企业MDM应用时，需要使用企业MDM应用发布证书和企业MDM应用发布Profile手动签名后，才能编译构建正式发布包。登录AppGallery Connect申请证书时，弹窗界面证书类型选择“企业MDM应用发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/IQU0dDmoTwiQ4qg5Wiv87A/zh-cn_image_0000002628394644.png?HW-CC-KV=V1&HW-CC-Date=20260811T005624Z&HW-CC-Expire=86400&HW-CC-Sign=F7E04B4B940D3844209F1081FEECE6796C53AC55DA3384D4C33792AC0FD64D31)

10. [申请企业MDM应用发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-profile-0000002248341094)时，对应的证书类型选择“企业MDM应用发布”。
 
 

#### 常见FAQ

Q：In-house账号能否申请调试证书，进行本地HDC命令安装测试？
 
A：In-house账号可以申请“调试证书”和“调试Profile”构建软件包本地HDC命令安装，也可以申请“In-house发布证书”和“指定设备发布Profile”，构建的软件包也可以本地HDC命令安装。
