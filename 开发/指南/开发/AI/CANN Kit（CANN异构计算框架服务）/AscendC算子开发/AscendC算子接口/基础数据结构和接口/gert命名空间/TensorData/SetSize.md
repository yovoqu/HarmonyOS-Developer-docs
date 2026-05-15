# SetSize

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsize

## 函数功能

设置tensor数据的内存大小。

## 函数原型


```text
void SetSize(const size_t size)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| size | 输入 | tensor的内存大小，单位为字节。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
std::vector a = {10};
auto addr = reinterpret_cast(a.data());
TensorData td(addr, HostAddrManager, 100U, kOnHost);
td.SetSize(10U);
```
