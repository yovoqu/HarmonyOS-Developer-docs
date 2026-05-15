# GetPlacement

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplacement

## 函数功能

获取tensor的placement，tensor数据所在的设备位置。
```text
// tensor数据所在的设备位置
enum TensorPlacement {
  kOnDeviceHbm, //

## 函数原型


```text
TensorPlacement GetPlacement() const
```


## 参数说明

无

## 返回值

tensor的placement。 关于TensorPlacement类型的定义，请参见[TensorPlacement](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement)。

## 约束说明

无

## 调用示例


```text
std::vector a = {10};
auto addr = reinterpret_cast(a.data());
TensorData td(addr, HostAddrManager, 100U, kOnHost);
auto td_place = td.GetPlacement(); // kOnHost
```
