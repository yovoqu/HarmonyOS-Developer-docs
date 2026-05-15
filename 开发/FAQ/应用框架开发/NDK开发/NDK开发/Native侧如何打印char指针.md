# Native侧如何打印char指针

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-47

引入hilog库后直接打印。打印时需要加{public}。

OH_LOG_INFO(LOG_APP, “%{public}s”,path); //可正常打印

OH_LOG_INFO(LOG_APP, “%s”,path); //不可正常打印

示例代码如下：

```cpp
char *path = "abc";
OH_LOG_INFO(LOG_APP, "path: %{public}s", path);
```
