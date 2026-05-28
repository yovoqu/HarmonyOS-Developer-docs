# Rdb_SubscribeCallback

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef union Rdb_SubscribeCallback {...} Rdb_SubscribeCallback
```
  

##### 概述

表示回调函数。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rdb_DetailsObserver detailsObserver | 端云数据更改事件的细节的回调函数。 |
| Rdb_BriefObserver briefObserver | 端云数据更改事件的回调函数。 |
