# 病毒防护服务管理(C/C++)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-vps-c

#### 场景介绍

从6.0.0(20)开始，三方EDR（Endpoint Detection and Response）应用在Device Security Kit上注册后，可以调用注册、更新、卸载（删除数据）接口，将自身应用信息提交至HarmonyOS安全防护服务进行统一管理；零信任应用在Device Security Kit上注册后，可以查询所有注册的EDR信息列表（包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID）；MDM应用在Device Security Kit上注册后，企业管理员可通过MDM（Mobile Device Management）应用启用或禁用HarmonyOS自带的安全防护服务。



#### 约束与限制
1. 当前能力仅支持PC/2in1设备。
2. 不支持并发场景，同一时间仅允许一个三方EDR应用或MDM应用调用该模块接口。



#### 业务流程


![](assets/病毒防护服务管理(C／C++)/file-20260514131141805-0.png)



![](assets/病毒防护服务管理(C／C++)/file-20260514131141805-1.png)



![](assets/病毒防护服务管理(C／C++)/file-20260514131141805-2.png)


**流程说明**：
1. 三方EDR应用注册、更新、卸载时调用该模块接口向HarmonyOS安全防护服务进行应用信息同步。
2. 零信任应用调用该模块接口查询当前注册的所有三方EDR应用的信息。
3. MDM应用调用该模块接口实现HarmonyOS安全防护功能的启停。



#### 接口说明

以下是病毒防护服务管理的相关接口，更多接口及使用方法请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityantivirus)。

| 接口名 | 描述 |
| --- | --- |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_RegisterAntivirus(const char* bundleName) | 三方EDR应用向HarmonyOS安全防护服务注册。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_UnregisterAntivirus(const char* bundleName) | 三方EDR应用从HarmonyOS安全防护服务注销。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_UpdateAntivirus(const SecurityAntivirus_Antivirus* antivirus) | 三方EDR应用向HarmonyOS安全防护服务更新自身应用信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_QueryAntivirus(SecurityAntivirus_Antivirus** list, uint32_t* length) | 零信任应用向HarmonyOS安全防护服务查询当前所有三方EDR注册信息。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_QueryPreinstalledAntivirus (SecurityAntivirus_Antivirus** list, uint32_t* length) | MDM应用向HarmonyOS安全防护服务查询所有用户的防病毒功能状态。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_EnablePreinstalledAntivirus(void) | MDM应用启用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_DisablePreinstalledAntivirus(void) | MDM应用禁用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_EnablePreinstalledAntivirusByAccount(int32_t accountId) | MDM应用启用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |
| SecurityAntivirus_ErrCode HMS_SecurityAntivirus_DisablePreinstalledAntivirusByAccount(int32_t accountId) | MDM应用禁用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |




#### 开发步骤

> [!NOTE]
> 在开发准备过程中，需要申请权限：ohos.permission.REGISTER_ANTIVIRUS、ohos.permission.MANAGE_ANTIVIRUS、ohos.permission.MANAGE_PREINSTALLED_ANTIVIRUS。 只允许名单内的应用申请该权限，申请方式请参考： 申请使用企业类应用可用权限 ， 申请使用仅MDM应用可用权限

1. 在CMakeLists.txt中导入病毒防护服务管理共享库，并链接该库。

  
```text
find_library(dsm-lib libsecurityantivirus_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
```

2. 导入病毒防护服务管理的头文件。

  
```text
#include <cstdio>
#include <cstdlib>
#include "DeviceSecurityKit/security_antivirus.h"
```

3. EDR应用执行接口调用，分别向HarmonyOS安全防护服务中注册、更新、注销应用的信息，需要ohos.permission.REGISTER_ANTIVIRUS权限。

  
注册应用信息。
4. 更新应用信息。
5. 注销应用信息。
6. 零信任应用执行接口调用，查询当前所有在HarmonyOS安全防护服务中注册的三方EDR应用信息，需要ohos.permission.MANAGE_ANTIVIRUS权限。

  
![](assets/病毒防护服务管理(C／C++)/file-20260514131141805-4.png)
 

  零信任应用在根据应用进程信息进行业务处理后，需要释放查询接口出入参的内存。

  
```text
SecurityAntivirus_Antivirus *list = nullptr; // 构造查询接口出参1
uint32_t length = 0; // 构造查询接口出参2
int ret = HMS_SecurityAntivirus_QueryAntivirus(&list, &length);
printf("HMS_SecurityAntivirus_QueryAntivirus ret = %d \n", ret);
```

7. MDM应用执行接口调用，实现HarmonyOS安全防护服务的启停，需要ohos.permission.MANAGE_PREINSTALLED_ANTIVIRUS权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/DELuigMwSs-C5QcA4Qngfw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260730T071917Z&HW-CC-Expire=86400&HW-CC-Sign=4985A5B5431347261A1E3B828B30E49A98CB092A3EB23EA65689E6FF1ABDC7D0)
 

  MDM应用在根据应用进程信息进行业务处理后，需要释放查询接口出入参的内存。

  
查询内置杀毒注册信息。
8. 全局启用内置杀毒。
9. 全局禁用内置杀毒。
10. 启用指定用户的内置杀毒。
11. 禁用指定用户的内置杀毒。
