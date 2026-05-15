# XML概述

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-overview

XML（可扩展标记语言）是一种用于描述数据的标记语言，提供通用的数据传输和存储方式。XML不预定义标记，因此更加灵活，适用于广泛的应用领域。

XML文档由元素（element）、属性（attribute）和内容（content）组成。


XML使用XML Schema或DTD（文档类型定义）定义文档结构，开发人员可以利用这些机制创建自定义规则，以验证XML文档的格式是否符合预期规范。

XML支持命名空间、实体引用、注释和处理指令，灵活适应各种数据需求。

语言基础类库提供了XML相关的基础能力，包括：[XML的生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-generation)、[XML的解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-parsing)和[XML的转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-conversion)。

以下是一个简单的XML样例及对应说明，更多XML的接口和具体使用，请见[@ohos.xml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-xml)。


```text


    Happy

    &


            Apples
            Bananas


```
