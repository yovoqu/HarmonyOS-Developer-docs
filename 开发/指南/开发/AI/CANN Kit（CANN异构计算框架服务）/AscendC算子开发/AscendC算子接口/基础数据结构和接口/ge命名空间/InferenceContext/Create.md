# Create

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-create

## 函数功能

在资源类算子推理的上下文中，创建资源算子的上下文对象。

## 函数原型


```text
static std::unique_ptr Create(
void *resource_context_mgr = nullptr
)
```


## 参数说明


| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| resource_context_mgr | 输入 | Resource Context管理器指针。 Session创建时候会初始化此指针，由InferShape框架自动传入，生命周期同session。 |


## 返回值


| 类型 | 描述 |
| --- | --- |
| std::unique_ptr | 资源类算子间传递的上下文对象。 |


## 异常处理

无

## 约束说明

无
