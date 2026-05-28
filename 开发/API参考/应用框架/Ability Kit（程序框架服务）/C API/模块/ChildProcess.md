# ChildProcess

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

提供子进程的管理能力，支持创建Native子进程并在父子进程间建立IPC通道，用于实现多进程应用开发。
 
创建的子进程不支持UI界面，也不支持Context相关的接口调用。通过此模块和[childProcessManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager)（非SELF_FORK模式）启动的子进程总数最大为512个。
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**起始版本：** 12
 
  

##### 文件汇总
 
| 名称 | 描述 |
| --- | --- |
| native_child_process.h | 支持创建Native子进程，并在父子进程间建立IPC通道。 引用文件：<AbilityKit/native_child_process.h> 库：libchild_process.so |
