# GetOriginOpTypeSet

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginoptypeset

##### 函数功能

获取原始模型的算子类型集合。
 
  

##### 函数原型

> [!NOTE]
> 数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

 
```text
std::set<std::string> GetOriginOpTypeSet () const;
Status GetOriginOpTypeSet(std::set<ge::AscendString> &ori_op_type) const;
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ori_op_type | 输出 | 原始模型的算子类型集合。 |
 
 
  

##### 约束说明

无
