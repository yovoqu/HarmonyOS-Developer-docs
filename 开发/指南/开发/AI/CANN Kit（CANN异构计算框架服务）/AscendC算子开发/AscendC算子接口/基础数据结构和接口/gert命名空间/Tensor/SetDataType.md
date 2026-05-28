# SetDataType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdatatype

##### 函数功能

设置Tensor的数据类型。
 
  

##### 函数原型

```text
void SetDataType(const ge::DataType data_type)
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data_type | 输入 | 需要设置的Tensor的数据类型。 关于ge::DataType的定义，请参见DataType。 |
 
 
  

##### 返回值

无
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
t.SetDataType(ge::DT_DOUBLE);
```
