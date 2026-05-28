# GetInstanceNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinstancenum

#### 函数功能

获取IR定义某个输入对应的实际输入个数。
 
  

#### 函数原型

```text
uint32_t GetInstanceNum() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

IR定义某个输入对应的实际输入个数。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
// IR定义的第一个输入是动态输入，且有10个实际输入
AnchorInstanceInfo anchor_0(0, 10);
auto input_num_0 = anchor_0.GetInstanceNum(); // input_num_0 = 10
```
