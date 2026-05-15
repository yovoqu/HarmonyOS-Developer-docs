# ohpm-repo restore

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restore

将ohpm-repo pack打包产物替换目录下相应文件，重启服务。


## 前提条件

已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。已获得由[pack 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack)打包的.zip 文件。

## 命令格式


```text
ohpm-repo restore
```


## 功能描述

该命令会停止当前ohpm-repo服务，并用打包文件中的内容替换ohpm-repo部署根目录的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。
> [!NOTE]
> ：由ohpm-repo pack命令得到的打包产物。 支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。 ：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM_REPO_DEPLOY_ROOT的环境变量，记录的是ohpm-repo私仓部署目录。


## 参数


## <file_path>

类型：String必填参数 指定待解压的打包文件路径。

## 示例

执行以下命令：
```text
ohpm-repo restore "D:\pack_1702625827995.zip"
```

结果示例：
![](assets/ohpm-repo%20restore/file-20260514134322781-0.png)
