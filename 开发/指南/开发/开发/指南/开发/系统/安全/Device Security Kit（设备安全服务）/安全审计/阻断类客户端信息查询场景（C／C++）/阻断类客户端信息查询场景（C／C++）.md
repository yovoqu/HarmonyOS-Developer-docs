# 阻断类客户端信息查询场景（C/C++）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallauthclientsinfo-c

从API版本26.0.0开始，新增阻断类客户端信息查询功能，支持应用获取设备上订阅了阻断类事件的所有客户端信息。其中，阻断类信息是指被系统拦截并阻止执行的安全审计事件记录。


#### 场景介绍

应用调用[HMS_SecurityAudit_AcquireAllAuthClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)接口获取设备上订阅了阻断类事件的所有客户端信息，包括当前已被创建的客户端数量，以及每个客户端创建者的进程名、进程ID和用户ID。该接口常用于在应用创建阻断类客户端失败时，获取设备上已被创建的客户端信息。



#### 约束和限制
1. 当前能力仅支持PC/2in1设备。
2. 当前支持查询全量安全审计阻断类客户端信息，最多存在16个客户端。



#### 业务流程


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/0HxfqMjKT8a0t534JehMHw/zh-cn_image_0000002668461252.png?HW-CC-KV=V1&HW-CC-Date=20260811T005947Z&HW-CC-Expire=86400&HW-CC-Sign=7057A613C257ABECAB49C9B64FB3F2002F069C50A0F5D83A1EB05DFA234FA336)


**流程说明：**
1. 应用调用查询阻断类客户端信息接口[HMS_SecurityAudit_AcquireAllAuthClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)获取全量安全审计阻断类客户端信息。
2. [HMS_SecurityAudit_AcquireAllAuthClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)接口同步返回阻断类客户端信息给应用，应用根据返回的阻断类客户端信息进行业务处理。



#### 接口说明

接口如下表，更多接口及使用方法请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| int32_t HMS_SecurityAudit_AcquireAllAuthClientsInfo(char** outOwnedResult) | 获取全量安全审计阻断类客户端信息。 |




#### 开发步骤

> [!NOTE]
> 在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考： 企业类应用可用权限 。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

  
```text
find_library(dsm-lib libsecurityaudit_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
```

2. 导入安全审计的头文件。

  
```text
#include <cstdio>
#include "DeviceSecurityKit/security_audit.h"
```

3. 应用调用[HMS_SecurityAudit_AcquireAllAuthClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)接口，获取全量安全审计阻断类客户端信息。

  
> [!NOTE]
> 应用在根据阻断类客户端信息进行业务处理后，需要释放查询接口出入参的内存。


  
```text
char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllAuthClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo failed with error: %d\n", ret);
}
// ...
if (outOwnedResult != nullptr) {
    delete[] outOwnedResult;
    outOwnedResult = nullptr;
}
```
