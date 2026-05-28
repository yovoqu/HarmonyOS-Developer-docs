# MutableStorageShape

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-mutablestorageshape

##### 函数功能

获取运行时Tensor的shape，此shape对象是可变的。
 
  

##### 函数原型

```text
Shape &MutableStorageShape()
```
 
  

##### 参数说明

无
 
  

##### 返回值

运行时shape的引用。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableStorageShape(); // 2,1,3
```
