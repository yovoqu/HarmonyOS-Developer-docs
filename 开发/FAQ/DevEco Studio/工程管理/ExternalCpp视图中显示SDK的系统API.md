# ExternalCpp视图中显示SDK的系统API

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-25

问题现象

ExternalCpp视图中显示SDK的系统API。


![](assets/ExternalCpp视图中显示SDK的系统API/file-20260515130020324-0.png)


可能原因

在本地存在多个DevEco Studio（包括Command Line Tools）打开同一个工程，并且使用daemon模式构建该工程。

解决措施

关闭多余的DevEco Studio（包括Command Line Tools）或者使用--no-daemon模式构建工程。

参考链接

守护进程
