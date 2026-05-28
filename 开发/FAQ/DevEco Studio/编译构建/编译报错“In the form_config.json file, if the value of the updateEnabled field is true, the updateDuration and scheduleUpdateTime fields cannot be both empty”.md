# 编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-40

**问题现象**
 
在form_config.json文件中，如果updateEnabled字段的值为true，则updateDuration和scheduleUpdateTime字段不能同时为空。
 

![](assets/编译报错“In%20the%20form_config.json%20file,%20if%20the%20value%20of%20the%20updateEnabled%20field%20is%20true,%20the%20updateDuration%20and%20scheduleUpdateTime%20fields%20cannot%20be%20both%20empty”/file-20260515130111528-0.png)

 
**问题原因**
 
从 DevEco Studio NEXT Developer Preview 2 版本开始，新增规则：卡片的配置文件中必须包含updateEnabled，设置为true时，可以选择定时刷新（updateDuration）或定点刷新（scheduledUpdateTime）。如果同时配置了两种刷新方式，定时刷新将优先生效。
 
**解决措施**
 
进入 module.json5 文件，根据需求选择配置 updateEnabled 为 false，或配置定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）。
