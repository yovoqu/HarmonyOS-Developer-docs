# GetOutputsNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputsnum

##### 函数功能

获取算子在网络中的实际输出个数。
 
  

##### 函数原型

```text
size_t GetOutputsNum() const
```
 
  

##### 参数说明

无
 
  

##### 返回值

算子的实际输出个数。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
size_t index = compute_node_info->GetOutputsNum();
```
