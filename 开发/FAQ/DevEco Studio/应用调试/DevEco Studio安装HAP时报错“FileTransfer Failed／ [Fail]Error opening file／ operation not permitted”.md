# DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-61

**问题现象**
 
DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”。
 

![](assets/DevEco%20Studio安装HAP时报错“FileTransfer%20Failed／%20[Fail]Error%20opening%20file／%20operation%20not%20permitted”/file-20260515130323972-0.png)

 
**解决措施**
 
出现该问题的原因是安装包HAP所在路径没有权限。
 
1、Windows系统建议将工程移出C盘，然后重新运行。
 
2、MAC系统为DevEco Studio获取完全磁盘访问权，请进入**“系统设置”>“隐私与安全性”>“完全磁盘访问权限”**，在列表中勾选DevEco Studio软件并重启。
