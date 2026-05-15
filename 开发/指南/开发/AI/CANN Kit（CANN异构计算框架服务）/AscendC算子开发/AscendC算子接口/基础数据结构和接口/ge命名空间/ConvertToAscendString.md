# ConvertToAscendString

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-converttoascendstring

## 函数功能

模板函数，接受一个模板参数T，并将其转换为AscendString类型。这个函数的主要功能是将不同类型的字符串转换为AscendString类型。

## 函数原型


```text
template ge::AscendString ConvertToAscendString(T str)
```

 支持以下几种拓展：
```text
template inline ge::AscendString ConvertToAscendString(const char *str)
```

 对于const char *类型的字符串，直接使用AscendString的构造函数进行转换。
```text
template inline ge::AscendString ConvertToAscendString(std::string str)
```

 对于std::string类型的字符串，先将其转换为const char *类型，然后再进行转换。
```text
template inline ge::AscendString ConvertToAscendString(ge::AscendString str)
```

 对于AscendString类型的字符串，直接返回AscendString类型字符串。

## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的字符串。 |


## 返回值

转换后的AscendString类型字符串。

## 异常处理

无

## 约束说明

无
