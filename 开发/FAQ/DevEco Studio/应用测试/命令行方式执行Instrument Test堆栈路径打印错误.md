# 命令行方式执行Instrument Test堆栈路径打印错误

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7

问题现象

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。


![](assets/命令行方式执行Instrument%20Test堆栈路径打印错误/file-20260515130343071-0.png)


原因

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

解决措施

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。


![](assets/命令行方式执行Instrument%20Test堆栈路径打印错误/file-20260515130343071-1.png)
