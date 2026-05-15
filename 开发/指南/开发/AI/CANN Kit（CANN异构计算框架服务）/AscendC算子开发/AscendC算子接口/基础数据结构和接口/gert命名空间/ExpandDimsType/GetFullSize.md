# GetFullSize

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getfullsize

## 函数功能

获取补维后的dim数。

## 函数原型


```text
AxisIndex GetFullSize() const
```


## 参数说明

无

## 返回值

返回补维规则的长度，或者说是补维规则描述的维度。

## 约束说明

无

## 调用示例


```text
ExpandDimsType type1("1001");
auto dim_num = type1.GetFullSize(); // dim_num=4
```
