# GetAddr

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getaddr

#### 函数功能

获取tensor数据地址。若存在manager函数，则由manager函数给出地址。
 
  

#### 函数原型

```text
TensorAddress GetAddr() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

tensor地址。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
auto addr0 = reinterpret_cast<void *>(0x10);
TensorData td(addr, nullptr);
auto addr1 = td.GetAddr(); // 0x10
```
