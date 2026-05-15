# 运行时出现Import DevEco Studio Settings弹窗

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16

问题现象

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现Import DevEco Studio Settings弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现Import DevEco Studio Settings弹窗。


![](assets/运行时出现Import%20DevEco%20Studio%20Settings弹窗/file-20260515130003904-0.png)


解决措施

方案一：建议保持默认勾选项Do not import settings。

方案二：勾选Config or installation directory，上传配置项压缩包（settings.zip）。


> [!NOTE]
> 点击File > Manage IDE Settings > Export Settings...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。
