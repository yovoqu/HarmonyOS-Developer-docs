# ohpm-repo restart

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart

重新启动ohpm-repo服务。
 

##### 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。
 
 

##### 命令格式

```text
ohpm-repo restart
```
 
 

##### 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。
 
> [!NOTE]
> 启动时将ohpm-repo服务的pid存放到&lt;deploy_root&gt;/runtime/.pid文件，其中&lt;deploy_root&gt;为 ohpm-repo私仓部署目录 。

 
 

##### 示例

执行以下命令：
 
```text
ohpm-repo restart
```
 
结果示例：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/zK-gOdpjQnuJSEyov1-Nxw/zh-cn_image_0000002602185115.png?HW-CC-KV=V1&HW-CC-Date=20260528T015018Z&HW-CC-Expire=86400&HW-CC-Sign=A588B3D8018D651F15C7906AE861ED2EABB639FEE13371D08B42437F90780FB6)
