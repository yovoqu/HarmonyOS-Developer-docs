# operator!=

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatorb

#### 函数功能

判断格式是否不相等。
 
  

#### 函数原型

```text
bool operator!=(const StorageFormat &other) const
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一种格式。 |
 
 
  

#### 返回值

true表示格式不同。
 
false表示格式相同。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
bool is_diff_fmt = format != another_format; // true
```
