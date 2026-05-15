# 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-29

Native抛异常，如需查看backtrace，运行以下命令。

打开异常栈：

```bash
hdc shell param set persist.ark.properties 0x125c
hdc shell reboot
```

恢复默认值：

```bash
hdc shell param set persist.ark.properties 0x105c
hdc shell reboot
```
