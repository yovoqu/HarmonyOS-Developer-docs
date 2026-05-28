# SetStorageFormat

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setstorageformat

##### 函数功能

设置运行时format。
 
  

##### 函数原型

```text
void SetStorageFormat(const ge::Format storage_format)
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage_format | 输入 | 运行时format。 |
 
 
  

##### 返回值

无
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
format.SetStorageFormat(ge::Format::FORMAT_NC);
```
