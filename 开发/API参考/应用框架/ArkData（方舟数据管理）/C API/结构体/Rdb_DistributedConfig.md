# Rdb_DistributedConfig

更新时间：2026-03-20 09:49:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-distributedconfig
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

记录表的分布式配置信息。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb_DistributedConfig结构的版本。 |
| bool isAutoSync | 表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用OH_Rdb_CloudSync接口触发端云同步。 |
