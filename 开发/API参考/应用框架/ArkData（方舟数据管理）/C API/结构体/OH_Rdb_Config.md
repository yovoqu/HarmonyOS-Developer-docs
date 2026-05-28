# OH_Rdb_Config

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-config
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct  {...} OH_Rdb_Config
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

管理关系数据库配置。
 
**起始版本：** 10
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int selfSize | 该结构体的大小。 |
| const char* dataBaseDir | 数据库文件路径。 |
| const char* storeName | 数据库名称。 |
| const char* bundleName | 应用包名。 |
| const char* moduleName | 应用模块名。 |
| bool isEncrypt | 指定数据库是否加密。true表示加密，false表示不加密。 |
| int securityLevel | 设置数据库安全级别OH_Rdb_SecurityLevel。 |
| int area | 设置数据库安全区域等级Rdb_SecurityArea 起始版本： 11 |
