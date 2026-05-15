# ConvertToListAscendString

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-converttolistascendstring

## 函数功能

定义了一个模板函数ConvertToListAscendString，用于将不同类型的字符串列表转换为AscendString类型的列表。

## 函数原型


```text
template std::vector ConvertToListAscendString(T strs)
```

 支持以下两种拓展：
```text
template inline std::vector ConvertToListAscendString(std::vector strs)
```

 对于std::vector类型的字符串列表，先将其转换为std::vector类型，然后再进行转换。
```text
template inline std::vector ConvertToListAscendString(std::vector strs)
```

 对于std::vector类型的字符串列表，直接返回原列表。

## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| strs | 输入 | 待转换的字符串列表。 |


## 返回值

转换后的AscendString类型字符串列表。

## 异常处理

无

## 约束说明

无
