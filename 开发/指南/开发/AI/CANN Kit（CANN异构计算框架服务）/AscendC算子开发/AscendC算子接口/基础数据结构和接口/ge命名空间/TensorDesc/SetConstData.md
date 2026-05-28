# SetConstData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setconstdata

#### 函数功能

如果TensorDesc是常量节点的描述，向TensorDesc中设置权重值。
 
  

#### 函数原型

```text
void SetConstData(std::unique_ptr<uint8_t[]> const_data_buffer, const size_t &const_data_len);
```
 
  

#### 参数说明
 
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| const_data_buffer | 输入 | 权重地址。 |
| const_data_len | 输入 | 权重长度。 |
 
 
  

#### 返回值

无
 
  

#### 异常处理

无
 
  

#### 约束说明

无
