# GetMin

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmin

## 函数功能

获取最小的T对象指针。

## 函数原型


```text
const T *GetMin() const;
T *GetMin();
```


## 参数说明

无

## 返回值

返回最小的T对象指针。

## 约束说明

无

## 调用示例


```text
int min = -1;
int max = 1024;
Range range(&min,&max);

auto ret = range.GetMin(); // ret指针指向min
```
