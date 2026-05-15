# GetOutputAttr

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputattr

## 函数功能

根据属性名称获取算子输出Tensor对应的属性值。

## 函数原型


```text
graphStatus GetOutputAttr(const int32_t index, const char_t *name, AscendString &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, AscendString &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, int64_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, int64_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, int32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, int32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, uint32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, uint32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, bool &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, bool &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, float32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, float32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector &attr_value) const;
```


## 参数说明


| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 属性名称。 |
| index | 输入 | 输出索引。 |
| dst_name | 输入 | 输出边名称。 |
| attr_value | 输出 | 获取到的int64_t表示的整型类型属性值。 |
| attr_value | 输出 | 获取到的int32_t表示的整型类型属性值。 |
| attr_value | 输出 | 获取到的uint32_t表示的整型类型属性值。 |
| attr_value | 输出 | 获取到的vector表示的整型列表类型属性值。 |
| attr_value | 输出 | 获取到的vector表示的整型列表类型属性值。 |
| attr_value | 输出 | 获取到的vector表示的整型列表类型属性值。 |
| attr_value | 输出 | 获取到的浮点类型的属性值。 |
| attr_value | 输出 | 获取到的浮点列表类型的属性值。 |
| attr_value | 输出 | 获取到的布尔类型的属性值。 |
| attr_value | 输出 | 获取到的布尔列表类型的属性值。 |
| attr_value | 输出 | 获取到的字符串类型的属性值。 |
| attr_value | 输出 | 获取到的字符串列表类型的属性值。 |


## 返回值


| 类型 | 描述 |
| --- | --- |
| graphStatus | 找到对应属性，返回GRAPH_SUCCESS，否则返回GRAPH_FAILED。 |


## 异常处理

无

## 约束说明

无
