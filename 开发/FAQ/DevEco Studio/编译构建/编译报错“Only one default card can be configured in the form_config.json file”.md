# 编译报错“Only one default card can be configured in the form_config.json file”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39

问题现象

DevEco Studio编译失败。提示：Only one default card can be configured in the form_config.json file。


![](assets/编译报错“Only%20one%20default%20card%20can%20be%20configured%20in%20the%20form_config.json%20file”/file-20260515130111129-0.png)


问题原因

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

解决措施

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
