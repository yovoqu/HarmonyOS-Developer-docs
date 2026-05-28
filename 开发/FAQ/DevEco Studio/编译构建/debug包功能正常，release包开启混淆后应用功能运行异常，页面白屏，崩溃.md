# debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187

**解决措施**
 
在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。
 

![](assets/debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃/file-20260515130222189-0.png)

 
如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。
 
**参考链接**
 
[通过混淆助手配置保留选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation#section19439175917123)
