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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ZVvHkSfJRnGLn36sHvP_Zg/zh-cn_image_0000002648076396.png?HW-CC-KV=V1&HW-CC-Date=20260811T005949Z&HW-CC-Expire=86400&HW-CC-Sign=1DE8687A67BD769DC1CCAB17AB1CA9432D6D1EF7A444087AFD3B43B2EDA2EFB5)

 
或者先attach调试主进程，再点击调试面板的
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Zen_rpPMQA28pVOlMreQ6A/zh-cn_image_0000002678156115.png?HW-CC-KV=V1&HW-CC-Date=20260811T005949Z&HW-CC-Expire=86400&HW-CC-Sign=51029EC33FB2FF933C60AF4EEFD8B13BCF9B480FF607BB6A4FC5A44126294EFD)
，打开attach窗口选择子进程进行调试。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/eJXrdpI7RySf5NlwdyZrgA/zh-cn_image_0000002647916496.png?HW-CC-KV=V1&HW-CC-Date=20260811T005949Z&HW-CC-Expire=86400&HW-CC-Sign=57495478E8FF258507E634CB7CD48C4806BD4BD1923919AF0AA4E058BE228995)
