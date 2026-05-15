# SetDimNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdimnum

## 函数功能

设置dim num。

## 函数原型


```text
void SetDimNum(const size_t dim_num)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| dim_num | 输入 | 将Shape对象的dim_num_设置为dim_num。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
Shape shape0({3, 256, 256});
shape0.SetDimNum(1);
auto dim_num = shape0.GetDimNum(); // 1
```
