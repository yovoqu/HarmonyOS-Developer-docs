# Asset_ResultSet

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-resultset
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} Asset_ResultSet
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

关键资产查询结果集合，用于定义多条关键资产。
 
**起始版本：** 11
 
**相关模块：** [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)
 
**所在头文件：** [asset_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t count | 关键资产的条数。 |
| Asset_Result *results | 指向关键资产数组的指针。 |
