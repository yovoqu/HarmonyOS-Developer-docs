# 如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-123

问题现象

编译错误：“Error: cJSON\_Parse failed”。请检查JSON文件。


![](assets/如何解决编译报错“Error／%20cJSON_Parse%20failed,%20please%20check%20the%20JSON%20file.”的问题/file-20260515130145791-0.png)


报错原因

module.json 文件格式不正确。

常见场景

1. JSON文件末尾有多余的逗号。

2. 根标签不是大括号{}。

解决方案

检查报错指向的 JSON 文件格式，例如末尾是否有多余的逗号，根标签是否为大括号 {}。
