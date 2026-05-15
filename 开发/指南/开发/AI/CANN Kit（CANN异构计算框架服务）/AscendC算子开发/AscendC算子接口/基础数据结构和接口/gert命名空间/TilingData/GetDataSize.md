# GetDataSize

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdatasize

## 函数功能

获取tiling data长度。

## 函数原型


```text
size_t GetDataSize() const;
```


## 参数说明

无

## 返回值

tiling data长度。

## 约束说明

无

## 调用示例


```text
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast(td_buf.get());
size_t data_size = td->GetDataSize(); // 0

td->SetDataSize(100U);
data_size = td->GetDataSize(); // 100
```
