# GetStorageFormat

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getstorageformat

#### 函数功能

获取运行时format。
 
  

#### 函数原型

```text
ge::Format GetStorageFormat() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

运行时format。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto storage_format = format.GetStorageFormat(); // Format::FORMAT_C1HWNC0
```
