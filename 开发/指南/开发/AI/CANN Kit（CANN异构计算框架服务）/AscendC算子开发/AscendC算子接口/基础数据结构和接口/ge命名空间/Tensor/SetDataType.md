# SetDataType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdatatype

##### 函数功能

设置Tensor的Datatype。
 
  

##### 函数原型

```text
graphStatus SetDataType(const ge::DataType &dtype);
```
 
  

##### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dtype | 输入 | 需设置的DataType值。 关于DataType类型，请参见DataType。 |
 
 
  

##### 返回值
 
| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH_SUCCESS，否则，返回GRAPH_FAILED。 |
 
 
  

##### 异常处理

无
 
  

##### 约束说明

无
