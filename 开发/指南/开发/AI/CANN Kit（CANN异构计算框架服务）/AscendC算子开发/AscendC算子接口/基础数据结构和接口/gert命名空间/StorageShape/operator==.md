# operator==

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-operatora

#### 函数功能

判断shape是否相等。
 
  

#### 函数原型

```text
bool operator==(const StorageShape &other) const
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个shape。 |
 
 
  

#### 返回值

true：相等。
 
false：不相等。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
StorageShape shape0({3, 256, 256}, {256, 256, 3});
StorageShape shape1({3, 256, 256}, {3, 256, 256});
bool is_same_shape = shape0 == shape1; // false
```
