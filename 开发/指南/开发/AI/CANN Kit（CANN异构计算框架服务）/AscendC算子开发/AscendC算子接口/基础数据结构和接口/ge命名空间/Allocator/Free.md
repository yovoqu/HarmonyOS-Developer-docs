# Free

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-free

## 函数功能

根据指定的MemBlock释放内存到内存池。

## 函数原型


```text
virtual void Free(MemBlock *block) = 0;
```


## 参数说明


| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| block | 输入 | 内存block指针。 |


## 返回值

无

## 异常处理

无

## 约束说明

虚函数开发者必须实现。
