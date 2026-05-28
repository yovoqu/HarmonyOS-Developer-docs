# ohpm-repo restore

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restore

将ohpm-repo pack打包产物替换&lt;deploy_root&gt;目录下相应文件，重启服务。
 

##### 前提条件

- 已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。
- 已获得由[pack 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack)打包的.zip 文件。

 
 

##### 命令格式

```text
ohpm-repo restore <file_path>
```
 
 

##### 功能描述

该命令会停止当前ohpm-repo服务，并用打包文件&lt;file_path&gt;中的内容替换ohpm-repo部署根目录&lt;deploy_root&gt;的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。
 
> [!NOTE]
> &lt;file_path&gt;：由ohpm-repo pack命令得到的打包产物。 支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。 &lt;deploy_root&gt;：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM_REPO_DEPLOY_ROOT的环境变量，记录的是 ohpm-repo私仓部署目录 。

 
 

##### 参数

 

##### &lt;file_path&gt;

- 类型：String
- 必填参数

 
指定待解压的打包文件路径。
 
 

##### 示例

执行以下命令：
 
```text
ohpm-repo restore "D:\pack_1702625827995.zip"
```
 
结果示例：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/dnoZA9KASHGvGKsxYoUaHg/zh-cn_image_0000002602184995.png?HW-CC-KV=V1&HW-CC-Date=20260528T015018Z&HW-CC-Expire=86400&HW-CC-Sign=FFA04B6FD1D381175262A0C4BF2CBC424DA957654735166307B2ABEB474CA0B2)
