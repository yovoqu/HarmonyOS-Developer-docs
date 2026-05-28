# GetKernelName

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkernelname

#### 函数功能

获取当前内核的名称。
 
  

#### 函数原型

```text
const char *GetKernelName() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

当前内核的名称。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto kernel_name = extend_context->GetKernelName();
```
