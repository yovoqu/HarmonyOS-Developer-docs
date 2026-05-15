# 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4

问题现象

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

解决措施

导致该问题的原因是包名使用错误。在工程级oh-package.json5中，将devDependencies字段下"hypium"修改为"@ohos/hypium"。


![](assets/打开历史工程，报错提示“Install%20failed%20FetchPackageInfo／%20hypium%20failed”/file-20260515130007859-0.png)


@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入ohpm info @ohos/hypium命令，输出结果中dist-tags下方即为版本号。


![](assets/打开历史工程，报错提示“Install%20failed%20FetchPackageInfo／%20hypium%20failed”/file-20260515130007859-1.png)
