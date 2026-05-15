# SetInstantiationNum

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstantiationnum

## 函数功能

设置IR定义某个输入对应的实际输入个数。

## 函数原型


```text
void SetInstantiationNum(const uint32_t instantiation_num)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| instantiation_num | 输入 | 实例化的个数。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
const auto &ir_inputs = node->GetOpDesc()->GetIrInputs(); // 算子IR定义的所有输入
for (size_t i = 0; i SetInstantiationNum(instance_num); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
}
```
