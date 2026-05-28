# GetDim

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdim

##### 函数功能

获取对应idx轴的dim值。
 
  

##### 函数原型

```text
int64_t GetDim(const size_t idx) const
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| idx | 输入 | dim的index，调用者需要保证index合法。 |
 
 
  

##### 返回值

dim值，在idx>=kMaxDimNum时，返回kInvalidDimValue。
 
  

##### 约束说明

调用者需要保证index合法，即idx<kMaxDimNum。
 
  

##### 调用示例

```text
Shape shape0({3, 256, 256});
auto dim0 = shape0.GetDim(0); // 3
auto invalid_dim = shape0.GetDim(kMaxDimNum); // kInvalidDimValue
```
