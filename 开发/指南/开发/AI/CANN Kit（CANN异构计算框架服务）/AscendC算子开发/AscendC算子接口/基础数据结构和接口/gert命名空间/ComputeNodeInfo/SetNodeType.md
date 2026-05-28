# SetNodeType

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setnodetype

#### 函数功能

设置算子的类型。
 
  

#### 函数原型

```text
void SetNodeType(const ge::char_t *node_type)
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| node_type | 输入 | 算子的类型。 |
 
 
  

#### 返回值

无
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
compute_node_info.SetNodeType("Const");
```
