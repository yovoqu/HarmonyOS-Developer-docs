# napi_module结构体字段描述解析

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-37

关于napi_module_register(napi_module* mod)方法的入参napi_module有两个关键属性：一个是.nm_register_func，定义模块初始化函数；另一个是.nm_modname，定义模块的名称，也就是ArkTS侧引入的so库的名称，模块系统会根据此名称来区分不同的so。napi_module字段的详细描述如下：

```cpp
static napi_module demoModule = {
.nm_version = 1, // nm Version number, default value is 1
.nm_flags = 0, // nm Identifier
.nm_filename = nullptr, // File name, don't pay attention to it for now, just use the default value
.nm_register_func = Init, // Specify the entrance function for nm
.nm_modname = "entry", // Specify the module name to import from the ArkTS page
.nm_priv = ((void*)0), // Don't follow for now, just use the default settings
.reserved = { 0 }, // Don't pay attention for now, just use the default value
};
```
