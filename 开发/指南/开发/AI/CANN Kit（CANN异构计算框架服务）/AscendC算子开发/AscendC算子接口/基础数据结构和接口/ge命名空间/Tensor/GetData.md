# GetData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getdata

#### 函数功能

获取Tensor中的数据。
 
const uint8_t* GetData() const返回的数据不可修改，uint8_t* GetData()返回的数据可修改。
 
  

#### 函数原型

```text
const uint8_t *GetData() const;
uint8_t *GetData();
```
 
  

#### 参数说明

无
 
  

#### 返回值
 
| 类型 | 描述 |
| --- | --- |
| const uint8_t | Tensor中所存放的数据。 |
 
 
  

#### 异常处理

无
 
  

#### 约束说明

无
