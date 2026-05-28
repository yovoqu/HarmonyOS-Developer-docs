# SetPlacement

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setplacement

#### 函数功能

设置tensor的placement。
 
  

#### 函数原型

```text
void SetPlacement(const TensorPlacement placement)
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| placement | 输入 | tensor的placement。 关于TensorPlacement类型的定义，请参见TensorPlacement。 |
 
 
  

#### 返回值

无
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
auto addr = reinterpret_cast<void *>(0x10);
TensorData td(addr, nullptr);
auto td_place = td.SetPlacement(kOnHost);
```
