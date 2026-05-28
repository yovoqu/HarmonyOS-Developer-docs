# GetSize

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-getsize

#### 函数功能

获取Tensor数据的内存大小。
 
  

#### 函数原型

```text
size_t GetSize() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

内存大小，单位是字节。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto td_size = t.GetSize(); // 1*2*3*sizeof(float) = 24;
```
