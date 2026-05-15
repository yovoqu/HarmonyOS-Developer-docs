# CloudDisk_FailedList

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-failedlist
**支持设备：** PC/2in1 / Tablet


```text
typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```


## 概述
**支持设备：** PC/2in1 / Tablet

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

**起始版本：** 21

**相关模块：** [CloudDisk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk)

**所在头文件：** [oh_cloud_disk_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h)


## 汇总
**支持设备：** PC/2in1 / Tablet


### 成员变量
**支持设备：** PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [CloudDisk_PathInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo) pathInfo | 失败文件的绝对路径信息。 |
| [CloudDisk_ErrorReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#clouddisk_errorreason) errorReason | 文件同步失败的原因。 |
