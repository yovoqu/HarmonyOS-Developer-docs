# DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35

问题现象

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。


![](assets/DevEco%20Studio安装HAP时报错“FileTransfer%20Failed／%20Error%20while%20Deploy%20Hap”/file-20260515130323086-0.png)


解决措施

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

- 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
- 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
