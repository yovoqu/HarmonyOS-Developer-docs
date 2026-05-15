# GetInputInstanceInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputinstanceinfo

## 函数功能

根据算子IR原型中的输入索引，获取对应的实例化对象。

## 函数原型


```text
const AnchorInstanceInfo *GetInputInstanceInfo(const size_t ir_index) const
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |


## 返回值

返回const类型的实例化对象的地址。

## 约束说明

无

## 调用示例


```text
for (size_t i = 0; i
