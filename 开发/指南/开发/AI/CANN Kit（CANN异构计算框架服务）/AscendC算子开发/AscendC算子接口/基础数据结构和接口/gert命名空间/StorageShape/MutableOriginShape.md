# MutableOriginShape

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableoriginshape

#### 函数功能

获取可写的原始shape。
 
  

#### 函数原型

```text
Shape &MutableOriginShape()
```
 
  

#### 参数说明

无
 
  

#### 返回值

可写的原始shape。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto origin_shape = shape.MutableOriginShape(); // 3,256,256
```
