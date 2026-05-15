# 出现“container is not running”错误

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4

问题现象

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。


![](assets/出现“container%20is%20not%20running”错误/file-20260515130339953-0.png)


解决措施

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。


![](assets/出现“container%20is%20not%20running”错误/file-20260515130339953-1.png)
