# SetExpandDimsType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setexpanddimstype

## 函数功能

设置补维规则。

## 函数原型


```text
void SetExpandDimsType(const ExpandDimsType &expand_dims_type)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| expand_dims_type | 输入 | 补维规则。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
ExpandDimsType new_dim_type("1010");
format.SetExpandDimsType(new_dim_type);
```
