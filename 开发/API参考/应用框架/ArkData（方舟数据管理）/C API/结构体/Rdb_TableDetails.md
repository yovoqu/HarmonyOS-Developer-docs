# Rdb_TableDetails

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-tabledetails
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rdb_TableDetails {...} Rdb_TableDetails
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

描述数据库表执行端云同步任务上传和下载的统计信息。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char* table | 数据库表名。 |
| Rdb_Statistic upload | 表示数据库表中端云同步上传过程的统计信息。 |
| Rdb_Statistic download | 表示数据库表中端云同步下载过程的统计信息。 |
