# MutableStorageShape

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutablestorageshape

## 函数功能

获取可写的运行时shape。

## 函数原型


```text
Shape &MutableStorageShape()
```


## 参数说明

无

## 返回值

可写的运行时shape。

## 约束说明

无

## 调用示例


```text
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto storage_shape = shape.MutableStorageShape(); // 256,256,3
```
