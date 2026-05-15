# 编译打包CPU架构设置

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-86

问题描述

在编译打包时，若需移除v7a，可以参考以下配置文档。

解决方案

可参考 bm工具

```json
"externalNativeOptions": {
"path": "./src/main/cpp/CMakeLists.txt",
//CMake configuration file, providing CMake build scripts
"arguments": "",
//Optional compilation parameters passed to CMake
"abiFilters": [
"x86_64",
"arm64-v8a"
],
//Used to set up the local ABI compilation environment
"cppFlags": ""
//Set optional parameters for the C++ compiler
},
```
