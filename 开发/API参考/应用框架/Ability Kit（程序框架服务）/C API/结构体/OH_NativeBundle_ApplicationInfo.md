# OH_NativeBundle_ApplicationInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-applicationinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_NativeBundle_ApplicationInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

应用包信息数据结构，包含应用包名和应用指纹信息。
 
**起始版本：** 9
 
**相关模块：** [Native_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)
 
**所在头文件：** [native_interface_bundle.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char* bundleName | 应用包名。 |
| char* fingerprint | 应用的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。 |
