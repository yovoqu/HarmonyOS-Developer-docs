# GetFormat

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getformat

##### 函数功能

获取TensorDesc所描述的Tensor的Format。
 
  

##### 函数原型

```text
Format GetFormat() const;
```
 
  

##### 参数说明

无
 
  

##### 返回值
 
| 类型 | 描述 |
| --- | --- |
| Format | TensorDesc所描述的Tensor的format信息。 |
 
 
  

##### 异常处理

无
 
  

##### 约束说明

由于返回的Format信息为值拷贝，因此修改返回的Format信息，不影响TensorDesc中已有的Format信息。
