# GetBlockDim

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblockdim

##### 函数功能

获取blockDim，即参与计算的Vector或者Cube核数。blockDim的详细概念和设置方式请参考[SetBlockDim](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setblockdim)。
 
  

##### 函数原型

```text
uint32_t GetBlockDim() const;
```
 
  

##### 参数说明

无
 
  

##### 返回值

返回blockDim。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto block_dim = context->GetBlockDim();
  // ...
}
```
