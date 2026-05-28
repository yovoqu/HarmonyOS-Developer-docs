# SetStorageFormat

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsorageformat

##### 函数功能

设置运行时Tensor的format。
 
  

##### 函数原型

```text
void SetStorageFormat(const ge::Format storage_format)
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage_format | 输入 | 运行时format。 关于ge::Format类型的定义，请参见Format。 |
 
 
  

##### 返回值

无
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetStorageFormat(); // ge::FORMAT_NC1HWC0
```
