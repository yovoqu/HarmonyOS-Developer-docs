# 如何处理include &lt;stddef.h&gt;编译报错

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-59

问题现象

C语言代码中包含<stddef.h>时编译报错：

lib/clang/15.0.4/include/stddef. h:74:24: error: typedef redefinition with different types ('unsigned short" vs 'unsigned int")typedefWCHAR_TYPE _ wchar_t;… 10/native/sysroot/us/include/aarch64-linux-ohos/bits/alltypes.h:15:18: note: previous definition is here typedef unsigned wchar_t。

解决措施

在CMakeLists.txt中删除TARGET_COMPILE_OPTIONS内的参数-fshort-wchar。
