# FileShare_PolicyErrorResult

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyerrorresult
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct FileShare_PolicyErrorResult {...} FileShare_PolicyErrorResult
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

授予或使能权限失败的URI策略结果。
 
**起始版本：** 12
 
**相关模块：** [fileShare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare)
 
**所在头文件：** [oh_file_share.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| char *uri | 授予或使能策略失败的URI。 |
| FileShare_PolicyErrorCode code | 授予或使能策略失败的URI对应的错误码。 |
| char *message | 授予或使能策略失败的URI对应的原因。 |
