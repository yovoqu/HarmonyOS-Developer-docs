# operator==

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expanddimstype-operator

##### 函数功能

判断本补维规则对象与另一个对象是否一致。
 
  

##### 函数原型

```text
bool operator==(const ExpandDimsType &other) const
```
 
  

##### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个补维规则对象。 |
 
 
  

##### 返回值

true表示一致，false表示不一致。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
ExpandDimsType type1("1001");
ExpandDimsType type2("1001");
bool is_same_type = type1 == type2; // true
```
