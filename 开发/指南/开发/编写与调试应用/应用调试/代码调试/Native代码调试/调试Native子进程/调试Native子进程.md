# 调试Native子进程

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-child-process

从26.0.0 Beta2版本开始，DevEco Studio支持对[Native子进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-development-guideline)进行调试，包括OH_Ability_StartNativeChildProcess和OH_Ability_CreateNativeChildProcess接口创建的Native子进程。
 

#### 使用约束

- 支持API 26.0.0及以上版本的2in1设备。
- 通过OH_Ability_StartNativeChildProcess接口创建Native子进程时，不支持调试[隔离模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h#oh_ability_childprocessconfigs_setisolationmode)（NCP_ISOLATION_MODE_ISOLATED = 1）的Native子进程。
- 通过OH_Ability_CreateNativeChildProcess接口创建Native子进程时，不支持调试[独立uid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h#oh_ability_childprocessconfigs_setisolationuid)的Native子进程。

 
 

#### 调试方式

通过attach方式对Native子进程进行调试，在attach窗口中直接选择子进程进行调试。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5k6R4p6NSMqTPGoaI8L8Qg/zh-cn_image_0000002648076396.png?HW-CC-KV=V1&HW-CC-Date=20260730T072213Z&HW-CC-Expire=86400&HW-CC-Sign=CB15302425F7DBA4DE7C4AD2242B154D305995523DE1DAE71356B34C255F34FF)

 
或者先attach调试主进程，再点击调试面板的
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KV_bSe0MRVi8fYSY24yF3A/zh-cn_image_0000002678156115.png?HW-CC-KV=V1&HW-CC-Date=20260730T072213Z&HW-CC-Expire=86400&HW-CC-Sign=7BB036508F90879131CD274B917B2473D08785CA0165F4947D1670BCDFF53E27)
，打开attach窗口选择子进程进行调试。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/QPMGJBWrQnGSXAIUWFHGjA/zh-cn_image_0000002647916496.png?HW-CC-KV=V1&HW-CC-Date=20260730T072213Z&HW-CC-Expire=86400&HW-CC-Sign=2B73E18EA2664C8F0280F0FFA54E08B72F4B41AAE92C32004F09D3F5ABD3D2E4)
