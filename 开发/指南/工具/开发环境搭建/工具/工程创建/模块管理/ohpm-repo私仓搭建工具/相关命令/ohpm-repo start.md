# ohpm-repo start

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start

启动ohpm-repo服务。
 

##### 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。
 
 

##### 命令格式

```text
ohpm-repo start
```
 
 

##### 功能描述

用于启动ohpm-repo服务，创建一个ohpm-repo实例。
 
> [!NOTE]
> 启动时将ohpm-repo服务的pid存放到&lt;deploy_root&gt;/runtime/.pid文件中，其中&lt;deploy_root&gt;为 ohpm-repo私仓部署目录 。

 
 

##### 示例

执行以下命令：
 
```text
ohpm-repo start
```
 
结果示例：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/d6lcCYxORtK38c3bIowXrw/zh-cn_image_0000002602064957.png?HW-CC-KV=V1&HW-CC-Date=20260528T015019Z&HW-CC-Expire=86400&HW-CC-Sign=753303CB5FE57D2F7789901C211FEEAA87534A8DC28EB1A0D2F47125FE9DA85A)
