# SetTiling

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling

##### 函数功能

注册Tiling函数。
 
  

##### 函数原型

```text
OpAICoreDef &SetTiling(gert::OpImplRegisterV2::TilingKernelFunc func);
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Tiling函数。TilingKernelFunc类型定义如下。 using TilingKernelFunc = UINT32 (*)(TilingContext *); |
 
 
  

##### 返回值

[OpAICoreDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling)算子定义。
 
  

##### 约束说明

无
