# Native C++模板中，生成的so库的名称在哪里定义，需要与哪些内容保持一致

更新时间：2026-03-12 12:31:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-46

导入使用的模块名和注册时的模块名大小写保持一致。例如，模块名为 entry，则so的名字为libentry.so，napi_module中nm_modname字段应为entry，ArkTS侧使用时，代码为：import xxx from 'libentry.so'。
