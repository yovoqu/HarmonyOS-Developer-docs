# OH_HiDebug_ResProfilerConfig

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-resprofilerconfig
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_HiDebug_ResProfilerConfig {...} OH_HiDebug_ResProfilerConfig
```
  

##### 概述

定义资源采集配置结构体类型。
 
**起始版本：** 24
 
**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
 
**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t maxDuration | 最大采集时长，取值范围为 [1, 3600]，单位为秒。 传入参数超出取值范围，接口将返回错误码HIDEBUG_RES_PROF_INVALID_MAX_DURATION。 起始版本： 24 |
| uint32_t filterSize | 过滤大小，取值范围为 [1, 4294967295]，单位为字节。 传入参数超出取值范围，接口将返回错误码HIDEBUG_RES_PROF_INVALID_FILTER_SIZE。 起始版本： 24 |
| uint32_t maxStackDepth | 最大栈追踪深度，取值范围为 [0, 30]，单位为帧。 传入参数超出取值范围，接口将返回错误码HIDEBUG_RES_PROF_INVALID_MAX_STACK_DEPTH。 起始版本： 24 |
| uint32_t statisticsInterval | 统计间隔，取值范围为 [0, 3600]，单位为秒。 传入参数超出取值范围，接口将返回错误码HIDEBUG_RES_PROF_INVALID_STATISTICS_INTERVAL。 起始版本： 24 |
| uint32_t sampleInterval | 采样大小，取值范围为 [384, 4294967295]，单位为字节。 在采样模式下，如果内存分配大小小于等于采样大小，则概率性采样，否则全量采样。 传入参数超出取值范围，接口将返回错误码HIDEBUG_RES_PROF_INVALID_SAMPLE_INTERVAL。 起始版本： 24 |
