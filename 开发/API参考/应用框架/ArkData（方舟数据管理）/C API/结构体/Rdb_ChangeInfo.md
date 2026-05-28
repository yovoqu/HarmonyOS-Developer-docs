# Rdb_ChangeInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-changeinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rdb_ChangeInfo {...} Rdb_ChangeInfo
```
  

##### 概述

记录端云同步过程详情。
 
**起始版本：** 11
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb_DistributedConfig结构的版本。 |
| const char* tableName | 表示发生变化的表的名称。 |
| int ChangeType | 表示发生变化的数据的类型，数据或者资产附件发生变化。 |
| Rdb_KeyInfo inserted | 记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。 |
| Rdb_KeyInfo updated | 记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。 |
| Rdb_KeyInfo deleted | 记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。 |
