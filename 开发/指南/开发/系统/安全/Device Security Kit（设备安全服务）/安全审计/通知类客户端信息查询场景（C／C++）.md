# 通知类客户端信息查询场景（C/C++）

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallclientsinfo-c

从26.0.0开始，支持三方安全应用获取设备上全量的安全审计通知类客户端信息。


#### 场景介绍

应用调用[HMS_SecurityAudit_AcquireAllClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)接口可以获取设备上订阅了安全审计通知类事件的所有客户端信息，用于查看当前已被创建的客户端数量以及每个客户端创建者的进程名、进程ID和用户ID。



#### 约束和限制
1. 当前能力仅支持2in1设备。
2. 当前支持查询全量安全审计通知类客户端信息，最多存在16个客户端。



#### 业务流程


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/uFxALgNvSLa2M0JSlpuXaQ/zh-cn_image_0000002659100339.png?HW-CC-KV=V1&HW-CC-Date=20260701T041504Z&HW-CC-Expire=86400&HW-CC-Sign=241D16BADBA6CEC4112DA8BBC2EE51125C74B143F06D816237A52D479A6AC234)


**流程说明：**
1. 应用调用查询通知类客户端信息接口[HMS_SecurityAudit_AcquireAllClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)获取全量安全审计通知类客户端信息。
2. [HMS_SecurityAudit_AcquireAllClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)接口同步返回通知类客户端信息给应用，应用根据返回的通知类客户端信息进行业务处理。



#### 接口说明

接口如下表，更多接口及使用方法请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)。

| 接口名 | 描述 |
| --- | --- |
| int32_t HMS_SecurityAudit_AcquireAllClientsInfo(char** outOwnedResult) | 获取全量安全审计通知类客户端信息。 |




#### 开发步骤

> [!NOTE]
> 在开发准备过程中，需要申请权限：ohos.permission.QUERY_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考： 申请使用企业类应用可用权限 。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

  
```text
find_library(dsm-lib libsecurityaudit_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
```

2. 导入安全审计的头文件。

  
```text
#include <DeviceSecurityKit/security_audit.h>
#include <cstdio>
```

3. 调用[HMS_SecurityAudit_AcquireAllClientsInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)接口，获取全量安全审计通知类客户端信息。

  
> [!NOTE]
> 应用在根据通知类客户端信息进行业务处理后，需要释放查询接口出入参的内存。


  
```text
char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllClientsInfo failed with error: %d\n", ret);
}
if (outOwnedResult != nullptr) {
    delete[] outOwnedResult;
    outOwnedResult = nullptr;
}
```
