# Malloc

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-malloc

#### 函数功能

在开发者内存池中根据指定size大小申请device内存。
 
  

#### 函数原型

```text
virtual MemBlock *Malloc(size_t size) = 0
```
 
  

#### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| size | 输入 | 指定需要申请内存大小。 |
 
 
  

#### 返回值
 
| 类型 | 描述 |
| --- | --- |
| MemBlock* | 返回MemBlock指针。 |
 
 
  

#### 异常处理

无
 
  

#### 约束说明

纯虚函数开发者必须实现。
