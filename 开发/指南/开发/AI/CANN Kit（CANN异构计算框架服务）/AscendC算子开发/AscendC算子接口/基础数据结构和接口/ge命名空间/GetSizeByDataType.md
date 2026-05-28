# GetSizeByDataType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsizebydatatype

##### 函数功能

根据传入的data_type，获取该data_type所占用的内存大小。
 
  

##### 函数原型

```text
inline int GetSizeByDataType(DataType data_type)
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data_type | 输入 | 数据类型，请参见DataType。 |
 
 
  

##### 返回值

该data_type所占用的内存大小（单位为bytes），如果传入非法值或不支持的数据类型，返回-1。
 
  

##### 异常处理

无
 
  

##### 约束说明

无
