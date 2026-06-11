# TensorDescInfo

更新时间：2026-06-05 02:03:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordescinfo

```text
struct TensorDescInfo {
    Format format_ = FORMAT_RESERVED;        /* tbe op注册支持的格式 */
    DataType dataType_ = DT_UNDEFINED;       /* tbe op注册支持的数据类型 */
    };
```
 
Format为枚举类型，定义请参考[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。
 
DataType为枚举类型，定义请参考[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。
