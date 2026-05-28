# 编译报错“Failed to obtain the module type.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162

**错误描述**
 
未找到指定的模块类型。
 
**可能原因**
 
在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。
 

![](assets/编译报错“Failed%20to%20obtain%20the%20module%20type.”/file-20260515130206824-0.png)

 
**解决措施**
 
确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
