# GetKernelType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkerneltype

#### 函数功能

获取当前内核的类型。
 
  

#### 函数原型

```text
const char *GetKernelType() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

当前内核的类型。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto kernel_type = extend_context->GetKernelType();
```
