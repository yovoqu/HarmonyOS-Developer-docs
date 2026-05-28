# 如何解决hdc server和client版本不一致的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-38

**问题现象**
 
hdc.log 中的报错信息为“Daemon Session Handshake failed”。
 

![](assets/如何解决hdc%20server和client版本不一致的问题/file-20260515125605892-0.png)

 
**解决措施**
 1. 通过以下命令检查server和client的版本是否匹配。hdc checkserver
2. 执行以下命令，终止其他版本的服务器。hdc kill
