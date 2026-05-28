# Native侧如何使用hilog打印出日志信息

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-35

1.在CMakeLists.txt中新增libhilog_ndk.z.so链接：
 
```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
```
 
2.在源文件中包含hilog头文件, 并定义domain、tag宏：
 
```cpp
#include "hilog/log.h"
#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG_TAG "MY_TAG"  // Global tag macro, identifying module log tags
```
 
3.打印日志，以打印ERROR级别的日志为例：
 
注意，需要加上{public}才会显示打印内容，不添加默认是{private}
 
```cpp
int a = 5, b = 10;
OH_LOG_ERROR(LOG_APP, "Pure a:%{public}d b:%{private}d.", a, b);
```
 
结果展示：
 

![](assets/Native侧如何使用hilog打印出日志信息/file-20260515125713378-0.png)

 
**参考链接：**
 
[使用HiLog打印日志(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-guidelines-ndk)
