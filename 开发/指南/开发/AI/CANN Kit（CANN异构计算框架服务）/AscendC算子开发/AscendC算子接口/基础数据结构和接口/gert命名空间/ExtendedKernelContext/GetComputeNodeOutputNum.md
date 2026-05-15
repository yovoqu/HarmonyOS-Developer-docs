# GetComputeNodeOutputNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeoutputnum

## 函数功能

获取算子的输出个数。

## 函数原型


```text
size_t GetComputeNodeOutputNum() const;
```


## 参数说明

无

## 返回值

算子的输出个数。

## 约束说明

无

## 调用示例


```text
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast(context);
for (size_t idx = 0; idx GetComputeNodeOutputNum(); ++idx) {
  auto input_td = extend_context->GetOutputDesc(idx);
  // ...
}
```
