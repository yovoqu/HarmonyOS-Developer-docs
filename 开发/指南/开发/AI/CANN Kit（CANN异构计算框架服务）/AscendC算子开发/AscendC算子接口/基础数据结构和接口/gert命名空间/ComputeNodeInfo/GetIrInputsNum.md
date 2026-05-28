# GetIrInputsNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getirinputsnum

##### 函数功能

获取算子IR原型定义中的输入个数。
 
  

##### 函数原型

```text
size_t GetIrInputsNum() const
```
 
  

##### 参数说明

无
 
  

##### 返回值

IR原型中定义的输入个数，size_t类型。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
size_t index = compute_node_info->GetIrInputsNum();
```
