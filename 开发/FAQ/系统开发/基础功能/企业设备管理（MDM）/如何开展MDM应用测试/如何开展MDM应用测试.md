# 如何开展MDM应用测试

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-7

#### 问题现象

MDM应用开发进入测试阶段后，开发者在申请企业MDM应用发布证书及profile、运行、以及设备重置后自动部署场景中。
 1. 申请企业MDM应用发布证书及profile。已申请了企业MDM应用发布证书及profile，在signingConfigs里面配置了企业MDM的证书和profile，但是应用编译后无法安装到手机中。报错如下：

  
```text
Install Failed: error: failed to install bundle.
code:9568266
error: install permission denied.
```

2. MDM应用激活。使用EMM控制台，添加了测试设备的SN，上传了测试应用的hap，设备重置后也成功下载了应用，但是应用无法获得设备管理权限。
 
 

#### 背景知识
1. MDM应用开发需要[申请企业MDM应用发布证书和企业MDM应用发布profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-profile-0000002248341094)。
2. MDM接口需要在激活企业设备管理扩展能力后使用，调试时仍需手动通过hdc命令来激活/解除激活扩展能力，参见[调试说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide#调试说明)。
 
 

#### 解决方案
1. MDM应用调试、测试阶段，可以正常[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)，MDM应用的调试证书申请流程和普通APP一致，但是一定要先完成以下操作再申请调试证书：
[申请企业MDM应用发布证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-enterprise-mdm-cert-0000002283256801)，确认开发者账号已经有了MDM应用开发权限。
2. 申请企业MDM应用发布profile，在申请profile的时候勾选上“受限ACL权限”，然后在权限选择时选择MDM的相关权限。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/SG8khCOpRMmzldFzCswxjQ/zh-cn_image_0000002628774292.png?HW-CC-KV=V1&HW-CC-Date=20260730T072606Z&HW-CC-Expire=86400&HW-CC-Sign=D8B9F3ECD5E61723F1547D1C88333F879B46709BC82AA580F0657D0942ADF1AD)

3. 使用调试证书打包出APP。由于MDM接口需要在激活企业设备管理扩展能力后使用，调试时仍需手动通过hdc命令来激活/解除激活扩展能力，因此APP安装后，需要通过命令行“hdc shell edm enable-admin”开启测试设备的MDM权限。
4. 若设备重置后未自动安装部署，需要检查EMM控制台的配置是否正确，最常见的错误是“设备型号”填错。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/wIie_8dxTVqGOBbMqBWGVA/zh-cn_image_0000002658973603.png?HW-CC-KV=V1&HW-CC-Date=20260730T072606Z&HW-CC-Expire=86400&HW-CC-Sign=11F396B4D5558D22094FD67B57B1EA7E9701ACF82FC704727BD53C2B48690F7B)


  “设备型号”请填写“型号代码”，比如ALN-AL00：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/BXd_Rq-SRPiJ4fyS1iEh-w/zh-cn_image_0000002628614394.png?HW-CC-KV=V1&HW-CC-Date=20260730T072606Z&HW-CC-Expire=86400&HW-CC-Sign=87A2C41184F67AF417ABF6F21026175C9860C4C6462AB813C732829D3D2C34A3)

5. 完成测试后，可使用“hdc shell edm disable-admin -n 包名”去激活。
 
 

#### 常见FAQ

Q：为什么申请调试证书前，需要先申请发布证书？
 
A：因为申请发布证书时，会申请MDM权限，有了权限，调试证书才能正常工作。
