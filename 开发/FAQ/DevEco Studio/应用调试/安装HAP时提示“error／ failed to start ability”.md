# 安装HAP时提示“error: failed to start ability”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-23

**问题现象**
 
启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，请检查应用的可见性设置。
 

![](assets/安装HAP时提示“error／%20failed%20to%20start%20ability”/file-20260515130308404-0.png)

 
**解决措施**
 
- 在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
- FA模型工程：在config.json文件的abilities字段中，将visible设置为true。
