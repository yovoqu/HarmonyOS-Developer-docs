# SetNodeName

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setnodename

##### 函数功能

设置该ComputeNodeInfo对应的算子的名称。
 
  

##### 函数原型

```text
void SetNodeName(const ge::char_t *node_name)
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| node_name | 输入 | 算子的名称。 |
 
 
  

##### 返回值

无
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
compute_node_info->SetNodeName("Conv2d");
```
