# OH_NativeBundle_ModuleMetadata

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_NativeBundle_ModuleMetadata {...} OH_NativeBundle_ModuleMetadata
```
  

##### 概述

模块元数据的信息。
 
**起始版本：** 20
 
**相关模块：** [Native_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)
 
**所在头文件：** [native_interface_bundle.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char* moduleName | 模块名称。 |
| OH_NativeBundle_Metadata* metadataArray | 模块的元数据数组。 |
| size_t metadataArraySize | 模块的元数据数组大小。 |
