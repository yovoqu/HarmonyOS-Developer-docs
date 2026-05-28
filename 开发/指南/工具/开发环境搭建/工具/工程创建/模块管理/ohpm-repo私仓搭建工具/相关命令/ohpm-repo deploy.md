# ohpm-repo deploy

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-deploy

使用备份文件部署新的ohpm-repo实例。
 

#### 前提条件

已获得由[pack 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack)打包的.zip文件。
 
 

#### 命令格式

```text
ohpm-repo deploy <file_path> [options]
```
 
 

#### 功能描述

命令将使用由ohpm-repo pack得到的打包产物部署新的ohpm-repo实例。 命令要求数据存储必须使用mysql，文件存储必须使用sftp或者custom ，且在命令执行时，会检查数据库mysql中存储的ohpm-repo实例列表与配置的sftp或者custom存储目录中的ohpm-repo实例列表是否一致，若不一致则命令执行失败。
 
 

#### 参数

 

#### &lt;file_path&gt;

- 类型：String
- 必填参数

 
必须在deploy命令后面配置&lt;file_path&gt;参数，指定打包产物路径。
 
 

#### 选项

 

#### deploy_root

- windows系统默认值："~/AppData/Roaming/Huawei/ohpm-repo"
- 其他系统默认值："~/ohpm-repo"
- 类型： String

 
可以在deploy命令后面配置--deploy_root &lt;string&gt;参数，未配置将使用默认值。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
 
 

#### logs

- 类型： String

 
可以在deploy命令后面配置--logs &lt;string&gt;参数，指定log目录，优先级高于config.yaml中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
 
 

#### uplinkCachePath

- 类型： String

 
可以在deploy命令后面配置--uplinkCachePath &lt;string&gt;参数，指定远程包缓存路径，优先级高于config.yaml中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
 
> [!NOTE]
> 部署实例成功后，命令行所配置的deploy_root，logs和uplinkCachePath会写入到运行时配置文件中，可从&lt;deploy_root&gt;/conf目录中的配置文件config.yaml中查看。

 
 

#### skip-db

- 默认值：false
- 类型：Boolean
- 别名：s

 
在deploy命令后面配置-s或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。
 
> [!NOTE]
> 1. 在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。 2. 从ohpm-repo 5.2.0 版本起， -sd 已标记废弃，替换为 -s。

 
 

#### 示例

执行以下命令：
 
```text
ohpm-repo deploy D:\ohpm-repo\bin\pack_1695805599689.zip --deploy_root D:\new-ohpm-repo\ohpm-repo-deploy
```
 
结果示例：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/T4xf__-aRMCb-J2PcR0lwA/zh-cn_image_0000002571545446.png?HW-CC-KV=V1&HW-CC-Date=20260528T030649Z&HW-CC-Expire=86400&HW-CC-Sign=E299F2B2D755D26EC966A50E4B921596C28A5D5D90C5957BF8362727AE41157F)
