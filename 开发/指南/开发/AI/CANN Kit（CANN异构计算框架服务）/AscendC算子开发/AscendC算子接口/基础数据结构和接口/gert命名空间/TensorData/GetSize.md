# GetSize

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsize

##### 函数功能

获取tensor数据的内存大小。
 
  

##### 函数原型

```text
size_t GetSize() const
```
 
  

##### 参数说明

无
 
  

##### 返回值

tensor所占内存大小，单位为字节。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
auto addr = reinterpret_cast<void *>(0x10);
TensorData td(addr, HostAddrManager, 100U, kOnHost);
auto td_size = td.GetSize(); // 100U
```
