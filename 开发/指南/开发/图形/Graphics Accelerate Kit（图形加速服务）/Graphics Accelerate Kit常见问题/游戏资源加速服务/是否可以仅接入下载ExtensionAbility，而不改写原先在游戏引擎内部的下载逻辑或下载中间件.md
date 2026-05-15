# 是否可以仅接入下载ExtensionAbility，而不改写原先在游戏引擎内部的下载逻辑或下载中间件

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-6

可以，支持仅接入下载ExtensionAbility。

但建议在应用进入前台时，通过[removeAllAssetDownloadTasks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadmanagerremoveallassetdownloadtasks)移除系统中的所有下载任务，对于已完成下载的任务可以复用，避免重复下载。对于未完成下载的任务建议使用应用自身下载器进行重新下载。
