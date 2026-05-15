# InferFormatFuncRegister

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferformatfuncregister

## 函数功能

InferFormatFuncRegister构造函数和析构函数。

## 函数原型


> [!NOTE]
> 数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。


```text
InferFormatFuncRegister(const std::string &operator_type, const InferFormatFunc &infer_format_func);
InferFormatFuncRegister(const char_t *const operator_type, const InferFormatFunc &infer_format_func);
~InferFormatFuncRegister() = default;
```


## 参数说明


| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator_type | 输入 | 算子类型。 |
| infer_format_func | 输入 | 算子InferFormat函数。 |


## 返回值

InferFormatFuncRegister构造函数返回InferFormatFuncRegister类型的对象。

## 约束说明

算子InferFormat函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
