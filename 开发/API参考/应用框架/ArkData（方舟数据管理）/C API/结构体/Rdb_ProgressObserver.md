# Rdb_ProgressObserver

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressobserver
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rdb_ProgressObserver {...} Rdb_ProgressObserver
```
  

##### 概述

端云同步进度观察者。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| void* context | 端云同步进度观察者的上下文。 |
| Rdb_ProgressCallback callback | 端云同步进度观察者的回调函数。 |
