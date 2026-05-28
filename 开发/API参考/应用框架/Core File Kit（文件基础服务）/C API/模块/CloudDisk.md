# CloudDisk

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk
**支持设备：** PC/2in1 | Tablet

#### 概述

**支持设备：** PC/2in1 | Tablet

此模块提供云盘管理模块的接口和错误码。应用注册一个同步路径的作为根节点，以该路径为父目录的所有子目录都属于同步的范围，该目录简称为：同步根路径。
 
 注册成功后，可以监听该同步根路径下文件的变更，可以查询同步根路径下文件的历史操作记录，以及设置或查询同步根路径下文件的同步状态。
 
**起始版本：** 21
 
  

#### 文件汇总

**支持设备：** PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| cloud_disk_error_code.h | 提供云盘管理模块的错误码定义。 |
| oh_cloud_disk_manager.h | 云盘管理模块的接口定义。 |
