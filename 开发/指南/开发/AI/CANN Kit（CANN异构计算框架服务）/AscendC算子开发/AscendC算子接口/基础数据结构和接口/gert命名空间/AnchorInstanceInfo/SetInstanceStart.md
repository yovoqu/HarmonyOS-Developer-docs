# SetInstanceStart

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstancestart

## 函数功能

设置算子某个IR输入在实际输入中的起始序号（index）。

## 函数原型


```text
void SetInstanceStart(const uint32_t instance_start)
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| instance_start | 输入 | 首个实例化Anchor的index。 |


## 返回值

无

## 约束说明

无

## 调用示例


```text
const auto &ir_inputs = node->GetOpDesc()->GetIrInputs(); // 算子IR定义的所有输入
for (size_t i = 0; i SetInstanceStart(input_index); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
}
```
