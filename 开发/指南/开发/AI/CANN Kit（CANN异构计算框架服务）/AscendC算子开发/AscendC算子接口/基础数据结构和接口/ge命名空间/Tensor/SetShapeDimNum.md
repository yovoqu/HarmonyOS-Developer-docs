# SetShapeDimNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setshapedimnum

#### 函数功能

设置shape的维度大小，即rank大小。
 
  

#### 函数原型

```text
graphStatus SetShapeDimNum(const size_t dim_num);
```
 
  

#### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dim_num | 输入 | shape的维度大小，即原始shape的rank。 |
 
 
  

#### 返回值
 
| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH_SUCCESS，否则，返回GRAPH_FAILED。 |
 
 
  

#### 异常处理

无
 
  

#### 约束说明

无
