# SetMax

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmax

## 函数功能

设置最大的T对象指针。

## 函数原型


```text
void SetMax(T *max)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| max | 输入 | 最大的T对象指针。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
Range range;
int max = 1024;
range.SetMax(&max);
```
