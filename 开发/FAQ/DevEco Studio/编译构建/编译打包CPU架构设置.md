# 编译打包CPU架构设置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-86

**问题描述**
 
在编译打包时，若需移除v7a，可以参考以下配置文档。
 
**解决方案**
 
可参考 [bm工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bm-tool)
 
```json
"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  <em>// CMake configuration file, providing CMake build scripts</em>
  "arguments": "",
  <em>// Optional compilation parameters passed to CMake</em>
  "abiFilters": [
    "x86_64",
    "arm64-v8a"
  ],
  <em>// Used to set up the local ABI compilation environment</em>
  "cppFlags": ""
  <em>// Set optional parameters for the C++ compiler</em>
},
```
