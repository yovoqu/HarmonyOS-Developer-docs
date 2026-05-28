# ScalarGetSFFValue

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalargetsffvalue

#### 功能说明

获取一个uint64_t类型数字的二进制中第一个0或1出现的位置，如果没找到则返回-1。
 
  

#### 函数原型

```text
template <int countValue>  
__aicore__ inline int64_t ScalarGetSFFValue(uint64_t valueIn)
```
 
  

#### 参数说明

**表1** 参数说明
  
| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 输入数据，数据类型是uint64_t。 |
| countValue | 输入 | 获取到第一个0或1的位置。数据类型是int，值为0或1。 |
 
 
  

#### 返回值

valueIn中第一个0或1出现的位置。
 
  

#### 支持的型号

Kirin9020系列处理器
 
KirinX90系列处理器
 
  

#### 约束说明

无。
 
  

#### 调用示例

```text
uint64_t valueIn = 28;
// 输出数据(oneCount): 2
int64_t oneCount = AscendC::ScalarGetSFFValue<1>(valueIn);
```
