# ohpm-repo restart

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart

重新启动ohpm-repo服务。


## 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。

## 命令格式


```text
ohpm-repo restart
```


## 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。
> [!NOTE]
> 启动时将ohpm-repo服务的pid存放到/runtime/.pid文件，其中为ohpm-repo私仓部署目录。


## 示例

执行以下命令：
```text
ohpm-repo restart
```

结果示例：
![](assets/ohpm-repo%20restart/file-20260514134320656-0.png)
