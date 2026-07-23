# HarmonyOS中如何使用SSE方式请求大模型流式数据

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-80

#### 问题现象

HarmonyOS中如何使用SSE方式请求大模型流式数据？要求如下：
 
- 使用SSE方式请求。
- 请求类型为POST类型。

 
 

#### 解决方案

可以使用官方提供的[EventSource](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/eventsource)三方库实现。
