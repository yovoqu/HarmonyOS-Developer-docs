# 2in1设备attach调试失败和增量调试失败

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63

问题现象

1、2in1设备应用调试失败，报错信息如下图所示。


![](assets/2in1设备attach调试失败和增量调试失败/file-20260515130328060-0.png)


2、2in1设备应用使用增量调试失败，报错信息如下图所示。


![](assets/2in1设备attach调试失败和增量调试失败/file-20260515130328060-1.png)


解决措施

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的设置 > 应用加速服务中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。


![](assets/2in1设备attach调试失败和增量调试失败/file-20260515130328060-2.png)
