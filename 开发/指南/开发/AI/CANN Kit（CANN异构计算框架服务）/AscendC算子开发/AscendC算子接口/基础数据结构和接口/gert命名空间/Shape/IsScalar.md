# IsScalar

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isscalar

## 函数功能

判断本shape是否为标量，所谓标量，是指GetDimNum()为0的张量。

## 函数原型


```text
bool IsScalar() const
```


## 参数说明

无

## 返回值

true为标量，false为非标量。

## 约束说明

无

## 调用示例


```text
Shape shape0({3, 256, 256});
Shape shape2;
shape0.IsScalar(); // false
shape2.IsScalar(); // true
```
