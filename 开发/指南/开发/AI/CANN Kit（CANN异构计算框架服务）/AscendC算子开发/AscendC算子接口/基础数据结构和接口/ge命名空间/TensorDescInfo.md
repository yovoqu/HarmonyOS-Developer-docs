# TensorDescInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordescinfo

```text
struct TensorDescInfo {
    Format format_ = FORMAT_RESERVED;        /* tbe op register support format */
    DataType dataType_ = DT_UNDEFINED;       /* tbe op register support datatype */
    };
```
 
Format为枚举类型，定义请参考[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。
 
DataType为枚举类型，定义请参考[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。
