# GetSubgraphBuilder

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphbuilder

##### 函数功能

根据子图名称获取算子对应的子图构建的函数对象。
 
  

##### 函数原型

> [!NOTE]
> 数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

 
```text
SubgraphBuilder GetSubgraphBuilder(const std::string &name) const;
SubgraphBuilder GetSubgraphBuilder(const char_t *name) const;
```
 
  

##### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 子图名称。 |
 
 
  

##### 返回值

SubgraphBuilder对象。
 
  

##### 异常处理

无
 
  

##### 约束说明

无
