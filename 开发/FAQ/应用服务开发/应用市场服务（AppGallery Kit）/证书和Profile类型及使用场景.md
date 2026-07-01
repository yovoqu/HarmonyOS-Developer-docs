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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/exr93n2RRvefh5dDRpWb8w/zh-cn_image_0000002628554532.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=6CF510F3F100B43B099B0AD109F739D10A7C1929A1EEC004CF12E18576CF9F79)

5. 在弹出的“新增证书”窗口选择证书类型，填写要申请的证书信息，点击“提交”。
6. 申请Profile的通用步骤：
登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“证书、APP ID和Profile”。
7. 在左侧导航栏选择“证书、APP ID和Profile > Profile”，进入“Profile”页面，点击右上角“添加”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/imtfgXl7T72cFXaGXAzWMg/zh-cn_image_0000002658913851.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=6CF0F999863D1E9B90C13AEB5370C8AE5A556F5FA3B852963245E9143E65A279)

8. 在“添加Profile”页面，选择证书，根据证书类型选择Profile类型，填写应用名称、Profile名称等必填信息。
 
 

#### 解决方案

按照安装方式，设备类型，账号类型，应用类型，上架类型等多个维度来阐述证书和Profile的类型和使用场景：
 1. 调试证书和调试Profile。**适用场景**：本地调试应用。

  
本地通过HDC命令即可安装的应用需要申请调试证书和调试Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“调试证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1JR-NjCbT7WuTvfLsBKw8A/zh-cn_image_0000002658793911.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=FC3487193311F161232EA80655DD9028A0CDA5F250C6A62463689135E3AC6082)

2. 调试证书除了登录AppGallery Connect手动申请，也可以通过DevEco Studio自动签名方式从AppGallery Connect申请。详细操作可参考[自动签名。](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section18815157237)申请成功也可登录AppGallery Connect查看，证书名称以“auto_debug”开头：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/xU2uD6UeQ6qy1JEpKJ2Pgg/zh-cn_image_0000002628394642.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=FB73475CE6C3ECAB7078AF7E5A6DA81FCDF21C7B94CF99B6FA69BFD30E8CEAE4)

3. [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)时，对应的证书类型选择“调试”。
4. 发布证书和发布Profile。

  **适用场景**：上架应用市场。包括正式上架，非公开发布，公开测试，邀请测试等。
HarmonyOS应用上架应用市场必须申请发布证书和发布Profile，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/aHM4iiauRYuihBqfA65mSQ/zh-cn_image_0000002628554534.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=7A23DE82E2EF552055F8213801EC9ECE965162ABFB3A38E2EC3422B4ED7DD454)

5. [申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)时，对应的证书类型选择“发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“发布”。
6. In-house发布证书和In-house发布Profile。

  **适用场景**：[发布In-house应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-0000002281532696)。适用于在企业内部网络环境中分发专属应用给内部员工的场景，In-house应用不适合在任何公开渠道发布。
In-house应用打包需要申请In-house发布证书，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“In-house发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_Hkg9bE3QJqxhnPP2BAb_g/zh-cn_image_0000002658913853.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=E99188F6FE6663BCBB513AE98F9C4BAD0B8D7AB6D94BAC19B812C13A25A9A146)

7. [申请In-house发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-inhouse-profile-0000002283340021)时，对应的证书类型选择“In-house发布”；[申请指定设备发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internaltest-profile-0000002283260129)时，对应的证书类型也选择“In-house发布”。
8. 二进制证书。

  **适用场景**：涉及二进制程序，需使用华为颁发的二进制证书签名，才能在PC上正常运行。
二进制程序需使用华为颁发的二进制证书签名，登录AppGallery Connect申请证书时，弹窗界面证书类型选择“二进制证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/RXaOm-bSTNa78WsXiQ4CBw/zh-cn_image_0000002658793913.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=6C1D820EB3BE1C5E0E2165F1F772E5721CFBA0E5283EEC8436CE564C31B315A8)

9. 企业MDM应用发布证书和企业MDM应用发布Profile。

  **适用场景**：发布企业MDM应用。
发布企业MDM应用时，需要使用企业MDM应用发布证书和企业MDM应用发布Profile手动签名后，才能编译构建正式发布包。登录AppGallery Connect申请证书时，弹窗界面证书类型选择“企业MDM应用发布证书”，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Vh3Jbub_Smed2NIJo3GszQ/zh-cn_image_0000002628394644.png?HW-CC-KV=V1&HW-CC-Date=20260701T041120Z&HW-CC-Expire=86400&HW-CC-Sign=FB4165C10215B983FFB73B3D62C1606C0E183CCCC02C7736B7B4374CFB28BE91)

10. [申请企业MDM应用发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-profile-0000002248341094)时，对应的证书类型选择“企业MDM应用发布”。
 
 

#### 常见FAQ

Q：In-house账号能否申请调试证书，进行本地HDC命令安装测试？
 
A：In-house账号可以申请“调试证书”和“调试Profile”构建软件包本地HDC命令安装，也可以申请“In-house发布证书”和“指定设备发布Profile”，构建的软件包也可以本地HDC命令安装。
