# GetCapacity

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-getcapacity

## 函数功能

获取最大可保存的元素个数。

## 函数原型


```text
size_t GetCapacity() const
```


## 参数说明

无

## 返回值

最大可保存的元素个数。

## 约束说明

无

## 调用示例


```text
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create(capacity);
auto cv = reinterpret_cast(cv_holder.get());
auto cap = cv->GetCapacity(); // 100U
```
