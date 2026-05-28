# 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13

**问题描述**
 
Mac启动DevEco Studio时，“DevEco Studio”意外退出。
 

![](assets/如何解决mac启动DevEco%20Studio报错提示“DevEco%20Studio”意外退出问题/file-20260515130014132-0.png)

 
**解决方案**
 
问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。
 
规避措施：删除启动脚本 /Users/{USER_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
