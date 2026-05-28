# Rdb_DataObserver

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-dataobserver
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rdb_DataObserver {...} Rdb_DataObserver
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示数据观察者。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void* context | 表示数据观察者的上下文。 |
| Rdb_SubscribeCallback callback | 数据观察者的回调。 |
