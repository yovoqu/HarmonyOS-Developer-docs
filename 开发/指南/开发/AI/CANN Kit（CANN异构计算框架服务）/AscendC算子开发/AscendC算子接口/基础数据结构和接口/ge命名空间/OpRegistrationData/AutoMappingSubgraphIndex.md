# AutoMappingSubgraphIndex

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingsubgraphindex

## 函数功能

设置子图的输入输出和主图对应父节点输入输出的对应关系。

## 函数原型


```text
Status AutoMappingSubgraphIndex(const ge::Graph &graph,
const std::function &input,
const std::function &output)
Status AutoMappingSubgraphIndex(const ge::Graph &graph,
const std::function &input,
const std::function &output)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| graph | 输入 | 子图对象 |
| input | 输入 | 输入对应关系函数 |
| output | 输入 | 输出对应关系函数 |


## 约束说明

无
