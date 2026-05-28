# FileShare_PolicyInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyinfo
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct FileShare_PolicyInfo {...} FileShare_PolicyInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

需要授予或使能权限URI的策略信息。
 
**起始版本：** 12
 
**相关模块：** [fileShare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare)
 
**所在头文件：** [oh_file_share.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| char *uri | 需要授予或使能权限的URI。 |
| unsigned int length | URI的字节长度。 |
| unsigned int operationMode | 授予或使能权限的URI访问模式。 示例：FileShare_OperationMode.READ_MODE 、 FileShare_OperationMode.WRITE_MODE 或者 FileShare_OperationMode.READ_MODE\|FileShare_OperationMode.WRITE_MODE。 |
