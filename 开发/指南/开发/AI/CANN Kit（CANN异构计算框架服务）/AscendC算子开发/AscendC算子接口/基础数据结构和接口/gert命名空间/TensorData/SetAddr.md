# SetAddr

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setaddr

## 函数功能

设置tensor地址。

## 函数原型


```text
ge::graphStatus SetAddr(const ConstTensorAddressPtr addr, TensorAddrManager manager)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| addr | 输入 | tensor地址。 using ConstTensorAddressPtr = const void *; |
| manager | 输入 | tensor的管理函数。 |


## 返回值

成功时返回ge::GRAPH_SUCCESS；失败时返回manager管理函数中定义的错误码。

## 约束说明

无

## 调用示例


```text
auto addr = reinterpret_cast(0x10);
TensorData td(addr, nullptr);
td.SetAddr(addr, HostAddrManager);
```
