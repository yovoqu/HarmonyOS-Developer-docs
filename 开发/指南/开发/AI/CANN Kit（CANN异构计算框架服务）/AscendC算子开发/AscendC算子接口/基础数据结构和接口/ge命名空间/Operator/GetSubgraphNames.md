# GetSubgraphNames

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphnames

#### 函数功能

获取一个算子的子图名称列表。
 
  

#### 函数原型

> [!NOTE]
> 数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

 
```text
std::vector<std::string> GetSubgraphNames() const;
graphStatus GetSubgraphNames(std::vector<AscendString> &names) const;
```
 
  

#### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| names | 输出 | 获取一个算子的子图名称列表。 |
 
 
  

#### 返回值
 
| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH_FAILED：失败。 GRAPH_SUCCESS：成功。 |
 
 
  

#### 异常处理

无
 
  

#### 约束说明

无
