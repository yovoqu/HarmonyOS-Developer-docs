# SetData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdata

#### 函数功能

设置Tensor的数据。
 
  

#### 函数原型

```text
void SetData(TensorData &&data)
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data | 输入 | 需要设置的数据。 关于TensorData类型的定义，请参见TensorData。 |
 
 
  

#### 返回值

无
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
Tensor t = {{}, {}, {}, {}, nullptr};
void *a = &t;
TensorData td(a, nullptr);
t.SetData(std::move(td));
```
