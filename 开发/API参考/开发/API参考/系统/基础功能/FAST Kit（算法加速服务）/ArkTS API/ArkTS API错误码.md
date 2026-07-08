# ArkTS API错误码

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-errorcode
**支持设备：** Phone | PC/2in1 | Tablet

> [!TIP]
> 以下仅介绍本模块特有错误码，通用错误码请参考 通用错误码说明文档 。

  

#### 1023100001 数组长度无效

**支持设备：** Phone | PC/2in1 | Tablet

**错误信息**
 
Array length invalid.
 
**错误描述**
 
数组长度无效。
 
**可能原因**
 
传入的采样点数组长度不足2个。
 
**处理步骤**
 
检查传入的samples数组是否包含至少2个数据点。
