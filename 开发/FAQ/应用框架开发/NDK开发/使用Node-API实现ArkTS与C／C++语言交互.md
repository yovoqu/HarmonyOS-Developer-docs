# 在ArkTS层往C++层注册一个object或function，C++层可以按需往这个回调上进行扔消息同步到上层应用么，请提供示例？在注册object或function时，napi_env是否可以被长时持有？扔消息同步到上层应用时，是否需要在特定线程

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-49

在ArkTS侧不能向C++层注册对象或函数，开发者需要在C++层自行处理。Env可以长期持有，但在使用Env时，必须在创建该Env的ArkTS线程中进行。
 
**参考链接**
 
[Native与ArkTS对象绑定](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process)
