# HSP/HAR包中如何引用外部编译的so库文件

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6

1. libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86_64。
![](assets/HSP／HAR包中如何引用外部编译的so库文件/file-20260515125614044-0.png)

2. 在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target_link_libraries(entry PUBLIC libxxx)
