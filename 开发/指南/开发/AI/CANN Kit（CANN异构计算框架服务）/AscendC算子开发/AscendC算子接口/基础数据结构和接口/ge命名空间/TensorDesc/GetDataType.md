# GetDataType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getdatatype

#### 函数功能

获取TensorDesc所描述Tensor的数据类型。
 
  

#### 函数原型

```text
DataType GetDataType() const;
```
 
  

#### 参数说明

无
 
  

#### 返回值
 
| 类型 | 描述 |
| --- | --- |
| DataType | TensorDesc所描述的Tensor的数据类型。 |
 
 
  

#### 异常处理

无
 
  

#### 约束说明

由于返回的DataType信息为值拷贝，因此修改返回的DataType信息，不影响TensorDesc中已有的DataType信息。
