# GetNodeName

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodename

## 函数功能

获取算子的名称。

## 函数原型


```text
const char *GetNodeName() const
```


## 参数说明

无

## 返回值

算子的名称。

## 约束说明

无

## 调用示例


```text
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast(context);
auto node_name = extend_context->GetNodeName();
```
