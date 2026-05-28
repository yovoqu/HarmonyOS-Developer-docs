# IsExpandIndex

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isexpandindex

#### 函数功能

基于补维后的shape，判断指定的index轴是否为补维轴。
 
  

#### 函数原型

```text
bool IsExpandIndex(const AxisIndex index) const
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 指定轴的索引。 |
 
 
  

#### 返回值

- true代表指定的轴为补维轴。
- false代表指定的轴为原始轴。

 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ExpandDimsType type1("1001");
bool is_expand_index0 = type1.IsExpandIndex(0); // true
bool is_expand_index1 = type1.IsExpandIndex(1); // false
```
