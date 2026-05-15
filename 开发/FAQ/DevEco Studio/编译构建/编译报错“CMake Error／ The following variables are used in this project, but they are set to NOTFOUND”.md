# 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-33

问题现象

Native工程使用find_path时出现报错。因find_path未在CMAKE_SYSROOT限定路径中找到目标文件而触发该报错。


![](assets/编译报错“CMake%20Error／%20The%20following%20variables%20are%20used%20in%20this%20project,%20but%20they%20are%20set%20to%20NOTFOUND”/file-20260515130106490-0.png)


解决措施

OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将“D:/demo”添加至搜索路径：

list(APPEND CMAKE_FIND_ROOT_PATH_MODE_INCLUDE "D:demo")

添加后，即可使用find_path查找“D:/demo”目录下的文件。
