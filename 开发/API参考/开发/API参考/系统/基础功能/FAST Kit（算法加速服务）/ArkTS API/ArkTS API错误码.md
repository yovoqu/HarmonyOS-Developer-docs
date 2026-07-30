# ArkTS API错误码

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-errorcode
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

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
 
  

#### 1027700001 系统高负载

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
High system load.
 
**错误描述**
 
系统高负载。
 
**可能原因**
 
当前系统高负载，资源紧张。
 
**处理步骤**
 
等待系统负载降低后重试。
 
  

#### 1027700002 省电模式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
Power Saving Mode.
 
**错误描述**
 
系统当前处于省电模式。
 
**可能原因**
 
系统当前处于省电模式。
 
**处理步骤**
 
系统省电模式关闭后重试。
 
  

#### 1027700003 低电量模式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
Low Power Mode.
 
**错误描述**
 
系统当前处于低电量模式。
 
**可能原因**
 
系统当前处于低电量模式。
 
**处理步骤**
 
退出低电量模式后重试。
 
  

#### 1027700004 非前台调用场景

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
Non-frontend calling scenarios.
 
**错误描述**
 
非前台调用场景。
 
**可能原因**
 
应用不在前台运行。
 
**处理步骤**
 
确保应用在前台运行时调用。
 
  

#### 1027700005 间隔不满足要求

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
The interval does not meet the requirement.
 
**错误描述**
 
调用间隔不满足要求。
 
**可能原因**
 
两次调用之间的间隔时间过短。
 
**处理步骤**
 
根据[DurationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-scheduling-optimization#durationtype)调整调用间隔。
 
  

#### 1027700006 执行系统性能优化失败

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**
 
Failed to execute scheduling optimization.
 
**错误描述**
 
执行系统性能优化失败。
 
**可能原因**
 
系统性能优化执行过程中发生错误。
 
**处理步骤**
 
稍后重试。
