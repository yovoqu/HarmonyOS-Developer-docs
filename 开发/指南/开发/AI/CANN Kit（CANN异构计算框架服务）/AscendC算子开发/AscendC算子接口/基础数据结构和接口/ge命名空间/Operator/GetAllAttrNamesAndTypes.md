# GetAllAttrNamesAndTypes

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallattrnamesandtypes

## 函数功能

获取算子所有已配置的属性名称及类型，包含IR定义的普通属性和开发者自定义属性。

## 函数原型


> [!NOTE]
> 数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。


```text
const std::map GetAllAttrNamesAndTypes() const;
graphStatus GetAllAttrNamesAndTypes(std::map &attr_name_types) const;
```


## 参数说明


| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| attr_name_types | 输出 | 所有的属性名称和属性类型。 |


## 返回值


| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH_FAILED：失败。 GRAPH_SUCCESS：成功。 |


## 异常处理

无

## 约束说明

无
