# GetOriginFormat

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginformat

## 函数功能

获取原始format。

## 函数原型


```text
ge::Format GetOriginFormat() const
```


## 参数说明

无

## 返回值

原始format。

## 约束说明

无

## 调用示例


```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto origin_format = format.GetOriginFormat(); // Format::FORMAT_NCHW
```
