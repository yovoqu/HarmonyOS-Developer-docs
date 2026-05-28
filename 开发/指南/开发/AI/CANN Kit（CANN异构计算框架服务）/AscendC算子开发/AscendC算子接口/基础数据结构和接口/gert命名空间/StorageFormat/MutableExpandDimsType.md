# MutableExpandDimsType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableexpanddimstype

##### 函数功能

获取可写的补维规则。
 
  

##### 函数原型

```text
ExpandDimsType &MutableExpandDimsType()
```
 
  

##### 参数说明

无
 
  

##### 返回值

补维规则引用。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
ExpandDimsType new_dim_type("1010");
format.SetExpandDimsType(new_dim_type);
auto &fmt_dim_type = format.MutableExpandDimsType();
```
