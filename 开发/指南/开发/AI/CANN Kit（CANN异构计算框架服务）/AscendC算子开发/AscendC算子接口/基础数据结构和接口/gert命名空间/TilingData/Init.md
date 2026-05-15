# Init

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-init

## 函数功能

初始化TilingData。

## 函数原型


```text
void Init(const size_t cap_size, void *const data);
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| cap_size | 输入 | 最大容量，单位为字节。 |
| data | 输入 | tiling data的地址。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
size_t cap_size = 100U;
size_t total_size = cap_size + sizeof(TilingData);
auto td_buf = std::unique_ptr(new (std::nothrow) uint8_t[total_size]());
auto td = reinterpret_cast(td_buf.get());
td->Init(cap_size, td_buf.get() + sizeof(TilingData)); // 内存平铺
```
